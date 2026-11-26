# Unique drift-optimal resetting for an asymmetric instantaneous Brownian ratchet

## Finding

For Brownian motion with instantaneous Poisson projection into asymmetric periodic capture wells, the **physical drift speed at fixed cell length** has exactly one positive maximizing reset rate at every nonzero, nondegenerate asymmetry. Write \(D>0\) for the Brownian diffusivity, \(L>0\) for the lattice spacing, \(r>0\) for the reset rate, and \(0<c<1\) for the normalized basin asymmetry. With \(x=(L/2)\sqrt{r/D}\), the unique optimum is
\[
 \frac{2}{x_*}+c\coth(cx_*)-\coth x_*=0,
 \qquad r_* = \frac{4D x_*^2}{L^2}.
\]
Both \(x_*\) and \(r_*\) strictly increase with \(c\). As \(c\uparrow1\), \((1-c)x_*\to2\), equivalently \(r_*\sim16D/[L^2(1-c)^2]\). These conclusions optimize the known mean drift, not the diffusivity.

## Assumptions and scope

Start from zero. Between points of an independent rate-\(r\) Poisson process the particle evolves by \(dX_t=\sqrt{2D}\,dB_t\). At an alarm, a position in \([jL-L(1+c)/2,jL+L(1-c)/2)\) is projected to \(jL\), for integer \(j\). Projection takes zero time. The mean defining the physical speed \(v=\lim_{t\to\infty}\mathbb E[X_t]/t\) is on the unwrapped line. Vary only \(r\) when maximizing speed; \(D,L,c\) are fixed. The symmetric case \(c=0\) has zero drift at every rate and no distinguished optimum. The degenerate endpoint \(c=1\) is not in the optimizer statement.

## Proof

The instantaneous current of Roberts, Sezik and Lardet [1], Eq. (24), gives
\[
 v=rL\frac{\sinh(cx)}{2\sinh x}=\frac{2D}{L}x^2\frac{\sinh(cx)}{\sinh x}.
\]
In their notation \(\ell=2x\), the forward basin boundary is at \(\delta L\) with \(\delta=(1-c)/2\), and the dimensionless current is the number of signed lattice steps per cycle. Multiplication by \(rL\) produces a physical distance per unit time.

The positive speed has logarithmic derivative in \(x\)
\[
 H(x,c)=\frac{2}{x}+c\coth(cx)-\coth x.
\]
Since \(\sinh(cx)<c\sinh x\) by strict convexity of \(\sinh\) on the positive half-line and \(\sinh(0)=0\),
\[
 \partial_x H=-\frac{2}{x^2}-c^2\operatorname{csch}^2(cx)+\operatorname{csch}^2 x<0.
\]
At \(x\downarrow0\), the leading singular terms in \(c\coth(cx)-\coth x\) cancel, so \(H\to+\infty\). At \(x\to\infty\), \(H\to c-1<0\). Thus there is a unique zero, with the speed increasing before it and decreasing after it. The map from \(x\) to \(r\) is strictly increasing, so the zero is the unique global maximizing rate.

For \(y=cx>0\), \(\partial_c H=\coth y-y\operatorname{csch}^2y>0\): the numerator over \(\sinh^2y\) is \(\sinh y\cosh y-y\), vanishing at zero with strictly positive derivative for \(y>0\). By implicit differentiation \(dx_*/dc=-\partial_c H/\partial_x H>0\). In the limit \(c\uparrow1\), any bounded optimizer would tend to a finite positive value by monotonicity, contradicting \(H(x,1)=2/x>0\). At the zero, apply the mean-value theorem in \(c\) to \(u\mapsto u\coth(ux_*)\):
\[
 \frac{2}{x_*}=(1-c)\left[\coth(\theta x_*)-\theta x_*\operatorname{csch}^2(\theta x_*)\right],\qquad c<\theta<1.
\]
As \(\theta x_*\to\infty\), the bracket tends to one, proving the claimed scaling.

## Verification

The accompanying `check.py` uses only the Python standard library. It brackets and solves the critical-point equation, checks the derivative signs on either side of representative roots, checks the ordered roots at those asymmetries, and illustrates the large-asymmetry scaling. These bounded numerical diagnostics do not replace the strict inequalities and limiting argument above.

## Relationship to prior work and limitations

The mean-current formula is from [1]. Their Eq. (27) and Fig. 7 emphasize nonmonotonicity of dimensionless velocity versus system length. For the physical rate optimization with fixed \(D,L,c\), conversion to physical units gives the \(x^2\) prefactor, rather than the dimensionless velocity's \(x\) prefactor. The result here is the exact uniqueness, strict comparative statics and singular asymptotic for this physical optimum. The related asymmetric-diffusivity record [2] concerns the unwrapped variance and a diffusivity maximum, not the physical drift optimum; no dispersion result is asserted here. These conclusions do not address finite return duration, other renewal-clock distributions, finite-time transport, or efficiency optimization. The literature comparison is not exhaustive.

## References

1. C. Roberts, E. Sezik and E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698 (2024), Sec. IV. https://arxiv.org/abs/2405.10698
2. *Exact drift-dependent diffusivity and weak-reset enhancement in an asymmetric Brownian ratchet*. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-drift-dependent-diffusivity-and-weak-reset-enhancement-in--1be33cfa05c2
