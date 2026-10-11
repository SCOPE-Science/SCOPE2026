# Exact intrinsic Euclidean inradius and centers of transportation polytopes
## Finding
Let \(m,n\ge2\), let \(r=(r_1,\ldots,r_m)\) and \(c=(c_1,\ldots,c_n)\) have strictly positive entries, and assume
\[
\sum_{i=1}^{m}r_i=\sum_{j=1}^{n}c_j.
\]
For the transportation polytope
\[
T(r,c)=\left\{X\in\mathbb R^{m\times n}:
X_{ij}\ge0,\ 
\sum_{j=1}^{n}X_{ij}=r_i,\ 
\sum_{i=1}^{m}X_{ij}=c_j
\right\},
\]
equipped with the intrinsic Euclidean metric induced by the Frobenius norm on its affine hull, define
\[
t_*=
\min\left\{
\frac{\min_i r_i}{n},
\frac{\min_j c_j}{m}
\right\}.
\]
Then the exact inradius is
\[
\boxed{
\rho(T(r,c))
=
\sqrt{\frac{mn}{(m-1)(n-1)}}\,t_*.
}
\]

Moreover, the complete set of centers of largest intrinsic balls is
\[
\boxed{
t_*J+
T\!\left(
r-nt_*\mathbf 1_m,\,
c-mt_*\mathbf 1_n
\right),
}
\]
where \(J\) is the all-ones \(m\times n\) matrix and zero residual rows or columns are simply forced to be zero.

Consequently, for the \(d\times d\) Birkhoff polytope \(B_d\),
\[
\rho(B_d)=\frac{1}{d-1},
\]
and its largest intrinsic ball has the unique center \(J/d\).

## Assumptions and scope
The margins are strictly positive. This guarantees that \(T(r,c)\) contains the strictly positive matrix with entries \(r_i c_j/N\), where \(N=\sum_i r_i\), and hence has its usual affine dimension \((m-1)(n-1)\).

All distances are intrinsic to the affine hull, but are measured using the ambient Frobenius inner product. Thus a ball means the intersection of an ordinary Frobenius ball with that affine hull.

The formula concerns the standard complete-support transportation polytope. Transportation polytopes with structural zeroes have a different tangent space and are not included in the claim.

## Proof
Let
\[
\mathcal A=
\left\{
X:
X\mathbf1_n=r,\ 
X^{\mathsf T}\mathbf1_m=c
\right\}
\]
be the affine hull, and let
\[
L=
\left\{
H:
H\mathbf1_n=0,\ 
H^{\mathsf T}\mathbf1_m=0
\right\}
\]
be its translation space.

For the coordinate functional \(X\mapsto X_{ij}\), the orthogonal projection of the ambient normal \(E_{ij}\) onto \(L\) is
\[
Q_{ij}
=
\left(e_i-\frac1m\mathbf1_m\right)
\left(e_j-\frac1n\mathbf1_n\right)^{\mathsf T}.
\]
Indeed, \(Q_{ij}\in L\), and \(E_{ij}-Q_{ij}\) is a sum of a row-potential matrix and a column-potential matrix, hence lies in \(L^\perp\). Its Frobenius norm is independent of \(i,j\):
\[
\|Q_{ij}\|_F^2
=
\left(1-\frac1m\right)
\left(1-\frac1n\right)
=
\frac{(m-1)(n-1)}{mn}.
\]
Write
\[
\kappa=
\sqrt{\frac{(m-1)(n-1)}{mn}}.
\]

For any \(X\in T(r,c)\), the intrinsic distance in \(\mathcal A\) from \(X\) to the restricted coordinate hyperplane \(Y_{ij}=0\) is therefore
\[
\frac{X_{ij}}{\kappa}.
\]
Since
\[
T(r,c)=
\mathcal A\cap\bigcap_{i,j}\{X:X_{ij}\ge0\},
\]
the largest intrinsic ball centered at \(X\) that is contained in the polytope has radius
\[
\frac{\min_{i,j}X_{ij}}{\kappa}.
\]
Thus the inradius problem reduces exactly to maximizing the minimum entry of a feasible transportation matrix.

Suppose \(X_{ij}\ge t\) for every \(i,j\). Each row sum gives
\[
nt\le r_i,
\]
and each column sum gives
\[
mt\le c_j.
\]
Hence every feasible \(t\) satisfies \(t\le t_*\).

