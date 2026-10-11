# A tetrahedral dimension jump for the inscribed-quadrilateral constant of real \(\ell_4\)
## Finding
For every real \(X=\ell_4(I)\) with \(|I|\ge3\),
\[
J_{\mathrm{in}}(X)=8\sqrt6,
\]
where
\[
J_{\mathrm{in}}(X)=\sup\left\{\sum_{1\le i<j\le4}\|x_i-x_j\|^2:x_i\in S_X,\ \sum_{i=1}^4x_i=0\right\}.
\]
The value is attained by the centered tetrahedral four-tuple
\[
3^{-1/4}(1,1,1),\quad 3^{-1/4}(1,-1,-1),\quad 3^{-1/4}(-1,1,-1),\quad 3^{-1/4}(-1,-1,1).
\]
Thus
\[
J_{\mathrm{in}}(\ell_4(I))=8\sqrt6>8(1+\sqrt2)=J_{\mathrm{in}}(\ell_4^2),
\]
so there is a strict dimension jump between two and three available coordinates.

## Assumptions and scope
All scalars are real. The result applies to finite- and infinite-dimensional \(\ell_4(I)\) whenever at least three coordinates are available. The upper bound is coordinatewise; the extremizer is supported on exactly three coordinates.

## Proof
Let \(x_1,x_2,x_3,x_4\in S_{\ell_4(I)}\) and assume
\[
x_1+x_2+x_3+x_4=0.
\]
Set
\[
S=\sum_{1\le i<j\le4}\|x_i-x_j\|_4^2.
\]
Cauchy--Schwarz over the six unordered pairs gives
\[
S^2\le6\sum_{i<j}\|x_i-x_j\|_4^4.
\tag{1}
\]
For one coordinate put \(a_i=x_i(k)\). Since \(\sum_i a_i=0\), direct expansion gives
\[
\sum_{i<j}(a_i-a_j)^4=4\sum_i a_i^4+3\left(\sum_i a_i^2\right)^2.
\tag{2}
\]
Summing (2) over coordinates and using \(\|x_i\|_4=1\),
\[
\sum_{i<j}\|x_i-x_j\|_4^4=16+3T,
\]
where
\[
T=\sum_k\left(\sum_i x_i(k)^2\right)^2
=4+2\sum_{i<j}\sum_kx_i(k)^2x_j(k)^2.
\]
For every pair \(i<j\), coordinatewise Cauchy--Schwarz gives
\[
\sum_kx_i(k)^2x_j(k)^2\le
\left(\sum_kx_i(k)^4\right)^{1/2}
\left(\sum_kx_j(k)^4\right)^{1/2}=1.
\]
Hence \(T\le16\), so
\[
\sum_{i<j}\|x_i-x_j\|_4^4\le64.
\]
Together with (1),
\[
S\le\sqrt{6\cdot64}=8\sqrt6.
\tag{3}
\]
For sharpness, put \(a=3^{-1/4}\) and use
\[
x_1=a(1,1,1),\quad x_2=a(1,-1,-1),\quad x_3=a(-1,1,-1),\quad x_4=a(-1,-1,1).
\]
Each vector has unit \(\ell_4\)-norm and their sum is zero. Every pair differs in exactly two coordinates by magnitude \(2a\), so
\[
\|x_i-x_j\|_4^4=2(2a)^4=\frac{32}{3},
\qquad
\|x_i-x_j\|_4^2=4\sqrt{\frac23}.
\]
All six pairwise squared distances therefore sum to
\[
24\sqrt{\frac23}=8\sqrt6,
\]
which meets (3). Finally, \(\sqrt6>1+\sqrt2\) because this reduces successively to \(3>2\sqrt2\) and \(9>8\), proving the strict comparison with the known planar value.

## Verification
The bundled `verify.py` symbolically verifies identity (2), the tetrahedral unit norms and zero sum, the common pairwise fourth-power distance \(32/3\), the objective \(8\sqrt6\), and the strict comparison with \(8(1+\sqrt2)\).

These computations are reproducibility checks only. The infinite-dimensional statement follows from the analytic inequalities above and does not rely on finite enumeration.

## Relationship to prior work
Ahmad, Liu and Li introduced \(J_{\mathrm{in}}\) in 2021, proved
\[
16\le J_{\mathrm{in}}(X)\le24,
\]
and gave Hilbert-space rigidity and selected two-dimensional examples. The inspected defining article contains no \(\ell_4\) evaluation.

A later published research record proves for real strictly convex normed planes that
\[
J_{\mathrm{in}}(X)=8+8C'_{\mathrm{NJ}}(X),
\]
which yields
\[
J_{\mathrm{in}}(\ell_4^2)=8(1+\sqrt2).
\]
That result is intrinsically two-dimensional and does not imply the three-coordinate tetrahedral value. The strict inequality between the two exact values rules out a dimension-free reduction to the planar formula for \(\ell_4\).

Searches under the exact invariant, \(\ell_4\), dimension-three and tetrahedral aliases, and the candidate value \(8\sqrt6\) located no public statement covering the theorem above.

## Limitations
The theorem is specific to exponent \(4\). It does not determine \(J_{\mathrm{in}}(\ell_p(I))\) for general \(p\), and it does not classify all extremizing four-tuples. Bibliographic and semantic searches cannot prove absolute novelty; an equivalent result could appear under different centered-four-point or simplex terminology.

## References
1. A. Ahmad, Q. Liu and Y. Li, “Geometric Constants in Banach Spaces Related to the Inscribed Quadrilateral of Unit Balls,” *Symmetry* 13 (2021), 1294, doi:10.3390/sym13071294. Published 19 July 2021. MSC 46B20.
2. “Inscribed-quadrilateral collapse in strictly convex normed planes,” published research record, 2026, identifier `2026/10/4/SCOPE-inscribed-quadrilateral-collapse-in-strictly-convex-normed-plane--269b2accf6dc`.
