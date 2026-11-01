# Exact triple-Poisson peak-resolution threshold and fold contrast

## Finding

Let \(P_h(x)=h/[\pi(x^2+h^2)]\), with \(h>0\), be the Poisson kernel of the upper half-plane. Let
\[
F_h(x)=\sum_{j=-1}^{1}P_h(x-j),\qquad x\in\mathbb R.
\]
This is the harmonic Poisson extension, at height \(h\), of the three-point measure \(\delta_{-1}+\delta_0+\delta_1\). Its complete real critical-point diagram has one sharp threshold \(h_c=1/\sqrt2\).

**Exact phase diagram.** If \(0<h<h_c\), there are exactly five distinct stationary points, ordered
\[
-x_+<-x_-<0<x_-<x_+,
\]
with strict maxima at \(-x_+,0,x_+\) and strict minima at \(-x_-,x_-\). For \(h=h_c\), the stationary points are exactly \(-1/\sqrt2,0,1/\sqrt2\); the two outer points are stationary inflections (neither maxima nor minima), while the center is a strict maximum. For \(h>h_c\), the center is the sole stationary point and \(F_h\) is strictly decreasing on \((0,\infty)\) and increasing on \((\! -\infty,0)\).

**Exact algebraic radii.** Write \(s=h^2\). For \(0<s<1/2\) the polynomial
\[
Q_s(y)=3(y+s)^4+(4s+1)(1-4y)
\]
has precisely two positive roots, \(0<y_-(s)<y_+(s)\), both simple. Then \(x_-=\sqrt{y_-}\) and \(x_+=\sqrt{y_+}\).

**Sharp collision and contrast.** Put \(\mu=1/2-h^2\). As \(\mu\downarrow0\),
\[
x_\pm=\frac1{\sqrt2}\pm\frac{\sqrt2}{3}\sqrt\mu+O(\mu),\qquad
x_+-x_-=\frac{2\sqrt2}{3}\sqrt\mu+O(\mu),
\]
and
\[
F_h(x_+)-F_h(x_-)=\frac{8\sqrt2}{9\pi}\mu^{3/2}+O(\mu^2).
\]
The latter positive coefficient is the exact leading-order peak-to-valley contrast of the outer mode. The three-maxima phase therefore disappears by two symmetric folds, not by flattening the central maximum.

## Assumptions and scope

All assertions hold for every real \(h>0\) and all \(x\in\mathbb R\). A stationary point means a zero of the derivative with respect to \(x\); multiplicity of a derivative zero is distinguished from the number of **distinct** stationary points. At \(h=h_c\) each off-center derivative zero has multiplicity two, and the central zero is simple. The \(O\)-terms are as \(\mu\downarrow0\), with fixed unit source spacing. Rescaling the source sites to \(-d,0,d\), \(d>0\), replaces the threshold by \(d/\sqrt2\), by \(F_{h,d}(x)=d^{-1}F_{h/d}(x/d)\). All three source strengths are positive and equal; arbitrary unequal masses, non-equispaced sites, and more sites are outside the theorem.

## Proof

**Step 1: an exact derivative factorization.** Remove the positive constant \(h/\pi\) and put
\[
V_s(x)=\frac1{x^2+s}+\frac1{(x-1)^2+s}+\frac1{(x+1)^2+s},\qquad s>0.
\]
Set
\[
D_s(x)=(x^2+s)^2((x-1)^2+s)^2((x+1)^2+s)^2>0.
\]
Direct differentiation and collection of the three rational terms gives the polynomial identity
\[
D_s(x)V_s'(x)=-2xQ_s(x^2),\quad
Q_s(y)=3(y+s)^4+(4s+1)(1-4y).
\]
Thus all nonzero real critical points correspond bijectively to positive roots of \(Q_s\), with the same multiplicity. The origin is always critical. It is a strict maximum since
\[
V_s''(0)=-\frac{2(3s^3-3s^2+3s+1)}{s^2(1+s)^3}<0,
\]
using \(3s^3-3s^2+3s+1=3s(s^2-s+1)+1>0\).

**Step 2: a complete positive-root census.** Differentiating on \(y\ge0\) gives
\[
Q_s'(y)=12(y+s)^3-4(4s+1),\qquad Q_s''(y)=36(y+s)^2>0.
\]
Write \(r=((4s+1)/3)^{1/3}\). The unique unconstrained minimizer is \(y_0=r-s\); at that point
\[
Q_s(y_0)=9r^4(r^2-1).
\]
When \(0<s<1/2\), one has \(r<1\) and \(y_0>0\): indeed \(r^3-s^3=(4s+1)/3-s^3>0\) on this interval (or use \(r>s\) directly there). Consequently \(Q_s(y_0)<0\), whereas \(Q_s(0)=3s^4+4s+1>0\) and \(Q_s(y)\to+\infty\). Strict convexity gives exactly two distinct positive simple roots. When \(s=1/2\), direct factorization yields
\[
Q_{1/2}(y)=\frac3{16}(2y-1)^2(4y^2+12y+17),
\]
and the quadratic factor is positive for every \(y\ge0\). Thus \(y=1/2\) is the only positive root, double. When \(s>1/2\), \(r>1\). If \(y_0\ge0\), the global minimum \(9r^4(r^2-1)\) is positive. If \(y_0<0\), \(Q_s\) is increasing for \(y\ge0\), starting at its strictly positive value at zero. Therefore there are no positive roots for any \(s>1/2\).

