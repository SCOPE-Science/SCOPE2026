# Genus-four transverse curvature transition in finite-dimensional pseudoconvex Bergman examples

## Finding
For every integer \(n\ge3\) and genus parameter \(d\ge2\), consider the pseudoconvex domains \(\Omega_{n,d}\) of Yuan (2026), biholomorphic to \(X_d\times D\), where
\[
 X_d=\{(x,y)\in\mathbb C^2:y^2=x^{2d+1}-1\},\qquad
 A^2(D)=\mathbb C f_0,\quad \|f_0\|_2=1.
\]
Their intrinsic Bergman Hermitian form has rank one away from the \(2d+1\) submanifolds corresponding to \(\{y=0\}\times D\), and rank zero exactly on these submanifolds. Its nondegenerate transverse metric at the two points of \(X_d\) with \(x=0\) has **positive** Gaussian curvature for \(d=2,3\), and **negative** Gaussian curvature for every \(d\ge4\). Thus the genus-four threshold is exact. The case \(d=1\) has identically zero Bergman form.

A quantitative version uses \(a_j=(j+1)/(2d+1)\) and the positive coefficients
\[
 c_j=\frac{2d+1}{2\pi}\,
 \frac{\Gamma(1-a_j)\Gamma(\tfrac12+a_j)}
      {\Gamma(a_j)\Gamma(\tfrac12-a_j)},\qquad
 p_d(t)=\sum_{j=0}^{d-1}c_jt^j.
\]
In the coordinate \(x\) away from the branch locus, the transverse Bergman form is \(i g_d(|x|^2)dx\wedge d\bar x\) with
\[
 g_d(t)=\frac{d}{dt}\left[t\frac{d}{dt}\log p_d(t)\right]>0.
\]
With normalized curvature \(\kappa_d=-(1/g_d)\partial_x\partial_{\bar x}\log g_d\) (equal to one half the Gaussian curvature for the convention \(ds^2=g_d|dx|^2\)), at \(x=0\) one has
\[
 \boxed{\kappa_d(0)=2-4\frac{c_0c_2}{c_1^2}},\qquad
 c_2=0\ \text{when }d=2.
\]
In particular \(\kappa_2(0)=2\), \(\kappa_3(0)=0.2363427315\ldots\), and \(\kappa_4(0)=-0.6066468109\ldots\). These decimals are diagnostics; the all-genus signs are proved using rational inequalities below.

## Assumptions and scope
The domain \(D\), its base-point-free one-dimensional Bergman space, the Runge embedding \(T\), and the biholomorphic product representation are precisely those of the construction in Section 3.2 of Yuan's 2026 paper. All statements are invariant under that biholomorphism. The Bergman Hermitian form here means \(i\partial\bar\partial\log K(z,z)\), not the distinct canonical/Theta metric \(\sum_j|\alpha_j|^2\,|dx|^2\) on a Riemann surface. It is a semipositive, generally degenerate form in complex dimension \(n\), so curvature is asserted only along the positive transverse direction away from degeneration points. No positive-definite Bergman metric on the whole domain is asserted.

## Proof
**1. Orthogonal holomorphic differentials.** By the full construction and the isometric product lemma of Yuan, the Bergman space corresponds isometrically to the holomorphic differentials \(\alpha_j=x^jdx/y\) on the compactified curve for \(0\le j<d\). Rotation \(x\mapsto e^{2\pi i/(2d+1)}x\), with \(y\) unchanged, is an isometry of the canonical \(L^2\) pairing and gives distinct characters to these differentials, proving their pairwise orthogonality.

Write \(m=2d+1\) and \(a=(j+1)/m\). Summing over the two sheets and substituting \(w=x^m\) gives, with \(dA\) Euclidean area,
\[
 \|\alpha_j\|^2=2\int_{\mathbb C}\frac{|x|^{2j}}{|x^m-1|}\,dA(x)
 =\frac2m\int_{\mathbb C}|w|^{2a-2}|1-w|^{-1}\,dA(w).
\]
For \(0<a<1/2\), a Gaussian-integral calculation yields the complex beta integral
\[
 \int_{\mathbb C}|w|^{2a-2}|1-w|^{-1}\,dA(w)
 =\pi\frac{\Gamma(a)\Gamma(\tfrac12-a)}
 {\Gamma(1-a)\Gamma(\tfrac12+a)}.
\]
For completeness, insert the Laplace representations of \(|w|^{-2(1-a)}\) and \(|1-w|^{-1}\), integrate the Gaussian over \(w\), then substitute \(u=st,v=s(1-t)\). The \(s\) integral is \(\Gamma(\tfrac12-a)[t(1-t)]^{a-1/2}\); the remaining integral is \(B(\tfrac12,a)\), giving exactly the displayed formula. Thus \(c_j=\|\alpha_j\|^{-2}\) in the stated common norm convention (any uniform canonical-norm factor would cancel from all metric formulas).

**2. Rank and explicit metric.** The diagonal Bergman density in any local trivialization of the canonical bundle is a nowhere-vanishing holomorphic factor in absolute square times \(p_d(|x|^2)\); taking \(\partial\bar\partial\log\) eliminates that factor. Thus the form is \(i\partial\bar\partial\log p_d(|x|^2)\), pulled back from \(x\), with no dependence on the \(D\) coordinates. For \(t>0\) let \(\pi_j(t)=c_jt^j/p_d(t)\). Direct differentiation gives
\[
 t g_d(t)=\sum_j j^2\pi_j(t)-\left(\sum_j j\pi_j(t)\right)^2>0
\]
for \(d\ge2\); at \(t=0\), \(g_d(0)=c_1/c_0>0\). Therefore the form has rank one wherever \(dx\ne0\). On \(X_d\), \(dx=0\) exactly at \(y=0\): indeed \(2y\,dy=mx^{m-1}dx\), and these are \(m=2d+1\) simple branch points. The pullback form vanishes exactly there. When \(d=1\), \(p_d\) is constant and the form vanishes identically.

