"""Direct spectral, determinant, KKT and numerical checks for a two-block conductance-price theorem."""
import itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize


def analytic(p, q, P, Q, B=1.0):
    assert p >= 2 and q >= 2 and P > 0 and Q > 0 and B > 0
    N = p + q
    lam = (N - 1) / B
    if P >= 2 * p / (N - 1) and Q >= 2 * q / (N - 1):
        regime = 'bipartite'
        a, b, c = 0., 0., B / (p * q)
    elif Q < 2 * q / (N - 1) and P >= 2 - (q - 1) * Q / q:
        regime = 'A-off'
        E = q - (q - 1) * Q / 2
        c = 1 / (lam * E)
        V = 2 / (lam * Q)
        a, b = 0., (V - p * c) / q
    elif P < 2 * p / (N - 1) and Q >= 2 - (p - 1) * P / p:
        regime = 'B-off'
        F = p - (p - 1) * P / 2
        c = 1 / (lam * F)
        U = 2 / (lam * P)
        a, b = (U - q * c) / p, 0.
    else:
        regime = 'all'
        D = p*q - q*(p-1)*P/2 - p*(q-1)*Q/2
        c = 1 / (lam * D)
        U = 2 / (lam * P)
        V = 2 / (lam * Q)
        a, b = (U - q*c)/p, (V - p*c)/q
    return regime, (a,b,c)


def graph(p,q,a,b,c):
    N=p+q; L=np.zeros((N,N))
    edges=[]
    for i in range(N):
        for j in range(i+1,N):
            t=0 if j<p else (1 if i>=p else 2)
            w=(a,b,c)[t]
            L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
            edges.append((i,j,t))
    return L,edges


def objective(p,q,a,b,c):
    U=p*a+q*c; V=q*b+p*c
    return (p-1)*np.log(U)+(q-1)*np.log(V)+np.log(c)


def direct_logdet(p,q,a,b,c):
    L,_=graph(p,q,a,b,c)
    return np.linalg.slogdet(L[:-1,:-1])[1]


def check_kkt(p,q,P,Q,B,abc):
    a,b,c=abc; N=p+q
    U=p*a+q*c; V=q*b+p*c
    lam=(N-1)/B
    grad=np.array([2/(P*U),2/(Q*V), (1/c+(p-1)*q/U+(q-1)*p/V)/(p*q)])
    assert abs(grad[2]-lam)<1e-8*max(1,lam), (p,q,P,Q,abc,grad)
    for w,g in zip(abc[:2],grad[:2]):
        if w>1e-10: assert abs(g-lam)<1e-7*max(1,lam)
        else: assert g<=lam+1e-7*max(1,lam)


def full_numeric(p,q,P,Q,B):
    regime,abc=analytic(p,q,P,Q,B)
    L,edges=graph(p,q,*abc)
    prices=np.array([(P,Q,1)[t] for _,_,t in edges])
    analytic_vec=np.array([abc[t] for _,_,t in edges]); m=len(prices)
    def f(w):
        L=np.zeros((p+q,p+q))
        for (i,j,_),x in zip(edges,w):
            L[i,i]+=x; L[j,j]+=x; L[i,j]-=x; L[j,i]-=x
        sign,logdet=np.linalg.slogdet(L[:-1,:-1])
        return -logdet if sign>0 else 1e8
    bounds=[(0,None)]*m
    constr={'type':'eq','fun':lambda w: np.dot(prices,w)-B}
    x0=np.full(m,B/(m*np.mean(prices)))
    x0*=B/np.dot(prices,x0)
    sol=minimize(f,x0,method='SLSQP',bounds=bounds,constraints=[constr],options={'maxiter':2000,'ftol':1e-12})
    if not sol.success and not (abs(sol.fun +objective(p,q,*abc))<1e-6):
        raise AssertionError((p,q,P,Q,sol.message,sol.fun,abc))
    assert abs(sol.fun+objective(p,q,*abc))<5e-6, (p,q,P,Q,sol.fun,abc)
    assert abs(f(analytic_vec)+objective(p,q,*abc))<1e-8
    return len(edges)


def main():
    # Exact rational budget and threshold checks for the two-stage example.
    assert Fraction(10, 9) < Fraction(6, 5) < Fraction(5, 3)
    assert 10 * Fraction(5, 78) + 10 * Fraction(6, 5) * Fraction(7, 234) == 1
    rng=np.random.default_rng(269031)
    counts={'spectral':0,'kkt':0,'asymmetric':0,'global':0}
    regimes=set()
    for p in range(2,7):
        for q in range(2,7):
            for P,Q in [(float(x),float(y)) for x,y in itertools.product([0.12,0.55,0.9,1.,1.3,1.9,3.5],repeat=2)]:
                regime,abc=analytic(p,q,P,Q,1)
                regimes.add(regime)
                a,b,c=abc
                assert min(abc)>-1e-10
                assert abs(p*(p-1)*P*a/2+q*(q-1)*Q*b/2 +p*q*c-1)<1e-8
                assert abs(direct_logdet(p,q,*abc)-objective(p,q,*abc))<1e-8
                counts['spectral']+=1
                check_kkt(p,q,P,Q,1,abc)
                counts['kkt']+=1
    for i in range(30):
        p=int(rng.integers(2,7));q=int(rng.integers(2,7));P=float(np.exp(rng.uniform(-2,2))); Q=float(np.exp(rng.uniform(-2,2)))
        regime,abc=analytic(p,q,P,Q)
        L,edges=graph(p,q,*abc)
        prices=np.array([(P,Q,1.)[t] for _,_,t in edges]); best=objective(p,q,*abc)
        for j in range(60):
            ws=rng.dirichlet(np.full(len(prices),0.75)); ws=ws/np.dot(prices,ws)
            L2=np.zeros_like(L)
            for (ii,jj,_),w in zip(edges,ws):
                L2[ii,ii]+=w;L2[jj,jj]+=w;L2[ii,jj]-=w;L2[jj,ii]-=w
            sign,lg=np.linalg.slogdet(L2[:-1,:-1]); assert sign>0
            assert lg<=best+1e-7, (p,q,P,Q,regime,lg-best)
            counts['asymmetric']+=1
    for p,q in [(2,2),(2,3),(3,4),(4,2),(4,5)]:
        for P,Q in [(0.3,0.3),(1,1),(0.15,4),(4,0.15),(5,5),(1.7,1.1)]:
            counts['global']+=1
            full_numeric(p,q,P,Q,1.)
    assert regimes=={'all','A-off','B-off','bipartite'}
    print('PASS',counts,'regimes',sorted(regimes))

if __name__=='__main__': main()
