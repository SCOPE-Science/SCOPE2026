# Face-rank orbit stratification for cube and cross-polytope norms

## Finding

For an integer \(n\ge 2\) and \(\mathbb F\in\{\mathbb R,\mathbb C\}\), consider either \(X=\ell_1^n(\mathbb F)\) or \(X=\ell_\infty^n(\mathbb F)\). For \(x\in S_X\), define the sphere orbit under invertible linear contractions by
\[
\mathcal O_X(x)=\{Tx:T\in\operatorname{GL}_n(\mathbb F),\ \|T\|_{X\to X}\le 1\}\cap S_X.
\]
Let \(d_X(x)\) be the *real affine dimension* of the smallest face of the convex unit ball containing \(x\). Then for all \(x,y\in S_X\),
\[
\boxed{\ y\in\mathcal O_X(x)\iff d_X(x)\le d_X(y).\ }
\]
The explicit equivalent criteria, valid over both fields, are:

* For \(\ell_1^n\): writing \(s(x)=|\{j:x_j\ne0\}|\), reachability is exactly \(s(x)\le s(y)\).
* For \(\ell_\infty^n\): writing \(r(x)=|\{j:|x_j|=1\}|\), reachability is exactly \(r(y)\le r(x)\).

Every \(\mathcal O_X(x)\) is relatively open and dense in \(S_X\). The mutual-reachability equivalence relation has exactly \(n\) classes, ordered as a chain. Thus every sphere point is a *pilgrim point* (has dense contraction orbit), but the semigroup is not transitive when \(n\ge2\).

## Assumptions and scope

All operators are bounded linear maps over the given field; finite dimensionality makes every linear map bounded. A contraction means operator norm at most one, with no assumption that the inverse is contractive. An automorphism means an invertible linear map. The orbit is on the unit sphere, so contractions carrying \(x\) strictly into the open unit ball do not enter the stated relation.

For \(\ell_1^n\), over either field, \(d_X(x)=s(x)-1\): the minimal face is a real simplex with the coordinate phases fixed. For \(\ell_\infty^n\), the minimal face is the product of disks at inactive coordinates, so \(d_X(x)=\delta_\mathbb F(n-r(x))\), where \(\delta_\mathbb R=1\) and \(\delta_\mathbb C=2\). The complex balls need not be polytopes, but their minimal convex faces are well defined.

## Proof

**The cross-polytope, necessity.** Fix \(x,y\in S_{\ell_1^n}\), put \(a_i=|x_i|\), and suppose \(Tx=y\) with \(T\) invertible and \(\|T\|\le1\). Then
\[
1=\|y\|_1=\left\|\sum_{i:x_i\ne0} x_iTe_i\right\|_1
\le\sum_{i:x_i\ne0}|x_i|\,\|Te_i\|_1\le\sum_i|x_i|=1.
\]
Every inequality is equality. At each coordinate \(j\) for which \(y_j=0\), equality in the coordinatewise triangle inequality forces \((Te_i)_j=0\) for every \(i\) with \(x_i\ne0\). Therefore the \(s(x)\) active columns of the invertible matrix \(T\) lie in the coordinate subspace supported on \(\operatorname{supp}(y)\), of dimension \(s(y)\). Thus \(s(x)\le s(y)\).

**The cross-polytope, sufficiency.** Apply coordinate permutations and unit-modulus diagonal isometries to reduce to \(x=(a_1,\ldots,a_s,0,\ldots,0)\) and \(y=(b_1,\ldots,b_t,0,\ldots,0)\), where \(a_i,b_j>0\), the positive entries on each side sum to one, and \(s\le t\). If \(s=1\), take the sole active matrix column to be \(y\). Otherwise choose linearly independent zero-sum vectors \(h_1,\ldots,h_{s-1}\) supported on the first \(t\) coordinates and set
\[
h_s=-\frac{1}{a_s}\sum_{i=1}^{s-1}a_i h_i.
\]
For all sufficiently small \(\varepsilon>0\), the columns \(v_i=y+\varepsilon h_i\) are nonnegative, supported on the first \(t\) coordinates, and have \(\ell_1\)-norm one; their weighted mean is
\[
\sum_{i=1}^s a_i v_i=y.
\]
These \(s\) columns are linearly independent. Indeed, if \(\sum_i c_iv_i=0\), summing coordinates gives \(\sum_i c_i=0\), while the independence of the first \(s-1\) vectors \(h_i\) implies \(c_i=(a_i/a_s)c_s\) for \(i<s\); hence all \(c_i=0\). Extend these columns to a basis by adding \(n-s\) standard coordinate vectors. Every column remains nonnegative with norm one, so the resulting invertible column-stochastic matrix \(T\) has \(\|T\|_{1\to1}=1\) and sends \(x\) to \(y\). Undo the coordinate isometries.

