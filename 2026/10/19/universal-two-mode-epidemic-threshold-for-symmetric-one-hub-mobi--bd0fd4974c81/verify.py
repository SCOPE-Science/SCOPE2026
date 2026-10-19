"""Exact-rational checks for a one-hotspot symmetric SIR-network threshold.

This checks finite instances of a general theorem; it is not a proof for all sizes.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A): return list(map(list,zip(*A)))

def matvec(A,v): return [sum(a*b for a,b in zip(row,v)) for row in A]

def identity(n): return [[F(i==j) for j in range(n)] for i in range(n)]

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def trace(A): return sum(A[i][i] for i in range(len(A)))

def det(A):
    a=[row[:] for row in A]; n=len(a); ans=F(1)
    for i in range(n):
        k=next((k for k in range(i,n) if a[k][i]),None)
        if k is None: return F(0)
        if k!=i: a[i],a[k]=a[k],a[i]; ans=-ans
        z=a[i][i]; ans*=z
        for j in range(i+1,n):
            if a[j][i]:
                t=a[j][i]/z
                for c in range(i+1,n): a[j][c]-=t*a[i][c]
                a[j][i]=F(0)
    return ans

def flux(n,a,variant):
    m=n-1
    if variant==0: weights=(F(1,2),F(1,3),F(1,6))
    else: weights=(F(1,5),F(3,5),F(1,5))
    u,v,w=weights
    # Mixture of identity, the undirected cycle random walk, and all-to-all mixing.
    Q=[[u*F(i==j)+v*(F((i-j)%m==1)+F((j-i)%m==1))/2+w/F(m)
        for j in range(m)] for i in range(m)]
    if m==2:  # For two vertices both neighbors coincide: deterministic swap.
        Q=[[u*F(i==j)+v*F(i!=j)+w/F(m) for j in range(m)] for i in range(m)]
    Phi=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(m):
        for j in range(m): Phi[i][j]=(1-a)*Q[i][j]
        Phi[i][-1]=Phi[-1][i]=a
    Phi[-1][-1]=1-m*a
    assert all(sum(row)==1 for row in Phi)
    assert all(Phi[i][j]==Phi[j][i] for i in range(n) for j in range(n))
    assert all(v>=0 for row in Phi for v in row)
    return Phi

def test(n,a,r,zeta,variant):
    P=flux(n,a,variant)
    E=identity(n)
    e=[F(i==n-1) for i in range(n)]
    ones=[F(1)]*n
    delta=1-n*a
    assert matvec(P,ones)==ones
    assert matvec(P,e)==[a+delta*x for x in e]
    PP=mm(P,P)
    hotspot=matvec(P,e)
    h=r*(zeta-1)
    K=[[r*PP[i][j]+h*hotspot[i]*hotspot[j] for j in range(n)] for i in range(n)]
    # Two-dimensional block: an orthonormal basis need not be built over Q.
    T=r*(1+delta*delta)+(h/n)*(1+(n-1)*delta*delta)
    D=r*r*zeta*delta*delta
    # On span{1,e}, characteristic trace/determinant use the exact basis {1,e}.
    b1=ones; b2=e
    y1=matvec(K,b1); y2=matvec(K,b2)
    assert all(y1[i]==y1[0] for i in range(n-1))
    assert all(y2[i]==y2[0] for i in range(n-1))
    a00=y1[0]; a10=y1[-1]-y1[0]
    a01=y2[0]; a11=y2[-1]-y2[0]
    assert a00+a11==T and a00*a11-a01*a10==D
    # Exact positive-definiteness condition, valid with 0<r<1 and zeta>1.
    numerator=n*(1-r)-r*(zeta-1)
    denominator=r*(1+(n-1)*zeta-n*r*zeta)
    expression=(n*(1-r)-r*(zeta-1))-denominator*delta*delta
    block_det=1-T+D
    # Actual determinant identity: directly expand rank-one update.
    assert n*block_det==expression, (n,a,r,zeta,T,D,block_det,expression)
    # Distinct leaf mixing matrices share the same T,D and epidemic threshold.
    return (T,D,block_det)

def main():
    cases=0
    for n in range(3,11):
        for a in (F(1,n),F(1,2*n),F(1,n-1)):
            for r,zeta in ((F(3,5),F(2)),(F(3,5),F(4)),(F(3,4),F(5)),(F(1,4),F(2))):
                t0=test(n,a,r,zeta,0)
                t1=test(n,a,r,zeta,1)
                assert t0==t1
                cases+=2
    print('PASS:',cases,'finite exact-rational flux/threshold comparisons')
    # Parameter boundary check at δ=0: threshold zeta*=1+n*(1-r)/r.
    for n in range(3,20):
        r=F(3,5); zeta=1+F(n)*(1-r)/r
        assert test(n,F(1,n),r,zeta,0)[2]==0
    print('PASS: 17 distinct exact neutral thresholds')

if __name__=='__main__': main()
