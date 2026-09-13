# Fixed-s 120-degree law is false: the 120-degree trihedral cone is not fractionally stationary

## Context

Classical double bubbles meet at 120 degrees. The target asks whether this persists at fixed
fractional order: for a volume-constrained stationary symmetric fractional double-bubble pair
(E1,E2) in R^3 with |E1|=|E2|=1 and fixed s in [3/4,1), are blow-up cones along the singular
circle Gamma planar triods with all dihedral angles exactly 2pi/3? Stationarity means vanishing
first variation of F_s=P_s(E1)+P_s(E2) under volume-preserving flows, so each regular sheet has
constant fractional mean curvature H_s. The claim is two-sided: prove the 120-degree law for all
s in [3/4,1) or disprove it by an explicit s with a stationary cone whose angles differ by a
positive s-dependent amount.

## Definitions

P_s(E)=int_E int_{R^3\E}|x-y|^{-3-s}dxdy. H_s[E](x)=p.v. int_{R^3}(1-2 chi_E)/|x-y|^{3+s}dy.
Let C=C0 x R with C0=S(2pi/3)={0<=arg<=2pi/3} in R^2: the cylinder over the 120-degree sector,
the blow-up model of a triod with three equal 120-degree dihedral angles. Face point
p=(p0,0), p0=(1,0). Tangent half-plane at p0 is T={v>0} with H^{2d}_s[T](p0)=0 by symmetry.
For beta<pi define W(beta)={beta<arg<pi]}, the wedge of angle pi-beta between S(beta) and T.

## Result

For every s in [3/4,1) the 120-degree cone C has strictly positive unnormalized fractional
mean curvature on each regular face, uniformly bounded away from zero:
H^{3d}_s[C]>=0.17 (analytic floor; computed values ~2.85 at s=0.75 down to ~1.97 at s=0.95).
Since cone stationarity forces vanishing face curvature by dilation scaling H(lx)=l^{-s}H(x),
C is never a stationary blow-up cone at fixed s. Hence no stationary symmetric pair can have
120-degree blow-up cones for all s; any stationary symmetric cone has angles differing from
2pi/3 by a positive s-dependent amount, or none exists. The universal fixed-s 120-degree law
is false.

## Proof / evidence

Lemma 1 (cylinder reduction, exact): H^{3d}_s[C](p)=B(s) H^{2d}_s[C0](p0) with
B(s)=int_R(1+t^2)^{-(3+s)/2}dt=sqrt(pi)Gamma(1+s/2)/Gamma((3+s)/2), B in [1.571,1.653] on
[3/4,1). Fubini in y=(z,tau) with u=tau/|p0-z|; sign pattern depends only on z.
Lemma 2 (stationarity forces zero): a stationary cone has constant face curvature, and
H(lx)=l^{-s}H(x) forces that constant to be 0.
Lemma 3 (half-plane subtraction, exact): for beta<pi, S(beta) subset T and
H^{2d}_s[S(beta)](p0)=2 int_{W(beta)}|p0-z|^{-(2+s)}dz. W is at positive distance from p0
(true distance 1 at beta=2pi/3), so the integral is absolutely convergent, finite, strictly
positive; zero only at beta=pi, negative for beta>pi.
Quantitative gap: inscribe disc D of radius r=1/2 in W(2pi/3) (bisector 150deg, inradius
1/2, Dmax=|p0-c|+r=hyp(1+sqrt3/2,1/2)+1/2~2.4319); then H^{2d}>=2 pi r^2 Dmax^{-(2+s)}>=0.136
at s=0.75, >=0.109 uniform, times B(s)>=1.571 gives H^{3d}>=0.171 uniform. Pure-numpy
integrator with exact u=1/r tail transform (output/artifacts/wedge_flux.py) gives
H^{2d}(120deg,0.75)~1.7248, monotone angle sweep (2.90 at 90deg, 1.72 at 120deg, 0.81 at
150deg, 0 only at 180deg), confirming the margin exceeds 12x the floor. The s->1 classical
limit is untouched: (1-s)H_s renormalizes the positive term away and recovers 120deg only
asymptotically.

## Limitations

Disproof only: the true stationary angle function beta(s) is not computed (requires coupled
three-sector system with Lagrange multipliers). It assumes the target's hypothesis of a
stationary pair with blow-up cones and refutes the angle conclusion. Beta>180deg wedge
values diverge to -infinity (not needed). Off-center numeric scaling checks are weak;
analytic scaling is exact. Minor exposition slip in dist(p0,W) formula does not affect
positivity.

## Reproducibility

Run output/artifacts/wedge_flux.py (pure numpy+math); it regenerates
output/artifacts/wedge_flux_results.json including the beta=120deg sweep, angle sweep at
s=0.75, scaling check at d=1 (rel err 2.3e-8), and uniform bounds. B(s) and the disc bound
verify by hand from the Gamma formula and Dmax above.

## References

Caffarelli-Roquejoffre-Savin nonlocal minimal surfaces (via Lombardini thesis
arXiv:1508.06241); Lawson s-minimal cones (Davila-del Pino-Wei); fractional capillarity
cones (arXiv:2008.06175); classical stationary double-bubble 120-degree theory
(arXiv:2301.10705); stable 2D s-minimal cones for s~0.
