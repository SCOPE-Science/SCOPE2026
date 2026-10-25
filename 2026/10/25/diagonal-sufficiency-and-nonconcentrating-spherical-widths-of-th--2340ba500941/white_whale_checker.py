"""Reproducible finite checks for the White Whale spherical-width limit.
Standard-library Python 3.10+, with no outside packages.
Not an infinite-dimensional proof: see RESULT.md for the proof.
"""
import math
import random

SEED = 729413
rng = random.Random(SEED)
PHI = lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
CDF = lambda z: (1+math.erf(z/math.sqrt(2)))/2

def profile(t):
    return PHI(t)+t*(CDF(t)-0.5)

def exact_normalized_width(u):
    vals = [0.0]
    for a in u:
        vals += [v+a for v in vals]
    return sum(map(abs,vals))/len(vals)

def independent_cube_width(u):
    # All corners of the (2^d-1)-dimensional cube defining the zonotope.
    # Feasible only up to d=4, where there are 32768 corners.
    bsum=[0.0]
    for a in u:
        bsum += [v+a for v in bsum]
    corners=[0.0]
    for p in bsum[1:]:
        corners += [c+p for c in corners]
    return (max(corners)-min(corners))/(2**len(u))

def sph(d):
    g=[rng.gauss(0,1) for _ in range(d)]
    s=math.sqrt(sum(a*a for a in g))
    return [a/s for a in g]

def exact_first(d):
    mu=math.exp(math.lgamma(d/2)-math.lgamma((d+1)/2))/math.sqrt(math.pi)
    return mu*sum(math.comb(d,k)*math.sqrt(k) for k in range(1,d+1))/(2**d)

def abs_correlated(rho):
    return 2/math.pi*(math.sqrt(max(0,1-rho*rho))+rho*math.asin(min(1,max(-1,rho))))

def exact_second(d):
    # (B,C) uniform independent Boolean vectors. Four cell types: 11,10,01,00.
    # Gaussian/sphere radial independence gives conditional E |<U,B>||<U,C>|.
    total=0.0
    for j in range(d+1):
        for a in range(d-j+1):
            for c in range(d-j-a+1):
                z=d-j-a-c
                k=j+a; ell=j+c
                if not k or not ell: continue
                logpr=(math.lgamma(d+1)-sum(math.lgamma(t+1) for t in [j,a,c,z])-d*math.log(4))
                corr=j/math.sqrt(k*ell)
                total+=math.exp(logpr)*math.sqrt(k*ell)/d*abs_correlated(corr)
    return total

def run():
    count=0
    for d in (2,3,4):
        for t in range(14):
            u=sph(d)
            exact=exact_normalized_width(u)
            brute=independent_cube_width(u)
            assert math.isclose(exact,brute,rel_tol=1e-11,abs_tol=1e-11),(d,t,exact,brute)
            count+=1
    print('Independent cube-corner/zonotope width identities:',count,'passed')
    for d in (2,4,8,12,16):
        samples=80 if d==16 else 160
        widths=[]; ts=[]; diffs=[]
        for t in range(samples):
            u=sph(d); x=exact_normalized_width(u); z=sum(u)
            widths.append(x); ts.append(z); diffs.append(abs(x-profile(z)))
        print('d=%-2d  count=%-3d  mean=%.7f  exact_mean=%.7f  max_profile_gap=%.6f mean_gap=%.6f' %
              (d,samples,sum(widths)/samples,exact_first(d),max(diffs),sum(diffs)/samples))
    for d in (2,4,8,16,32,64):
        m1=exact_first(d); m2=exact_second(d); vv=m2-m1*m1
        print('EXACT_SPHERICAL_MOMENTS d=%d mean=%.9f variance=%.9f'%(d,m1,vv))
    mean_limit=1/math.sqrt(math.pi)
    var_limit=1/12+(math.sqrt(3)-2)/(2*math.pi)
    print('THEORETICAL_LIMIT mean=%.12f variance=%.12f'%(mean_limit,var_limit))
    for d in (4,8,12,16,20):
        u=[1/math.sqrt(d)]*(d//2)+[-1/math.sqrt(d)]*(d-d//2)
        if d%2:continue
        print('BALANCED_DIRECTION d=%d width_normalized=%.10f profile_at_zero=%.10f'%(d,exact_normalized_width(u),profile(0)))
    print('ALL_CHECKS_COMPLETED')

if __name__=='__main__': run()
