"""Self-contained finite checks for phase-only fifth-power Fourier synthesis on F_13."""
import cmath
from collections import defaultdict
from math import isclose
P=13

def fibers():
    r=defaultdict(list)
    for a in range(P):
        for b in range(a,P):
            r[((a+b)%P,(pow(a,5,P)+pow(b,5,P))%P)].append((a,b))
    return r

def phase_family(z0,A,B,C,D):
    g=[0j]*P
    g[0]=z0
    for representative,a,b in ((1,A,B),(2,C,D)):
        vector=(a,b,b/a,1/a,1/b,a/b)
        for j,v in enumerate(vector):g[representative*pow(4,j,P)%P]=z0*v
    assert all(abs(abs(v)-1)<1e-12 for v in g)
    return g

def energy(g,r):
    return sum(abs(sum((2 if a!=b else 1)*g[a]*g[b] for a,b in pairs))**2 for pairs in r.values())

def check():
    r=fibers()
    collisions={s:pairs for (s,z),pairs in r.items() if len(pairs)>1}
    assert set(collisions)==set(range(P))
    assert collisions[0]==[(0,0)]+[(a,P-a) for a in range(1,7)]
    for s in range(1,P):
        assert set(collisions[s])==set((tuple(sorted((0,s))),tuple(sorted(((4*s)%P,(10*s)%P)))))
    energy_count=sum(sum(2 if a!=b else 1 for a,b in pairs)**2 for pairs in r.values())
    assert energy_count==565
    residues={i*i%P for i in range(P)}
    assert residues=={0,1,3,4,9,10,12}
    valid_t=[t for t in range(P) if (1-4*t)%P in residues and (4*t-3)%P in residues]
    assert valid_t==[0,1,7]
    for k in range(17):
        c=lambda j: cmath.exp(2j*cmath.pi*((j*37+11*k*k+23*k+7*j*j)%131)/131)
        g=phase_family(c(1),c(2),c(3),c(4),c(5))
        assert abs(energy(g,r)-565)<1e-8
        assert all(abs(g[0]**2-g[t]*g[-t%P])<1e-10 for t in range(1,P))
        assert all(abs(g[0]*g[s]-g[(4*s)%P]*g[(10*s)%P])<1e-10 for s in range(1,P))
    # Arbitrary unimodular sequences cannot attain the flat-input bound in general.
    h=[cmath.exp(2j*cmath.pi*j*j/31) for j in range(P)]
    assert energy(h,r)<565-1e-4
    zpair={t:h[t]*h[(-t)%P] for t in range(1,7)}
    defect=2*sum(abs(h[0]**2-zpair[t])**2 for t in range(1,7))
    defect+=4*sum(abs(zpair[a]-zpair[b])**2 for a in range(1,7) for b in range(a+1,7))
    defect+=4*sum(abs(h[0]*h[u]-h[4*u%P]*h[10*u%P])**2 for u in range(1,P))
    assert abs(defect+energy(h,r)-565)<1e-8
    # Full ambient Fourier transform in the raw normalization.
    g=phase_family(1+0j,1+0j,1j,-1j,cmath.exp(0.5j))
    z=cmath.exp(2j*cmath.pi/P)
    moment=sum(abs(sum(g[t]*z**((u*t+v*pow(t,5,P))%P) for t in range(P)))**4 for u in range(P) for v in range(P))/P**2
    assert abs(moment-565)<1e-7
    print('PHASE13_FIFTH_GRAPH_PASS; energy=565, collisions=13, torus=5, checks=17')
if __name__=='__main__':check()
