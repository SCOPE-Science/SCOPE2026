# Sharp two-ball reconstruction and three-ball nonuniqueness from random widths of coaxial ball hulls

## Finding
Let \(d\ge2\), and let \(K\subset\mathbb R^d\) be the convex hull of finitely many positive-radius closed Euclidean balls with centers on one line. If \(W\) is the length of its orthogonal projection onto a uniformly random unoriented line, its complete probability law uniquely determines the *directional width function* of \(K\), equivalently its central difference body \(K-K\). In dimension three this law consists of a possible initial atom followed by piecewise-constant densities with nonincreasing heights.

For the hull of **two** balls, provided neither ball contains the other, the law uniquely recovers their two radii and center separation, up to exchanging the balls. This is sharp: there exist hulls of **three pairwise disjoint, individually exposed balls** that are noncongruent yet have identical widths in **every direction**, not merely equal random-width laws.

## Assumptions and scope
Write \(e\in S^{d-1}\) for the common center direction and \(B(c_je,r_j)\) for balls with \(r_j>0\), where \(c_j\in\mathbb R\). A ball is *exposed* here if an open set of support normals selects it as the unique maximizing ball. Let \(T=|U\cdot e|\) for \(U\) uniform on \(S^{d-1}\), and \(W=h_K(U)+h_K(-U)\).

The CDF of \(T\), strictly increasing on \([0,1]\), is
\[
F_d(t)=I_{t^2}\left(\frac12,\frac{d-1}{2}\right).
\]
Its density for \(0<t<1\) is \(2\Gamma(d/2)(1-t^2)^{(d-3)/2}/[\sqrt\pi\,\Gamma((d-1)/2)]\).

## Proof
**1. Exact forward law and complete symmetral recovery.** The support function satisfies
\[
h_K(u)=H(u\cdot e),\qquad H(t)=\max_j\{r_j+c_jt\}.
\]
Hence the width depends only on \(T\), through
\[
g(t)=H(t)+H(-t),\quad 0\le t\le1.
\]
The function \(g\) is continuous, convex, nondecreasing and piecewise affine because \(H\) is convex piecewise affine and its even sum is convex. The uniform spherical-coordinate formula gives the stated \(F_d\). Since \(F_d\) is strictly increasing, the distribution of \(g(T)\) recovers \(g\): for \(0<t<1\),
\[
g(t)=\inf\{z:\mathbb P(W\le z)\ge F_d(t)\},
\]
with any endpoint ambiguity resolved by continuity. The values \(g(|u\cdot e|)\) equal \(h_{K-K}(u)\), so \(K-K\) is determined up to orientation. For \(d=3\), \(F_3(t)=t\), and the pushforward of uniform measure by nondecreasing convex piecewise-affine \(g\) is precisely an initial atom followed by uniform pieces of heights reciprocal to its positive successive slopes. Those slopes are nondecreasing.

**2. Explicit two-ball inverse.** Let the two radii be \(R\ge r>0\), with center separation \(L>R-r\), so neither ball contains the other. Define \(\Delta=R-r\). Up to translation and axis reversal,
\[
g(t)=\max\{2R,R+r+Lt\},\qquad 0\le t\le1.
\]
Let \(m=\min\operatorname{supp}W=2R\), \(M=\max\operatorname{supp}W=R+r+L\) and \(q=\mathbb P(W=m)=F_d(\Delta/L)\). Set \(\theta=F_d^{-1}(q)\), where \(\theta=0\) for \(q=0\). Then
\[
R=\frac m2,\qquad L=\frac{M-m}{1-\theta},\qquad r=\frac m2-\frac{\theta(M-m)}{1-\theta}.
\]
Every denominator is positive. In \(d=3\), the law has mass \(\Delta/L\) at \(2R\) and constant density \(1/L\) on \((2R,R+r+L)\). If \(L\le R-r\), the hull equals the larger ball and the smaller radius and center separation are not identifiable.

**3. Sharp three-ball obstruction.** With \(e\) a fixed unit vector, define
\[
K_1=\operatorname{conv}\bigl(B(0,2/5)\cup B(e,3/10)\cup B(2e,1/10)\bigr)
\]
and
\[
K_2=\operatorname{conv}\bigl(B(-e,1/5)\cup B(0,2/5)\cup B(e,3/10)\bigr).
\]
Each constituent pair is strictly disjoint: neighboring center distances equal one, exceeding every relevant radius sum. For \(-1\le t\le1\), direct comparison of affine supports gives
\[
H_1(t)=\frac25+(t-\tfrac1{10})_++(t-\tfrac15)_+,\quad
H_2(t)=\frac25+(t-\tfrac1{10})_++(-t-\tfrac15)_+,
\]
where \(x_+=\max\{x,0\}\). Therefore
\[
H_1(t)+H_1(-t)=H_2(t)+H_2(-t)
=\frac45+(|t|-\tfrac1{10})_++(|t|-\tfrac15)_+.
\]
Thus *every directional width* agrees. Nevertheless all three balls contribute genuine open spherical support patches: the active \(t\)-regions for the first hull are \(t<1/10\), \(1/10<t<1/5\), and \(t>1/5\), and for the second are \(t<-1/5\), \(-1/5<t<1/10\), and \(t>1/10\). An isometry preserves the positive curvature radii of exposed spherical boundary patches, but these multisets are respectively \(\{2/5,3/10,1/10\}\) and \(\{2/5,3/10,1/5\}\). Hence the hulls are not congruent. In dimension three their common law has an atom of weight \(1/10\) at \(4/5\), constant density \(1\) on \((4/5,9/10)\), and constant density \(1/2\) on \((9/10,5/2)\).

## Verification
The supplied standalone Python checker uses exact rational arithmetic to compare both three-ball support functions at 2001 sample directions, checks strict disjointness and unequal exposed-radius multisets, and algebraically verifies the two-ball inverse on a rational parameter grid. A seeded simulation independently checks the three-dimensional masses of the atom and two density intervals. The infinite-dimensional statements rest on the analytic support-function and pushforward proofs above, not on the finite tests.

Run \(\texttt{python verify.py}\) using a standard Python 3 interpreter; the code uses only the standard library.

## Relationship to prior work
Erdenebaatar and Ninjbat (2021) analyze convex hulls of disk configurations in a finite-packing and circumscribed-polygon problem; their main statements concern minimum area and optimal configurations rather than random-direction widths. Chernov, Drach and Tatarko (2018) establish a reverse isoperimetric characterization of two-congruent-ball sausage bodies, not identifiability of radii and separation from unlabeled width laws. The usual support-function and difference-body identities are classical and are not claimed as new. The contribution here is the sharp **two-versus-three exposed-ball identifiability boundary**, including the explicit disjoint three-ball counterexample and the dimension-free reconstruction formulas.

## Limitations
The theorem assumes all centers lie on a common line and all balls have positive Euclidean radii. The inverse formulas use the exact population law rather than finitely many noisy measurements. The three-ball examples have different radii; this does not assert nonuniqueness for congruent-ball configurations. The example proves nonidentifiability already at three balls, not a classification of every larger fiber. Independent validation and exhaustive historical-priority checking have not been performed.

## References
1. O.-E. Erdenebaatar and U. Ninjbat, *The smallest convex k-gon containing n congruent disks*, arXiv:2102.02568v1, first public February 4, 2021. https://arxiv.org/html/2102.02568v1
2. R. Chernov, K. Drach and K. Tatarko, *A sausage body is a unique solution for a reverse isoperimetric problem*, arXiv:1810.00127, first public September 29, 2018. https://arxiv.org/abs/1810.00127
