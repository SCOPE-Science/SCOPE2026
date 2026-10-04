#!/usr/bin/env python3
from itertools import product

def absorb(a,b,q):
    return min(a+b,q-1)

def outputs(x,q):
    x=tuple(x); n=len(x)
    out={x[:-1]}
    for i in range(n-1):
        out.add(x[:i]+(absorb(x[i],x[i+1],q),)+x[i+2:])
    return out

def parents_inverse(y,q):
    y=tuple(y)
    p={y+(a,) for a in range(q)}
    for i,c in enumerate(y):
        for a in range(q):
            for b in range(q):
                if absorb(a,b,q)==c:
                    p.add(y[:i]+(a,b)+y[i+1:])
    return p

def insertion_sphere(y,q):
    y=tuple(y); m=len(y)
    return {y[:g]+(a,)+y[g:] for g in range(m+1) for a in range(q)}

def genuine_splits(y,q):
    y=tuple(y); out=set()
    for i,c in enumerate(y):
        for a in range(q):
            for b in range(q):
                if a!=c and b!=c and absorb(a,b,q)==c:
                    out.add(y[:i]+(a,b)+y[i+1:])
    return out

def formula(q,n):
    return q+(n-1)*q*(q-1)//2

def check():
    cases=0
    # Full forward-vs-inverse incidence checks. Bounds chosen so replay is quick.
    for q,max_n in [(2,9),(3,7),(4,6)]:
        for n in range(2,max_n+1):
            by_y={y:set() for y in product(range(q), repeat=n-1)}
            for x in product(range(q), repeat=n):
                for y in outputs(x,q):
                    by_y[y].add(x)
            observed=0
            for y,pf in by_y.items():
                pi=parents_inverse(y,q)
                assert pf==pi, (q,n,y,'forward_inverse')
                I=insertion_sphere(y,q)
                G=genuine_splits(y,q)
                assert pi <= I|G, (q,n,y,'decomposition')
                assert len(I)==q+(n-1)*(q-1), (q,n,y,'insertion_size')
                observed=max(observed,len(pi))
            target=formula(q,n)
            sat=(q-1,)*(n-1)
            assert observed==target, (q,n,observed,target)
            assert len(by_y[sat])==target, (q,n,'saturated')
            cases+=1
    # Direct inverse checks at a larger alphabet without enumerating all sources separately.
    for q in (5,6):
        for n in range(2,6):
            target=formula(q,n)
            observed=max(len(parents_inverse(y,q)) for y in product(range(q), repeat=n-1))
            assert observed==target, (q,n,observed,target)
            assert len(parents_inverse((q-1,)*(n-1),q))==target
            cases+=1
    # Symbol-level genuine-split count used in the proof.
    for q in range(2,20):
        cap=(q-1)*(q-2)//2
        vals=[]
        for c in range(q):
            g=sum(1 for a in range(q) for b in range(q)
                  if a!=c and b!=c and absorb(a,b,q)==c)
            vals.append(g)
            assert g<=cap
        assert vals[-1]==cap
    print(f'VERIFY_OK cases={cases} q<=6 forward_q<=4 symbol_q<=19')

if __name__=='__main__':
    check()
