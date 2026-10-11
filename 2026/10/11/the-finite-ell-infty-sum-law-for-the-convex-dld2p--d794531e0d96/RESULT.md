# The finite \(\ell_\infty\)-sum law for the convex-DLD2P
## Finding
For every integer \(m\ge 2\) and every finite family of nonzero real Banach spaces \(X_1,\ldots,X_m\), set
\[
Z=\left(\bigoplus_{i=1}^m X_i\right)_{\ell_\infty},
\qquad
\|(x_1,\ldots,x_m)\|=\max_i\|x_i\|.
\]
Then \(Z\) has the convex diametral local diameter two property if and only if at least one factor \(X_i\) has the convex diametral local diameter two property.

Thus, for two factors, the \(\ell_\infty\)-case excluded from the recent factor-inheritance theorem has a sharp and different law:
\[
X\oplus_\infty Y\text{ has convex-DLD2P}
\quad\Longleftrightarrow\quad
X\text{ has convex-DLD2P or }Y\text{ has convex-DLD2P}.
\]

## Assumptions and scope
All spaces are nonzero real Banach spaces. A point \(x\in S_X\) is a \(\Delta\)-point when every slice of \(B_X\) containing \(x\) contains points arbitrarily close to distance \(2\) from \(x\). Write \(\Delta_X\) for the set of such points. The convex-DLD2P is
\[
B_X=\overline{\operatorname{conv}}(\Delta_X).
\]
Only finite \(\ell_\infty\)-sums are asserted here. No statement is made for infinite \(c_0\)- or \(\ell_\infty\)-sums.

## Proof
First record the pointwise finite-sum fact
\[
\Delta_Z
=
\bigcup_{i=1}^m
B_{X_1}\times\cdots\times B_{X_{i-1}}\times
\Delta_{X_i}\times
B_{X_{i+1}}\times\cdots\times B_{X_m}.
\tag{1}
\]
For the forward inclusion in the useful direction, suppose \(x=(x_j)\in S_Z\) and \(x_i\in\Delta_{X_i}\) for some \(i\). Let a slice of \(B_Z\) containing \(x\) be defined by \(F=(f_j)\in S_{Z^*}\), where \(\sum_j\|f_j\|=1\). If \(f_i\ne0\), choose a sufficiently small \(\eta>0\) so that replacing only the \(i\)-th coordinate by any \(u\in B_{X_i}\) satisfying
\[
\operatorname{Re}f_i(u)>
\operatorname{Re}f_i(x_i)-\eta
\]
keeps the resulting vector in the original slice. This condition itself defines a slice of \(B_{X_i}\) containing \(x_i\). Since \(x_i\) is a \(\Delta\)-point, one can choose such a \(u\) with \(\|u-x_i\|>2-\varepsilon\). Replacing \(x_i\) by \(u\) gives a point in the original slice whose distance from \(x\) exceeds \(2-\varepsilon\). If \(f_i=0\), use any slice of \(B_{X_i}\) containing \(x_i\) to obtain the same distance conclusion; the original slice value is unchanged. Hence \(x\in\Delta_Z\).

Conversely, suppose that no norm-attaining coordinate of \(x\in S_Z\) is a \(\Delta\)-point. Let
\[
I=\{i:\|x_i\|=1\}.
\]
For each \(i\in I\), since \(x_i\notin\Delta_{X_i}\), the standard rank-one characterization of \(\Delta\)-points gives a norming functional \(f_i\in S_{X_i^*}\), with \(f_i(x_i)=1\), such that
\[
c_i:=\|I-f_i\otimes x_i\|<2.
\]
Choose positive weights \(\lambda_i\) summing to \(1\), and define \(F\in S_{Z^*}\) by \(F=(\lambda_i f_i)_{i\in I}\), with all other coordinates zero. Then \(F(x)=1\). If \(u=(u_j)\) lies in a sufficiently thin slice
\[
\operatorname{Re}F(u)>1-\alpha,
\]
then for every \(i\in I\),
\[
1-\operatorname{Re}f_i(u_i)<\alpha/\lambda_i.
\]
Moreover,
\[
\|x_i-u_i\|
\le
\|u_i-f_i(u_i)x_i\|+|1-f_i(u_i)|
\le
c_i+\alpha/\lambda_i.
\]
For \(j\notin I\),
\[
\|x_j-u_j\|\le 1+\|x_j\|<2.
\]
Taking \(\alpha>0\) small enough makes all coordinate distances uniformly \(<2\). Thus this slice contains no points arbitrarily close to distance \(2\) from \(x\), so \(x\notin\Delta_Z\). This proves (1).

