# Frobenius radii and contact ranks of every Schur-Horn orbitope
## Finding
Let
\[
a_1\ge a_2\ge\cdots\ge a_d
\]
be real numbers that are not all equal. Put
\[
\bar a=\frac1d\sum_{i=1}^d a_i,\qquad
A_k=\sum_{i=1}^k a_i,\qquad
c_k=\sqrt{\frac{k(d-k)}d}.
\]
The Schur-Horn orbitope is
\[
\mathcal{SH}(a)
=
\{X\in\mathrm S_2\mathbb R^d:\lambda(X)\preceq a\},
\]
viewed inside the affine trace hyperplane
\[
\mathcal H_a=
\left\{
X:\operatorname{tr}X=\sum_{i=1}^d a_i
\right\}
\]
with its intrinsic Frobenius metric.

Its Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}(\mathcal{SH}(a))
=
\min_{1\le k<d}
\frac{A_k-k\bar a}{c_k}
}.
\tag{1}
\]
If the value in (1) is denoted by \(r_*\), then the complete set of incenters is
\[
\boxed{
\left\{
C\in\mathcal H_a:
\sum_{i=1}^k\lambda_i(C)
\le
A_k-r_*c_k
\quad\text{for }1\le k<d
\right\}.
}
\tag{2}
\]
In particular, \(\bar a I\) is always an incenter.

The centered maximal ball at \(\bar a I\) is tangent exactly to the supporting-hyperplane orbits arising from ranks
\[
\boxed{
\mathcal K(a)=
\operatorname*{arg\,min}_{1\le k<d}
\frac{A_k-k\bar a}{c_k}.
}
\tag{3}
\]
Thus (3) gives the complete contact-rank profile of the canonical centered inball.

The circumradius is
\[
\boxed{
R_{\mathrm{out}}(\mathcal{SH}(a))
=
\left(
\sum_{i=1}^d(a_i-\bar a)^2
\right)^{1/2}.
}
\tag{4}
\]
Its circumcenter is uniquely \(\bar a I\), and the points on the minimum enclosing sphere are exactly
\[
\boxed{
\{U\operatorname{diag}(a)U^{\mathsf T}:U\in O(d)\}.
}
\tag{5}
\]

For the standard Schur-Horn orbitope
\[
a=(d-1,d-3,\ldots,-(d-3),-(d-1)),
\]
the formulas reduce to
\[
\boxed{
r_{\mathrm{in}}=\sqrt{d(d-1)},
\qquad
R_{\mathrm{out}}=
\sqrt{\frac{d(d^2-1)}3},
}
\]
and the centered inball touches exactly the rank-\(1\) and rank-\((d-1)\) supporting-hyperplane orbits.

## Assumptions and scope
The eigenvalues \(\lambda_1(X)\ge\cdots\ge\lambda_d(X)\) are ordered decreasingly, and \(\preceq\) denotes ordinary majorization. The metric on \(\mathcal H_a\) is induced by the Frobenius norm
\[
\|X\|_F=\sqrt{\operatorname{tr}(X^2)}.
\]
The tangent space of \(\mathcal H_a\) is the traceless symmetric matrices.

The hypothesis that the coordinates of \(a\) are not all equal guarantees that the orbitope has positive intrinsic dimension. Repeated eigenvalues are allowed. No genericity or simple-spectrum assumption is used.

For a \(k\)-dimensional subspace \(L\), write \(P_L\) for its orthogonal projection. The rank-\(k\) supporting inequalities are
\[
\operatorname{tr}(P_LX)\le A_k.
\]
When eigenvalues repeat, an individual supporting set can have codimension larger than one; the phrase “contact-rank profile” refers to the ranks of supporting-hyperplane normal orbits, not to a claim that every such exposed face is a facet.

## Proof
The Schur-Horn theorem and the standard majorization description give
\[
X\in\mathcal{SH}(a)
\quad\Longleftrightarrow\quad
\operatorname{tr}X=\sum_i a_i
\quad\text{and}\quad
\sum_{i=1}^k\lambda_i(X)\le A_k
\quad(1\le k<d).
\tag{6}
\]
Equivalently, by the Ky Fan variational principle,
\[
\operatorname{tr}(P_LX)\le A_k
\tag{7}
\]
for every \(k\)-dimensional subspace \(L\).

Inside the trace hyperplane, the normal in (7) is not \(P_L\) itself but its orthogonal projection to the traceless tangent space:
\[
N_L=P_L-\frac{k}{d}I.
\]
Since \(P_L^2=P_L\),
\[
\|N_L\|_F^2
=
\operatorname{tr}
\left(
P_L-\frac{2k}{d}P_L+\frac{k^2}{d^2}I
\right)
=
k-\frac{k^2}{d}
=
\frac{k(d-k)}d
=
c_k^2.
\tag{8}
\]
Therefore the intrinsic distance from a point \(C\in\mathcal H_a\) to the supporting hyperplane in (7) is
\[
\frac{A_k-\operatorname{tr}(P_LC)}{c_k}.
\tag{9}
\]

A Frobenius ball of radius \(r\) centered at \(C\) lies in the orbitope if and only if it lies on the correct side of every supporting hyperplane (7). By (8)--(9), this is equivalent to
\[
\operatorname{tr}(P_LC)+rc_k\le A_k
\]
for every \(L\) of dimension \(k\). Maximizing the left side over such \(L\) by the Ky Fan principle yields
\[
\sum_{i=1}^k\lambda_i(C)+rc_k\le A_k
\quad(1\le k<d).
\tag{10}
\]
Hence, for each fixed \(r\), the complete set of centers of radius-\(r\) balls is described by (10).