**3. Curvature formula.** Let \(t=|x|^2\). Expanding \(p_d\) at zero yields \(g_d(0)=c_1/c_0\) and \(g_d'(0)=4(c_2/c_0-c_1^2/(2c_0^2))\). Since \(\partial_x\partial_{\bar x}\log g_d(|x|^2)|_{x=0}=g_d'(0)/g_d(0)\), we obtain \(\kappa_d(0)=2-4c_0c_2/c_1^2\). For \(d=2\) the \(c_2\) term is absent, giving \(2\).

**4. Exact universal genus threshold.** Set \(a=1/(2d+1)\), and let \(W(s)=\Gamma(1-s)\Gamma(\tfrac12+s)/[\Gamma(s)\Gamma(\tfrac12-s)]\). For \(d\ge3\), the gamma Taylor expansions (valid for \(|s|<1/2\)) give
\[
 \log\frac{W(s)}s=-4s\log2
 -\sum_{\substack{k\ge3\\k\;\mathrm{odd}}}
 \frac{2(2^k-2)\zeta(k)}{k}s^k.
\]
Consequently
\[
 \frac{c_0c_2}{c_1^2}=\frac34e^{-E(a)},\qquad
 E(a)=\sum_{\substack{k\ge3\\k\;\mathrm{odd}}}
 \frac{2(2^k-2)\zeta(k)(1+3^k-2^{k+1})}{k}a^k.
\]
Every displayed coefficient is strictly positive. Hence \(\kappa_d(0)=2-3e^{-E(a)}\), whose sign is positive precisely when \(E(a)>\log(3/2)\).

At \(d=3\), \(a=1/7\); since \(\zeta(k)>1\), truncation at \(k=11\) provides an exact rational lower bound
\[
 E(1/7)>\frac{865827184}{1977326743}>\frac5{12}>
 \log(3/2).
\]
The last inequality is the third-order alternating-series upper bound for \(\log(1+1/2)\).

For every \(d\ge4\), \(a\le1/9\). The cubic term is \(48\zeta(3)a^3\le60/729\) since \(\zeta(3)\le5/4\). For all odd \(k\ge5\), bound its coefficient by \((2\zeta(5)/5)6^k\), and use \(\zeta(5)\le9/8\). Summing the geometric odd tail gives
\[
 0<E(a)\le\frac{60}{729}+
 \frac{2(9/8)}5\frac{(2/3)^5}{1-(2/3)^2}
 =\frac{1148}{6075}<\frac25<\log(3/2).
\]
The final strict inequality follows, for example, from \(\log(1+t)\ge 2t/(2+t)\) at \(t=1/2\), where equality in the logarithmic bound holds only at \(t=0\). This proves the negative sign for all \(d\ge4\) and completes the classification.

## Verification
The standalone `verify_curvature.py` checks the exact coefficients and rational bounds, verifies \(865827184/1977326743>5/12\) and \(1148/6075<2/5\), and optionally evaluates six genus samples with high-precision gamma functions. The actual replay printed `PASS`. These finite computations supplement, but do not replace, the universal analytic series bounds in the proof.

## Relationship to prior work
Yuan's arXiv:2610.21749, Section 3.2 and Remark 12, establishes the underlying pseudoconvex examples, their dimension, product structure, and holomorphic-differential basis. Those construction facts are assumed, not claimed as discoveries here. Classical hyperelliptic canonical-map theory already implies the branch-point degeneracy, also discussed explicitly by Castorena (2007). The new contribution is the complete gamma-normalized transverse Bergman kernel and the exact all-genus curvature sign transition for Yuan's specific weighted series. Castorena studies Gaussian curvature of the canonical/Theta metric, which is not the curvature of the derived \(i\partial\bar\partial\log K\) form. General Bergman and Fubini–Study identities do not by themselves determine the coefficient-dependent genus cutoff.

## Limitations
This is a statement for the specified family \(\Omega_{n,d}\), not all pseudoconvex domains with finite-dimensional Bergman spaces. The positive curvature in genus two and three occurs only along a nondegenerate transverse direction of a globally degenerate Hermitian form; it does not answer the Huang–Li conjecture about well-defined positive-definite Bergman metrics. No statement is made about curvature elsewhere, except the given exact metric formula. The rank-drop observation alone is classical; the exact genus transition is the distinguishing conclusion. Historical specialized calculations not identified in the targeted source searches might anticipate the gamma formula or its curvature consequence; independent review remains outstanding.

## References
1. Yuan Yuan, *Pseudoconvex domains in complex Euclidean space with finite-dimensional Bergman spaces*, arXiv:2610.21749, first submitted 2026-10-15, Section 3.2 and Remark 12. https://arxiv.org/html/2610.21749v2
2. Abel Castorena, *Gaussian curvature at the hyperelliptic Weierstrass points*, arXiv:math/0703075 (2007), especially the canonical/Theta metric and its branch-point degeneracy. https://arxiv.org/abs/math/0703075
3. Zheng Huang, *Asymptotics of the Gaussian Curvatures of the Canonical Metric on the Surface*, arXiv:math/0604579 (2006); background on the distinct canonical metric. https://arxiv.org/abs/math/0604579
