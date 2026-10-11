"""Numerical independent tests of the stated complete-tripartite outer ellipsoid."""
import math
import numpy as np

def candidate(a,b):
    assert a>=2 and b>=1
    disc = 16*a*a-8*a*b-8*a+b*b+14*b+1
    raw=(2*a-2*b-2+math.sqrt(disc))/(3*(2*a+b-1))
    t=max(0.,raw)
    n=2*a+b; d=n-1
    alpha=t/(a*a); beta=(1-t)/(2*a*b)
    C=np.zeros((n,n))
    groups=[range(a),range(a,2*a),range(2*a,n)]
    edges=[]
    for u in groups[0]:
        for v in groups[1]:edges.append((u,v,'AA',alpha))
    for g in groups[:2]:
        for u in g:
            for v in groups[2]:edges.append((u,v,'AB',beta))
    for u,v,kind,w in edges:
        z=np.zeros(n);z[u]=1;z[v]=-1;C+=w*np.outer(z,z)
    Q=d*C
    w,V=np.linalg.eigh(Q)
    assert abs(w[0])<1.e-9
    inv=(V[:,1:] / w[1:]) @ V[:,1:].T
    lev={'AA':[],'AB':[]}
    for u,v,kind,p in edges:
        z=np.zeros(n);z[u]=1;z[v]=-1
        lev[kind].append(z@inv@z)
    lam=[d*(1+t)/(2*a)]*(2*a-2)+[d*(1-t)/b]*(b-1)+[d*(1+3*t)/(2*a), d*n*(1-t)/(2*a*b)]
    assert np.allclose(sorted(lam), sorted(w[1:]),rtol=1.e-9,atol=1.e-9)
    assert max(lev['AA']+lev['AB']) <= 1+1.e-9
    assert max(abs(x-1) for x in lev['AB'])<1.e-9
    if b<=2*a+1:assert max(abs(x-1) for x in lev['AA'])<1.e-9
    else:assert max(lev['AA'])<1-1.e-8
    if t>1.e-9:assert abs((2*a-2)/(1+t)-b/(1-t)+3/(1+3*t))<1.e-8
    assert abs(a*a*alpha+2*a*b*beta-1)<1.e-9
    # Verify contact second moment, the D-optimal design certificate.
    assert np.allclose(inv @ C @ inv, inv/d,rtol=1.e-8,atol=1.e-8)
    return t,lev['AA'][0],lev['AB'][0]

if __name__=='__main__':
    cases=0
    for a in range(2,12):
        for b in range(1,3*a+8):
            candidate(a,b);cases+=1
    for a,b in [(2,4),(2,5),(2,6),(3,6),(3,7),(3,8),(5,10),(5,11),(5,12)]:
        t,aa,ab=candidate(a,b)
        print(f'a={a} b={b} t={t:.9f} AA-leverage={aa:.9f} AB-leverage={ab:.9f}')
    print('PASS',cases,'parameter cases: all eigenvalues, facet contacts, and covariance moment identities')
