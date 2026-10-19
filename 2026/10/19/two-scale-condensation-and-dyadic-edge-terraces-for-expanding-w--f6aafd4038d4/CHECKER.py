"""Exact rational finite-truncation checks of the W-map boundary layer.

These checks are finite illustrations; the limiting theorem has an analytic proof.
"""
from fractions import Fraction as Q


def w_step(x, a):
    m = Q(2) + a
    if x < Q(1, 4):
        return 1 - 4*x, Q(-4)
    if x < Q(1, 2):
        return m*(x-Q(1,4)), m
    if x < Q(3, 4):
        return Q(1,2)+a/4-m*(x-Q(1,2)), -m
    return 4*(x-Q(3,4)), Q(4)


def data(a, n=72):
    m=Q(2)+a
    z=Q(1,2)
    beta=Q(1)
    s=Q(0)
    integral=Q(0)
    entries=[]
    for j in range(1,n+1):
        z,der=w_step(z,a)
        # The critical point is approached from the left on the first step.
        beta*=m if j==1 else der
        weight=1/abs(beta)
        positive=beta>0
        s+=weight*int((z>Q(1,2)) if positive else (z<Q(1,2)))
        integral+=weight*(z if positive else 1-z)
        entries.append((z,positive,weight))
        if j<=3:
            if j==1:assert z==Q(1,2)+a/4
            else:assert z==Q(1,2)-a*(1+a*m**(j-1))/(4*(1+a))
    tail=m**(-n)/(m-1)
    # Bounds are rigorous because each subsequent inverse slope is at most m^(-j).
    assert s>Q(1,2)
    Aminus=1/(1-2*s)
    Aplus=1/(1-2*(s+tail))
    assert Aminus<Aplus<0
    zmin=1+2*Aminus*(integral+tail)
    zmax=1+2*Aplus*integral
    assert zmin<zmax<0
    return entries,(Aminus,Aplus),(zmin,zmax),tail


def mass_bounds(a, r, records):
    entries,(amin,amax),(zmin,zmax),tail=records
    lo=Q(1,2)-r
    hi=Q(1,2)+r
    def overlap(z,pos):
        left=lo if pos else max(lo,z)
        right=min(hi,z) if pos else hi
        return max(Q(0),right-left)
    j=sum((w*overlap(z,pos) for z,pos,w in entries),Q(0))
    nmin=(hi-lo)+2*amin*(j+tail)
    nmax=(hi-lo)+2*amax*j
    assert nmin<nmax<0
    quotients=(nmin/zmin,nmin/zmax,nmax/zmin,nmax/zmax)
    return min(quotients),max(quotients)


def scaled_density_bounds(a,t,records):
    entries,(amin,amax),(zmin,zmax),tail=records
    x=Q(1,2)+a*t
    s=sum((w for z,pos,w in entries if (x<=z if pos else x>=z)),Q(0))
    fmin=1+2*amin*(s+tail)
    fmax=1+2*amax*s
    assert fmin<fmax<0
    quotients=(a*fmin/zmin,a*fmin/zmax,a*fmax/zmin,a*fmax/zmax)
    return min(quotients),max(quotients)


def main():
    for a in (Q(1,100),Q(1,1000),Q(1,10000)):
        d=data(a)
        print('parameter',str(a))
        for t in (Q(-1,2),Q(0),Q(1,2)):
            lower,upper=scaled_density_bounds(a,t,d)
            print('  scaled density at',str(t),f'[{float(lower):.8g}, {float(upper):.8g}]')
        for ell in (Q(1,8),Q(1,4),Q(1,2)):
            lower,upper=mass_bounds(a,a*ell,d)
            print('  centered window ratio',str(ell),f'[{float(lower):.8g}, {float(upper):.8g}]')
            target=min(Q(4,3)*ell,Q(1,3))
            assert abs(float((lower+upper)/2-target))<(0.07 if a>=Q(1,100) else 0.015)
        if a<=Q(1,1000):
            for u,target in ((Q(-2),Q(2,3)),(Q(0),Q(2,3)),
                             (Q(1,2),Q(1,3)),(Q(1),Q(1,6)),
                             (Q(2),Q(1,12)),(Q(4),Q(1,24)),
                             (Q(10),Q(1,48))):
                # x=1/2-a/4-a^2 u, written on the primary a-scale.
                lo,hi=scaled_density_bounds(a,-Q(1,4)-a*u,d)
                val=(lo+hi)/2
                assert abs(float(val-target))<0.017
                print('  left-edge step at',str(u),f'[{float(lo):.8g}, {float(hi):.8g}]')
        low,hi=scaled_density_bounds(a,Q(0),d)
        assert abs(float((low+hi)/2-Q(2,3)))<(0.02 if a>=Q(1,100) else 0.005)
    print('VERIFY_OK')

if __name__=='__main__':main()
