# Universal logarithmic dispersion fingerprint in degenerate mKdV–Burgers shocks

## Statement

Consider the modified Korteweg–de Vries–Burgers equation
\[
 u_t+(u^3)_x=\mu u_{xx}-\kappa u_{xxx},\qquad \mu>0,\ \kappa\ge0,
\]
and the monotone degenerate Oleinik traveling shock \(U(\xi)\), \(\xi=x-3s^2t\), connecting
\[
 U(-\infty)=-2s,\qquad U(+\infty)=s,\qquad s>0.
\]
For \(\kappa>0\), assume the monotone regime
\[
 36\kappa s^2/\mu^2\le1.
\]
Then there is a constant \(C_U\), depending on the translation of the profile, such that
\[
\boxed{
 \frac1{s-U(\xi)}
 =\frac{3s}{\mu}\,\xi
 -\left(\frac1{3s}+\frac{6\kappa s}{\mu^2}\right)\log\xi
 +C_U+o(1)
 }
 \qquad(\xi\to+\infty).
\]
Equivalently,
\[
\boxed{
 s-U(\xi)
 =\frac{\mu}{3s\,\xi}
 +\left(\frac{\mu^2}{27s^3}+\frac{2\kappa}{3s}\right)
 \frac{\log\xi}{\xi^2}
 +O(\xi^{-2}).
 }
\]
The leading algebraic coefficient is independent of dispersion, while dispersion first appears in the logarithmic second term.

A translation-invariant consequence is the following comparison law. Let \(U_{\kappa_1}\) and \(U_{\kappa_2}\) be any two monotone profiles with the same \((\mu,s)\), with arbitrary fixed translations, and with \(\kappa_i\ge0\) in the corresponding monotone regime. Then
\[
\boxed{
 \lim_{\xi\to\infty}
 \frac{\xi^2}{\log\xi}
 \big(U_{\kappa_1}(\xi)-U_{\kappa_2}(\xi)\big)
 =\frac{2(\kappa_2-\kappa_1)}{3s}.
 }
\]
In particular, taking \(\kappa_1=0\),
\[
 \lim_{\xi\to\infty}
 \frac{\xi^2}{\log\xi}
 \big(U_0(\xi)-U_\kappa(\xi)\big)
 =\frac{2\kappa}{3s}.
\]
Thus profiles with different dispersion strengths have the same \(\xi^{-1}\) tail but are separated at order \((\log\xi)/\xi^2\). Their difference is integrable on every right half-line.

## Relation to the source paper

