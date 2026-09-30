\
# Local signed-triangle geometry of Gaussian absolute product moments

## Corrected scope

Let \(X\sim N(0,R)\), where \(R=(\rho_{ij})\) is a positive-definite correlation matrix, and let
\(\alpha_1,\ldots,\alpha_n>0\) be fixed.  Define the normalized absolute product moment
\[
M_R(\alpha)
=
\frac{\mathbb E\prod_{i=1}^n |X_i|^{\alpha_i}}
{\prod_{i=1}^n \mathbb E|Z|^{\alpha_i}},
\qquad Z\sim N(0,1).
\]

This corrected record does **not** claim the exact order-2 Rényi total-correlation formula for
Gaussian magnitudes.  That theorem, including its finiteness threshold and its quartic/triangle
weak-correlation expansion, already appears in the earlier SCOPE record
`2026/09/18/gaussian-magnitude-renyi2-total-correlation--4eebefe6d8fe`.

The surviving claim is the following local, sign-sensitive expansion of the Gaussian product
moment itself.

## Theorem

Write \(R=I+E\), so the off-diagonal entries of \(E\) are the correlations \(\rho_{ij}\).
For fixed dimension and fixed positive \(\alpha_i\), as \(\|E\|\to0\),
\[
\boxed{
M_R(\alpha)
=
1
+\frac12\sum_{i<j}\alpha_i\alpha_j\rho_{ij}^2
+\sum_{i<j<k}\alpha_i\alpha_j\alpha_k
 \rho_{ij}\rho_{ik}\rho_{jk}
+O(\|E\|^4).
}
\tag{1}
\]
The quadratic term is sign-blind, whereas the first genuinely three-way term is cubic and
records the signed product around each correlation triangle.

If \(a_*=\min_i\alpha_i>0\), then for \(R\) sufficiently close to \(I\),
\[
\boxed{
M_R(\alpha)-1
\ge
\frac{a_*^2}{8}\,\|R-I\|_F^2.
}
\tag{2}
\]
Thus independence is a strict local minimum with a quantitative quadratic gap.

For comparison, the already-established Rényi-2 total correlation of the magnitude vector has
the different local geometry
\[
D_2(P_R\|Q)
=
\sum_{i<j}\rho_{ij}^4
+
8\sum_{i<j<k}\rho_{ij}^2\rho_{ik}^2\rho_{jk}^2
+
O(\|E\|^8).
\tag{3}
\]
Hence the ordinary positive-exponent product moment detects pair dependence at second order and
signed triangular interaction at third order, while the order-2 magnitude Rényi divergence begins
at fourth order and loses those signs.

## Derivation

Let \(H_m\) be the probabilists' Hermite polynomials and set
\[
h_m(\alpha)=
\frac{\mathbb E[|Z|^\alpha H_m(Z)]}{\mathbb E|Z|^\alpha}.
\]
Parity gives \(h_m(\alpha)=0\) for odd \(m\), and the Gaussian integration identity gives
\[
h_2(\alpha)=\alpha.
\tag{4}
\]

The classical Gaussian product-moment/Hermite expansion can be indexed by loopless multigraphs.
If \(m_{ij}\) is the multiplicity of edge \(\{i,j\}\) and
\(d_i=\sum_{j\ne i}m_{ij}\), then locally around independence
\[
M_R(\alpha)
=
\sum_{(m_{ij})}
\left(\prod_{i<j}\frac{\rho_{ij}^{m_{ij}}}{m_{ij}!}\right)
\left(\prod_i h_{d_i}(\alpha_i)\right).
\tag{5}
\]
Only even vertex degrees survive because the functions \(|x|^{\alpha_i}\) are even.

At total edge degree two, the only surviving graph is a doubled edge.  For \(\{i,j\}\),
its contribution is
\[
\frac{\rho_{ij}^2}{2!}\,h_2(\alpha_i)h_2(\alpha_j)
=
\frac12\alpha_i\alpha_j\rho_{ij}^2.
\]
At total edge degree three, the only nonempty loopless multigraph with all degrees even is a
triangle, giving
\[
\alpha_i\alpha_j\alpha_k\rho_{ij}\rho_{ik}\rho_{jk}.
\]
All remaining surviving graphs have at least four edges, which proves (1) in fixed dimension.

As a sanity check, when all three exponents equal \(2\), Wick's formula gives exactly
\[
\mathbb E[X_1^2X_2^2X_3^2]
=
1+2(\rho_{12}^2+\rho_{13}^2+\rho_{23}^2)
+8\rho_{12}\rho_{13}\rho_{23},
\]
matching (1).

For (2), the quadratic term in (1) is at least
\[
\frac{a_*^2}{2}\sum_{i<j}\rho_{ij}^2
=
\frac{a_*^2}{4}\|R-I\|_F^2.
\]
The cubic and higher terms are \(o(\|R-I\|_F^2)\), so shrinking the neighborhood of \(I\)
absorbs at most half of this leading contribution.

## Relation to prior work

Ouimet and Greaves prove the strong Gaussian product inequality globally for all positive
exponents.  Ogasawara gives general convergent series formulas for multivariate Gaussian absolute
product moments; those general series are prior work and are not claimed here.  The contribution
retained in this corrected record is the explicit low-order graph extraction (1), its local
quadratic gap, and the comparison with the already-known magnitude Rényi-2 expansion (3).

The exact determinant formula, finiteness criterion, bivariate identity, and weak-correlation
expansion for order-2 Rényi total correlation were already recorded by SCOPE on 18 September 2026
and are therefore removed from this record's originality claim.

## Limitations

The expansion is fixed-dimensional and local near independence.  No dimension-uniform remainder
is claimed.  The general absolute-product-moment series itself is prior art.  The retained
contribution is an explicit local coefficient extraction and comparison, not a new proof of the
global Gaussian product inequality.
