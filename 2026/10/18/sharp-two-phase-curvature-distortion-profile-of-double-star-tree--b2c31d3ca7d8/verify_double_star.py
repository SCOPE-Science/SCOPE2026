"""Independent numerical and exact checks for two-center tree curvature profiles.
Run: python verify_double_star.py
"""
from fractions import Fraction
from math import sqrt, isclose
from scipy.optimize import minimize


def candidate(a, b, k):
    assert 1 <= a <= b and 0 <= k <= 2/(a+b+1)+1e-13
    h = 4/(2*b+1 + sqrt(1+4*a*(b+1)))
    if k <= h:
        t = (k*(a+b) + sqrt(k*k*(a-b)**2 + 16*a*b))/(2*(2-k))
        y=1.0
    else:
        t=a*k*(b+1)/(2-k*(b+1))
        y=k*t/(2-k*b)
    return 1.0,y,t,h

def curvatures(a,b,x,y,t):
    return (2*x/(a*x+t), 2*y/(b*y+t),2*t/(a*x+t)+2*t/(b*y+t)-2)

def scalar_root(a,b,k):
    # Derive the lower bound without using the closed-form branch formulas.
    lo,hi=0.0,2.0*(a+b+1)+10
    for _ in range(120):
        t=(lo+hi)/2
        B=max(1.0,k*t/(2-k*b))
        f=2*t/(t+a)+2*t/(t+b*B)-2
        if f < k: lo=t
        else: hi=t
    return (lo+hi)/2

tests=0;optim=0
for a in range(1,12):
    for b in range(a,12):
        end=2/(a+b+1)
        h=4/(2*b+1+sqrt(1+4*a*(b+1)))
        assert 0<h<=end+1e-12,(a,b,h,end)
        for scale in (0,0.05,0.3,0.7,0.99,1,1.01,1.2,1.5,3,6):
            k=(min(scale*h,end)) if scale<=1 else (h+(end-h)*min((scale-1)/5,1))
            x,y,t,_=candidate(a,b,k)
            c=curvatures(a,b,x,y,t)
            assert min(c)+1e-9>=k,(a,b,k,x,y,t,c)
            assert 1-1e-9<=y<=t+1e-9,(a,b,k,y,t)
            assert t>=1-1e-10
            root=scalar_root(a,b,k)
            assert isclose(root,t,abs_tol=2e-9,rel_tol=2e-9),(a,b,k,root,t)
            tests+=1

# An independent constrained nonlinear solver on normalized orbit weights.
# This is a stress test, not the proof of global optimality.
for a in range(1,9):
    for b in range(a,9):
        end=2/(a+b+1)
        h=4/(2*b+1+sqrt(1+4*a*(b+1)))
        for k in [0.0,h*0.7, h, (h+end)/2,end]:
            x,y,t,_=candidate(a,b,k)
            def objective(z):return z[2]
            def constraints(z):
                return [z[0]-1,z[1]-1,z[2]-1,z[2]-z[0],z[2]-z[1],*(v-k for v in curvatures(a,b,*z))]
            res=minimize(objective,[x,y,t],method='SLSQP',bounds=[(1,None)]*3,
                         constraints=[{'type':'ineq','fun':constraints}],
                         options={'ftol':1e-11,'maxiter':200})
            assert res.success or abs(res.fun-t)<1e-6,(a,b,k,res.message,res.fun,t)
            assert abs(res.fun-t)<3e-6,(a,b,k,res.fun,t)
            optim+=1

# Boundary check done with rational values, not float rounding.
for a in range(1,25):
    for b in range(a,25):
        m=a+b+1;k=Fraction(2,m)
        t=Fraction(b+1);x=Fraction(1);y=Fraction(b+1,a+1)
        assert tuple(Fraction(2)*p for p in [x/(a*x+t),y/(b*y+t)])==(k,k)
        assert Fraction(2)*t/(a*x+t)+Fraction(2)*t/(b*y+t)-2==k
        assert y<=t
print(f"PASS: {tests} closed-form/root/curvature checks; {optim} independent SLSQP optimizations; 300 exact rational endpoint profiles")

# Independently recover the curvature of each edge from the original
# optimal-transport (Wasserstein-1) definition, using an LP, not a formula.
from scipy.optimize import linprog
from collections import deque

def direct_wasserstein_curvatures(a,b,x,y,t):
    n=a+b+2
    edges=[(0,1,t)]+[(0,i,x) for i in range(2,a+2)]+[(1,j,y) for j in range(a+2,n)]
    adj=[[] for _ in range(n)]
    wt={}
    for u,v,w in edges:
        adj[u].append(v);adj[v].append(u);wt[u,v]=wt[v,u]=w
    degrees=[sum(wt[v,z] for z in adj[v]) for v in range(n)]
    distances=[]
    for s in range(n):
        d=[n+1]*n;d[s]=0;queue=deque([s])
        while queue:
            z=queue.popleft()
            for v in adj[z]:
                if d[v]>d[z]+1:d[v]=d[z]+1;queue.append(v)
        distances.append(d)
    cost=[distances[i][j] for i in range(n) for j in range(n)]
    import numpy as np
    Aeq=np.zeros((2*n,n*n))
    for i in range(n):
        for j in range(n):
            Aeq[i,i*n+j]=1
            Aeq[n+j,i*n+j]=1
    eps=0.001
    def mu(i):
        p=np.zeros(n);p[i]=1-eps
        for j in adj[i]:p[j]=eps*wt[i,j]/degrees[i]
        return p
    results=[]
    for u,v,_ in edges:
        r=linprog(cost,A_eq=Aeq,b_eq=np.r_[mu(u),mu(v)],bounds=(0,None),method='highs')
        assert r.success,r.message
        results.append((1-r.fun)/eps)
    return results

transport_tests=0
for a in range(1,5):
    for b in range(a,5):
        for p in (0.0,0.37,1.0):
            k=p*2/(a+b+1)
            x,y,t,_=candidate(a,b,k)
            transport=direct_wasserstein_curvatures(a,b,x,y,t)
            expected=[curvatures(a,b,x,y,t)[2]]+[curvatures(a,b,x,y,t)[0]]*a+[curvatures(a,b,x,y,t)[1]]*b
            assert max(abs(i-j) for i,j in zip(transport,expected))<2e-8,(a,b,k,transport,expected)
            transport_tests+=len(transport)
print(f"PASS: {transport_tests} direct Wasserstein transport LP curvature comparisons")
