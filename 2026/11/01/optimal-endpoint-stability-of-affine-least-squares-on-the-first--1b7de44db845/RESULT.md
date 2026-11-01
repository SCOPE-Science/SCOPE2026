# Optimal endpoint stability of affine least squares on the first two Boolean layers

## Finding

Let \(n\ge3\), and let \(\Omega_n\) consist of all subsets of \(\{1,\ldots,n\}\) having cardinality one or two. For \(0<\theta<1\), equip the singleton layer with total probability \(1-\theta\) and the pair layer with total probability \(\theta\), uniformly within each layer. Let \(P_\theta\) be the real \(L^2\)-orthogonal projection of functions on \(\Omega_n\) onto the restrictions of all affine coordinate functions \(a_0+\sum_{i=1}^n a_i\mathbf1_{\{i\in X\}}\).

Set
\[
H=n-1+(n-3)\theta,\qquad
A=\frac{4(n-1)(n-2)}{nH},\qquad
r=\frac{(n-2)(n-3)}{n(n-1)}.
\]
Then the exact, attained \(\ell^\infty\)-operator norm is
\[
\boxed{\ \|P_\theta\|_{\infty\to\infty}=\max\{R_1(\theta),R_2(\theta)\}\ },
\]
where
\[
R_1(\theta)=1+\theta A,\qquad
R_2(\theta)=1+(1-\theta)A+2r\left(\frac{4(n-1)\theta}{H}-1\right)_+,
\quad (u)_+=\max\{u,0\}.
\]
Every singleton row of the projection kernel has absolute mass \(R_1\), and every pair row has absolute mass \(R_2\).

**Sharp design law.** Among all such positive exchangeable two-layer probability measures,
\[
\boxed{\ \min_{0<\theta<1}\|P_\theta\|_{\infty\to\infty}
=3-\frac4n,\qquad
\theta_*=\frac{n-1}{n+1}\ },
\]
and the minimizing mixture \(\theta_*\) is unique. For \(\theta<\theta_*\), precisely the pair-layer rows maximize; for \(\theta>\theta_*\), precisely the singleton-layer rows maximize; and at \(\theta=\theta_*\), all rows maximize. This minimizing measure is uniform on all \(n+\binom n2\) points, equivalently the law of independent fair Bernoulli coordinates conditioned on having exactly one or two successes. Thus, in the one-parameter conditional Bernoulli family, the fair parameter uniquely minimizes worst-case affine least-squares amplification.

For \(0\le f\le1\), the largest possible negative value of \(P_\theta f\) in absolute magnitude, as well as the largest overshoot above one, is \((\|P_\theta\|-1)/2\). Its minimum over mixtures is \(1-2/n\), attained only at \(\theta_*\). All asserted norms and undershoots are realized by explicit kernel-sign indicator inputs.

## Assumptions and scope

The finite sample space includes **both** the singleton and pair layers, with strictly positive probability on each atom. The coordinate representation identifies a subset \(X\) with its indicator vector in \(\mathbb R^n\). The affine range has dimension \(n+1\) when \(n\ge3\), because an affine function vanishing on all singletons and pairs is zero. All operator norms here use the supremum norm on functions over \(\Omega_n\), not the Hilbert norm. We optimize only the relative masses of the two uniform layers, not arbitrary nonexchangeable atomic weights or arbitrary projections onto the same affine space.

## Proof

**1. Exact kernel.** For a random \(X\) with the stated law, write \(S=|X|\). Its first and second moments satisfy \(\mathbb ES=1+\theta=:m\), \(\operatorname{Var}S=\theta(1-\theta)\), and \(\mathbb E[S(n-S)]=H\). Coordinate exchangeability gives the covariance eigenvalue \(\theta(1-\theta)/n\) in the constant-vector direction and eigenvalue \(H/[n(n-1)]\) on the orthogonal complement. Both are positive. Thus the affine reproducing kernel is
\[
K_\theta(x,y)=1+
\frac{(|x|-m)(|y|-m)}{\theta(1-\theta)}
+\frac{n(n-1)}{H}\left(|x\cap y|-\frac{|x||y|}{n}\right).
\]
It satisfies \((P_\theta f)(x)=\mathbb E[K_\theta(x,Y)f(Y)]\) and \(\mathbb E[K_\theta(x,Y)]=1\). For \(s=|x|\), \(\ell=|y|\), the constant part of the kernel is \(1/(1-\theta)\) if \(s=\ell=1\), \(1/\theta\) if \(s=\ell=2\), and zero if \(s\ne\ell\).

