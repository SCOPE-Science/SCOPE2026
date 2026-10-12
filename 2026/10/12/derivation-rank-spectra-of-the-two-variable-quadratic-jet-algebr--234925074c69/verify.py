#!/usr/bin/env python3
"""Direct finite-field census of ranks of derivations of k[x,y]/(x,y)^3.

No external dependencies.  Uses direct Leibniz matrices, not block-rank arguments
from the proof.  Elements of GF(4) use polynomial basis modulo t^2+t+1.
"""
from collections import Counter
from itertools import product


def add(x,y,q):
    return x^y if q == 4 else (x+y)%q

def sub(x,y,q):
    return x^y if q == 4 else (x-y)%q

def mul(x,y,q):
    if q != 4: return (x*y)%q
    r=0
    while y:
        if y&1: r ^= x
        y >>= 1
        x <<= 1
        if x&4: x ^= 7
    return r

def inverse(x,q):
    if x == 0: raise ZeroDivisionError
    return next(y for y in range(1,q) if mul(x,y,q)==1)

def rank(mat,q):
    m=[row[:] for row in mat]
    R=len(m); C=len(m[0])
    p=0
    for c in range(C):
        piv=next((i for i in range(p,R) if m[i][c]),None)
        if piv is None: continue
        m[p],m[piv]=m[piv],m[p]
        inv=inverse(m[p][c],q)
        m[p]=[mul(v,inv,q) for v in m[p]]
        for i in range(p+1,R):
            if m[i][c]:
                a=m[i][c]
                m[i]=[sub(v,mul(a,w,q),q) for v,w in zip(m[i],m[p])]
        p+=1
        if p == R: break
    return p

def derivation_matrix(q,v):
    # v=(a,c,u,v,w,b,d,U,V,W), so D(x)=ax+cy+ux²+vxy+wy²,
    # D(y)=bx+dy+Ux²+Vxy+Wy².
    a,c,u,vv,w,b,d,U,V,W=v
    # column order x,y,x²,xy,y²; D(x²)=2xD(x), D(xy)=yD(x)+xD(y)
    # and D(y²)=2yD(y). Note coefficients are in GF(q), not integers.
    two=add(1,1,q)
    cols=[
        [a,c,u,vv,w], [b,d,U,V,W],
        [0,0,mul(two,a,q),mul(two,c,q),0],
        [0,0,b,add(a,d,q),c],
        [0,0,0,mul(two,b,q),mul(two,d,q)]
    ]
    return [list(row) for row in zip(*cols)]

def matcount(d,c,j,q):
    # number of c by d matrices of rank j
    if j>min(d,c): return 0
    # calculate Gaussian q-binomial exactly from product
    num=den=1
    for i in range(j):
        num *= q**d - q**i
        den *= q**j - q**i
    gaussian=num//den
    r=gaussian
    for i in range(j): r*=q**c-q**i
    return r

def prediction(q):
    R1=matcount(2,3,1,q)
    R2=matcount(2,3,2,q)
    Nr1=(q-1)*(q+1)**2
    G2=(q*q-1)*(q*q-q)
    if q%2:
        Nzero=q*q*(q-1)  # invertible traceless matrices
        Nother=G2-Nzero
        return {0:1,1:R1,2:R2,3:Nr1*q**5,
                4:Nr1*(q-1)*q**5+Nzero*q**6,
                5:Nother*q**6}
    return {0:1,1:R1,2:R2+(q-1)*q**6+Nr1*q**4,
            3:Nr1*q**4*(q*q-1)+(G2-(q-1))*q**6}

def main():
    for q in [2,3]:
        hist=Counter()
        for v in product(range(q),repeat=10):
            hist[rank(derivation_matrix(q,v),q)]+=1
        assert dict(hist)==prediction(q),(q,hist,prediction(q))
        assert sum(hist.values())==q**10
        print('EXHAUSTIVE',q,dict(sorted(hist.items())))
    # Exhaustive coefficient-matrix classification, independent of the proof's
    # determinant/traces derivation (uses the same direct Leibniz matrix).
    for q in [2,3,4,5]:
        observed=Counter()
        for a,c,b,d in product(range(q),repeat=4):
            A=[[a,b],[c,d]]
            T=[row[2:] for row in derivation_matrix(q,(a,c,0,0,0,b,d,0,0,0))[2:]]
            observed[(rank(A,q),rank(T,q))]+=1
        nr1=(q-1)*(q+1)**2
        g2=(q*q-1)*(q*q-q)
        if q%2:
            expect={(0,0):1,(1,2):nr1,(2,2):q*q*(q-1),
                    (2,3):g2-q*q*(q-1)}
        else:
            expect={(0,0):1,(1,1):nr1,(2,0):q-1,
                    (2,1):g2-(q-1)}
        assert dict(observed)==expect,(q,observed,expect)
        print('LINEAR_BLOCKS',q,dict(sorted(observed.items())))
    # Nonprime extension field: for every linear coefficient quadruple,
    # test diverse complete degree-two coefficient subfamilies.
    for q in [4,5]:
        seen=Counter()
        for a,c,b,d in product(range(q),repeat=4):
            for u,v,w,U,V,W in [(0,0,0,0,0,0),
                 (1,0,0,0,0,0),(0,1,0,0,1,0),
                 (1,1,1,1,1,1),(a,b,c,d,1,0),
                 (a,c,b,d,a,c),(q-1,0,b,0,a,d)]:
                params=(a,c,u,v,w,b,d,U,V,W)
                # Build directly from the Leibniz action on basis elements.
                mat=derivation_matrix(q,params)
                rr=rank(mat,q)
                assert 0<=rr<=(3 if q%2==0 else 5)
                seen[rr]+=1
        print('SAMPLED',q,dict(sorted(seen.items())))
    for q in [2,3,4,5,7,8,9,11]:
        assert sum(prediction(q).values())==q**10
    print('FORMULA_NORMALIZATION_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