Eun, Han and Kim prove existence and monotonicity of this degenerate viscous-dispersive shock and establish two-sided bounds showing \(s-U(\xi)\asymp \xi^{-1}\) and \(U'(\xi)\asymp\xi^{-2}\) in the monotone regime. Their center-manifold calculation already contains the local expansion that drives the refinement below. The claim here is not the center-manifold coefficient itself; it is the resulting exact far-field coefficient, logarithmic correction, and the dispersion-comparison limit.

For the source normalization \(\mu=1\), write
\[
 z=U/s,\qquad \zeta=s^2\xi,\qquad \nu=\kappa s^2,
\]
and \(w=z-1\). The source paper derives the center-manifold graph
\[
 z'=g(w),\qquad
 g(w)=3w^2+(1+18\nu)w^3+O(w^4).
\]
This contains more asymptotic information than is used in its stated two-sided tail bounds.

## Proof

Set
\[
 v(\xi)=s-U(\xi)>0.
\]
In the source normalization \(\mu=1\), the center-manifold expansion above gives
\[
 U'=3s\,v^2-(1+18\kappa s^2)v^3+O(v^4),
\]
hence
\[
 v'=-3s\,v^2+(1+18\kappa s^2)v^3+O(v^4).
\]
For general \(\mu>0\), rescaling \(\eta=\xi/\mu\) replaces \(\kappa\) by \(\kappa/\mu^2\), so
\[
 v'=-\frac{3s}{\mu}v^2
 +\frac{1+18\kappa s^2/\mu^2}{\mu}v^3
 +O(v^4).
\]
Define \(y=1/v\). Then
\[
 y'=\frac{3s}{\mu}
 -\frac{1+18\kappa s^2/\mu^2}{\mu}\frac1y
 +O(y^{-2}).
\]
The source two-sided estimate already implies \(y\asymp\xi\). Therefore the last display first yields
\[
 y=\frac{3s}{\mu}\xi+O(\log\xi).
\]
Consequently,
\[
 \frac1y=\frac{\mu}{3s\,\xi}+O\!\left(\frac{\log\xi}{\xi^2}\right).
\]
Subtracting the leading linear term and the corresponding logarithm now leaves an integrable derivative:
\[
 \frac{d}{d\xi}\left[
 y-\frac{3s}{\mu}\xi
 +\left(\frac1{3s}+\frac{6\kappa s}{\mu^2}\right)\log\xi
 \right]
 =O\!\left(\frac{\log\xi}{\xi^2}\right).
\]
Hence the bracket converges to a finite constant \(C_U\), proving the inverse-tail expansion. Inverting it gives the stated expansion for \(s-U\).

A fixed translation \(\xi\mapsto\xi-a\) changes only the nonlogarithmic \(\xi^{-2}\) term. Therefore, subtracting the expansions for \(\kappa_1\) and \(\kappa_2\) gives the comparison limit. The same subtraction shows that the right-tail difference is \(O((\log\xi)/\xi^2)\), hence integrable.

## A reusable local mechanism

The calculation has a simple general form. Suppose a scalar diffusive-dispersive traveling wave approaches a characteristic right state \(u_+\) from below and its integrated flux defect satisfies
\[
 F(u_+-v)=A v^2+C v^3+O(v^4),\qquad A>0.
\]
Writing \(q=U'=-v'>0\), the profile equation
\[
 F(U)=\mu U'-\kappa U''
\]
becomes
\[
 F(u_+-v)=\mu q+\kappa q q_v.
\]
Thus
\[
 q=\frac{A}{\mu}v^2+
 \left(\frac{C}{\mu}-\frac{2\kappa A^2}{\mu^3}\right)v^3+O(v^4),
\]
and asymptotic integration gives
\[
 v(\xi)=\frac{\mu}{A\xi}
 +\left(-\frac{C\mu^2}{A^3}+\frac{2\kappa}{A}\right)
 \frac{\log\xi}{\xi^2}+O(\xi^{-2}).
\]
For the cubic flux at the right state \(s\), \(A=3s\) and \(C=-1\), recovering the formulas above. This local calculation is included as a proof mechanism, not as a claim of a new general theory of degenerate shocks.

## Why the refinement matters

The source paper shows that dispersion does not alter the coarse algebraic decay scale and obtains constants uniform in \(\kappa\). The expansion above identifies the first place where dispersion becomes visible: the \((\log\xi)/\xi^2\) coefficient changes by exactly \(2\kappa/(3s)\), independently of viscosity. This also upgrades a coarse same-scale statement to an explicit, translation-independent comparison between viscous and viscous-dispersive profiles.

## Verification

`artifacts/verify_logarithmic_tail.py` symbolically checks:

- the next center-manifold coefficients from the invariance equation;
- the general-viscosity \(\xi^{-1}+(\log\xi)\xi^{-2}\) ansatz directly in the integrated profile equation;
- the general local formula for a quadratic characteristic degeneracy;
- the viscosity-independent dispersion shift \(2\kappa/(3s)\).

The recorded output is in `artifacts/verification_output.txt`. These checks support the algebra; the proof above is analytic and does not rely on computation.

## Originality boundary and literature

The center-manifold expansion
\[
 g(w)=3w^2+(1+18\nu)w^3+O(w^4)
\]
is already present in arXiv:2609.20591v1 and is not claimed as new. The purely viscous profile equation is also explicit in Huang–Wang–Zhang, so the \(\kappa=0\) tail can be obtained directly from their first-order ODE. The present claim is restricted to the source-specific viscous-dispersive sharpening and, especially, the logarithmic dispersion fingerprint and pairwise comparison law.

Jacobs–McKinney–Shearer (1995) is the most relevant older source because it classifies traveling waves of the same modified KdV–Burgers equation. Its complete text was not inspected here; available bibliographic records and later literature establish its role in existence/classification, but this leaves a residual possibility that a comparable endpoint expansion appears there. Zhang et al. (2016) was inspected at the abstract/reference level and concerns global phase portraits and bounded traveling waves. Valls (2020) was inspected in full-text form sufficiently to verify that its term “algebraic traveling wave” refers to invariant algebraic curves in phase space, not algebraic far-field decay. No source located in the search stated the logarithmic coefficient or the pairwise dispersion-comparison limit above.

## Limitations

The result concerns the monotone degenerate shock profile and its right characteristic tail. It does not improve the nonlinear stability theorem for the full PDE, does not treat oscillatory shock profiles outside the monotone regime, and does not classify higher-order terms beyond the displayed logarithmic correction. The general local mechanism requires a smooth monotone profile on the relevant center manifold and a nonzero quadratic flux-defect coefficient. Originality is asserted only to the best of current knowledge.

## References

1. N. Eun, S. Han, J. Kim, *Large-Time Behavior towards Composite Waves of Degenerate Shock and Rarefaction Wave for Modified KdV–Burgers Equation*, arXiv:2609.20591v1 (2026).
2. F. Huang, Y. Wang, J. Zhang, *Time-asymptotic stability of composite waves of degenerate Oleinik shock and rarefaction for non-convex conservation laws*, Math. Ann. 392 (2025), 1–46; arXiv:2408.06801; DOI: 10.1007/s00208-024-03083-5.
3. D. Jacobs, B. McKinney, M. Shearer, *Travelling wave solutions of the modified Korteweg-de Vries-Burgers equation*, J. Differential Equations 116 (1995), 448–467; DOI: 10.1006/jdeq.1995.1043.
4. W. Zhang, Y. Sun, Z. Li, S. Pei, X. Li, *Bounded traveling wave solutions for MKdV-Burgers equation with the negative dispersive coefficient*, Discrete Contin. Dyn. Syst. B 21 (2016), 2883–2903; DOI: 10.3934/dcdsb.2016078.
5. C. Valls, *Algebraic traveling waves for the modified Korteweg–de Vries–Burgers equation*, Electron. J. Qual. Theory Differ. Equ. 2020, No. 48; DOI: 10.14232/ejqtde.2020.1.48.