The sign of \(V_s'(x)\), for \(x>0\), is opposite to the sign of \(Q_s(x^2)\). Below threshold, \(Q_s\) alternates positive, negative, positive across its two roots, yielding a local minimum at \(x_-\) and maximum at \(x_+\). At threshold its only positive root is double and the derivative does not change sign, yielding a stationary inflection. Above threshold the derivative is strictly negative on the positive half-axis. Symmetry handles negative \(x\).

**Step 3: collision scale and exact contrast.** Set \(s_c=y_c=1/2\), \(x_c=1/\sqrt2\), and \(\mu=s_c-s>0\). At the double root, direct differentiation yields
\[
Q_{s_c}(y_c)=0,\quad \partial_yQ_{s_c}(y_c)=0,\quad
\partial_y^2Q_{s_c}(y_c)=36,\quad
\partial_sQ_{s_c}(y_c)=8.
\]
The analytic Taylor expansion gives
\[
Q_{s_c-\mu}(y_c+\eta)=18\eta^2-8\mu+
O(|\eta|^3+\mu|\eta|+\mu^2).
\]
The two simple roots therefore satisfy \(y_\pm=y_c\pm(2/3)\sqrt\mu+O(\mu)\); taking positive square roots yields \(x_\pm=x_c\pm(\sqrt2/3)\sqrt\mu+O(\mu)\).

For the height contrast, the exact analytic derivatives at the collision are
\[
\partial_sV_s'(x)\big|_{(x_c,s_c)}=-2\sqrt2,
\qquad \partial_x^2V_s'(x)\big|_{(x_c,s_c)}=-18\sqrt2.
\]
Consequently, uniformly when \(|\xi|=O(\sqrt\mu)\),
\[
V_{s_c-\mu}'(x_c+\xi)=2\sqrt2\,\mu-9\sqrt2\,\xi^2+
O(|\xi|^3+\mu|\xi|+\mu^2).
\]
Integrate from \(x_-\) to \(x_+\), using endpoints \(x_c\pm a\sqrt\mu+O(\mu)\), where \(a=\sqrt2/3\). The leading integral is
\[
\int_{-a\sqrt\mu}^{a\sqrt\mu}
(2\sqrt2\,\mu-9\sqrt2\,\xi^2)\,d\xi
=\frac{16}{9}\mu^{3/2}.
\]
Replacing the approximate endpoints by the true critical points changes this integral by \(O(\mu^2)\), as does the integrated Taylor remainder. Hence
\[
V_s(x_+)-V_s(x_-)=\frac{16}{9}\mu^{3/2}+O(\mu^2).
\]
Since \(F_h=(h/\pi)V_{h^2}\) and \(h=1/\sqrt2+O(\mu)\), the claimed Poisson contrast follows. This completes the classification and the two sharp local exponents. \(\square\)

## Verification

The included `CHECK.py` independently expands the exact derivative numerator in two polynomial variables, verifies the factored threshold polynomial over rational coefficients, and evaluates representative strict-minimum inequalities. Run `python CHECK.py` with the Python standard library. The exact normal-form derivatives, and the two root-count arguments, are displayed in the proof rather than inferred from finite tests. The root-count proof applies to the entire continuum \(s>0\). Numerical checks at \(s=1/2-10^{-3},1/2-10^{-5},1/2-10^{-7}\) corroborated convergence of the contrast coefficient to \(16/9\) before packaging; numerical agreement is not used as a proof.

## Relationship to prior work

Duan's 2026 theorem (arXiv:2608.28376v1) and Oliveira's independently obtained 2026 theorem (arXiv:2609.00336v1) establish a sharp universal upper bound of \(2n-1\) distinct stationary points for the restriction to a line of an \(n\)-source inverse-power potential. Their theorems imply **at most five** stationary points for the present three-source family, and their constructions show that this upper bound can be attained for some small heights. Neither of the examined full texts derives the exact all-height threshold \(h_c\), the complete topology at equality, or the quantitative fold and peak-to-valley contrast. The present result does not replace or extend the general zero-count theorem; it answers a separate optimal resolution question for an important minimal symmetric source geometry. The same harmonic function may equivalently be viewed as a three-component equal-scale Cauchy density mixture, so literature on Cauchy mixture modality is a possible route to implicit earlier coverage.

## Limitations

The sources are assumed to be equispaced, equally weighted, and positive. This theorem does not classify arbitrary three-atom measures, more sources, or unrelated scale-space kernels. The terminal stationary points at the threshold are not genuine extrema. General line-restriction upper bounds and the bimodality theory of two-component Cauchy mixtures predate this result. Literature searching and the two primary-text comparisons did not establish an exhaustive global priority claim; unindexed or implicit historical classifications of this specific Cauchy mixture remain possible. No independent mathematical audit has been performed.

## References

1. Xiuqing Duan, *Critical Points of Line Restrictions of Signed Point-Charge Potentials*, arXiv:2608.28376v1, first public version 2026-08-28. https://arxiv.org/abs/2608.28376
2. Gonçalo Oliveira, *Critical points of point charge potentials along lines*, arXiv:2609.00336v1, first public version 2026-08-31. https://arxiv.org/abs/2609.00336
3. Zakiah I. Kalantan and Jochen Einbeck, *Quantile-Based Estimation of the Finite Cauchy Mixture Model*, *Symmetry* **11** (2019), 1186, DOI:10.3390/sym11091186. This gives Cauchy-mixture context, not a claimed covering result.
