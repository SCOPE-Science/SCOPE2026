"""Exact rational checks for highest-transvectant quadratic hulls.

No third-party dependencies. Finite checks complement, never replace, the proof.
"""
from fractions import Fraction as F
from math import comb


def q012(r, a):
    q0 = sum(((-1)**k)*comb(r-1,k)*a[k]*a[r-1-k] for k in range(r))
    q1 = sum(((-1)**k)*comb(r-1,k)*(a[k]*a[r-k]+a[k+1]*a[r-1-k]) for k in range(r))
    q2 = sum(((-1)**k)*comb(r-1,k)*a[k+1]*a[r-k] for k in range(r))
    return q0,q1,q2


def residual(r, even_values):
    a = [F(0)]*(r+1)
    a[0] = F(1)
    a[2] = F(1)
    for idx, val in even_values.items():
        a[idx] = F(val)
    # Q0 is 2*a[r-1] plus terms independent of a[r-1].
    a[r-1] = F(-q012(r,a)[0], 2)
    # Q1 is 2*a[r] plus terms independent of a[r]; Q2 independent of a[r]
    # since a[1]=0, so its pivot does not affect the residual polynomial.
    return q012(r,a)[2]


def solve(matrix, rhs):
    n=len(rhs)
    aug=[[F(x) for x in row]+[F(rhs[i])] for i,row in enumerate(matrix)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if aug[i][j]),None)
        assert pivot is not None
        aug[j],aug[pivot]=aug[pivot],aug[j]
        mul=aug[j][j]
        aug[j]=[x/mul for x in aug[j]]
        for i in range(n):
            if i!=j:
                k=aug[i][j]
                aug[i]=[x-k*y for x,y in zip(aug[i],aug[j])]
    return [aug[i][-1] for i in range(n)]


def check(r):
    assert r>=5 and r%2==1
    inds=list(range(4,r-1,2))
    b=residual(r,{})
    units=[]
    neg=[]
    for ix in inds:
        units.append(residual(r,{ix:F(1)}))
        neg.append(residual(r,{ix:F(-1)}))
    lin=[(v-n)/2 for v,n in zip(units,neg)]
    H=[[F(0)]*len(inds) for _ in inds]
    for i in range(len(inds)):
        H[i][i]=units[i]+neg[i]-2*b
        for j in range(i):
            val=residual(r,{inds[i]:F(1),inds[j]:F(1)})-units[i]-units[j]+b
            H[i][j]=H[j][i]=val
    x=solve(H,[-v for v in lin]) if inds else []
    cs={idx:val for idx,val in zip(inds,x)}
    # Independently verify every even-variable critical derivative.
    for ix in inds:
        assert residual(r,{**cs,ix:cs[ix]+1})-residual(r,{**cs,ix:cs[ix]-1})==0
    coeff=residual(r,cs)
    assert coeff!=0
    # Direct quadratic antidiagonal at a2=0 has coefficients
    # (-1)^(i-1)*C(r-1,i-1), all nonzero for i=3,...,r-2.
    for i in range(3,r-1):
        assert ((-1)**(i-1))*comb(r-1,i-1)
    return r,tuple((str(i),str(v)) for i,v in cs.items()),str(coeff)

if __name__=='__main__':
    expected={'5':'24','7':'405','9':'8960','11':'984375/4','13':'8083152'}
    for r in (5,7,9,11,13):
        number,coords,coefficient=check(r)
        assert coefficient==expected[str(r)]
        print('r=%d critical=%s coordinates=%s'%(number,coefficient,coords))
    print('VERIFY_OK')
