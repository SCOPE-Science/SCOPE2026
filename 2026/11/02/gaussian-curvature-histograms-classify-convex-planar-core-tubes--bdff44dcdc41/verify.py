"""Deterministic finite checks for the curvature-law tube theorem; not a proof."""
import math

R, eps, r = 3.0, 0.25, 0.18
N = 720
phis = [2*math.pi*(i+0.5)/N for i in range(N)]
thetas = [2*math.pi*(j+0.5)/N for j in range(N)]

def run(m):
    assert m >= 2
    rho = [R*(1+eps*math.cos(m*p)) for p in phis]
    kap = [1/x for x in rho]
    assert r < min(rho)
    # Fourier support h=R+R*eps*cos(m phi)/(1-m*m): h+h''=rho.
    for i in range(0,N,36):
        p=phis[i]
        h=R+R*eps*math.cos(m*p)/(1-m*m)
        hpp=-R*eps*m*m*math.cos(m*p)/(1-m*m)
        assert abs((h+hpp)-rho[i]) < 1e-12
    # Area measure normalized by 2 pi r L; L=sum rho dphi=2 pi R.
    assert abs(sum(rho)/N-R)<1e-12
    km=max(kap)
    kp=km/(r*(1+r*km)); kn=-km/(r*(1-r*km))
    assert abs((1/kp+1/kn)/2-r*r) < 1e-12
    core=[sum(rho[i]*kap[i]**(2*j) for i in range(N))/(N*R) for j in (1,2,3)]
    rec=[0.0,0.0,0.0]; observed=[0.0,0.0,0.0,0.0]
    costh=[math.cos(t) for t in thetas]
    for i in range(N):
        k=kap[i]
        for c in costh:
            w=1-r*k*c
            K=-k*c/(r*w)
            assert abs(-r*K/(1-r*r*K)-k*c) < 1e-12
            wt=rho[i]*w/(N*N*R)
            for z in range(4):observed[z]+=wt*K**(z+1)
            for j in (1,2,3):
                rec[j-1]+=wt*4**j*r**(2*j)*K**(2*j)/(math.comb(2*j,j)*(1-r*r*K)**(2*j-1))
    for a,b in zip(rec,core):assert abs(a-b)<2e-10,(m,a,b)
    assert abs(observed[0])<1e-11 # Gauss--Bonnet on torus
    # Known mean core curvature gives its perimeter.
    mean_k=sum(rho[i]*kap[i] for i in range(N))/(N*R)
    assert abs(2*math.pi/mean_k-2*math.pi*R)<1e-12
    return core,observed

cores=[]; moments=[]
for m in (2,3):
    c,o=run(m);cores.append(c);moments.append(o)
for a,b in zip(cores[0],cores[1]):assert abs(a-b)<2e-12
for a,b in zip(moments[0],moments[1]):assert abs(a-b)<2e-11,(a,b)
print('CURVATURE_EXTREMA_RADIUS_IDENTIFICATION_PASSED')
print('SURFACE_AREA_REWEIGHTING_AND_MOMENT_INVERSION_PASSED')
print('NONCONGRUENT_HARMONIC_CURVATURE_HISTOGRAM_PASSED')
print('ALL_CHECKS_PASSED')
