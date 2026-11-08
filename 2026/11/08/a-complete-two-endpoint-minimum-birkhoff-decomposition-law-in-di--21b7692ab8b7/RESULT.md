# A complete two-endpoint minimum Birkhoff decomposition law in dimension three

## Finding

Let \(D=(d_{ij})_{i,j=0}^{2}\) be a doubly stochastic \(3\times3\) matrix. For the six permutations, ordered as
\[
(012),(120),(201),(021),(102),(210),
\]
let \(c_i\ge0\) denote their respective convex weights. Set
\[
L=\max\{0,d_{22}-d_{01},d_{11}-d_{02}\},\qquad
U=\min\{d_{00},d_{11},d_{22}\}.
\]
Then \(L\le U\), and **every** Birkhoff--von Neumann representation is uniquely given by the following one-parameter family, after coalescing repeated permutations:
\[
(c_0,c_1,c_2,c_3,c_4,c_5)=
(t,\ d_{01}-d_{22}+t,\ d_{02}-d_{11}+t,\ d_{00}-t,\ d_{22}-t,\ d_{11}-t),
\qquad L\le t\le U.
\]
The least number of distinct positive-weight permutation terms over **arbitrary real weights** is exactly
\[
\boxed{\ k_{\min}(D)=\min\{\#\{i:c_i(L)>0\},\#\{i:c_i(U)>0\}\ }. 
\]
Every optimal representation belongs to the two listed endpoints (or to their single common endpoint when \(L=U\)); in particular, there are at most two distinct minimum-term representations. If \(D\) has entries in \(Q^{-1}\mathbb Z\), for any positive integer \(Q\), then these endpoints also have coefficients in \(Q^{-1}\mathbb Z\). Therefore **restricting weights to the input grid never increases minimum decomposition length in dimension three**. The sharp universal upper bound is five terms. This is a complete exact small-dimensional classification, including boundary and degenerate matrices.

## Assumptions and scope

A permutation \((p_0p_1p_2)\) denotes the \(3\times3\) matrix with a one at \((i,p_i)\). Doubly stochastic means all entries are nonnegative and each row and column sums to one. A *term* is one **distinct** permutation with strictly positive coefficient; zero coefficients do not count. Real-valued inputs are permitted for the endpoint law. The grid comparison assumes every entry is an integer multiple of \(1/Q\); no rounding or approximate equality is involved.

The smallest nontrivial dimension is three: a \(2\times2\) doubly stochastic matrix has only two permutation vertices and a unique coefficient representation. In dimension three six vertices have one nontrivial affine dependence, permitting an actual optimization over representations.

## Proof

**Step 1 (enumerate all coefficients).** The six listed permutation matrices are distinct and exhaust \(S_3\). Their contributions to the entries \((0,0),(1,1),(2,2),(0,1),(0,2)\) are, respectively,
\[
d_{00}=c_0+c_3,\quad d_{11}=c_0+c_5,\quad d_{22}=c_0+c_4,
\quad d_{01}=c_1+c_4,\quad d_{02}=c_2+c_5.
\]
Taking \(t=c_0\) and solving gives precisely the six coefficients displayed in the Finding. The other four matrix entries then agree automatically by the row/column sum identities (e.g. \(d_{12}=d_{00}+d_{01}-d_{22}\)); hence this family describes all possible representations. In particular, the six permutation incidence columns have one-dimensional nullspace with generator \((1,1,1,-1,-1,-1)\), corresponding to the equality between the sums of the even and odd permutation matrices.

**Step 2 (feasible interval and all boundary cases).** Nonnegativity of the first three coefficients yields \(t\ge0\), \(t\ge d_{22}-d_{01}\), \(t\ge d_{11}-d_{02}\); nonnegativity of the last three yields \(t\le d_{00},d_{22},d_{11}\). These are exactly \(L\le t\le U\). The classical Birkhoff--von Neumann theorem guarantees some nonnegative coefficient vector, so the interval is nonempty. The displayed formula also constructs the coefficients directly, without relying on the existence theorem for an algorithm.

**Step 3 (optimal support).** If \(L<U\), every one of the six affine coordinates is strictly positive for \(L<t<U\), since each is a nonconstant affine function of \(t\), nonnegative on the closed interval and can vanish there only at one endpoint. At least one coordinate vanishes at each endpoint because \(L\) is a maximum of the three lower constraints and \(U\) a minimum of the three upper constraints. Thus interior representations use six terms, while endpoint representations use at most five. The optimum is exactly the smaller of the two endpoint support counts; the only candidates are the endpoints. If \(L=U\), the representation is unique and is covered by the same formula. The claim of at most two optimal representations follows as well.

**Step 4 (precision preservation).** If \(Qd_{ij}\) are all integers then \(QL\) and \(QU\) are integers because the endpoints are maxima/minima of input entries and differences. Every coefficient at either endpoint is an integer linear combination of those entries. Thus both optimal candidates remain on the \(1/Q\) grid. Since an arbitrary-real optimum cannot be worse than a grid-restricted optimum, and the real optimum is achieved at a grid endpoint, the minima coincide.

**Step 5 (sharpness).** For \(Q=13\), take
\[
D=\frac1{13}\begin{pmatrix}2&4&7\\5&5&3\\6&4&3\end{pmatrix}.
\]
The endpoints have integer numerator coefficient vectors \((0,1,2,2,3,5)\) and \((2,3,4,0,1,3)\). Each contains exactly five positive terms. All interior points have six; therefore five is attained and is the universal sharp upper bound.

## Verification

Run `python3 verify.py` in the directory containing this document and the included standalone verifier. It uses only Python's standard library and enumerates every integer doubly stochastic \(3\times3\) input with common row sum \(Q\), for each integer \(1\le Q\le12\), by enumerating coefficient compositions, forming distinct input matrices, and independently computing their best grid-support counts. On 13,558 matrix/denominator pairs, the endpoint formula agrees with this independent enumeration; the script also checks exact matrix reconstruction, nonnegativity, and a sharp five-term witness. The run performed 67,790 core assertions. Finite enumeration is a check of the implementation, **not** the reason the universal theorem holds; Steps 1--5 supply the proof for every real input and every integer \(Q\).

## Relationship to prior work

Czégel (2026, arXiv:2610.25837) studies short exact Birkhoff decompositions on fixed input precision and distinguishes precision-specific certificates from bounds for all real weights. Its finite-precision existence argument through bipartite edge coloring and its computational optimizers apply generally, but its stated contributions and conclusions do not give the all-input \(3\times3\) two-endpoint formula, the complete optimizer classification, or the zero precision gap in dimension three. Dufossé, Kaya, Panagiotas, and Uçar (2018) study generalized Birkhoff heuristics and the polytope of decompositions, including the fact that minimum-term decompositions are extreme points; that general observation is used here, but does not alone compute the endpoints or establish the grid property. Classical Birkhoff geometry establishes the six permutation vertices and their affine relation; the present claim specializes that geometry to explicit minimum-cardinality optimization and its integer-grid integrality. The result is deliberately limited to the first nonunique dimension and makes no novelty claim about the standard Birkhoff theorem, the parity relation, or the general extreme-point principle.

## Limitations

This theorem does not address \(n\ge4\), for which the feasible coefficient polytope has many dimensions and an integer-grid optimal solution need not follow from the one-dimensional argument. It does not solve the general NP-hard minimum decomposition problem or prove an input-grid versus real-weight gap in larger dimensions. The calculation is in exact arithmetic; implementing the minimum/maximum tests in floating-point without exact comparisons can alter support at boundary cases. Historical equivalences of this small-dimensional characterization in older polytope or assignment literature cannot be ruled out merely from accessible indexing; independent audit and broader bibliographic review have not been performed.

## References

1. A. Czégel, *Exact minimum Birkhoff decompositions of doubly stochastic matrices with finite precision*, arXiv:2610.25837 (first public October 19, 2026), https://arxiv.org/abs/2610.25837 .
2. F. Dufossé, K. Kaya, I. Panagiotas, and B. Uçar, *Further notes on Birkhoff--von Neumann decomposition of doubly stochastic matrices*, Linear Algebra and its Applications 554 (2018), 68--78, https://doi.org/10.1016/j.laa.2018.05.017 .
3. G. Birkhoff, *Three observations on linear algebra*, Univ. Nac. Tucumán Rev. Ser. A 5 (1946), 147--151.
4. I. Bengtsson, Å. Ericsson, M. Kuś, W. Tadej, and K. Życzkowski, *Birkhoff's polytope and unistochastic matrices, N=3 and N=4*, Commun. Math. Phys. 259 (2005), 307--324, https://arxiv.org/abs/math/0402325 .