Now assume some factor, say \(X_k\), has the convex-DLD2P. Given any \(x=(x_j)\in B_Z\), approximate \(x_k\) by convex combinations of points of \(\Delta_{X_k}\) while holding every other coordinate fixed. By (1), every resulting vector is a \(\Delta\)-point of \(Z\). Hence
\[
B_Z=\overline{\operatorname{conv}}(\Delta_Z).
\]

For the converse, assume no factor has the convex-DLD2P. Put
\[
C_i=\overline{\operatorname{conv}}(\Delta_{X_i})\subsetneq B_{X_i}.
\]
If \(\Delta_{X_i}\ne\varnothing\), Hahn--Banach separation yields \(f_i\in S_{X_i^*}\) and \(a_i<1\) with
\[
\sup_{c\in C_i}\operatorname{Re}f_i(c)\le a_i.
\]
For a factor with no \(\Delta\)-points choose an arbitrary \(f_i\in S_{X_i^*}\); such an index can never be the active coordinate in (1). Let
\[
H(x_1,\ldots,x_m)=\sum_{i=1}^m f_i(x_i).
\]
The supremum of \(\operatorname{Re}H\) on \(B_Z\) is \(m\). But by (1), every \(\Delta\)-point has at least one coordinate \(i\) lying in \(\Delta_{X_i}\), and therefore
\[
\operatorname{Re}H(x)\le m-1+a_i<m.
\]
Because the family is finite, the same strict upper bound holds on \(\overline{\operatorname{conv}}(\Delta_Z)\). Hence this closed convex hull is a proper subset of \(B_Z\), contradicting convex-DLD2P. Therefore at least one factor must have the property.

## Verification
The proof uses only the slice characterization of \(\Delta\)-points, the rank-one characterization for a non-\(\Delta\) point, the dual identity
\[
\left(\bigoplus_{i=1}^m X_i\right)_{\ell_\infty}^*
=
\left(\bigoplus_{i=1}^m X_i^*\right)_{\ell_1},
\]
and Hahn--Banach separation. No finite experiment, numerical approximation, or unproved classification is used.

As a concrete check, take \(X=\mathbb R\) and \(Y=C[0,1]\). The one-dimensional space \(\mathbb R\) has no \(\Delta\)-points, while \(C[0,1]\) has the convex-DLD2P. The theorem therefore gives convex-DLD2P for \(\mathbb R\oplus_\infty C[0,1]\), showing directly that factor inheritance fails in the exceptional norm.

## Relationship to prior work
Guerrero-Viu and Markowicz prove in arXiv:2607.01875v1 that if an absolute sum \(X\oplus_NY\) has the convex-DLD2P and \(N\) is not the \(\ell_\infty\)-norm, then both factors have the property. They explicitly exclude the \(\ell_\infty\)-norm because \(\Delta\)-points there can have coordinates that are not \(\Delta\)-points.

Abrahamsen, Haller, Lima, and Pirk prove the earlier sufficient stability theorem that if both \(X\) and \(Y\) have convex-DLD2P, then \(X\oplus_NY\) has convex-DLD2P for every absolute normalized norm \(N\). The present result sharpens that statement specifically at \(N=\ell_\infty\): one factor is sufficient, and one factor is also necessary.

The pointwise coordinate behavior of \(\Delta\)-points in absolute sums is part of the established direct-sum literature; it is used here as a proved ingredient and reconstructed above. The new claim is the exact convex-hull consequence for finite \(\ell_\infty\)-sums.

## Limitations
The theorem is restricted to finite \(\ell_\infty\)-sums. Infinite coordinate sums can behave differently because convex generation can exploit different coordinates across an unbounded family. The result does not classify convex-DLD2P for arbitrary absolute norms beyond the finite \(\ell_\infty\) case.

A residual literature risk remains that the finite \(\ell_\infty\) equivalence may appear as an unstated or poorly indexed corollary of earlier direct-sum work. Targeted searches of the focal paper, the foundational convex-DLD2P direct-sum paper, the recent erratum on \(M\)-ideal stability, and the available research index did not locate such a statement.

## References
1. J. Guerrero-Viu and J. Markowicz, *On super Delta-points and the convex-DLD2P in absolute sums*, arXiv:2607.01875v1, 2026.
2. T. A. Abrahamsen, R. Haller, V. Lima, and K. Pirk, *Delta- and Daugavet-points in Banach spaces*, Proc. Edinburgh Math. Soc. 63 (2020), 475--496; arXiv:1812.02450.
3. K. Pirk, *Diametral diameter two properties, Daugavet-, and \(\Delta\)-points in Banach spaces*, PhD thesis, University of Tartu, 2020.
4. J. Langemets, *Erratum and a counterexample to: Stability of diametral diameter two properties*, arXiv:2609.28569v1, 2026.
