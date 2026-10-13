#!/usr/bin/env python3
from itertools import product
from math import factorial

def invmod(a,n):
    return pow(a,-1,n)

def make_group(p, nonabelian):
    n=p*p
    k=1+p
    elems=[(r,s) for r in range(n) for s in range(p)]
    if nonabelian:
        def op(x,y):
            r,s=x; u,v=y
            return ((r + pow(k,s,n)*u)%n,(s+v)%p)
    else:
        def op(x,y):
            return ((x[0]+y[0])%n,(x[1]+y[1])%p)
    e=(0,0)
    def inv(x):
        for y in elems:
            if op(x,y)==e and op(y,x)==e: return y
        raise AssertionError
    def gen(S):
        H={e}; frontier=[e]
        gens=list(S)+[inv(g) for g in S]
        while frontier:
            x=frontier.pop()
            for g in gens:
                y=op(x,g)
                if y not in H:
                    H.add(y); frontier.append(y)
        return frozenset(H)
    return elems,op,gen

def all_proper_subgroups(p, nonabelian):
    elems,op,gen=make_group(p,nonabelian)
    subs={gen([x]) for x in elems}
    for x in elems:
        for y in elems:
            H=gen([x,y])
            if len(H)<len(elems): subs.add(H)
    proper=[H for H in subs if 1<len(H)<len(elems)]
    return elems,proper

def check_double_star(p, nonabelian):
    elems,subs=all_proper_subgroups(p,nonabelian)
    lo=[H for H in subs if len(H)==p]
    hi=[H for H in subs if len(H)==p*p]
    assert len(subs)==2*p+2, (p,nonabelian,len(subs))
    assert len(lo)==p+1 and len(hi)==p+1
    edges=[]
    deg={H:0 for H in subs}
    for H in lo:
        for K in hi:
            if H < K:
                edges.append((H,K)); deg[H]+=1; deg[K]+=1
    assert len(edges)==2*p+1
    centers=[H for H,d in deg.items() if d==p+1]
    leaves=[H for H,d in deg.items() if d==1]
    assert len(centers)==2 and len(leaves)==2*p
    assert centers[0] < centers[1] or centers[1] < centers[0]
    # Each center has exactly p leaf neighbors.
    for C in centers:
        assert sum(1 for H,K in edges if (H==C and K in leaves) or (K==C and H in leaves))==p
    return len(subs),len(edges)

def induced_A(p):
    # A=C_{p^2} x C_p.  C_t=<e+t f>, Q_s=<s p e+f>.
    perms=set(); total=0
    for a in range(1,p*p):
        if a%p==0: continue
        A=a%p
        for b,c in product(range(p),repeat=2):
            for d in range(1,p):
                total+=1
                C=tuple(((b+d*t)*invmod(A,p))%p for t in range(p))
                Q=tuple(((A*s+c)*invmod(d,p))%p for s in range(p))
                perms.add((C,Q))
    return total,perms

def induced_M(p):
    # M=<a,b | a^(p^2)=b^p=1, b a b^-1=a^(1+p)>.
    # Every automorphism is a->a^i b^j, b->a^(pk)b with p not dividing i.
    perms=set(); total=0
    for i in range(1,p*p):
        if i%p==0: continue
        I=i%p
        for j,k in product(range(p),repeat=2):
            total+=1
            C=tuple(((j+t)*invmod(I,p))%p for t in range(p))
            Q=tuple((I*s+k)%p for s in range(p))
            perms.add((C,Q))
    return total,perms

def expected_H(p):
    H=set()
    for alpha in range(1,p):
        ia=invmod(alpha,p)
        for beta,gamma in product(range(p),repeat=2):
            C=tuple((alpha*t+beta)%p for t in range(p))
            Q=tuple((ia*s+gamma)%p for s in range(p))
            H.add((C,Q))
    return H

for p in (3,5):
    print('A direct subgroup census',p,check_double_star(p,False))
    print('M direct subgroup census',p,check_double_star(p,True))

for p in (3,5,7):
    autA,imgA=induced_A(p)
    autM,imgM=induced_M(p)
    H=expected_H(p)
    assert imgA==H and imgM==H
    assert autA==p**3*(p-1)**2
    assert autM==p**3*(p-1)
    assert len(H)==p*p*(p-1)
    assert autA//len(H)==p*(p-1)
    assert autM//len(H)==p
    graph_aut=2*factorial(p)**2
    assert graph_aut%len(H)==0
    print(f'p={p}: graph_aut={graph_aut}, common_image={len(H)}, index={graph_aut//len(H)}, kernels=({autA//len(H)},{autM//len(H)})')
print('VERIFY_OK')
