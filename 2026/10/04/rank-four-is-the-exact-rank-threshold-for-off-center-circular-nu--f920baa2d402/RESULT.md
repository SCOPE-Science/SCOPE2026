# Rank four is the exact rank threshold for off-center circular numerical ranges
## Finding
Let \(r\) be a positive integer. A finite-dimensional real partial isometry of rank \(r\) can have a nondegenerate circular numerical range with nonzero center if and only if \(r\ge 4\).

A quantitative construction is available. O’Loughlin and Virtanen proved that there are \(\varepsilon>0\) and real rank-four partial isometries \(V_a\in M_6(\mathbb R)\), for \(0<a<\varepsilon\), such that
\[
W(V_a)=D(a,3/4)=\{z\in\mathbb C:|z-a|\le 3/4\}.
\]
Put
\[
\varepsilon_0=\min\{\varepsilon,3/4-\sqrt{2}/2\}>0.
\]
Then for every integer \(r\ge4\), every \(0<a<\varepsilon_0\), and every integer
\[
n\ge 6+\left\lceil\frac{3(r-4)}{2}\right\rceil,
\]
there is a real rank-\(r\) partial isometry \(A_{r,n}(a)\in M_n(\mathbb R)\) with
\[
W(A_{r,n}(a))=D(a,3/4).
\]

## Assumptions and scope
For a complex matrix \(A\), its numerical range is
\[
W(A)=\{\langle Ax,x\rangle:\|x\|_2=1\}.
\]
A matrix is a partial isometry when \(A^*A\) is an orthogonal projection. Real matrices are viewed as complex matrices when their numerical ranges are taken.

Let \(J_m\) denote the \(m\times m\) nilpotent Jordan shift with ones on the first superdiagonal. Then \(J_m\) is a partial isometry of rank \(m-1\), and the classical Jordan-block numerical-range formula gives
\[
W(J_m)=D\!\left(0,\cos\frac{\pi}{m+1}\right).
\]
Only \(J_2\) and \(J_3\) are needed below.

The statement classifies which ranks can occur at all. The displayed dimension bound is a sufficient constructive bound; no claim is made that it is the minimum possible dimension for a given rank.

## Proof
The obstruction for ranks at most three is known: Popov, Shen and Spitkovsky proved the Gau–Wang–Wu assertion for partial isometries of rank at most three in arbitrary finite dimension. Hence a nonzero-centered circular numerical range is impossible when \(r\le3\).

For the converse, fix \(r\ge4\) and write
\[
r-4=2s+t,\qquad s\ge0,\qquad t\in\{0,1\}.
\]
For \(0<a<\varepsilon_0\), define the unpadded block matrix
\[
B_r(a)=V_a\oplus J_3^{\oplus s}\oplus J_2^{\oplus t}.
\]
A direct sum of partial isometries is a partial isometry. Its rank is
\[
4+2s+t=r,
\]
and its dimension is
\[
6+3s+2t=6+\left\lceil\frac{3(r-4)}{2}\right\rceil.
\]

The Jordan-block formula gives
\[
W(J_3)=D(0,\sqrt{2}/2),\qquad W(J_2)=D(0,1/2).
\]
Because \(a<3/4-\sqrt{2}/2\), every point \(z\) of \(W(J_3)\) satisfies
\[
|z-a|\le |z|+a<\sqrt{2}/2+3/4-\sqrt{2}/2=3/4.
\]
Thus \(W(J_3)\subset D(a,3/4)\), and the same inclusion holds for \(W(J_2)\). The numerical range of a finite direct sum satisfies
\[
W(A_1\oplus\cdots\oplus A_m)
=\operatorname{conv}\!\left(\bigcup_{j=1}^m W(A_j)\right).
\]
Since one summand already has numerical range exactly \(D(a,3/4)\) and every other summand range is contained in that convex disc,
\[
W(B_r(a))=D(a,3/4).
\]

If a larger ambient dimension \(n\) is desired, append a zero block. Because \(0\in D(a,3/4)\) for \(0<a<\varepsilon_0<3/4\), padding does not change the numerical range. Hence
\[
A_{r,n}(a)=B_r(a)\oplus 0_{n-6-\lceil3(r-4)/2\rceil}
\]
has the asserted rank and numerical range for every allowed \(n\).

Combining this construction with the rank-at-most-three obstruction proves the exact rank threshold.

## Verification
The proof uses only three ingredients beyond the focal existence theorem: the explicit ranks of \(J_2\) and \(J_3\), the standard formula \(W(J_m)=D(0,\cos(\pi/(m+1)))\), and the direct-sum identity for numerical ranges. The containment is strict for the chosen open parameter interval, so no boundary coincidence is required.

For parity, if \(r-4=2s\), the construction adds \(s\) copies of \(J_3\); if \(r-4=2s+1\), it adds \(s\) copies of \(J_3\) and one copy of \(J_2\). These give exactly the stated rank and dimension in both cases.

## Relationship to prior work
O’Loughlin and Virtanen constructed the first counterexamples, all of rank four, and propagated them to every ambient dimension at least six by adjoining zero blocks. Their paper identifies rank four in dimension six as the first case not covered by earlier positive results. It does not state a construction at every higher rank.

Popov, Shen and Spitkovsky proved that the Gau–Wang–Wu assertion remains true for ranks at most three in arbitrary dimension. Together with the construction above, that result turns the rank question into a complete dichotomy: ranks \(1,2,3\) are impossible, while every rank at least \(4\) occurs.

The Jordan-block numerical-range formula is classical and is used only as a centered-disc padding device; the new point is the rank-complete propagation of the 2026 rank-four counterexample.

## Limitations
The construction gives a sufficient ambient-dimension threshold \(6+\lceil3(r-4)/2\rceil\), not an optimal one. It also preserves the specific radius \(3/4\) and sufficiently small positive centers inherited from the focal family; it does not classify all possible radii, centers, or minimum dimensions at each rank.

## References
1. R. O’Loughlin and J. Virtanen, *A Counterexample to the Gau--Wang--Wu Conjecture on Partial Isometries*, arXiv:2608.12579v1, 2026.
2. N. Popov, E. Shen and I. M. Spitkovsky, *On Kippenhahn Curves of Low Rank Partial Isometries*, Integral Equations and Operator Theory 98 (2026), Article 32, DOI 10.1007/s00020-026-02846-w.
3. P. Y. Wu, *A numerical range characterization of Jordan blocks*, Linear and Multilinear Algebra 43 (1998), 351–361, DOI 10.1080/03081089808818536.
