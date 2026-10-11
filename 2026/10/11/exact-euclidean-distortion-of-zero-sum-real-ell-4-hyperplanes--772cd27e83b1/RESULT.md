# Exact Euclidean distortion of zero-sum real \(\ell_4\) hyperplanes

## Finding
For every integer \(n\ge3\), equip the zero-sum hyperplane
\[
H_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\}
\]
with the norm inherited from real \(\ell_4^n\). Its multiplicative Banach--Mazur distance to the Euclidean space of the same dimension is
\[
\boxed{d_{\mathrm{BM}}(H_n,\ell_2^{n-1})^4=
\begin{cases}
\dfrac{n^2-3n+3}{n-1},&n\text{ even},\\[2mm]
\dfrac{(n^2-3n+3)(n+1)}{n^2+3},&n\text{ odd}.
\end{cases}}
\]
In particular, \(H_3\) is linearly isometric to Euclidean two-space up to a constant scale, whereas the distance is strictly larger than one for \(n\ge4\). The distance is asymptotic to \(n^{1/4}\).

Equivalently, the sharp comparison on \(H_n\) between its inherited norms is
\[
m_n\left(\sum_i x_i^2\right)^2\le\sum_i x_i^4\le
M_n\left(\sum_i x_i^2\right)^2,
\qquad x\in H_n,
\]
where
\[
M_n=\frac{n^2-3n+3}{n(n-1)},\qquad
m_n=\begin{cases}
1/n,&n\text{ even},\\[1mm]
(n^2+3)/(n(n^2-1)),&n\text{ odd}.
\end{cases}
\]
The constants on both sides are attained, and no nonorthogonal change of coordinates improves their distortion ratio.

## Assumptions and scope
All scalars are real. The norm on \(H_n\) is \(\|x\|_4=(\sum_i|x_i|^4)^{1/4}\), without probability normalization. The Euclidean comparison space has dimension \(n-1\); its isometry class is independent of chosen coordinates. The multiplicative distance is
\[
d_{\mathrm{BM}}(X,Y)=\inf_{T:X\to Y\ \mathrm{isomorphism}}\|T\|\,\|T^{-1}\|.
\]
Only integer \(n\ge3\) is asserted. Statements about positive-dimensional Euclidean sections, weighted coordinates, complex scalars, or general exponents are not implied.

## Proof
**1. Reduction of all fourth-moment extrema to two levels.** For arbitrary \(z\in\mathbb R^n\), write \(\bar z=n^{-1}\sum_i z_i\) and \(y_i=z_i-\bar z\). For any real \(c\), the polynomial
\[
F_c(z)=\sum_i y_i^4-c\left(\sum_i y_i^2\right)^2
\]
is symmetric and homogeneous of degree four. The half-degree principle for symmetric polynomials, in the form of Riener's Theorem 1.3 [1], says that a symmetric quartic is nonnegative on all of \(\mathbb R^n\) if and only if it is nonnegative at every vector with at most two distinct coordinates. Apply this principle both to \(F_c\) and to \(-F_c\). It follows that the greatest and least possible values of
\[
Q(y)=\frac{\sum_i y_i^4}{(\sum_i y_i^2)^2},\qquad y\in H_n\setminus\{0\},
\]
are exactly those obtained among nonzero zero-sum two-level vectors. This implication is a global polynomial-positivity reduction, not a conclusion from enumerating sample points.

**2. Two-level calculation.** Suppose \(y\) has \(k\) entries equal to \(a\) and the other \(n-k\) entries equal to \(b\), with \(1\le k\le n-1\). The constraints \(ka+(n-k)b=0\) and \(\sum_i y_i^2=1\) give
\[
a^2=\frac{n-k}{nk},\qquad b^2=\frac{k}{n(n-k)}.
\]
Consequently
\[
Q(y)=\frac{(n-k)^2}{n^2k}+\frac{k^2}{n^2(n-k)}
=\frac{n}{k(n-k)}-\frac3n.
\]
Since \(k(n-k)\) is smallest for \(k=1,n-1\) and greatest for \(k\) nearest \(n/2\), the extremal values are precisely \(M_n\) and \(m_n\) in the finding. Normalized vectors with one exceptional coordinate attain \(M_n\); vectors partitioned into the two most nearly equal groups attain \(m_n\). This proves the sharp norm comparison.

