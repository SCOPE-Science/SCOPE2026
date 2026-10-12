#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 80

def harmonic(n, r=1):
    return mp.fsum([mp.mpf(1)/(k**r) for k in range(1,n+1)])

def check_m(m):
    psi=mp.digamma
    tri=lambda x: mp.polygamma(1,x)

    EG=mp.mpf(2)/(m+1)
    EH=psi(m+1)-psi(2)

    a=mp.mpf(6)/(m*(m+1)*(m+2))*(psi(4)-psi(m+3))
    b=mp.mpf(2)/(m*(m+1)*(m+2))*(psi(2)-psi(m+3))
    EGH= -m*a-m*(m-1)*b
    cov=EGH-EG*EH
    cov_closed=-mp.mpf(m-1)/((m+1)**2*(m+2))

    EG2=mp.mpf(4)*(m+5)/((m+1)*(m+2)*(m+3))
    vg=EG2-EG**2
    vg_closed=mp.mpf(4)*(m-1)/((m+1)**2*(m+2)*(m+3))

    diag=mp.mpf(2)/(m*(m+1))*((psi(3)-psi(m+2))**2+tri(3)-tri(m+2))
    off=mp.mpf(1)/(m*(m+1))*((psi(2)-psi(m+2))**2-tri(m+2))
    EH2=m*diag+m*(m-1)*off
    vh=EH2-EH**2
    vh_closed=harmonic(m+1,2)-mp.pi**2/6+(mp.pi**2/3-2)/(m+1)-mp.mpf(1)/(m+1)**2

    corr=cov/mp.sqrt(vg*vh)
    corr_closed=-mp.sqrt((m-1)*(m+3))/(2*(m+1)*mp.sqrt((m+2)*vh_closed))

    tol=mp.mpf("1e-60")
    assert abs(cov-cov_closed)<tol
    assert abs(vg-vg_closed)<tol
    assert abs(vh-vh_closed)<tol
    assert abs(corr-corr_closed)<tol
    assert cov<0 and vg>0 and vh>0
    return corr

def run():
    dimensions=0
    identity_checks=0
    for m in range(2,202):
        check_m(m)
        dimensions+=1
        identity_checks+=4

    target=-1/(2*mp.sqrt(mp.pi**2/3-3))
    asymptotic_checks=0
    prev=None
    for m in [100,300,1000,3000,10000,30000,100000]:
        c=check_m(m)
        err=abs(c-target)
        if prev is not None:
            assert err<prev
        prev=err
        asymptotic_checks+=1
    assert prev < mp.mpf("2e-5")

    print(
        "VERIFY_OK "
        f"dimensions={dimensions} "
        f"identity_checks={identity_checks} "
        f"asymptotic_checks={asymptotic_checks} "
        f"limit={mp.nstr(target, 14)}"
    )

if __name__=="__main__":
    run()
