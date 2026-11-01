# Three random-point distance moments reconstruct parallelograms and recover their area

## Finding
Let \(K\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram. If \(X,Y\) are independent, uniform-by-area points of \(K\), let \(m_{2j}=\mathbb E\|X-Y\|^{2j}\), for \(j=1,2,3\), and let \(T=\operatorname{Area}(K)^2\). Then the exact, dimensionally homogeneous identity
\[
\boxed{T=\frac{105}{41m_2}\left(m_6-\frac{75}{7}m_2m_4+18m_2^3\right)}
\]
holds. The three numbers \((m_2,m_4,m_6)\) determine \(K\) uniquely up to Euclidean congruence. This is a sharp three-moment threshold: \((m_2,m_4)\) determine a square uniquely, but for **every nonsquare parallelogram** there is a continuous family of pairwise noncongruent parallelograms sharing those first two distance moments.

There is an exact attainable-moment classification. Normalize the sum of the squared edge lengths to one, equivalently \(m_2=1/6\). In the \((m_4,m_6)\)-plane the realizable region is the closed triangle with vertices
\[
V_0=(1/15,1/28),\qquad V_{\square}=(17/360,29/1680),\qquad V_{\mathrm{flat}}=(3/40,17/336),
\]
with the **entire side** \(V_0V_{\mathrm{flat}}\) removed and both endpoints \(V_0,V_{\mathrm{flat}}\) removed. Both other sides, except their excluded endpoints, are included; the vertex \(V_{\square}\) is included. The sides \(V_0V_{\square}\) and \(V_{\square}V_{\mathrm{flat}}\) correspond respectively to rectangles and equal-edge rhombi.

On the normalized class the inverse from \((m_4,m_6)\) to a canonical edge Gram matrix is uniformly Hölder continuous with exponent \(1/2\), and no larger exponent works uniformly near the square. In particular, the third distance moment measures squared area *strictly monotonically* at fixed \((m_2,m_4)\).

## Assumptions and scope
Write \(K=x_0+\{sa+tb:0\le s,t\le1\}\) with linearly independent edge vectors \(a,b\in\mathbb R^2\). Set \(A=\|a\|^2>0\), \(B=\|b\|^2>0\), \(C=\langle a,b\rangle\), \(S=A+B\), \(Q=AB\), and \(T=AB-C^2>0\). After swapping and reversing the two unoriented generators, the congruence class is encoded by
\[
G(K)=\begin{pmatrix}A&|C|\\|C|&B\end{pmatrix},\quad A\ge B>0,\quad 0\le |C|<\sqrt{AB}.
\]
Here \(\operatorname{Area}(K)=\sqrt T\). Distances are Euclidean between independent volume-uniform points, *not* line-selected chords, boundary-selected points, or intrinsic distances. The moment region statement is restricted to \(S=1\). The stability norm is Frobenius matrix norm.

## Proof
Let \(U,V\) be independent differences of two independent uniform random variables on \([0,1]\). Each has triangular density \(1-|t|\) on \([-1,1]\), vanishing odd moments and even moments
\[
\mathbb E U^{2k}=\frac{2}{(2k+1)(2k+2)}\quad (k\ge0).
\]
The random vector \(X-Y\) has the same law as \(Ua+Vb\), so its squared length is \(Z=AU^2+BV^2+2CUV\). Direct multinomial expansion, using \(\mathbb EU^2=1/6\), \(\mathbb EU^4=1/15\), and \(\mathbb EU^6=1/28\), gives the **exact** identities
\[
\begin{aligned}
m_2&=\frac S6,\\
m_4&=\frac{S^2}{15}-\frac{7Q}{90}+\frac{C^2}{9}
     =\frac{S^2}{15}+\frac Q{30}-\frac T9,\\
m_6&=\frac{S^3}{28}-\frac{31SQ}{420}+\frac{2SC^2}{15}
     =\frac{S^3}{28}+\frac{5SQ}{84}-\frac{2ST}{15}.
\end{aligned}
\]
From the fourth-moment identity, \(Q=30(m_4-S^2/15+T/9)\). Substitution in the sixth-moment identity gives
\[
m_6=\frac{25}{14}S m_4-\frac{S^3}{12}+\frac{41}{630}S T
=\frac{75}{7}m_2m_4-18m_2^3+\frac{41}{105}m_2T.
\]
This proves the area formula. It also yields an explicit inverse: first set \(S=6m_2\), compute \(T\) by the boxed formula, then
\[
Q=30m_4-2S^2+\frac{10}{3}T,\qquad C^2=Q-T,
\]
and finally recover \(\{A,B\}=\{(S\pm\sqrt{S^2-4Q})/2\}\), \(|C|=\sqrt{C^2}\). The allowable data have \(Q>0\), \(Q\le S^2/4\), and \(0\le C^2<Q\). Thus the recovered Gram matrix is the unique congruence-class representative, including rectangles and rhombi.

When \(S=1\), the parameters \((Q,C^2)\) range exactly over the planar triangle \(0<Q\le1/4\), \(0\le C^2<Q\); every such pair is realizable by independent vectors having the displayed Gram matrix. The displayed formulas for \((m_4,m_6)\) form an invertible affine map: its determinant is \(-41/18900\). Applying it to the closure's three vertices \((Q,C^2)=(0,0),(1/4,0),(1/4,1/4)\) yields precisely \(V_0,V_{\square},V_{\mathrm{flat}}\). The strict and nonstrict face conditions transfer exactly, proving the stated moment-region classification.

At fixed \(S\), the two-moment constraint is the line
\[
C^2=9\left(m_4-\frac{S^2}{15}\right)+\frac7{10}Q.
\]
Its direction vector \((\Delta Q,\Delta C^2)=(1,7/10)\) is transverse to all three triangle edges. A section of the admissible triangular domain by such a line is a nontrivial segment except at its unique minimizing vertex \((Q,C^2)=(S^2/4,0)\), which represents a square. For every other admissible point, a sufficiently small movement along the line preserves \(Q>0\), \(Q\le S^2/4\), \(0\le C^2<Q\), and gives noncongruent shapes. Thus two moments are insufficient at every nonsquare, but uniquely characterize squares, also seen directly from the sharp inequality \(m_4\ge17S^2/360\) with square-only equality.

For stability with \(S=1\), let \(\delta=\max\{|m_4-m_4'|,|m_6-m_6'|\}\). The inverse affine identities give
\[
|Q-Q'|\le\frac{4620}{41}\delta,\qquad |C^2-C'^2|\le\frac{3603}{41}\delta.
\]
Since \(|\sqrt u-\sqrt v|^2\le|u-v|\) for nonnegative \(u,v\), the canonical Gram matrices obey the uniform inequality
\[
\boxed{\|G(K)-G(K')\|_{\mathrm F}\le\sqrt{\frac{16446}{41}}\,\delta^{1/2}.}
\]
To prove optimality of the exponent, compare the square Gram matrix \(G_0=\left(\begin{smallmatrix}1/2&0\\0&1/2\end{smallmatrix}\right)\) with \(G_t=\left(\begin{smallmatrix}1/2&t\\t&1/2\end{smallmatrix}\right)\), for \(0<t<1/2\). Their normalized distance moments differ by exactly \(t^2/9\) and \(2t^2/15\), while their Frobenius Gram distance is \(\sqrt2\,t\). Therefore every uniform inverse Hölder exponent greater than \(1/2\) fails near the square. All statements follow.

## Verification
The standalone program `verify.py` uses only the Python standard library and independently expands symbolic even moments using rational arithmetic. It checks the area identity, the exact image vertices and affine determinant, explicit distinct two-moment examples, inversion on a rational sample of legitimate Gram matrices, and the sharp square-root perturbation. A seeded direct point-pair simulation for several nonorthogonal parallelograms separately checks the moment formulas within stated tolerances. Run `python3 verify.py`; the expected concluding marker is `ALL_CHECKS_PASSED`. The proof, not the finite tests, establishes the general theorem.

## Relationship to prior work
Pure, Durrani, Tong and Pan (arXiv:1903.07757, first posted March 18, 2019) derive a general distance-density framework for arbitrary pairs of polygonal regions. Their Theorem 3 and examples address **forward** distance distributions, not the sharp finite-moment inverse geometry of parallelograms, the moment-image triangle, or the area identity. Sheng (1985) explicitly derives all integer distance moments for parallelograms; the forward moment formulas themselves are **prior work**, not claimed as new here. The new statement uses their general type of observable but resolves a separate finite-data determination and exact attainable-data problem.

The publicly indexed *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* instead uses the mean, second moment and endpoint of **random projection width**, which is not the random interior-pair distance. The indexed *Fourth-chord moment amplification and angular phase transition for parallelograms* compares **area-uniform and boundary-uniform fourth moments**, not sixth-moment area reconstruction or the complete two-dimensional moment image. These are substantive comparisons of observables and implications, not novelty inferred from wording. The more general published moment formula of Sheng makes a historical equivalent formulation a genuine residual risk because its full text was unavailable for comparison.

## Limitations
The theorem concerns exact population moments and independent interior-uniform sampling from genuine planar parallelograms. It is not a finite-sample statistical guarantee. The Gram-matrix stability estimate is normalized by \(S=1\); it does not claim analogous uniform stability for unnormalized, arbitrarily large or degenerate bodies. The moment-data triangle is **only** an exact characterization within the parallelogram model, not a characterization among all convex bodies. Prior forward moment formulas and elementary probability identities are not new. No independent mathematical audit has been performed; historical priority is provisional, especially for inaccessible older material.

## References
1. R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757v1, first posted 2019-03-18, https://arxiv.org/abs/1903.07757. Full public HTML: https://ar5iv.labs.arxiv.org/html/1903.07757. Theorem 3, Sections III–VI.
2. T. K. Sheng, *The Distance between Two Random Points in Plane Regions*, *Advances in Applied Probability* 17 (1985), 748–773, DOI:10.2307/1427086. Abstract establishes explicit integer distance moments for parallelograms; full text not inspected.
3. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, public mathematical finding, 2026, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928/RESULT.md.
4. *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical finding, 2026, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e/RESULT.md.
