# For F_s=P_s(E1)+P_s(E2), the fixed-s 120-degree trihedral cone is not stationary

## Context

Classical double bubbles meet at 120 degrees. The target asks whether this persists at fixed
fractional order for the specific two-chamber sum functional
F_s(E1,E2)=P_s(E1)+P_s(E2), with the exterior phase not included as a third perimeter.
This functional is different from the standard nonlocal cluster energy that sums fractional
perimeters of all phases.

## Definitions

P_s(E)=int_E int_{R^3\E}|x-y|^{-3-s} dx dy and
H_s[E](x)=p.v. int_{R^3}(1-2 chi_E(y))/|x-y|^{3+s} dy.
Let C=C0 x R with C0=S(2pi/3)={0<=arg<=2pi/3} in R^2.
At the face point p=(p0,0), p0=(1,0), the tangent half-plane is
T={v>0}, whose two-dimensional fractional mean curvature at p0 is zero.
For beta<pi define W(beta)={beta<arg<pi}.

## Result

For every s in [3/4,1), the 120-degree sector cylinder C has strictly positive
unnormalized fractional mean curvature on each corresponding chamber face. In fact
H_s^{3d}[C](p)>=0.1715. A stationary homogeneous blow-up cone for the stated
two-chamber sum functional must have zero face curvature, because
H_s(lambda x)=lambda^{-s}H_s(x). Therefore the equal 120-degree triod cannot be
a stationary blow-up cone for this functional at fixed s.

This statement is functional-specific. It does not contradict results for the standard
three-phase nonlocal cluster energy, where all phase perimeters are included and 120-degree
minimal cones are known in two dimensions for s sufficiently close to 1.

## Proof / evidence

1. Cylinder reduction. Fubini in the axial variable gives
   H_s^{3d}[C](p)=B(s) H_s^{2d}[C0](p0), where
   B(s)=sqrt(pi) Gamma(1+s/2)/Gamma((3+s)/2).
   On s in [3/4,1), B(s)>pi/2 and is bounded away from zero.

2. Half-plane subtraction. For beta<pi, S(beta) is contained in T, so
   H_s^{2d}[S(beta)](p0)=2 int_{beta<arg z<pi}|p0-z|^{-(2+s)} dz.
   The difference wedge is a positive distance from p0. The integral is therefore
   absolutely convergent and strictly positive.

3. Uniform lower bound. For beta=2pi/3, inscribe a disk of radius 1/2 in the
   difference wedge, centered on the 150-degree bisector. If Dmax is the maximum
   distance from p0 to this disk, Dmax=
   hypot(1+sqrt(3)/2,1/2)+1/2=2.43185165..., then
   H_s^{2d} >= (pi/2) Dmax^{-(2+s)}
   >= (pi/2) Dmax^{-3}=0.1092216....
   Multiplying by inf B(s)=pi/2 gives the uniform three-dimensional lower bound
   0.17156... .

4. Stationarity. On a volume-constrained stationary configuration, each regular
   outer face has constant fractional mean curvature. For a cone the scaling law
   H_s(lambda x)=lambda^{-s}H_s(x) forces that constant to be zero. The positive
   bound from Step 3 excludes the 120-degree cone.

The corrected numerical certificate `artifacts/wedge_flux.py` evaluates the same
difference integrals. At s=0.75 it gives H_2d(120deg)=1.72477..., finite negative
values for beta>pi (for example H_2d(240deg)=-1.72477...), and verifies
H(d)=d^{-s}H(1) at d=0.5,1,2 to machine precision. These numerics support but are
not needed for the analytic bound.

## Limitations

The true stationary angle for the two-chamber sum functional is not computed.
The statement is not a theorem about the standard full three-phase cluster energy.
It assumes the target's blow-up/stationarity framework and only excludes the
equal-120-degree cone. Numerical sweeps are secondary to the analytic estimate.

## Reproducibility

Run `python3 artifacts/wedge_flux.py`; it regenerates
`artifacts/wedge_flux_results.json` with the beta=120-degree s-sweep, the angle
sweep on both sides of pi, the corrected scaling check, and the uniform analytic bound.

## References

A. Cesaroni and M. Novaga, Nonlocal minimal clusters in the plane,
arXiv:1910.03429. Caffarelli-Roquejoffre-Savin nonlocal minimal-surface theory.
Classical stationary double/triple bubble theory, arXiv:2301.10705.