**3. Why the ordinary Euclidean comparison is globally optimal.** Let \(K\subset H_n\) be the unit ball for \(\|\cdot\|_4\), and let \(E(Q)=\{x\in H_n:\langle Qx,x\rangle\le1\}\) for a positive definite self-adjoint \(Q\) on the Euclidean inner-product space \(H_n\). Every Banach--Mazur candidate can be rescaled so that
\[
K\subseteq E(Q)\subseteq dK.
\]
The first inclusion is equivalent to the affine inequalities \(\langle Qx,x\rangle\le1\) for all \(x\in K\). Let \(K^\circ\) denote its Euclidean polar inside \(H_n\). The second inclusion is equivalent, by support functions, to
\[
\langle Q^{-1}f,f\rangle\le d^2\quad\text{for all }f\in K^\circ.
\]
For fixed \(d\), the set of positive definite matrices satisfying both families is convex: the first conditions are affine in \(Q\); the second are the positive-semidefinite block conditions
\[
\begin{pmatrix}Q&f\\f^T&d^2\end{pmatrix}\succeq0,
\]
with coordinates taken in any orthonormal basis of \(H_n\). Both families are invariant under coordinate permutations, because \(K\) is. Average any feasible \(Q\) over the symmetric group. The averaged form remains positive definite and feasible and is invariant under every coordinate permutation. An invariant symmetric bilinear form on the zero-sum permutation representation is necessarily \(c\sum_i x_i^2\): indeed, on \(\mathbb R^n\) all diagonal entries of an invariant matrix coincide and all off-diagonal entries coincide; the all-ones form vanishes on \(H_n\).

Thus an optimal ellipsoid can be chosen as a Euclidean ball for the *original* Euclidean norm restricted to \(H_n\). Its best containment ratio is exactly
\[
\frac{\sup_{\|x\|_2=1,x\in H_n}\|x\|_4}{\inf_{\|x\|_2=1,x\in H_n}\|x\|_4}
=\left(\frac{M_n}{m_n}\right)^{1/4}.
\]
Substituting the two parity formulas proves the displayed Banach--Mazur distance. For \(n=3\), the identity \(\sum_i x_i^4=\tfrac12(\sum_i x_i^2)^2\) on \(H_3\) also proves the Euclidean isometry directly. For both parities the explicit formulas show \(d_{\mathrm{BM}}/n^{1/4}\to1\).

## Verification
The standalone `verify.py` checks the rational identities symbolically with SymPy, verifies the parity minimizers by exact rational arithmetic for a finite diagnostic range, and checks numerical sample inequalities. It additionally verifies the \(n=3\) polynomial identity exactly. Invoke `python verify.py` with SymPy installed from the directory containing this file and the script. It prints `VERIFY_OK` if the algebraic checks pass. Neither the finite checks nor numerical sampling replace the half-degree theorem or the convex-averaging proof; those are the steps establishing universal quantification and optimality over all linear isomorphisms.

## Relationship to prior work
Riener's half-degree principle [1], itself developing Timofte's earlier approach, provides the symmetric quartic positivity reduction but does not compute the sharp Banach--Mazur invariant of this codimension-one normed space. The theorem of Grundbacher and Kobos [2] determines Euclidean Banach--Mazur distances for direct \(\ell_p\)-sums of Banach spaces; its hypotheses describe direct sums rather than the coupled zero-sum subspace \(H_n\). Those published statements therefore do not yield the parity-sensitive formula by specializing their parameters. The additional symmetry-averaging argument and the explicit two-level quartic optimization are needed here. Distortion results for two-dimensional special norms do not supply the all-dimension family, even though the \(n=3\) member is a two-dimensional plane.

## Limitations
This is a real, fourth-power, finite-dimensional statement; the method here does not establish the same two-level pattern for higher even powers, or general complex spaces. The formula is an exact mathematical consequence of a published symmetric-quartic positivity theorem and an elementary optimal-ellipsoid argument, not a claim that either of those ingredients was independently discovered here. Bibliographic search cannot exclude every unindexed earlier calculation of the same hyperplane invariant; independent review of novelty and proof has not been carried out. The present result does not classify all extremizing vectors, all optimal ellipsoids, or all optimal isomorphisms.

## References
[1] Cordian Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464 (first version 25 January 2010), Theorem 1.3 and its proof. https://arxiv.org/abs/1001.4464

[2] Florian Grundbacher and Tomasz Kobos, *Exact Banach--Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268 (first version 18 March 2026), Theorem 1.1, Section 2. https://arxiv.org/abs/2603.18268
