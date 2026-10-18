"""Standalone finite diagnostics for exact finite-memory fractional-logistic critical law.
Run: python3 verify_critical_gl.py ; requires only Python standard library.
Finite tests are illustrative and do not replace the analytic proof.
"""
from fractions import Fraction
from math import gamma, isclose

def weights(q, M):
    gg = [1.0]
    for j in range(1,M+1):
        gg.append(gg[-1]*(j-1-q)/j)
    return gg

def exact_weights(q, M):
    g=[Fraction(1)]
    for j in range(1,M+1):g.append(g[-1]*(j-1-q)/j)
    return g

def parameters(q,M):
    g=weights(q,M)
    T=sum(g)
    r=1+T
    p=[q+T]+[-g[j] for j in range(2,M+1)]
    tau=sum((j+1)*p[j] for j in range(M))
    formula=T*(1+q*M/(1-q)) if q < 1 else 1.
    return r,p,tau,formula,T

# Exact fractional arithmetic proves each finite test identity, not its arbitrary-M extension.
for q in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
    for M in range(1,16):
        g=exact_weights(q,M)
        T=sum(g)
        p=[q+T]+[-g[j] for j in range(2,M+1)]
        assert sum(p)==1
        assert all(x>0 for x in p)
        tau=sum((j+1)*p[j] for j in range(M))
        assert tau==T*(1+q*M/(1-q))
        assert T==Fraction(1)-sum(-g[j] for j in range(1,M+1))
        assert tau>=1
print('Exact rational identities: 45 cases PASS')

# Exact local identity of renewal potential E_{n+1}-E_n=-r*x_n^2.
def trajectory(q,M,N,initial=0.07):
    r,p,tau,formula,T=parameters(q,M)
    assert isclose(tau,formula,rel_tol=1e-10,abs_tol=1e-10)
    delta=p[0]/r
    assert initial<delta
    w=[sum(p[j:]) for j in range(M)]
    window=[initial*(1+0.001*j) for j in range(M)]  # most recent first
    assert max(window)<delta
    E=sum(wj*xj for wj,xj in zip(w,window))
    for n in range(N):
        xnew=sum(pj*xj for pj,xj in zip(p,window))-r*window[0]**2
        assert 0<xnew<delta
        new=[xnew]+window[:-1]
        Enew=sum(wj*xj for wj,xj in zip(w,new))
        assert abs(Enew-E+r*window[0]**2)<1e-11
        window,E=new,Enew
    return (N*window[0],tau/r,delta, E)

for q,M,N in [(0.3,1,100000),(0.5,2,100000),(0.5,5,100000),(0.4,12,120000),(0.7,30,150000),(1.,8,100000)]:
    v,l,delta,E=trajectory(q,M,N)
    err=abs(v/l-1)
    print('q=',q,'M=',M,'n=',N,'n*x_n=',round(v,7),'target=',round(l,7),'relative=',round(err,6))
    assert err<0.025, (q,M,err)
print('Critical finite trajectory tests PASS')

for q in [0.25,0.5,0.8]:
    r,p,tau,form,T=parameters(q,10000)
    approx=(q/gamma(2-q))*10000**(1-q)
    assert abs(tau/approx-1)<0.002
print('Memory-scaling numerical asymptotics PASS')
