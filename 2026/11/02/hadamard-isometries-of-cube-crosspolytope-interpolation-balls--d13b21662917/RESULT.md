# Hadamard isometries of cube–crosspolytope interpolation balls

## Finding
For an integer \(n\ge2\) and \(s>0\), equip \(\mathbb R^n\) with the norm
\[
N_{n,s}(x)=\max\left\{\|x\|_\infty,\frac{\|x\|_1}{s}\right\}.
\]
Let \(H\) be any real Hadamard matrix of order \(n\), meaning that all entries are \(\pm1\) and \(H^{\mathsf T}H=nI\). The normalized matrix \(U=H/\sqrt n\) is a surjective linear isometry of this real normed space **if and only if**
\[
(n,s)=(2,\sqrt2)\quad\text{or}\quad(n,s)=(4,2).
\]
For every Hadamard order \(n\ge8\) and the only possible parameter \(s=\sqrt n\), it satisfies the quantitative obstruction
\[
\|U\|_{N_{n,\sqrt n}\to N_{n,\sqrt n}}
\ge \frac{3}{2\max\{1,3/\sqrt n\}}
=\begin{cases}\sqrt2,&n=8,\\3/2,&n\ge12.\end{cases}
\]
The dimension-one case is excluded; there, any one-by-one signed matrix is an isometry for all \(s>0\).

## Assumptions and scope
This is a result about **real** Hadamard matrices and the indicated **maximum** of two norms, not quadratic combinations, generic orthogonal operators, or complex Fourier matrices. Existence of a Hadamard matrix is assumed, not asserted for every multiple of four. For \(n>2\), elementary orthogonality implies every existing Hadamard order is divisible by four. The unit ball is exactly
\[
B_{n,s}=[-1,1]^n\cap sB_1^n.
\]
All statements quantify over *every* real Hadamard matrix of the specified order, without choosing a Sylvester form.

## Proof
**1. The parameter is forced by a single coordinate.** Each column of \(U\) has entries of modulus \(1/\sqrt n\). Hence for each standard basis vector \(e_j\),
\[
N_{n,s}(e_j)=\max\{1,1/s\},\qquad
N_{n,s}(Ue_j)=\max\{1/\sqrt n,\sqrt n/s\}.
\]
If \(s<1\), the second quantity is at least \(\sqrt n/s>1/s\), so isometry is impossible. If \(s\ge1\), equality of the two displayed norms with common value one forces \(s=\sqrt n\), since \(1/\sqrt n<1\). Thus no other parameter can work.

**2. The two-dimensional positive case.** Write \(c=\sqrt2-1\). The polygon
\(B_{2,\sqrt2}\) has exactly eight extreme points
\[
(\pm1,\pm c),\qquad(\pm c,\pm1),
\]
with signs independent. This follows directly by intersecting \(|x_1|\le1\), \(|x_2|\le1\), and \(|x_1|+|x_2|\le\sqrt2\). The normalized representative
\[
U_2=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\]
permutes these eight vertices: for example, \(U_2(1,c)=(1,c)\) and \(U_2(c,1)=(1,-c)\), and its action on signs follows by direct substitution. Therefore it preserves their convex hull. Every two-by-two real Hadamard matrix differs from this representative by signed coordinate permutations, which also preserve \(B_{2,\sqrt2}\); hence every such normalized matrix is an isometry.

**3. The four-dimensional positive case.** The vertices of
\(B_{4,2}=[-1,1]^4\cap\{\|x\|_1\le2\}\) are exactly the 24 vectors \(\pm e_i\pm e_j\), \(1\le i<j\le4\), with independent signs. To verify completeness, work in each closed orthant: the polytope is described by \(0\le y_i\le1\) and \(\sum_i y_i\le2\). Its vertices are zero-one vectors with at most two ones, and those with zero or one one cannot be extreme in the **full centrally symmetric intersection** because they lie on a line segment between distinct admissible two-support points. At any two-support point, enough independent cube and sum inequalities are tight to ensure extremality.

For any columns \(h_i,h_j\) of a four-by-four Hadamard matrix, orthogonality gives exactly two equal and two opposite coordinate signs. Thus
\[
U(\pm e_i\pm e_j)=\tfrac12(\pm h_i\pm h_j)
\]
is again a two-support vector with entries of modulus one. Since \(U\) is invertible, it permutes all 24 vertices and therefore preserves the entire unit ball.

**4. All higher Hadamard orders fail.** Choose *any* three distinct columns \(h_i,h_j,h_k\). Set \(p_r=h_{ri}h_{rj}\) and \(q_r=h_{ri}h_{rk}\). Pairwise column orthogonality gives
\(\sum_r p_r=\sum_r q_r=\sum_r p_rq_r=0\), and \(\sum_r1=n\). The four equations uniquely show that each possible pair \((p_r,q_r)\in\{\pm1\}^2\) occurs exactly \(n/4\) times. Consequently, for
\(x=e_i+e_j+e_k\), precisely \(n/4\) entries of \(Ux\) have modulus \(3/\sqrt n\), and precisely \(3n/4\) have modulus \(1/\sqrt n\). Therefore
\[
\|Ux\|_\infty=3/\sqrt n,\qquad\|Ux\|_1=3\sqrt n/2,
\]
so at \(s=\sqrt n\),
\[
N_{n,\sqrt n}(Ux)=\max\{3/\sqrt n,3/2\}=3/2
\quad (n\ge8),
\]
whereas
\[
N_{n,\sqrt n}(x)=\max\{1,3/\sqrt n\}<3/2.
\]
Thus no normalized Hadamard of order at least eight is an isometry. Dividing the two norms proves the quantitative inequality. The Hadamard order condition leaves no further possible dimensions, and the proof is complete.

## Verification
The standalone script `check.py` tests the eight polygon vertices, all 24 four-dimensional vertices, and every triple-support vector for Sylvester Hadamard orders 8, 16, and 32. Those finite tests reproduce the exact multiplicity pattern but are **not** substituted for the arbitrary-order orthogonality argument, nor do they check all Hadamard equivalence classes. The analytic proof above supplies the unrestricted quantifiers.

## Relationship to prior work
Holbrook, Johnston, and Schoch (2022) investigate real Hadamard matrices as extremizers of Hilbert-space Schur multiplier norms. Here the object is different: a normalized Hadamard matrix acts on a Banach space whose unit ball interpolates between a cube and a cross-polytope, and the question is whether the **same** polyhedral ball is preserved. The exceptional four-dimensional unit ball is the familiar regular 24-cell; its Hadamard symmetry is the positive exceptional case. The theorem adds the uniform three-column exclusion of every higher Hadamard order in this particular norm family.

## Limitations
No claim is made about all linear isometries, all orthogonal transformations, a classification of Hadamard existence, complex analogues, or the exact operator norms in higher dimensions. The stated higher-dimensional inequalities are lower bounds, not claimed sharp norms. The isometries in the two exceptional dimensions reflect familiar polygonal and four-polytope symmetries; the proposed new synthesis is their all-order rigidity in this particular Banach interpolation family. Previously unindexed equivalent formulations are a bibliographic risk, and independent assessment of novelty has not been performed.

## References
1. J. Holbrook, N. Johnston and J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863, first posted 6 June 2022 (published in *Linear and Multilinear Algebra*, 2024). https://arxiv.org/abs/2206.02863.
2. T. Etzion, A. Vardy and E. Yaakobi, *Coding for the Lee and Manhattan Metrics With Weighing Matrices*, *IEEE Transactions on Information Theory* **59** (2013), 6712–6723. Related background on Hadamard transforms of cross-polytopes; only the public summary and conclusion were available for comparison.