Conversely, let \(0\le t\le t_*\) and define residual margins
\[
r'_i=r_i-nt,\qquad c'_j=c_j-mt.
\]
They are nonnegative and have the same total
\[
S=N-mnt.
\]
If \(S=0\), then \(X=tJ\) has the required margins. If \(S>0\), set
\[
Y_{ij}=\frac{r'_i c'_j}{S}.
\]
Then \(Y\ge0\), its row sums are \(r'\), and its column sums are \(c'\). Therefore
\[
X=tJ+Y
\]
belongs to \(T(r,c)\) and satisfies \(X_{ij}\ge t\). Taking \(t=t_*\) proves that the maximum possible minimum entry is exactly \(t_*\), and division by \(\kappa\) gives the displayed inradius formula.

The same argument also identifies every optimal center. A matrix \(X\in T(r,c)\) is a center of a largest intrinsic ball if and only if \(X_{ij}\ge t_*\) for all \(i,j\). This is equivalent to writing
\[
X=t_*J+Y
\]
with
\[
Y\in
T\!\left(
r-nt_*\mathbf1_m,\,
c-mt_*\mathbf1_n
\right),
\]
which proves the center-set formula.

For \(B_d\), all row and column margins equal \(1\), so \(t_*=1/d\), while
\[
\kappa=\frac{d-1}{d}.
\]
Hence
\[
\rho(B_d)=\frac{1/d}{(d-1)/d}=\frac1{d-1}.
\]
All residual margins vanish, so \(J/d\) is the unique center.

## Verification
The accompanying `verify.py` checks the projected-normal norm exactly over a grid of dimensions, verifies the residual-product construction with exact rational arithmetic on a deterministic family of positive margins, and checks the Birkhoff specialization. These computations corroborate the displayed algebra but are not used as an exhaustive proof.

## Relationship to prior work
Blanchard, De Loera, and Louveaux treat transportation polytopes as a central class in their study of monotone paths and polyhedral combinatorics. Their transportation-polytope section concerns graph structure and monotone paths rather than intrinsic metric inradius; the published article lists \(52B12\) first among its MSC classifications.

Bauschke, Singh, and Wang study orthogonal projection onto affine spaces of matrices with prescribed row and column sums, and explicitly place transportation polytopes at the intersection of that affine geometry with entrywise nonnegativity. Their projection formulas support the affine-hull viewpoint used here, but the inspected article does not state the inradius formula or the complete largest-ball center set.

Bouthat, Mashreghi, and Morneau-Guérin study metric geometry of the Birkhoff polytope, including Frobenius/Schatten settings, but their Chebyshev-center problem is the smallest enclosing ball problem: a ball containing the polytope. That is the opposite containment direction from the largest inscribed intrinsic ball computed here.

Searches using the terms “transportation polytope inradius,” “largest inscribed ball,” “Birkhoff polytope inradius,” “Frobenius inradius,” and equivalent center formulations did not locate the displayed arbitrary-margin formula or center-set classification. This search evidence is not a proof that no unindexed source exists.

## Limitations
The result is for complete-support transportation polytopes with strictly positive margins. Structural zeroes change the tangent-space projections of coordinate normals and require additional feasibility conditions, so the displayed formula should not be transferred to sparse transportation polytopes without further work.

The result concerns the Euclidean/Frobenius metric intrinsic to the affine hull. Other matrix norms give different distances to coordinate halfspaces.

The literature comparison is necessarily finite. In particular, older operations-research literature could contain a differently phrased special case, even though the inspected transportation-polytope and Birkhoff-geometry sources do not supply this theorem.

## References
1. Moïse Blanchard, Jesús A. De Loera, and Quentin Louveaux, *On the Length of Monotone Paths in Polyhedra*, arXiv:2001.09575, first public version 2020-01-27; SIAM Journal on Discrete Mathematics 35 (2021), 1746–1768, DOI 10.1137/20M1315646.
2. Heinz H. Bauschke, Shambhavi Singh, and Xianfu Wang, *Projecting onto rectangular matrices with prescribed row and column sums*, arXiv:2105.12222; Fixed Point Theory and Algorithms for Sciences and Engineering 2021, article 23, DOI 10.1186/s13663-021-00708-1.
3. Ludovick Bouthat, Javad Mashreghi, and Frédéric Morneau-Guérin, *On the Geometry of the Birkhoff Polytope II: The Schatten \(p\)-norms*, arXiv:2310.14043; Acta Scientiarum Mathematicarum, DOI 10.1007/s44146-024-00153-7.