**2. Singleton rows.** For fixed singleton \(x\) and a uniformly sampled pair \(Y\), the overlap \(U=|x\cap Y|\) equals one with probability \(2/n\) and zero otherwise, giving
\[
\mathbb E|U-2/n|=\frac{4(n-2)}{n^2}.
\]
The kernel is nonnegative on singleton–singleton pairs: its minimum is \(1/(1-\theta)-(n-1)/H>0\). Its singleton-layer contribution to the row's absolute mass is therefore exactly one, whereas the cross-layer contribution is \(\theta A\). Hence the singleton row norm is \(R_1\).

**3. Pair rows.** The same overlap calculation gives a cross-layer absolute contribution \((1-\theta)A\) to a fixed pair row. On the pair layer, the overlap \(U=|x\cap Y|\) ranges over zero, one, two; the kernel is
\[
\frac1\theta+\frac{n(n-1)}H\left(U-\frac4n\right).
\]
It is positive whenever \(U\ge1\) (for \(n=3\), this follows from \(1/\theta-1>0\); for \(n\ge4\), it is immediate). The sole potentially negative case is \(U=0\), occurring with probability \(r\), and it is negative precisely when \(4(n-1)\theta/H>1\). The signed integral over the pair layer is one, so passing to absolute values adds twice the negative mass:
\[
R_2=1+(1-\theta)A+2r\left(\frac{4(n-1)\theta}{H}-1\right)_+.
\]
For \(n=3\), \(r=0\) because two pairs cannot be disjoint, and the same expression remains valid. Permutation symmetry makes these the only two row types. Taking \(f(y)=\operatorname{sgn}K_\theta(x,y)\) at a maximizing row gives equality in the operator-norm bound.

**4. Unique optimal mixture and transition.** The singleton expression is strictly increasing in \(\theta\), since
\[
\frac{dR_1}{d\theta}
=\frac{4(n-1)^2(n-2)}{nH^2}>0.
\]
Before the disjoint-pair sign threshold \(\theta_0=(n-1)/(3n-1)\), the second row expression has derivative
\[
\frac{dR_2}{d\theta}
=-\frac{8(n-1)(n-2)^2}{nH^2}<0.
\]
Above this threshold, for \(n\ge4\), its derivative is
\[
\frac{dR_2}{d\theta}
=-\frac{8(n-1)(n-2)}{nH^2}<0.
\]
For \(n=3\), the disjoint-pair term vanishes and \(R_2\) remains strictly decreasing by the first derivative formula. Substituting \(\theta_*=(n-1)/(n+1)>\theta_0\) gives
\[
H=\frac{2(n-1)^2}{n+1},\qquad
\frac{4(n-1)\theta_*}{H}-1=1,
\qquad R_1(\theta_*)=R_2(\theta_*)=3-\frac4n.
\]
As one row function is strictly increasing and the other strictly decreasing, their unique crossing is the unique global minimizer of their maximum. Their dominance on either side gives the asserted complete row-type classification.

**5. Uniformity, conditioning, and positivity.** Uniform mass on all singleton and pair atoms has pair-layer mass \(\binom n2/[n+\binom n2]=(n-1)/(n+1)\). If independent Bernoulli coordinates have success probability \(p\in(0,1)\), conditioning on \(S\in\{1,2\}\) gives pair-to-singleton mass ratio \((n-1)p/[2(1-p)]\); it equals \((n-1)/2\) exactly at \(p=1/2\). Finally every kernel row integrates to one. The maximal negative mass of a row is half of its absolute mass minus one. Choosing the indicator of its negative entries attains the maximal undershoot, while the complementary indicator attains the maximal overshoot.

