# Exact sub-Hilbert branch of the two-parameter geometric-mean constant on real \(\ell_p\)
## Finding
Let \(I\) be an index set with at least two elements and let \(\kappa,	au>0\). For the real sequence space \(\ell_p(I)\), define
\[
\mathcal T_1(\kappa,	au,\ell_p(I))
=
\sup_{x,y\in S_{\ell_p(I)}}
\sqrt{\|\kappa x+	au y\|_p\,\|\kappa x-	au y\|_p}.
\]
Then
\[
\mathcal T_1(\kappa,	au,\ell_p(I))=(\kappa^p+	au^p)^{1/p}
\qquad(1\le p\le2),
\]
and
\[
\mathcal T_1(\kappa,	au,\ell_\infty(I))=\kappa+	au.
\]
Together with the published formula of Wang, Liu, Zhou, Xia and Toseef for \(p>2\), this gives the complete exact real \(\ell_p\) profile. In particular, the Hilbert exponent is the transition point between the disjoint-support branch below \(2\) and the balanced two-coordinate branch above \(2\).

## Assumptions and scope
The scalar field is real, \(|I|\ge2\), and \(\kappa,	au\) are strictly positive. The definition is the two-parameter geometric-mean constant \(\mathcal T_1\) introduced by Wang, Liu, Zhou, Xia and Toseef. For finite \(p\), \(\ell_p(I)\) has its standard norm. For \(p=\infty\), the standard supremum norm is used. No assertion is made for arbitrary Banach spaces, for complex-only phenomena, or for a classification of every extremizing pair.

## Proof
First let \(1<p\le2\), and let \(q=p/(p-1)\) be the conjugate exponent. Fix \(x,y\in S_{\ell_p(I)}\), and put
\[
A=\|\kappa x+	au y\|_p,
\qquad
B=\|\kappa x-	au y\|_p.
\]
Clarkson's inequality in the sub-Hilbert range gives
\[
\left\|rac{u+v}2ight\|_p^q+
\left\|rac{u-v}2ight\|_p^q
\le
\left(rac{\|u\|_p^p+\|v\|_p^p}2ight)^{q/p}.
\]
Apply this with \(u=\kappa x\) and \(v=	au y\). Since \(q(1-1/p)=1\), multiplication by \(2^q\) yields
\[
A^q+B^q\le2(\kappa^p+	au^p)^{q/p}.
\]
By the arithmetic-geometric mean inequality,
\[
2(AB)^{q/2}\le A^q+B^q,
\]
and therefore
\[
\sqrt{AB}\le(\kappa^p+	au^p)^{1/p}.
\]
This proves the upper bound. Choose two distinct coordinates \(i,j\in I\) and set \(x=e_i\), \(y=e_j\). Their supports are disjoint, so
\[
\|\kappa x\pm	au y\|_p=(\kappa^p+	au^p)^{1/p}.
\]
Hence equality holds for every \(1<p\le2\).

For \(p=1\), the triangle inequality gives
\[
\|\kappa x\pm	au y\|_1\le\kappa+	au,
\]
so the geometric mean is at most \(\kappa+	au\). The same disjoint coordinate vectors satisfy equality in both signs, proving
\[
\mathcal T_1(\kappa,	au,\ell_1(I))=\kappa+	au.
\]
This is exactly the displayed finite-\(p\) formula at \(p=1\).

For \(p=\infty\), the triangle inequality again gives the upper bound \(\kappa+	au\). Choose distinct \(i,j\in I\), and set
\[
x=e_i+e_j,
\qquad
y=e_i-e_j.
\]
Both are unit vectors in \(\ell_\infty(I)\), and both \(\kappa x+	au y\) and \(\kappa x-	au y\) have supremum norm \(\kappa+	au\). Thus the endpoint value is exact.

At \(p=2\), the new branch gives \(\sqrt{\kappa^2+	au^2}\). The published super-Hilbert formula
\[
2^{-1/p}ig((\kappa+	au)^p+|\kappa-	au|^pig)^{1/p}
\]
has the same value at \(p=2\), so the two finite-\(p\) branches meet continuously and exactly there.

## Verification
The proof is analytic and dimension-free. The only nontrivial inequality is Clarkson's classical inequality for \(1<p\le2\), used with its exact conjugate exponent. The lower bounds are attained by explicit two-coordinate vectors, so there is no finite-dimensional approximation or limiting argument. The endpoint checks use only the triangle inequality and exact coordinate norms. Numerical sampling is unnecessary for the theorem and is not used as evidence.

## Relationship to prior work
Wang, Liu, Zhou, Xia and Toseef introduced \(\mathcal T_1(\kappa,	au,X)\), proved the universal bounds
\[
\sqrt{\kappa^2+	au^2}\le\mathcal T_1(\kappa,	au,X)\le\kappa+	au,
\]
and computed the exact \(\ell_p\) value only for \(p>2\). Their stated formula in that range is
\[
\mathcal T_1(\kappa,	au,\ell_p)
=2^{-1/p}ig((\kappa+	au)^p+|\kappa-	au|^pig)^{1/p}.
\]
The present result supplies the complementary full range \(1\le p\le2\) and the \(p=\infty\) endpoint.

The earlier Alonso--Llorens-Fuster geometric-mean constant is the one-parameter ancestor obtained from the unweighted triangle geometry. It does not by itself state the arbitrary two-parameter profile proved here. Closest published database records for generalized James and skew arithmetic-mean constants use different functionals: a minimum or an arithmetic mean rather than the geometric mean \(\sqrt{AB}\). Their formulas therefore do not supply the required product upper bound.

## Limitations
The statement is restricted to real classical sequence spaces and to this specific two-parameter geometric-mean constant. The proof does not classify all equality cases. The literature comparison cannot rule out an equivalent formula hidden under substantially different terminology, and the full text of the 2008 ancestor was not used to assert absence of a two-parameter theorem. The scientific claim does not depend on numerical computation.

## References
1. Y. Wang, Q. Liu, H. Zhou, J. Xia and M. Toseef, *On some generalized geometric constants with two parameters in Banach spaces*, arXiv:2505.17600v1, first posted 23 May 2025.
2. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society 40 (1936), 396--414.
3. J. Alonso and E. Llorens-Fuster, *Geometric mean and triangles inscribed in a semicircle in Banach spaces*, Journal of Mathematical Analysis and Applications 340 (2008), 1271--1283, DOI 10.1016/j.jmaa.2007.09.040.
