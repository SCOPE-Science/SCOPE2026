"""Exact finite checks for a cactus minimal connected domination theorem.
Run with Python 3.9+; standard library only. No third-party data needed.
"""
from itertools import product
from collections import Counter, deque
import random

# All 103 nonempty connected unlabelled cactus graphs with at most seven
# vertices, encoded in graph6. A graph6 decoder is supplied below.
ATLAS = '''@ A_ Bo Bw CF Ck CN Cl D?{ DBc Dh_ D@{ Dx_ DJc DbW Dhc D`{ E?Bw EhP? EsCO EiGO EBe? E`EG E?Fw EC{O E@dW EG}? E]a? EYWO E]_O EQKo EsCW EJe? EBy? Ehd? EhEG EtaG EtoO ERUO E{CW F??Fw FhG`? FiO`? FiOG_ FiO_G FIo`? Fk_`? FaOH_ FEW`? Fk_G_ FhCK? FsaC_ FItA? F?Bcw FkoK? FhG`G FMpA? FhoI? FhoGO FHAgg FiG`G FbW`? FiO`G FMoG_ Fg?hg Fko`? Fpq?_ FMoa? Fpq?G Fpa?g FhoG_ FhD@G FhoGG FIo`G Fh_gG FpQO_ FXAGg Fk_`G FMo`? FK_h_ FIc`G FMo@G FPq?g FhCKG F`?Fw FH?NW FmW`? FxaGG Fh?JW FLg`G FwaK_ FK{@G FsNA? F_{p? F_{Og FSYK_ F_sPg F_{PG F`EBW FMo`G F`ooo FGEFw FxCX_'''.split()

def g6(s):
    n = ord(s[0]) - 63
    bits = []
    for c in s[1:]:
        bits.extend((ord(c)-63 >> sh) & 1 for sh in range(5,-1,-1))
    adj = [0]*n
    k = 0
    for j in range(1,n):
        for i in range(j):
            if bits[k]:
                adj[i] |= 1<<j
                adj[j] |= 1<<i
            k += 1
    return adj

def reachable(adj,mask):
    if not mask:return False
    seen = first = mask & -mask
    frontier = first
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length()-1
        nxt = adj[v] & mask & ~seen
        seen |= nxt
        frontier |= nxt
    return seen==mask

def cds(adj,mask):
    n = len(adj)
    if not reachable(adj,mask): return False
    dom = mask
    for v in range(n):
        if mask>>v & 1: dom |= adj[v]
    return dom == (1<<n)-1

def brute(adj):
    n=len(adj); out=[]
    for mask in range(1,1<<n):
        if cds(adj,mask) and not any(cds(adj,mask & ~(1<<v)) for v in range(n) if mask>>v&1):
            out.append(mask)
    return sorted(out)

def cycles(adj):
    n=len(adj); out=set()
    for root in range(n):
        def walk(path):
            u=path[-1]
            for v in range(root+1,n):
                if not (adj[u]>>v&1):continue
                if v in path:continue
                walk(path+[v])
            if len(path)>=3 and adj[u]>>root&1:
                p=tuple(path)
                out.add(min(p,(p[0],)+p[:0:-1]))
        for v in range(root+1,n):
            if adj[root]>>v&1:walk([root,v])
    return sorted(out)

def cuts(adj):
    n=len(adj)
    if n<=2:return set()
    out=set()
    for v in range(n):
        allowed=(1<<n)-1 ^ (1<<v)
        if not reachable(adj, allowed):out.add(v)
    return out

def local_options(cycle,art):
    u=[v for v in cycle if v not in art]
    if not u:return [0]
    pair = [{cycle[i],cycle[(i+1)%len(cycle)]} for i in range(len(cycle))
            if cycle[i] not in art and cycle[(i+1)%len(cycle)] not in art]
    lonely = [{v} for v in u if cycle[(cycle.index(v)-1)%len(cycle)] in art
              and cycle[(cycle.index(v)+1)%len(cycle)] in art]
    omitted=pair+lonely
    assert omitted
    return [sum(1<<v for v in u if v not in o) for o in omitted]

def predicted(adj):
    n=len(adj)
    if n==1:return [1], []
    if n==2:return [1,2], [(1,2)]
    art=cuts(adj); cs=cycles(adj)
    if not art:
        assert len(cs)==1
        c=cs[0]
        states=[((1<<n)-1)^((1<<c[i])|(1<<c[(i+1)%n])) for i in range(n)]
        parts=[states]
        return sorted(states),[(a,b) for a,b in zip(states,states[1:]+states[:1])]
    parts=[local_options(c,art) for c in cs]
    amask=sum(1<<v for v in art)
    states=[]; choice=[]
    for ix in product(*(range(len(p)) for p in parts)):
        mask=amask
        for cidx,x in enumerate(ix):mask |= parts[cidx][x]
        states.append(mask);choice.append(ix)
    assert len(states)==len(set(states))
    edges=[]
    for i in range(len(states)):
        for j in range(i+1,len(states)):
            di=[k for k in range(len(parts)) if choice[i][k]!=choice[j][k]]
            if len(di)==1:
                k=di[0]
                x=parts[k][choice[i][k]]; y=parts[k][choice[j][k]]
                if (x^y).bit_count()==2:
                    edges.append((states[i],states[j]))
    return sorted(states),edges