**6. Connection to determinant-optimal weighting.** The same covariance decomposition gives
\[
\det\operatorname{Cov}(X)=
\frac{\theta(1-\theta)}n
\left(\frac{H}{n(n-1)}\right)^{n-1}.
\]
The logarithm, up to a constant, is \(\log\theta+\log(1-\theta)+(n-1)\log H\), with strictly negative second derivative. Its first derivative vanishes at \(\theta_*\). Consequently the unique minimum-endpoint-amplification design also maximizes the covariance determinant (the D-optimal design within the exchangeable two-layer family). The determinant criterion and the present endpoint criterion are different optimization objectives; the coincidence is special to this family. The determinant-optimality phenomenon is related to existing rank-selected Boolean-polytope ellipsoid calculations and is not independently asserted as new.

## Verification

The standalone `verify.py` forms the weighted Gram matrix for the constant and all \(n\) coordinate functions, inverts it over exact rational numbers, and evaluates **every** row sum over the full finite sample space independently of the displayed two-row derivation. It compares 46 parameter profiles and 1,061 individual row instances for \(3\le n\le9\), and checks symbolic monotonicity, the unique crossing, and the determinant stationary identity. Run `python verify.py` with Python 3 and SymPy. The checker verifies representative finite cases and symbolic identities; the proof of the universal statement is the analytic argument above, not bounded enumeration.

## Relationship to prior work

Filmus–Kindler–Mossel–Wimmer (2015) and Filmus–Mossel (2015) study harmonic/low-degree functions on **single** Boolean slices, their orthogonality and comparison of distributions across slices; in particular, the latter's Theorem 3.10 supplies general exchangeable-measure harmonic orthogonality. Those results do not determine sharp signed kernel row masses for the present **two-layer mixture**, nor optimize their \(\ell^\infty\) amplification. General covariance and projection-kernel identities are standard and are not claimed as new.

A published rank-selected Boolean-polytope ellipsoid calculation gives the covariance determinant and an optimal two-rank design for a *different* criterion, minimum enclosing ellipsoid volume. The present absolute-kernel norm and its layer-type crossover do not follow from an ellipsoid volume formula; conversely, the covariance-determinant corollary here is not new in isolation. Single-slice Johnson spectral-projection norms likewise apply to one Hamming layer with its own harmonic representation, not to the coupling between the present two layers. Possible equivalent endpoint calculations under design-theory, incidence-matrix or discrete least-squares terminology remain a publication-priority risk.

## Limitations

The result applies only to finite real affine orthogonal projection on exactly two positive-weight layers, of subset sizes one and two, with uniform conditional distributions on each layer. It does not address higher-degree functions, nonexchangeable reweighting, other pairs of ranks, or minimum-norm projections that need not be orthogonal. The parameter endpoints \(\theta=0,1\) are excluded, since one of the two layers then leaves the support. Same-method verification is not an independent audit, and the literature search does not certify worldwide priority.

## References

1. Y. Filmus, G. Kindler, E. Mossel and K. Wimmer, *Invariance principle on the slice*, arXiv:1504.01689, first submitted 2015-04-07, https://arxiv.org/abs/1504.01689. Sections 1–4 concern single-slice harmonic analysis and invariance, not the two-layer endpoint projection norm.
2. Y. Filmus and E. Mossel, *Harmonicity and Invariance on Slices of the Boolean Cube*, arXiv:1507.02713, first submitted 2015-07-09, https://arxiv.org/abs/1507.02713. Section 3.2 treats exchangeable harmonic orthogonality; Section 6 compares multiple slices in Hilbert-distribution norms rather than their sharp \(\ell^\infty\) projection constant.
3. *Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes*, publicly available mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-l-wner-ellipsoids-of-arbitrary-rank-selected-boolean-polyt--3c04f47dc8c3. Its covariance-determinant criterion is compared explicitly, not treated as evidence of a new determinant theorem.
