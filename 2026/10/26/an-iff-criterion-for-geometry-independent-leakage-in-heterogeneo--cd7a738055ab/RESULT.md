# An iff criterion for geometry-independent leakage in heterogeneous aquifers

## Finding

Within the linear no-flow leaky-aquifer model on a bounded Lipschitz domain, with time-independent uniformly elliptic symmetric transmissivity tensor \(\mathbf T(x)\), positive storage coefficient \(S(x)\), bounded leakance \(\lambda(x)\ge0\), zero initial drawdown, and pumping density \(q(x,t)\) whose total is \(Q(t)=\int_\Omega q(x,t)\,dx\), the aggregate leakage history is independent of transmissivity, domain geometry, and spatial pumping profile for every prescribed total pumping history if and only if \(\lambda(x)/S(x)=\kappa\ge0\) almost everywhere. In that case the total leakage rate is exactly \(\mathcal L(t)=\kappa\int_0^t e^{-\kappa(t-u)}Q(u)\,du\); for constant pumping \(Q\), it is \(\mathcal L(t)=Q(1-e^{-\kappa t})\).

## Assumptions and scope

Let \(\Omega\subset\mathbb R^d\) be bounded with a Lipschitz boundary. The drawdown \(s(x,t)\) satisfies

\[
S(x)\,\partial_t s=\nabla\!\cdot\!\bigl(\mathbf T(x)\nabla s\bigr)-\lambda(x)s+q(x,t),
\qquad \mathbf n\cdot\mathbf T\nabla s=0\text{ on }\partial\Omega,
\qquad s(x,0)=0.
\]

Assume \(S\) is bounded above and below by positive constants, \(\mathbf T\) is symmetric and uniformly elliptic, \(\lambda\ge0\) is bounded, and the coefficients are time-independent. The source \(q\ge0\) is integrable in space and locally integrable in time. Its aggregate pumping rate is \(Q(t)=\int_\Omega q(x,t)\,dx\). Total leakage rate means \(\mathcal L(t)=\int_\Omega\lambda(x)s(x,t)\,dx\), not cumulative leakage volume. The result concerns this spatial integral only; it does not assert that local drawdown is independent of geology or geometry.

## Proof

Define the storage-weighted drawdown \(M(t)=\int_\Omega S(x)s(x,t)\,dx\). Integrate the governing equation over \(\Omega\). The divergence term integrates to the boundary flux, which is zero by the no-flow condition. Thus

\[
M'(t)=Q(t)-\mathcal L(t),\qquad M(0)=0.
\]

If \(\lambda(x)/S(x)=\kappa\ge0\) almost everywhere, then \(\mathcal L(t)=\kappa M(t)\), so \(M'+\kappa M=Q\). Solving this scalar linear equation gives

\[
M(t)=\int_0^t e^{-\kappa(t-u)}Q(u)\,du,
\qquad
\mathcal L(t)=\kappa\int_0^t e^{-\kappa(t-u)}Q(u)\,du.
\]

This expression contains neither \(\mathbf T\), the shape of \(\Omega\), nor the spatial distribution of \(q\); only its spatial integral \(Q\) enters. If \(Q(t)\equiv Q\), direct integration yields \(\mathcal L(t)=Q(1-e^{-\kappa t})\). The cumulative leakage volume is \(\int_0^t\mathcal L(v)\,dv=\int_0^t Q(u)(1-e^{-\kappa(t-u)})\,du\).

For necessity, fix a nonzero initial pumping rate \(Q(0)>0\) and take \(q(x,t)=Q(t)w(x)\), where \(w\ge0\) is any admissible spatial profile with \(\int_\Omega w=1\). Since \(s(x,0)=0\), the governing equation gives \(\partial_t s(x,0^+)=Q(0)w(x)/S(x)\) in the weak initial-time sense. Therefore

\[
\mathcal L'(0^+)=Q(0)\int_\Omega\frac{\lambda(x)}{S(x)}w(x)\,dx.
\]

If the leakage response is the same for every normalized spatial pumping profile, this derivative is the same for every such \(w\). The only measurable function whose average is identical over all admissible normalized profiles is an almost-everywhere constant. Hence \(\lambda/S=\kappa\) almost everywhere. A nonconstant ratio already makes the initial leakage response depend on where pumping is applied, so the claimed universal independence fails. This proves both directions.

## Verification

The proof uses the weak mass balance with the constant test function and the exact solution of a scalar first-order ODE; no finite numerical experiment is used as a substitute for the theorem. Dimensional consistency holds because \(\kappa\) has units of inverse time and \(Q\) and \(\mathcal L\) have units of volume per time. For constant pumping and \(\kappa>0\), \(\mathcal L(t)\sim Q\kappa t\) as \(t\downarrow0\), while \(\mathcal L(t)\to Q\) as \(t\to\infty\). The cumulative leakage is \(Q\kappa t^2/2+o(t^2)\) at short times and \(Qt-Q/\kappa+o(1)\) at long times. If \(\kappa=0\), leakage is identically zero. These limits agree with zero initial leakage and eventual balance of constant pumping by leakage in a closed, leaky domain when \(\kappa>0\).

## Relationship to prior work

Hantush and Jacob introduced the classical transient radial-flow model for an infinite leaky aquifer with uniform aquifer properties and a constant-rate well. Butler and Tsou later established scale-invariant total leakage for the homogeneous Hantush–Jacob setting in bounded aquifers, using image-well arguments for representative geometries; their article explicitly notes that a completely general proof had not been obtained for the more complicated geometries discussed there. The present claim is not the homogeneous scale-invariance observation itself. It gives a weak-form proof and a necessary-and-sufficient coefficient condition for the broader class with spatially varying transmissivity, spatially varying storage and leakance satisfying \(\lambda/S=\kappa\), arbitrary admissible pumping profiles, and arbitrary time-dependent aggregate pumping. The necessity statement identifies exactly how the invariance fails when \(\lambda/S\) varies spatially.

## Limitations

The no-flow lateral boundary and the absence of other sinks or sources are essential: nonzero boundary fluxes or additional exchange terms enter the integrated balance. The coefficients are time-independent and the equation is linear; delayed storage in a confining bed, nonlinear leakage, or a spatially varying ratio \(\lambda/S\) is not covered by the invariance formula. When \(\lambda/S\) is nonconstant, the theorem establishes source-profile dependence through the initial leakage slope but does not classify the later-time dependence. The result predicts aggregate leakage, not pointwise drawdown, plume transport, or site-specific water-level response. The novelty assessment is limited to the explicit iff characterization and transfer-function extension; an equivalent conservation argument may be implicit in groundwater texts not located in the checked sources.

## References

1. J. J. Butler Jr. and M.-S. Tsou, “Pumping-induced leakage in a bounded aquifer: An example of a scale-invariant phenomenon,” *Water Resources Research* 39(12), 1344 (2003). DOI: 10.1029/2002WR001484. First published 5 December 2003.
2. M. S. Hantush and C. E. Jacob, “Non-steady radial flow in an infinite leaky aquifer,” *Transactions, American Geophysical Union* 36(1), 95–100 (1955). DOI: 10.1029/TR036i001p00095.