def edge_set(ss):
    return {tuple(sorted((a,b))) for i,a in enumerate(ss) for b in ss[i+1:]
            if a.bit_count()==b.bit_count() and (a^b).bit_count()==2}

def cycle_run_profile(adj):
    n=len(adj);art=cuts(adj); cs=cycles(adj)
    if not art:
        return (Counter({n-2:n}) if n>=3 else Counter({1:n}), [n] if n>=3 else [n])
    size_profile=Counter({len(art):1});comp_sizes=[1]
    for cyc in cs:
        mark=[v not in art for v in cyc]
        f=sum(mark)
        if f==0:
            localpoly=Counter({0:1}); localcc=[1]
        else:
            start=next(i for i,v in enumerate(mark) if not v)
            lens=[]; L=0
            for shift in range(1,len(cyc)+1):
                if mark[(start+shift)%len(cyc)]:L+=1
                elif L:lens.append(L);L=0
            n1=sum(x==1 for x in lens)
            np=sum(x-1 for x in lens if x>=2)
            localpoly=Counter()
            if n1:localpoly[f-1]=n1
            if np:localpoly[f-2]=np
            localcc=[x-1 for x in lens if x>=2]
            if n1:localcc.append(n1)
        nxt=Counter()
        for a,p in size_profile.items():
            for b,q in localpoly.items():nxt[a+b]+=p*q
        size_profile=nxt
        comp_sizes=[a*b for a in comp_sizes for b in localcc]
    return size_profile,sorted(comp_sizes)

def check(adj,label):
    actual=brute(adj)
    expected,ee=predicted(adj)
    assert actual==expected,('states',label,len(actual),len(expected),actual,expected)
    assert edge_set(actual)=={tuple(sorted(e)) for e in ee},('edges',label)
    sizes,cc=cycle_run_profile(adj)
    assert Counter(m.bit_count() for m in actual)==sizes,('polynomial',label)
    assert components(actual,edge_set(actual))==cc,('components',label)
    return len(actual),len(ee)

def gluing_random(seed,num):
    rng=random.Random(seed)
    for t in range(num):
        n=1; es=set(); block_types=[]
        for step in range(rng.randrange(2,7)):
            if n>=12:break
            kind=rng.randrange(3)
            attach=rng.randrange(n)
            if kind==0 or n+3>13:
                v=n; n+=1; es.add(tuple(sorted((attach,v))))
            else:
                c_len=rng.randrange(3,min(7,15-n))
                vs=[attach]+list(range(n,n+c_len-1));n+=c_len-1
                for u,v in zip(vs,vs[1:]+vs[:1]):es.add(tuple(sorted((u,v))))
        adj=[0]*n
        for a,b in es:adj[a]|=1<<b;adj[b]|=1<<a
        yield adj

def components(states,edges):
    ng={s:set() for s in states}
    for a,b in edges:ng[a].add(b);ng[b].add(a)
    cc=[]
    while ng:
        s=next(iter(ng)); q={s}; frontier=[s]
        while frontier:
            u=frontier.pop()
            for v in ng[u]:
                if v not in q:q.add(v);frontier.append(v)
        cc.append(len(q))
        for x in q:del ng[x]
        for z in ng:ng[z].difference_update(q)
    return sorted(cc)

def main():
    counts=Counter()
    for i,s in enumerate(ATLAS):
        x=check(g6(s),('atlas',i,s));counts[x[0]]+=1
    print('ATLAS_OK',len(ATLAS),'minimal_set_count_histogram',sorted(counts.items()))
    cc=Counter();examples=[]
    for i,adj in enumerate(gluing_random(728163,180)):
        x=check(adj,('generated',i));cc[x[0]]+=1
        if i<3:examples.append((len(adj),x))
    print('GENERATED_OK',sum(cc.values()),'minimal_set_count_histogram',sorted(cc.items()))
    # Two five- and six-cycles sharing one vertex: local path products.
    n=10; cyc1=[0,1,2,3,4,5];cyc2=[0,6,7,8,9]
    adj=[0]*n
    for c in (cyc1,cyc2):
        for a,b in zip(c,c[1:]+c[:1]):adj[a]|=1<<b;adj[b]|=1<<a
    ss,ee=predicted(adj)
    assert len(ss)==12 and len(ee)==17 and components(ss,ee)==[12]
    print('FIGURE_EIGHT',len(ss),len(ee),components(ss,ee))
    # An 8-cycle with leaves at opposite vertices gives two disjoint P2's.
    n=10;adj=[0]*n
    for i in range(8):
        j=(i+1)%8;adj[i]|=1<<j;adj[j]|=1<<i
    for a,b in ((0,8),(4,9)):adj[a]|=1<<b;adj[b]|=1<<a
    ss,ee=predicted(adj)
    assert len(ss)==4 and len(ee)==2 and components(ss,ee)==[2,2]
    print('OPPOSITE_ATTACHMENTS',len(ss),len(ee),components(ss,ee))
    print('VERIFY_OK')
if __name__=='__main__':main()
