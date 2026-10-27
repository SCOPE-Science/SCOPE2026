"""Independent direct and orbit-quotient checks for marked q-ary Hamming graphs."""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial


def types(d, t):
    return [(a,b,s) for a in range(t+1) for b in range(t-a+1)
            for s in range(d-t+1)]


def neighbours(d, q, t, v):
    a,b,s=v
    c=t-a-b; h=d-t-s
    z=Counter()
    def put(k,n):
        if n: z[k]+=n
    put((a-1,b+1,s), a)
    put((a-1,b,s), a*(q-2))
    put((a+1,b-1,s), b)
    put((a,b-1,s), b*(q-2))
    put((a+1,b,s), c)
    put((a,b+1,s), c)
    put((a,b,s), c*(q-3)+s*(q-2))
    put((a,b,s+1), h*(q-1))
    put((a,b,s-1), s)
    return z


def refine(states, neighbors, init, steps):
    colors=[init[v] for v in states]
    out=[colors]
    for i in range(steps):
        sigs=[]
        at={v:j for j,v in enumerate(states)}
        for j,v in enumerate(states):
            cnt=Counter()
            for k,n in neighbors[v].items(): cnt[colors[at[k]]]+=n
            sigs.append((colors[j],tuple(sorted(cnt.items()))))
        indices={sig:i for i,sig in enumerate(sorted(set(sigs)))}
        colors=[indices[sig] for sig in sigs]
        out.append(colors)
    return out


def quotient(d,q,t):
    st=types(d,t)
    initial={v: 1 if v==(t,0,0) else 2 if v==(0,t,0) else 0 for v in st}
    nb={v:neighbours(d,q,t,v) for v in st}
    for v in st:
        assert sum(nb[v].values())==d*(q-1), (d,q,t,v,nb[v])
    C=refine(st,nb,initial,max(0,d-1))
    assert len(set(C[d-1]))==len(st),(d,q,t,'upper')
    if d>1:
        assert len(set(C[d-2]))<len(st),(d,q,t,'lower')
    return len(st)


def direct(d,q,t):
    verts=list(product(range(q),repeat=d))
    pos={v:i for i,v in enumerate(verts)}
    A=(0,)*d; B=(1,)*t+(0,)*(d-t)
    neighbors={v:Counter({verts[pos[v[:j]+(z,)+v[j+1:]]]:1
                          for j in range(d) for z in range(q) if z!=v[j]}) for v in verts}
    init={v:1 if v==A else 2 if v==B else 0 for v in verts}
    C=refine(verts,neighbors,init,max(0,d-1))
    def inv(v):
        return (sum(v[j]==0 for j in range(t)),
                sum(v[j]==1 for j in range(t)),
                sum(v[j]!=0 for j in range(t,d)))
    by_col=defaultdict(set)
    by_type=defaultdict(set)
    for v,c in zip(verts,C[d-1]):
        by_col[c].add(inv(v));by_type[inv(v)].add(c)
    assert all(len(s)==1 for s in by_col.values()),(d,q,t,'col')
    assert all(len(s)==1 for s in by_type.values()),(d,q,t,'type')
    assert len(by_col)==len(types(d,t))
    for (a,b,s),cs in by_type.items():
        c=t-a-b
        predicted=(factorial(t)//(factorial(a)*factorial(b)*factorial(c))
                   *(q-2)**c*comb(d-t,s)*(q-1)**s)
        actual=sum(1 for v in verts if inv(v)==(a,b,s))
        assert predicted==actual,(d,q,t,(a,b,s),predicted,actual)
    if d>1:assert len(set(C[d-2]))<len(types(d,t))


def main():
    direct_checks=0
    for q,max_d in [(3,6),(4,5),(5,4)]:
        for d in range(1,max_d+1):
            for t in range(1,d+1):
                direct(d,q,t);direct_checks+=1
    quotient_checks=0
    for q in range(3,9):
        for d in range(1,15):
            for t in range(1,d+1):
                quotient(d,q,t);quotient_checks+=1
    print('DIRECT_CONFIGURATIONS_PASS',direct_checks)
    print('QUOTIENT_CONFIGURATIONS_PASS',quotient_checks)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