Average any feasible center over orthogonal conjugation. Convexity of the center set preserves feasibility, while the average is the scalar matrix \(\bar a I\). Thus some largest inscribed ball is centered at \(\bar a I\). Substituting this center into (10) gives
\[
k\bar a+rc_k\le A_k
\]
for every \(k\), proving (1). Substituting the maximal value \(r=r_*\) back into (10) proves the complete incenter description (2).

At the scalar center, equality in the rank-\(k\) inequality occurs exactly when
\[
r_*=
\frac{A_k-k\bar a}{c_k}.
\]
All rank-\(k\) subspaces are conjugate under \(O(d)\), so the centered maximal ball touches precisely the supporting-hyperplane orbits indexed by (3).

For the circumradius, every extreme point of \(\mathcal{SH}(a)\) belongs to the orthogonal orbit
\[
\mathcal O_a=
\{U\operatorname{diag}(a)U^{\mathsf T}:U\in O(d)\},
\]
and every point of the orbitope is a convex combination of points of this orbit. Every orbit point has the same distance from \(\bar a I\):
\[
\left\|
U\operatorname{diag}(a)U^{\mathsf T}-\bar a I
\right\|_F^2
=
\sum_i(a_i-\bar a)^2.
\tag{11}
\]
By convexity of the norm, the ball centered at \(\bar a I\) with radius given by (4) contains the entire orbitope.

The minimum enclosing Euclidean ball of a compact set is unique. Orthogonal conjugation preserves the orbitope and the Frobenius metric, so its unique circumcenter is fixed by every orthogonal conjugation. The only symmetric matrices fixed by all such conjugations are scalar matrices; the trace constraint forces the center to be \(\bar a I\). This proves (4) and uniqueness.

Finally, equality in the convexity estimate for the Euclidean norm is strict for a nontrivial convex combination of two distinct points lying on the same sphere about \(\bar a I\). Consequently the points of the orbitope at distance (4) are exactly the orbit points in (5).

For the standard vector \(a_i=d+1-2i\), one has \(\bar a=0\) and
\[
A_k=k(d-k).
\]
Thus
\[
\frac{A_k}{c_k}
=
\sqrt{dk(d-k)},
\]
whose minimum occurs exactly at \(k=1\) and \(k=d-1\), giving the stated inradius and contact ranks. Also
\[
\sum_{i=1}^d(d+1-2i)^2
=
\frac{d(d^2-1)}3,
\]
giving the stated circumradius.

## Verification
The proof is symbolic and applies in every dimension. The accompanying `verify.py` is only a corroborative exact-arithmetic replay.

It checks, for many sorted integer spectra in dimensions \(2\) through \(8\), the squared distances from the scalar center to every majorization-support orbit and verifies the stated minimizing-rank rule. It also enumerates permutation vertices to verify the centered circumradius and checks the closed formulas for the standard Schur-Horn vector through dimension \(12\).

The checker does not establish novelty and is not used in place of the arbitrary-dimensional proof.

## Relationship to prior work
Sanyal, Sottile, and Sturmfels give the Schur-Horn orbitope as the convex hull of an orthogonal conjugacy orbit and prove its spectrahedral and supporting-subspace descriptions. Their full text gives the rank-\(k\) inequalities used in (6)--(7), but it does not state an inradius or circumradius theorem for Schur-Horn orbitopes.

Sanyal and Saunderson define spectral convex sets \(\Lambda(K)\), identify Schur-Horn orbitopes as \(\Lambda(\Pi(a))\), record the majorization description of the permutahedron, and prove the support-function transfer
\[
h_{\Lambda(K)}(B)=h_K(\lambda(B)).
\]
They also single out the standard Schur-Horn orbitope in their discussion of spectral zonotopes. These results supply structural ingredients but do not give formulas (1)--(5).

Jeong and Gowda develop a broad transfer principle for spectral sets and functions, including topological and convexity operations. Their inspected transfer-principle section does not give the Schur-Horn Frobenius radii, complete incenter set, or contact-rank profile.

Targeted literature searches using Schur-Horn orbitope, Frobenius inradius, circumradius, Chebyshev center, largest inscribed ball, minimum enclosing ball, majorization radius, and the characteristic square-root formulas did not locate a source stating or implying the complete package (1)--(5). A residual risk remains that an equivalent metric statement is hidden in older spectral-set or matrix-nearness literature under different terminology.

## Limitations
The metric statements are for the canonical Frobenius realization in the trace hyperplane. They are not affine invariants of the underlying convex body.

The theorem treats symmetric real matrices. Closely analogous Hermitian statements should follow from the same eigenvalue inequalities, but they are outside the claim.

The originality assessment cannot exclude every unindexed or differently normalized statement in older spectral-set literature. In particular, general matrix-nearness and spectral-function theory may contain distance-transfer results that shorten parts of the proof, although no source located in the searches states the explicit Schur-Horn radius, complete incenter, and contact-rank formulas together or in a form that directly implies all of them without the rank-normal computation above.

## References
1. Raman Sanyal and James Saunderson, *Spectral Polyhedra*, arXiv:2001.04361, first public version 2020-01-13; Forum of Mathematics, Sigma 13 (2025), e30, DOI 10.1017/fms.2024.62.
2. Raman Sanyal, Frank Sottile, and Bernd Sturmfels, *Orbitopes*, arXiv:0911.5436; Mathematika 57 (2011), 275--314, DOI 10.1112/S002557931100132X.
3. Juyoung Jeong and M. Seetharama Gowda, *Spectral sets and functions on Euclidean Jordan algebras*, Linear Algebra and its Applications 518 (2017), 31--56, DOI 10.1016/j.laa.2016.12.020.
