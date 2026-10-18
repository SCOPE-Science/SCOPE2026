#!/usr/bin/env python3
"""Checks the flat-support/NE-obligation theorem for finite samples.
No external dependencies. The mathematical all-size proof is in RESULT.md.
"""
from functools import lru_cache
from random import Random

# Formula grammar: ('lit', atom) or ('and'|'or', left, right).

def flat(node, k, valuations):
    if node[0] == 'lit':
        name = node[1]
        if name == 'ne' or name == 'top': return valuations
        if name == 'bot': return 0
        idx = int(name[1:]); bit = 1 << idx
        return sum(1 << j for j, v in enumerate(range(1 << k))
                   if bool(v & bit) == (name[0] == 'p'))
    left = flat(node[1], k, valuations)
    right = flat(node[2], k, valuations)
    return (left & right) if node[0] == 'and' else (left | right)

def fast(node, team, k):
    universe = (1 << (1 << k)) - 1
    def build(sub):
        if sub[0] == 'lit':
            w = flat(sub, k, universe)
            return w, [(w if sub[1] == 'ne' else None)] if sub[1] == 'ne' else []
        fa,wa=build(sub[1]); fb,wb=build(sub[2])
        if sub[0]=='and':return fa&fb, [w&fb for w in wa]+[w&fa for w in wb]
        return fa|fb, wa+wb
    allowed, obligations=build(node)
    return (team & ~allowed) == 0 and all(team & x for x in obligations)

def topdown(node,team,k):
    universe = (1 << (1 << k)) - 1
    @lru_cache(None)
    def f(sub):return flat(sub,k,universe)
    if team & ~f(node):return False
    def check(sub,context):
        if sub[0]=='lit':return sub[1]!='ne' or bool(team & context)
        a,b=sub[1],sub[2]
        if sub[0]=='and':
            return check(a,context&f(b)) and check(b,context&f(a))
        return check(a,context) and check(b,context)
    return check(node,universe)

def semantic(root,team,k):
    @lru_cache(None)
    def sat(node,mask):
        if node[0]=='lit':
            if node[1]=='ne':return bool(mask)
            return (mask & ~flat(node,k,(1 << (1 << k))-1)) == 0
        a,b=node[1],node[2]
        if node[0]=='and':return sat(a,mask) and sat(b,mask)
        # All possibly overlapping lax splits: 3 options per present valuation.
        bits=[1<<j for j in range(1<<k) if mask>>j&1]
        for digits in __import__('itertools').product((1,2,3),repeat=len(bits)):
            left=right=0
            for v,s in zip(bits,digits):
                if s&1:left|=v
                if s&2:right|=v
            if sat(a,left) and sat(b,right):return True
        return False
    return sat(root,team)

def gen(r,depth,k):
    if not depth or r.random()<.31:
        return ('lit',r.choice(['ne','top','bot']+[t+str(i) for i in range(k) for t in ('p','n')]))
    return (r.choice(('and','or')),gen(r,depth-1,k),gen(r,depth-1,k))

def walk(node):
    yield node
    if node[0]!='lit':
        yield from walk(node[1]);yield from walk(node[2])

def fixed_point_trace(root,team,k):
    nodes={}
    def collect(node,path):
        nodes[path]=node
        if node[0]!='lit':
            collect(node[1],path+'0');collect(node[2],path+'1')
    collect(root,'')
    original={p:team for p in nodes}
    results=[original]
    universe=(1 << (1 << k))-1
    for i in range(1,7):
        prev=results[-1]
        now={}
        if i%2:
            for p in sorted(nodes,key=len,reverse=True):
                node=nodes[p]
                if node[0]=='lit':
                    if prev[p]==-1:now[p]=-1
                    elif node[1]=='ne':now[p]=prev[p] if prev[p] else -1
                    else:now[p]=prev[p]&flat(node,k,universe)
                else:
                    a,b=now[p+'0'],now[p+'1']
                    if -1 in (a,b):now[p]=-1
                    elif node[0]=='and':now[p]=a&b
                    else:now[p]=a|b
        else:
            now['']=prev['']
            for p in sorted(nodes,key=len):
                node=nodes[p]
                if node[0]!='lit':
                    for side in ('0','1'):
                        q=p+side
                        if node[0]=='and':now[q]=now[p]
                        else:now[q]=-1 if now[p]==-1 or prev[q]==-1 else now[p]&prev[q]
        results.append(now)
    return results

def main():
    r=Random(20261017)
    checks=0
    for k in (1,2):
        for depth in range(0,6):
            for _ in range(120):
                node=gen(r,depth,k)
                for team in range(1<<(1<<k)):
                    actual=semantic(node,team,k)
                    normal=fast(node,team,k)
                    direct=topdown(node,team,k)
                    assert actual==normal==direct,(k,node,team,actual,normal,direct)
                    checks+=1
    # The published alternating bottom-up/top-down algorithm is reproduced literally.
    rounds=0
    for k in (1,2):
        universe=(1 << (1 << k))-1
        for depth in range(6):
            for _ in range(180):
                tree=gen(r,depth,k)
                for team in range(1 << (1 << k)):
                    trace=fixed_point_trace(tree,team,k)
                    assert trace[4]==trace[5]==trace[6],(tree,team,trace)
                    assert (trace[4]['']==team)==semantic(tree,team,k)
                    rounds+=1
    sharp=('and',('lit','ne'),('lit','bot'))
    sharp_trace=fixed_point_trace(sharp,1,1)
    assert sharp_trace[3]!=sharp_trace[4] and sharp_trace[4]==sharp_trace[5]
    print('CONVEX_NE_FLAT_OBLIGATIONS_OK', checks)
    print('FOUR_ROUND_FIXED_POINT_BOUND_OK',rounds)
    print('FOUR_ROUND_SHARPNESS_OK')
    return

if __name__=='__main__':main()
