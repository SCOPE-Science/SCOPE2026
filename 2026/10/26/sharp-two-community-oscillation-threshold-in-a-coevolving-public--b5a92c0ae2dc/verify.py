"""Exact arithmetic checks for a two-community public-goods opinion cycle.

Run with: python3 verify.py.  Standard-library only.  All arithmetic is rational.
The checks support, rather than replace, the symbolic proof.
"""
from fractions import Fraction as F
from itertools import product


def network(s, eps):
    n = 2*s
    w = [[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                w[i][j] = eps/(s-1) if i//s == j//s else (1-eps)/s
    assert all(sum(row) == 1 for row in w)
    assert all(w[i][j] == w[j][i] for i in range(n) for j in range(n))
    return w


def update(y, w, p, theta):
    m = [sum(a*b for a, b in zip(row,y)) for row in w]
    x1 = [int(v>theta) for v in m]
    y1 = [p*v+(1-p)*a for v,a in zip(m,x1)]
    return x1,y1,m


def best_payoff(z, m, others, n, r, alpha, beta, lam):
    # Original single-player payoff, evaluated at its unique best opinion given z.
    y = (beta*m+lam*z)/(beta+lam)
    pgg = r*(others+z)/n-z
    fj = -F(1,2)*(y-m)**2 # difference of original quadratic opinion payoff only (variance constant)
    consistency = -F(1,2)*(z-y)**2
    return alpha*pgg+beta*fj+lam*consistency


checks=0
for s in (2,3,4,5):
    n=2*s
    for r in (F(3,2), F(n-1,1)):
        if not 1<r<n:
            continue
        for alpha,beta,lam in ((F(1,5),F(2,5),F(2,5)),(F(1,10),F(3,10),F(6,10)),(F(1,20),F(9,20),F(1,2))):
            p=beta/(beta+lam)
            theta=F(1,2)+alpha*(1-r/n)*(beta+lam)/(beta*lam)
            if not (F(1,2)<theta<1):
                continue
            eps_star=(1-theta)*(1-p)/(1-2*p*(1-theta))
            assert 0<eps_star<F(1,2)
            for fraction in (F(1,10),F(1,3),F(2,3),F(9,10)):
                eps=eps_star*fraction
                w=network(s,eps)
                D=1-p+2*p*eps
                high=(1-p+p*eps)/D
                low=p*eps/D
                y=[high]*s+[low]*s
                x=[1]*s+[0]*s
                x1,y1,m=update(y,w,p,theta)
                assert x1==[0]*s+[1]*s
                assert y1==[low]*s+[high]*s
                assert m==[eps/D]*s+[1-eps/D]*s
                x2,y2,m2=update(y1,w,p,theta)
                assert (x2,y2)==(x,y)
                assert 0<theta-m[0] and 0<m[-1]-theta
                for i in range(n):
                    others=sum(x)-x[i]
                    v0=best_payoff(0,m[i],others,n,r,alpha,beta,lam)
                    v1=best_payoff(1,m[i],others,n,r,alpha,beta,lam)
                    assert (v1>v0)==bool(x1[i])
                    assert (v1-v0==alpha*(r/n-1)+beta*lam/(beta+lam)*(m[i]-F(1,2)))
                checks+=1
            # Beyond the critical mixing, the specific anti-phase profile is not a cycle.
            eps=eps_star+(F(1,2)-eps_star)/2
            D=1-p+2*p*eps
            y=[(1-p+p*eps)/D]*s+[p*eps/D]*s
            x1,y1,m=update(y,network(s,eps),p,theta)
            assert m[-1]<=theta
            assert x1!=[0]*s+[1]*s
            checks+=1

# A fully explicit four-player complete, loopless, symmetric primitive network.
s=2;n=4;r=F(3); alpha=F(1,5);beta=lam=F(2,5)
p=F(1,2);theta=F(3,4);eps=F(1,8)
w=network(s,eps)
assert w==[[F(0), F(1,8), F(7,16), F(7,16)],
           [F(1,8), F(0), F(7,16), F(7,16)],
           [F(7,16), F(7,16), F(0), F(1,8)],
           [F(7,16), F(7,16), F(1,8), F(0)]]
x=[1,1,0,0];y=[F(9,10)]*2+[F(1,10)]*2
x1,y1,m=update(y,w,p,theta)
assert m==[F(1,5)]*2+[F(4,5)]*2
assert (x1,y1)==([0,0,1,1], [F(1,10)]*2+[F(9,10)]*2)
assert update(y1,w,p,theta)[:2]==(x,y)
assert F(1,6)==(1-theta)*(1-p)/(1-2*p*(1-theta))
# Supnorm errors contract by p while the strict-branch choices persist.
perturb=(F(1,100),-F(1,100),F(1,200),-F(1,200))
start=[v+d for v,d in zip(y,perturb)]
err=max(abs(q) for q in perturb)
assert err<F(1,20)
for t in range(16):
    x1,start,_=update(start,w,p,theta)
    target_x=([0,0,1,1] if t%2==0 else [1,1,0,0])
    target_y=([F(1,10)]*2+[F(9,10)]*2 if t%2==0 else [F(9,10)]*2+[F(1,10)]*2)
    assert x1==target_x
    assert max(abs(a-b) for a,b in zip(start,target_y))<=p**(t+1)*err
    checks+=1
assert all(w[i][j]>0 for i in range(4) for j in range(4) if i!=j)
print('PASS:',checks,'exact cycle/critical/perturbation cases; explicit original-payoff comparisons; nondegenerate four-agent witness')
