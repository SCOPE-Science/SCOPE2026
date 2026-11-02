"""Finite spot-checks for the regular-simplex light-cone dispersion theorem.

Requires Python >=3.10 and mpmath. The analytical proof, not this script,
justifies the statements for every admissible parameter.
"""
from mpmath import mp
mp.dps=60

def critical_q(n):
    return mp.re(mp.lambertw(mp.mpf(n-1)/mp.e))/(n-1)

def leading(n,p,c,d):
    a=(1+d)**(-p)
    tau=d/c
    q=a*tau
    z=-q*mp.exp((n-1)*q)
    return -(n-1)*a + mp.lambertw(z,0)/tau

for n in (2,3,4,5,12,100):
    q0=critical_q(n)
    assert mp.almosteq(q0*mp.exp((n-1)*q0),1/mp.e)
    for q in (q0/2,q0*mp.mpf('1.3')):
        z=-q*mp.exp((n-1)*q)
        lead=mp.lambertw(z)
        assert abs(lead*mp.exp(lead)-z) < mp.mpf('1e-52')
        for branch in (-5,-4,-3,-2,-1,1,2,3,4,5):
            root=mp.lambertw(z,branch)
            assert mp.re(lead)>=mp.re(root)-mp.mpf('1e-45')
        assert (abs(mp.im(lead)) < mp.mpf('1e-45')) == (q < q0)
for n,p,c in ((4,2,mp.mpf('.3')),(7,3,mp.mpf('.11'))):
    q0=critical_q(n)
    ccrit=(p-1)**(p-1)/(p**p*q0)
    assert c < ccrit
    peak=1/(p-1)
    f=lambda d:d/(c*(1+d)**p)-q0
    def bisect(lo,hi):
        flo=f(lo)
        for _ in range(220):
            mid=(lo+hi)/2
            if (f(mid)>0)==(flo>0):lo=mid
            else:hi=mid
        return (lo+hi)/2
    dl=bisect(mp.mpf('0'),mp.mpf(peak))
    dr=bisect(mp.mpf(peak),mp.mpf('1e6'))
    assert dl<peak<dr
    for d,osc in ((dl/2,False),((dl+peak)/2,True),((peak+dr)/2,True),(dr*2,False)):
        z=leading(n,p,c,d)
        assert (abs(mp.im(z))>mp.mpf('1e-20'))==osc,(n,p,d,z)
    print('two critical lengths:',n,p,str(dl)[:15],str(dr)[:15])

# Check large-separation spectral limits for unattenuated communication.
for n in (2,3,6):
    for d in (100,1000):
        tau=mp.mpf(d)
        root=leading(n,0,1,mp.mpf(d))
        if n==2:
            ratio=mp.re(root)*tau**3/(-mp.pi**2/2)
            assert abs(ratio-1) < mp.mpf('.04'),(n,d,ratio)
        else:
            ratio=mp.re(root)*tau/(-mp.log(n-1))
            assert abs(ratio-1) < mp.mpf('.04'),(n,d,ratio)
        print('large-delay check:',n,d,mp.nstr(ratio,12))

# Verify the N-dependent endpoints and limiting scaling as N grows.
p=2;c=mp.mpf('.4')
for n in (100,1000,10000):
    q0=critical_q(n)
    disc=mp.sqrt(1-4*c*q0)
    dminus=(1-disc)/(1+disc)
    dplus=1/dminus
    assert mp.almosteq(dminus/(c*(1+dminus)**2),q0)
    assert mp.almosteq(dplus/(c*(1+dplus)**2),q0)
    print('many-agent endpoints:',n,mp.nstr(dminus,12),mp.nstr(dplus,12))
print('ALL CHECKS PASSED')
