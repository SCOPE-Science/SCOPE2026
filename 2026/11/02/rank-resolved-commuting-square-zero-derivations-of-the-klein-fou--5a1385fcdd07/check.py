#!/usr/bin/env python3
"""Independent finite-field matrix-equation checks for commuting square-zero derivations.

For q=2 and q=4, enumerate every derivation via its generator images, form
its action on 1,x,y,xy directly, test D^2=0 and pairwise commutation.
No classification of commuting nilpotent matrices is used.
"""
from itertools import product

def mul(a,b,q):
    if q==2:
        return a & b
    p=0
    for i in range(2):
        if b>>i&1:p ^= a<<i
    if p&4:p^=0b111   # x^2=x+1
    return p

def mm(A,B,q):
    return tuple(tuple(
        __import__('functools').reduce(lambda s,k:s^mul(A[i][k],B[k][j],q),range(4),0)
        for j in range(4)) for i in range(4))

def rank(A,q):
    C=[list(r) for r in A];r=0
    for j in range(4):
        k=next((i for i in range(r,4) if C[i][j]),None)
        if k is None:continue
        C[k],C[r]=C[r],C[k]
        inv=next(x for x in range(1,q) if mul(x,C[r][j],q)==1)
        C[r]=[mul(inv,x,q) for x in C[r]]
        for i in range(4):
            if i!=r and C[i][j]:
                a=C[i][j]
                C[i]=[v^mul(a,w,q) for v,w in zip(C[i],C[r])]
        r+=1
    return r

def matrix(p):
    a,b,c,d,e,h,i,j=p
    # D(x)=a+bx+cy+dxy; D(y)=e+hx+iy+jxy
    # D(xy)=xD(y)+yD(x)=e*x+a*y+(b+i)*xy, char 2
    return ((0,a,e,0),(0,b,h,e),(0,c,i,a),(0,d,j,b^i))

for q in (2,4):
    square=[]
    Z=((0,)*4,)*4
    for p in product(range(q),repeat=8):
        A=matrix(p)
        if mm(A,A,q)==Z:square.append(A)
    expected=q**4+q**3-q
    assert len(square)==expected,(q,len(square),expected)
    hist={r:sum(rank(A,q)==r for A in square) for r in (0,1,2)}
    assert hist=={0:1,1:(q-1)*(q+1)**2,2:q*q*(q*q-1)},(q,hist)
    rankcache={A:rank(A,q) for A in square}
    from collections import Counter
    rankpairs=Counter()
    count2=0
    for A in square:
        for B in square:
            if mm(A,B,q)==mm(B,A,q):
                count2+=1
                rankpairs[(rankcache[A],rankcache[B])]+=1
    N=q*q+q+1
    formula=lambda m:1+N*(2*q**(2*m)-(q+1)*q**m+q-1)
    assert count2==formula(2),(q,count2,formula(2))
    def polyproduct(m, choices):
        # explicit independent coefficient convolution of per-coordinate rank weights
        out={():1}
        for _ in range(m):
            out={key+(rank,):coef*weight for key,old in out.items() for rank,weight in choices.items() for coef in [old]}
        return out
    def predicted(m):
        N=q*q+q+1
        terms=[
            (q+2,{0:1,1:q*q-1}),
            (N-1,{0:1,1:q-1,2:q*q-q}),
            (q*q,{0:1,2:q*q-1}),
            (-(q+1)**2,{0:1,1:q-1}),
            (-q*q*(q+1),{0:1,2:q-1})]
        ans=Counter({(0,)*m:1})
        for factor,choices in terms:
            for key,weight in polyproduct(m,choices).items():
                ans[key]+=factor*(weight-(1 if key==(0,)*m else 0))
        return {key:value for key,value in ans.items() if value}
    assert dict(rankpairs)==predicted(2),(q,'rank_pair_mismatch',rankpairs,predicted(2))
    print(f'q={q} all_derivations={q**8} square_zero={len(square)} rank_hist={hist} commuting_pairs={count2} expected={formula(2)} rank_pairs={dict(sorted(rankpairs.items()))}')
    if q==2:
        ranktriples=Counter()
        count3=0
        for A in square:
            for B in square:
                if mm(A,B,q)!=mm(B,A,q):continue
                for C in square:
                    if mm(A,C,q)==mm(C,A,q) and mm(B,C,q)==mm(C,B,q):
                        count3+=1
                        ranktriples[(rankcache[A],rankcache[B],rankcache[C])]+=1
        assert count3==formula(3)
        assert dict(ranktriples)==predicted(3),(ranktriples,predicted(3))
        print(f'q={q} commuting_triples={count3} expected={formula(3)}')
print('ALL_COMMUTING_SQUARE_ZERO_DERIVATION_CHECKS_OK')
