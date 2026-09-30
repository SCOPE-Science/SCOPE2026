# Three-point free convolution powers: no interior one-third cusp zero

## Setup

Let
\[
\mu=(\delta_{-1}+\delta_0+\delta_1)/3,\qquad t\ge 1.
\]
For \(t>1\), write \(G_t=G_{\mu^{\boxplus t}}\). With
\[
G_\mu(w)=\frac{3w^2-1}{3w(w^2-1)},\qquad F_\mu=1/G_\mu,
\]
the free-power subordination map is inverted by
\[
H_t(w)=tw-(t-1)F_\mu(w)
      =\frac{w(3w^2+2t-3)}{3w^2-1}.
\]
Thus \(H_t(w)=x\) is
\[
P_{t,x}(w)=3w^3-3xw^2+(2t-3)w+x=0.
\]

## Result

There is no interior point of the support, distinct from atoms and component endpoints, at which the absolutely continuous density vanishes like \(|x-x_0|^{1/3}\).

More precisely:

1. If \(1<t<3/2\), the absolutely continuous part has two symmetric bands. The density is strictly positive inside each band and vanishes with square-root order at the four band endpoints. The atoms at \(-t,0,t\) each have mass \(1-2t/3\).

2. If \(t=3/2\), there are no atoms and the support is \([-3/2,3/2]\). The density is positive away from \(0\) in the interior, while
   \[
   p_{3/2}(x)=\frac{3^{5/6}}{6\pi}|x|^{-1/3}(1+o(1))
   \]
   at \(x=0\). Thus the unique cubic degeneracy is a pole, not a cubic-root zero. The endpoints have inverse-square-root blow-up.

3. If \(t>3/2\), the absolutely continuous support is a single symmetric band, the density is strictly positive inside it, and its two endpoints are square-root zeros. There are no atoms.

## Algebraic verification

Direct differentiation gives
\[
H_t'(w)=\frac{9w^4-6tw^2+3-2t}{(3w^2-1)^2},
\]
and
\[
H_t''(w)=\frac{36(t-1)w(w^2+1)}{(3w^2-1)^3}.
\]
For \(t>1\), the only simultaneous real zero of \(H_t'\) and \(H_t''\) is
\((t,w)=(3/2,0)\). At that parameter
\[
H_{3/2}(w)=\frac{3w^3}{3w^2-1},
\]
and \(G_\mu(w)=1/(3w)+O(w)\), which yields the displayed \(|x|^{-1/3}\) constant.

The cubic discriminant is
\[
\operatorname{disc}_w P_{t,x}
 =12\left(9x^4+(3t^2-36t+27)x^2+(3-2t)^3\right).
\]
Putting \(y=x^2\), the quadratic in \(y\) has discriminant
\(9(t-1)(t+3)^3\). Its sign pattern gives the two-band, critical, and one-band regimes above. Simple real critical points give the usual square-root edge behavior under the standard free-convolution boundary regularity theory.

The atom formula for free convolution powers gives mass
\(t(1/3)-(t-1)=1-2t/3\), hence atoms occur exactly for \(1<t<3/2\).

The 2026-09-29 independent audit rederived the derivatives, discriminant, atom threshold, and cubic-pole constant symbolically.

## Reproducibility

Run `artifacts/verify_target.py`; the archived output is `artifacts/verify_output.txt`.

## Scope and literature context

Huang gives the general support/density framework for free convolution powers, and Moreillon gives general local classifications of singular support behavior. This record contributes only the explicit complete calculation for this three-atom law and the critical value \(t=3/2\); it does not claim a new general regularity theorem.

## References

- H.-W. Huang, “Supports of Measures in a free additive convolution semigroup,” arXiv:1205.5542.
- P. Moreillon, “Density of the free additive convolution of multi-cut measures,” arXiv:2209.15607.
- Z. Bao, L. Erdős, K. Schnelli, “On the support of the free additive convolution,” arXiv:1804.11199.
