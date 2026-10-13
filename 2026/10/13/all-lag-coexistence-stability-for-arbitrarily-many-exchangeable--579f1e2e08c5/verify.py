"""Reproduce algebraic stability identities for a symmetric coupled SIRS model.

Python 3 standard library only. Checks representative rational parameter tuples;
the accompanying proof establishes the identities for all admissible parameters.
"""
from fractions import Fraction as F
from itertools import permutations, product

def add(p, q):
    return [((p[i] if i < len(p) else 0)+(q[i] if i < len(q) else 0)) for i in range(max(len(p),len(q)))]
def neg(p): return [-x for x in p]
def mul(p, q):
    z = [F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): z[i+j] += x*y
    return z

def det3(m):
    result = [F(0)]
    for perm in permutations(range(3)):
        inversions = sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        q=mul(m[0][perm[0]],mul(m[1][perm[1]],m[2][perm[2]]))
        result=add(result,neg(q) if inversions%2 else q)
    return result

def polynomial_coefficients(a,b,c,u,v):
    z0=lambda t:[t]
    z1=lambda t:[t,F(1)]
    A=[[z1(u+b),z0(a+b),z0(-v)],
       [z0(-u),z1(F(0)),z0(v)],
       [z0(0),z0(-c),z1(c)]]
    return det3(A)

def expected(a,b,c,u,v):
    return [c*(u*(a+b)+b*v),u*(a+b)+c*(b+u+v),b+c+u,F(1)]

def hurwitz_delta(a,b,c,u,v):
    return (b+u)*(u*(a+b)+c*(b+u+c))+c*v*(u+c)

def multiply_jacobian(n,a,b,c,u,I,k,w,vector):
    out=[F(0)]*(3*n)
    for i in range(n):
        si,ii,pi=vector[3*i:3*i+3]
        external=sum(vector[3*j+2] for j in range(n) if j!=i)
        vself=a*I*k
        vp=vself*(pi+w*external)
        out[3*i]=-(b+u)*si-(a+b)*ii+vp
        out[3*i+1]=u*si-vp
        out[3*i+2]=c*(ii-pi)
    return out

checks=0
for a,b,c,u in product([F(1,7),F(1),F(11)], [F(1,11),F(2)], [F(1,1000),F(2),F(200)], [F(1,19),F(1),F(6)]):
    for n,w,k,I in product([2,3,7],[F(0),F(1,2),F(1)],[F(0),F(2,3),F(8)],[F(1,10)]):
        for mode in ['common','contrast']:
            gain=1+(n-1)*w if mode=='common' else 1-w
            v=a*I*k*gain
            got=polynomial_coefficients(a,b,c,u,v)
            assert got==expected(a,b,c,u,v)
            A0,A1,A2,_=got
            assert A0>0 and A1>0 and A2>0
            assert A2*A1-A0==hurwitz_delta(a,b,c,u,v)>0
            vec=[F(0)]*(3*n)
            modes=[F(1)]*n if mode=='common' else [F(1),F(-1)]+[F(0)]*(n-2)
            for i,t in enumerate(modes):
                vec[3*i:3*i+3]=[t*F(3,7),t*F(4,7),t*F(5,7)]
            gotJ=multiply_jacobian(n,a,b,c,u,I,k,w,vec)
            mat=[[-(b+u),-(a+b),v], [u,F(0),-v],[F(0),c,-c]]
            base=[F(3,7),F(4,7),F(5,7)]
            expectJ=[sum(mat[i][j]*base[j] for j in range(3)) for i in range(3)]
            assert all(gotJ[3*i+t]==modes[i]*expectJ[t] for i in range(n) for t in range(3))
            checks+=1
print(f'VERIFY_OK {checks} exact rational characteristic-polynomial and invariant-mode checks')
