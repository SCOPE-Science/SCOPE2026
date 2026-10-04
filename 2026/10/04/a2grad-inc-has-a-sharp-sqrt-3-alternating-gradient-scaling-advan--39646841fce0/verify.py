import math

def innovation(k,G):
    # Exact alternating running-mean innovation.
    if k % 2 == 1:
        return -G
    return G*k/(k+1.0)

def replay(K,G,beta,L,rho):
    vu=0.0
    vi=0.0
    ve=0.0
    vt=0.0
    rows=[]
    for k in range(K+1):
        d=innovation(k,G)
        vu += d*d
        if k == 0:
            vi=d*d
            vt=d*d
        else:
            vi=(k*k/((k+1.0)*(k+1.0)))*vi+d*d
            vt=rho*vt+(1.0-rho)*d*d
        ve=max(ve,vt)
        hu=math.sqrt(vu)
        hi=math.sqrt(vi)
        he=math.sqrt((k+1.0)*ve)
        gamma=2.0*L/(k+1.0)
        step_u=abs(G)/(gamma+beta*hu) if hu>0.0 else float("inf")
        step_i=abs(G)/(gamma+beta*hi) if hi>0.0 else float("inf")
        step_e=abs(G)/(gamma+beta*he) if he>0.0 else float("inf")
        rows.append((d,vu,vi,ve,hu,hi,he,step_u,step_i,step_e))
    return rows

# Exact innovation formulas.
G=2.7
for k in range(1,1000):
    d=innovation(k,G)
    if k % 2:
        assert d == -G
    else:
        assert abs(d-G*k/(k+1.0)) < 1e-15

# Exact A2Grad-inc unrolling.
rows=replay(2000,G,7.0,3.0,0.6)
for k in (1,2,3,10,100,1000,2000):
    exact=sum((t+1.0)**2*innovation(t,G)**2 for t in range(k+1))/(k+1.0)**2
    assert abs(rows[k][2]-exact) <= 2e-11*max(1.0,exact)

# Large-k normalized scale and step constants.
K=200000
beta=7.0
L=3.0
for rho in (0.1,0.5,0.9,0.99):
    rows=replay(K,G,beta,L,rho)
    d,vu,vi,ve,hu,hi,he,su,si,se=rows[-1]
    rt=math.sqrt(K)
    assert abs(hu/(abs(G)*rt)-1.0) < 2e-4
    assert abs(hi/(abs(G)*rt)-1.0/math.sqrt(3.0)) < 2e-4
    assert abs(he/(abs(G)*rt)-1.0) < 2e-4
    assert abs(rt*su-1.0/beta) < 2e-4
    assert abs(rt*si-math.sqrt(3.0)/beta) < 3e-4
    assert abs(rt*se-1.0/beta) < 2e-4
    assert abs(ve/(G*G)-1.0) < 2e-4

# Signal amplitude cancels from the normalized inner-step limits.
for G2 in (0.03,0.3,3.0,30.0):
    rows=replay(100000,G2,5.0,11.0,0.8)
    rt=math.sqrt(100000)
    su,si,se=rows[-1][-3:]
    assert abs(rt*su-0.2) < 5e-4
    assert abs(rt*si-math.sqrt(3.0)/5.0) < 7e-4
    assert abs(rt*se-0.2) < 5e-4

print("verification passed")
