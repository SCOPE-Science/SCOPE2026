#!/usr/bin/env python3
"""Direct coefficient-space rank enumerations for finite Alexander quandle algebras."""
from collections import Counter
from itertools import product
from math import prod


def rank_mod_p(rows,p,n):
    if p==2:
        basis={}
        for row in rows:
            bits=sum((int(v)&1)<<i for i,v in enumerate(row))
            while bits:
                pivot=bits.bit_length()-1
                if pivot in basis:bits^=basis[pivot]
                else:
                    basis[pivot]=bits;break
        return len(basis)
    x=[list(row) for row in rows]
    r=0
    for c in range(n):
        i=next((i for i in range(r,n) if x[i][c]%p),None)
        if i is None:continue
        x[r],x[i]=x[i],x[r]
        inv=pow(int(x[r][c]),-1,p)
        x[r]=[(y*inv)%p for y in x[r]]
        for i in range(n):
            if i!=r and x[i][c]:
                t=x[i][c]
                x[i]=[(a-t*b)%p for a,b in zip(x[i],x[r])]
        r+=1
    return r


def elementary(group, f, x):
    return tuple((f[i](x[i]))%group[i] for i in range(len(group)))


def test(group, multipliers, q, predict_left, predict_right, expected_zero):
    assert q in (2,3)
    X=list(product(*[range(n) for n in group]))
    n=len(X);idx={x:i for i,x in enumerate(X)}
    phi=lambda x:tuple((a*v)%d for a,v,d in zip(multipliers,x,group))
    beta=lambda x:tuple(((1-a)*v)%d for a,v,d in zip(multipliers,x,group))
    table=[[idx[tuple((a+b)%d for a,b,d in zip(phi(x),beta(y),group))] for y in X] for x in X]
    left=Counter();right=Counter()
    # Every linear map, fixed element, computed directly from the multiplication table;
    # no group-ring or Fourier formulas enter the verification.
    for coeff in product(range(q),repeat=n):
        # Columns for L_u: u*e_j;  columns for R_u: e_j*u.
        colsL=[[0]*n for _ in range(n)]
        colsR=[[0]*n for _ in range(n)]
        for i,c in enumerate(coeff):
            if c:
                for j in range(n):
                    colsL[j][table[i][j]]=(colsL[j][table[i][j]]+c)%q
                    colsR[j][table[j][i]]=(colsR[j][table[j][i]]+c)%q
        left[rank_mod_p(colsL,q,n)]+=1
        right[rank_mod_p(colsR,q,n)]+=1
    assert dict(left)==predict_left,(group,left,predict_left)
    assert dict(right)==predict_right,(group,right,predict_right)
    from_left=sum(c*q**(n-r) for r,c in left.items())
    from_right=sum(c*q**(n-r) for r,c in right.items())
    assert from_left==from_right==expected_zero,(group,from_left,from_right,expected_zero)
    print('CHECK_OK',group,'q',q,'left',dict(sorted(left.items())),
          'right',dict(sorted(right.items())),'zero_pairs',from_left)


def polynomial_mul(P,Q):
    C=Counter()
    for i,a in P.items():
        for j,b in Q.items():C[i+j]+=a*b
    return dict(C)


def expected(q,N,h,k,orbits,m):
    # q=p^f, H=C_(p^a) times a p'-group with Frobenius orbit sizes in orbits.
    left={0:1};right={0:q**(N-h)};Z=q**(N-h)
    for d in orbits:
        Q=q**d
        localL={0:1}
        localR={0:1}
        for t in range(1,m+1):
            localL[d*t]=Q**(k*t)-Q**(k*(t-1))
            localR[k*d*t]=(Q-1)*Q**(t-1)
        left=polynomial_mul(left,localL)
        right=polynomial_mul(right,localR)
        Z*=Q**(k*m)+(Q-1)*sum(Q**(t-1+k*(m-t)) for t in range(1,m+1))
    assert sum(left.values())==sum(right.values())==q**N
    return left,right,Z

if __name__=='__main__':
    # H=C_3 (modular chain length 3), k=1.
    L,R,Z=expected(3,3,3,1,[1],3)
    test((3,),(2,),3,L,R,Z)
    # H=C_2 (modular), k=2, nonlatin core quandle.
    L,R,Z=expected(2,4,2,2,[1],2)
    test((4,),(3,),2,L,R,Z)
    # H=C_3 (modular), k=2, nonlatin core quandle.
    L,R,Z=expected(3,6,3,2,[1],3)
    test((6,),(5,),3,L,R,Z)
    # H=C_2 x C_3 = C_6, q=2, k=2: Frobenius orbit sizes 1,2.
    L,R,Z=expected(2,12,6,2,[1,2],2)
    test((12,),(11,),2,L,R,Z)
    print('VERIFY_OK')
