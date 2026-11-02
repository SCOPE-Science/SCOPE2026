"""Reproducible finite checks for the ring-reset convex-order theorem.
Uses only the Python standard library. Finite computations are not a proof.
"""
import math

checks=0

def assert_close(x,y,tol=1e-9):
    global checks
    assert abs(x-y) <= tol*max(1.,abs(x),abs(y)),(x,y)
    checks+=1

def phi(L,D,s,d):
    k=math.sqrt(s/D)
    return math.cosh(k*(L/2-d))/math.cosh(k*L/2)

def beta(L,D,s,dist):
    return sum(w*phi(L,D,s,d) for d,w in dist)

def flt(L,D,r,s,d0,dist):
    b=beta(L,D,r+s,dist)
    return (s*phi(L,D,r+s,d0)+r*b)/(s+r*b)

def mfpt(L,D,r,d0,dist):
    return (1-phi(L,D,r,d0))/(r*beta(L,D,r,dist))

def u(L,d):
    return d*(L-d)

def d_from_u(L,x):
    return (L-math.sqrt(L*L-4*x))/2

def endpoints(L,a,b,m):
    ua,ub=u(L,a),u(L,b)
    w=(ub-m)/(ub-ua)
    return [(a,w),(b,1-w)]

# Independently integrate the unreset killed Brownian semigroup's
# ODE solution by a centered second-difference equation, then
# solve the resetting BVP as a dense linear system at interior nodes.
def solve_linear(A,b):
    n=len(b)
    A=[x[:] for x in A]; b=b[:]
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(A[i][j]))
        assert abs(A[p][j])>1e-14
        A[j],A[p]=A[p],A[j]; b[j],b[p]=b[p],b[j]
        q=A[j][j]
        for k in range(j,n): A[j][k]/=q
        b[j]/=q
        for i in range(j+1,n):
            q=A[i][j]
            if q==0:continue
            for k in range(j,n):A[i][k]-=q*A[j][k]
            b[i]-=q*b[j]
    for i in range(n-1,-1,-1):
        b[i]-=sum(A[i][j]*b[j] for j in range(i+1,n))
    return b

def finite_diff_F(L,D,r,s,d0,dist,n=61):
    # Choose all reset locations on the finite-difference mesh.
    h=L/n
    bvec=[0.]*(n-1)
    A=[[0.]*(n-1) for _ in range(n-1)]
    c=D/(h*h)
    for i in range(n-1):
        A[i][i]=2*c+r+s
        if i: A[i][i-1]=-c
        if i<n-2: A[i][i+1]=-c
        if i==0 or i==n-2:bvec[i]+=c
        for d,w in dist:
            j=round(d/h)
            assert 1<=j<=n-1 and abs(j*h-d)<1e-12
            A[i][j-1]-=r*w
    solution=solve_linear(A,bvec)
    j=round(d0/h)
    assert abs(j*h-d0)<1e-12
    return solution[j-1]

for L in (2.0,4.0,5.0):
    for D in (.5,1.0,2.0):
        a,b=L/8,L*3/8
        ua,ub=u(L,a),u(L,b)
        for t in (.12,.32,.51,.74,.89):
            m=t*ua+(1-t)*ub
            center=[(d_from_u(L,m),1.)]
            spread=endpoints(L,a,b,m)
            # mean of 'mid' not equal to m; instead construct a true
            # mean-preserving spread of the point mass center.
            left=m-(m-ua)*.5
            right=m+(ub-m)*.5
            mid=[(d_from_u(L,left),t),(d_from_u(L,right),1-t)]
            assert_close(sum(w*u(L,d) for d,w in mid),m)
            for rate in (.05,.4,2.0,9.0):
                for s in (.08,.8,4.0):
                    f0=flt(L,D,rate,s,L/4,center)
                    fm=flt(L,D,rate,s,L/4,mid)
                    fe=flt(L,D,rate,s,L/4,spread)
                    assert f0<fm<fe,(L,D,t,rate,s,f0,fm,fe)
                    checks+=1
                m0=mfpt(L,D,rate,L/4,center)
                mm=mfpt(L,D,rate,L/4,mid)
                me=mfpt(L,D,rate,L/4,spread)
                assert m0>mm>me,(L,D,t,rate,m0,mm,me)
                checks+=1
            for r in (.002*D/L**2,.004*D/L**2,.006*D/L**2):
                gain=mfpt(L,D,r,L/4,center)-mfpt(L,D,r,L/4,spread)
                coeff=u(L,L/4)*(ub-m)*(m-ua)/(48*D**3)
                assert abs((gain/r**2)/coeff-1)<.02, (gain/r**2,coeff)
                checks+=1
# Dense independent generator check on a mesh with reset distribution on nodes.
for n in (30,60):
    L=3.0;D=1.25; r=.8; s=.5
    dist=[(L*6/n, .3),(L*12/n,.7)]
    d0=L*9/n
    direct=finite_diff_F(L,D,r,s,d0,dist,n=n)
    exact=flt(L,D,r,s,d0,dist)
    assert abs(direct-exact)<.0008,(n,direct,exact)
    checks+=1
# Strict convexity via analytic derivative in the free first-passage-cost coordinate.
for k in (.2,.7,1.1,3.0):
    for y in (.01,.1,.5,1.0):
        fpp=k*(k*y*math.cosh(k*y)-math.sinh(k*y))/(4*y**3)
        assert fpp>0
        checks+=1
# High-frequency advantage of endpoint-mixed protocol over its deterministic cost match.
L,D,a,b=4.,1.5,.3,1.8
m=.45*u(L,a)+.55*u(L,b)
cent=[(d_from_u(L,m),1.)]
ext=endpoints(L,a,b,m)
for k in (8.,12.,18.):
    r=D*k*k
    ratio=mfpt(L,D,r,1.1,ext)/mfpt(L,D,r,1.1,cent)
    expected=math.exp(-(d_from_u(L,m)-a)*k)/.45
    assert abs(ratio/expected-1)<.03, (ratio,expected)
    checks+=1
print('PASS',checks,'finite checks')
