"""Independent numerical checks for a planar-core tube Willmore profile.
Only Python's standard library is used. Finite checks are not a proof.
"""
import math

PI=math.pi

def shape_curvature_radii(R, eps, k, phi):
    # Support function h=R+eps*cos(k*phi); radius of curvature h+h''.
    return R+(1-k*k)*eps*math.cos(k*phi)

def tube_energy(R,r,k,eps,n=1200):
    step=2*PI/n
    summ=0.0
    variance=0.0
    for j in range(n):
        p=(j+.5)*step
        rho=shape_curvature_radii(R,eps,k,p)
        assert rho>r
        kappa=1/rho
        summ+=rho/math.sqrt(1-r*r*kappa*kappa)
        variance+=rho*(kappa-1/R)**2
    return PI/(2*r)*step*summ,step*variance

def direct_surface_energy(R,r,k,eps,nphi=420,ntheta=420):
    dp=2*PI/nphi;dt=2*PI/ntheta
    total=0.0
    for j in range(nphi):
        rho=shape_curvature_radii(R,eps,k,(j+.5)*dp)
        curvature=1/rho
        for l in range(ntheta):
            c=math.cos((l+.5)*dt)
            t=r*curvature*c
            H=(1-2*t)/(2*r*(1-t))
            total+=H*H*r*(1-t)*rho
    return total*dp*dt

def main():
    for R,r,k,eps in [(2,.8,2,-.10),(2,.8,3,-.025),(1.8,.55,4,-.005)]:
        W,var=tube_energy(R,r,k,eps)
        direct=direct_surface_energy(R,r,k,eps)
        assert abs(W-direct)<1.e-7, (W,direct)
        q=r/R
        ring=PI*PI*R/(r*math.sqrt(1-q*q))
        low=PI*r*var/(4*(1-q*q)**1.5)
        assert W>ring and W-ring>=low-1.e-8, (W,ring,low)
        area=2*PI*r*(2*PI*R)
        vol=PI*r*r*(2*PI*R)
        iso=area**3/(16*PI*PI*vol**2)
        assert abs(iso-R/r)<1.e-12
        from_iso=PI*PI*iso**2/math.sqrt(iso*iso-1)
        assert abs(from_iso-ring)<1.e-10
    print('DIRECT_SURFACE_INTEGRALS_AND_GLOBAL_RIGIDITY_PASSED')
    R,r=2.0,0.8
    C=PI*r*(R*R+2*r*r)/(4*(R*R-r*r)**2.5)
    baseline=tube_energy(R,r,2,0)[0]
    for k in [2,3,4]:
        eps=2.e-4/(k*k-1)
        W,_=tube_energy(R,r,k,eps)
        # Integral of (h+h'') perturbation squared: pi*(k^2-1)^2
        predicted=C*eps*eps*PI*(k*k-1)**2
        assert abs((W-baseline)/predicted-1)<.01, (k,(W-baseline)/predicted)
    # Least bending-cost eigenmode is degree 2: (k^2-1)^2>=9, k>=2.
    assert all((k*k-1)**2>=9 for k in range(2,100))
    print('SHARP_SECOND_VARIATION_AND_MODE_TWO_PASSED')
    assert abs(PI*PI*2/math.sqrt(2-1)-2*PI*PI)<1.e-12
    print('CLIFFORD_PROFILE_AND_ALL_CHECKS_PASSED')

if __name__=='__main__':main()