**The cube, necessity.** Write \(A\) for the matrix of an invertible contraction on \(\ell_\infty^n\) satisfying \(Ax=y\). Every row has \(\ell_1\)-norm at most one. If \(|y_j|=1\), then
\[
1=\left|\sum_i A_{ji}x_i\right|\le\sum_i|A_{ji}|\,|x_i|\le\sum_i|A_{ji}|\le1.
\]
Thus row \(j\) vanishes at every column \(i\) where \(|x_i|<1\). The \(r(y)\) rows corresponding to active coordinates of \(y\) are linearly independent because \(A\) is invertible, yet all lie in the coordinate subspace of dimension \(r(x)\). Hence \(r(y)\le r(x)\).

**The cube, sufficiency.** Suppose \(t=r(y)\le r(x)\). Reorder coordinates so that the first \(t\) entries of \(x\) and of \(y\) have modulus one, and \(|y_j|<1\) when \(j>t\). For \(j\le t\), take matrix row \(j\) to be \(y_j\overline{x_j}e_j^{\mathsf T}\). For \(j>t\), fix one active input index, say \(1\), and choose row
\[
R_j=y_j\overline{x_1}e_1^{\mathsf T}
+\varepsilon(e_j^{\mathsf T}-x_j\overline{x_1}e_1^{\mathsf T}).
\]
Its value on \(x\) is \(y_j\), and its \(\ell_1\)-norm is at most \(|y_j|+\varepsilon(1+|x_j|)\le1\) for all sufficiently small *common* \(\varepsilon>0\). The resulting matrix is block lower triangular with nonzero leading diagonal and a trailing diagonal block \(\varepsilon I\), hence invertible. It has \(\|A\|_{\infty\to\infty}=1\) and \(Ax=y\).

**Orbits and the face-rank chain.** The two criteria become \(d_X(x)\le d_X(y)\) by the displayed face-dimension formulas. The set of vectors with at least \(s\) nonzero coordinates in \(S_{\ell_1^n}\) is relatively open and dense. The set of vectors with at most \(r\) coordinates of modulus one in \(S_{\ell_\infty^n}\) is also relatively open and dense: a small perturbation cannot create a new modulus-one coordinate, and every sphere vector can be approximated by vectors with exactly one such coordinate. Therefore all orbits are relatively open and dense. Mutual reachability is equality of the corresponding integer face rank, giving exactly \(n\) classes. A rank increase is possible, whereas a decrease is forbidden, so the classes form a chain.

## Verification

The analytic proof covers every finite dimension \(n\ge2\), both fields, and all boundary support patterns. The accompanying `check_orbits.py` uses exact rational arithmetic to verify 119 positive \(\ell_1\) construction instances and 119 \(\ell_\infty\) construction instances across dimensions \(2\) through \(8\), including invertibility, operator norms and the prescribed image. These finite checks test the constructions but do not certify the quantified theorem; the proof above is independent of them.

## Relationship to prior work

Cabello Sánchez and Cabello Sánchez (2022), arXiv:2209.04652v1, introduce the semigroup dynamics and explicitly describe the two strata of contraction orbits on real \(\ell_1^2\). They also show that polyhedral spaces have a dense set of pilgrim points. The theorem here gives the exact reachability relation in *every finite dimension* and over both scalar fields, for both the cross-polytope and cube coordinate norms; it strengthens dense availability of pilgrim points to *every* sphere point for these two families. It does not imply such a face-rank criterion for arbitrary polyhedral spaces.

Related qualitative work by Becerra Guerrero and Rodríguez Palacios (2019) concerns near-transitivity properties rather than this explicit face-rank orbit preorder. Work on isometric envelopes by Ferenczi and Lopez-Abad (2024) studies a different stabilizer/envelope construction.

## Limitations

The theorem concerns only finite-dimensional coordinate \(\ell_1\) and \(\ell_\infty\) spaces, not arbitrary polyhedral norms, general \(\ell_p\) norms, or infinite-dimensional sequence spaces. It does not bound the norm of the inverse of a realizing contraction, which can become large near lower-rank strata. No claim is made about previously unindexed results giving the same classification.

## References

1. F. Cabello Sánchez and J. Cabello Sánchez, *Dynamics of the semigroup of contractive automorphisms of Banach spaces*, arXiv:2209.04652v1 (first posted 2022-09-10). https://arxiv.org/abs/2209.04652
2. J. Becerra Guerrero and Á. Rodríguez Palacios, *Banach spaces with a large semigroup of contractive automorphisms*, J. Math. Anal. Appl. 475 (2019), 642–667. DOI: 10.1016/j.jmaa.2019.02.061.
3. V. Ferenczi and J. Lopez-Abad, *Envelopes in Banach spaces*, Banach J. Math. Anal. 18 (2024), article 59. DOI: 10.1007/s43037-024-00346-w.
