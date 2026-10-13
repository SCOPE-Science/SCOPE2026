#!/usr/bin/env python3
"""Finite replay of signed-neighbourhood witness-set compression.

The random checks are sanity tests; arbitrary-cardinality preservation is
established by the accompanying mathematical proof, not by sampling.
"""
import random

OPS = ('A', 'B')

def family(f):
    seen = set()
    def walk(node):
        if node in seen:
            return
        seen.add(node)
        for child in node[1:]:
            if isinstance(child, tuple):
                walk(child)
    walk(f)
    return sorted(seen, key=lambda x: (depth(x), str(x)))

def depth(node):
    if len(node)==2 and node[0]=='p':
        return 0
    return 1+max(depth(child) for child in node[1:] if isinstance(child,tuple))

def generate(rng, size):
    pool = [('p', 'p'+str(i)) for i in range(5)]
    for _ in range(size):
        kind=rng.choice(['not','and','or','imp','A','B'])
        if kind in ('not','A','B'):
            nd=(kind, rng.choice(pool))
        else:
            nd=(kind,rng.choice(pool),rng.choice(pool))
        pool.append(nd)
    return pool[-1]

def evaluate(nodes, n, rng):
    whole=(1<<n)-1
    nbs={(op,sgn,w,subset):rng.getrandbits(1)
        for op in OPS for sgn in ('+','-')
        for w in range(n) for subset in range(whole+1)}
    signed={}
    for f in nodes:
        k=f[0]
        if k=='p':
            plus,minus=rng.randint(0,whole),rng.randint(0,whole)
        elif k=='not':
            plus=signed[f[1]][1]
            minus=rng.randint(0,whole)
        elif k in ('and','or','imp'):
            a=signed[f[1]][0];b=signed[f[2]][0]
            plus={'and':lambda: a&b,'or':lambda:a|b,
                  'imp':lambda:(whole^a)|b}[k]()
            minus=rng.randint(0,whole)
        else:
            a,b=signed[f[1]]
            plus=sum(nbs[k,'+',w,a]<<w for w in range(n))
            minus=sum(nbs[k,'-',w,b]<<w for w in range(n))
        signed[f]=(plus,minus)
    return signed,nbs

def pick_witnesses(signed, nodes, n, root):
    children=list({f[1] for f in nodes if f[0] in OPS})
    used={root}
    for sign in (0,1):
        distinct=sorted({signed[f][sign] for f in children})
        while True:
            trace={}
            collision=None
            for mask in distinct:
                projected=mask & sum(1<<w for w in used)
                if projected in trace:
                    collision=(trace[projected],mask)
                    break
                trace[projected]=mask
            if collision is None:
                break
            a,b=collision
            candidates=[w for w in range(n) if ((a^b)>>w)&1 and w not in used]
            assert candidates
            used.add(candidates[0])
    if children:
        assert len(used) <= 2*len(children)-1
    else:
        assert len(used)==1
    return tuple(sorted(used))

def check_reconstruction(nodes,signed,nbs,used):
    n=len(used);m={w:i for i,w in enumerate(used)}
    whole=(1<<n)-1
    def trace(mask):
        return sum(((mask>>w)&1)<<i for w,i in m.items())
    children={f[1] for f in nodes if f[0] in OPS}
    reduced={}
    for op in OPS:
        for sign,j in (('+',0),('-',1)):
            for w in used:
                for child in children:
                    s=trace(signed[child][j]); b=nbs[op,sign,w,signed[child][j]]
                    key=(op,sign,w,s)
                    assert key not in reduced or reduced[key]==b, 'Collision in projected neighbourhood argument'
                    reduced[key]=b
    rebuilt={}
    for f in nodes:
        k=f[0]
        if k=='p':
            plus,minus=(trace(v) for v in signed[f])
        elif k=='not':
            plus=rebuilt[f[1]][1];minus=trace(signed[f][1])
        elif k in ('and','or','imp'):
            a=rebuilt[f[1]][0];b=rebuilt[f[2]][0]
            plus={'and':lambda:a&b,'or':lambda:a|b,'imp':lambda:(whole^a)|b}[k]()
            minus=trace(signed[f][1])
        else:
            a,b=rebuilt[f[1]]
            plus=sum(reduced[k,'+',w,a]<<i for i,w in enumerate(used))
            minus=sum(reduced[k,'-',w,b]<<i for i,w in enumerate(used))
        rebuilt[f]=(plus,minus)
        assert rebuilt[f]==(trace(signed[f][0]),trace(signed[f][1])), ('mismatch',f)
    return len(children)

def main():
    rng=random.Random(20261008)
    cases=0;with_modal=0;max_worlds=0;max_sub=0
    for n in range(1,10):
        for trial in range(300):
            f=generate(rng,rng.randint(3,43))
            nodes=family(f)
            signed,nbs=evaluate(nodes,n,rng)
            root=rng.randrange(n)
            used=pick_witnesses(signed,nodes,n,root)
            k=check_reconstruction(nodes,signed,nbs,used)
            cases+=1
            with_modal+=(k>0)
            max_worlds=max(max_worlds,len(used))
            max_sub=max(max_sub,len(nodes))
    print('VERIFY_OK cases=%d with_modal=%d max_worlds=%d max_subformulas=%d'%(cases,with_modal,max_worlds,max_sub))
if __name__=='__main__':main()
