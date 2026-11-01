# Ridge-skeleton rigidity for products of admissible planar polygons

## Finding

Let \(P\subset\mathbb R^n\), \(n\ge3\), be a Cartesian product of \(m\ge0\) planar polygons \(Q_i\) and \(\ell\ge0\) intervals \(I_j\), in pairwise orthogonal coordinate subspaces, with \(n=2m+\ell\). Suppose \(0\) belongs to the interior of every factor and every nonempty proper face \(F\) of each factor, of codimension \(k\), satisfies \(\operatorname{dist}(0,\operatorname{aff}F)\ge\sqrt{k}\). In particular, the same distance condition holds for every face of \(P\).

Write \(A_i\) for the area, \(L_i\) for the perimeter and \(v_i\) for the number of vertices of \(Q_i\). Put \(\delta_i=L_i/8-1\), and let \(T\) count the triangular planar factors. For the total \((n-2)\)-dimensional face measure \(\Phi_{n-2}\), one has the explicit remainder

\[
\frac{\Phi_{n-2}(P)}{2^n}-\binom n2\ge
\sum_{i=1}^m\left(\frac{v_i}{4}-1\right)
+2(n-2)\sum_{i=1}^m\delta_i
+4\sum_{1\le i<j\le m}\delta_i\delta_j
\ge\frac{6\sqrt3-9}{4}T.
\]

Consequently every such product satisfies the proposed sharp ridge inequality
\[
\Phi_{n-2}(P)\ge n(n-1)2^{n-1},
\]
with equality **exactly** when the product is a Euclidean cube of edge length \(2\) centered at the origin, up to orthogonal congruence. Moreover the coefficient of \(T\) in the displayed dimensional lower bound is best possible uniformly over all admissible dimensions and products: the product of an inradius-one equilateral triangle with \([-1,1]\) gives equality in this triangular-factor gap.

## Assumptions and scope

For a \(d\)-polytope \(K\), write \(\Phi_j(K)=\sum_{F\in\mathcal F_j(K)}\mathcal H^j(F)\), where \(\mathcal F_j(K)\) consists of the \(j\)-faces and \(\Phi_d(K)=\operatorname{vol}_d(K)\). Every polygon is nondegenerate and every interval has positive length. A planar factor's edge lines must be at distance at least \(1\), and its vertices at distance at least \(\sqrt2\), from the origin. Interval endpoints are at distance at least \(1\). No symmetry, regularity or fixed number of sides is assumed for the polygons. Cartesian products use their intrinsic orthogonal Euclidean metric. The assertion does **not** cover arbitrary admissible polytopes that fail to split into one- or two-dimensional factors.

## Proof

**Factor bounds.** The sharp two-dimensional volume and surface inequalities for face-distance-admissible polytopes give \(A_i\ge4\) and \(L_i\ge8\), respectively. Each interval has length \(s_j\ge2\). Every polygon has \(v_i\ge3\). If \(v_i=3\), its three supporting lines contain the unit disk. Let \(\theta_1,\theta_2,\theta_3\in(0,\pi)\) be the successive exterior-normal gaps, summing to \(2\pi\). Moving its sides inward to tangent lines around the unit disk cannot increase perimeter. The tangent triangle has perimeter \(2\sum_i\tan(\theta_i/2)\). Jensen's inequality gives \(L_i\ge6\sqrt3\). Equality requires the tangent equilateral triangle of inradius \(1\).

**Face polynomial.** Define the codimension polynomial \(C_K(z)=\sum_{k=0}^{d}\Phi_{d-k}(K)z^k\) for a \(d\)-polytope. Since every face of a Cartesian product is the product of faces and its intrinsic volume is the product of their volumes, \(C_{K\times M}=C_KC_M\). For our factors,

\[
C_{Q_i}(z)=A_i+L_i z+v_i z^2,
\qquad C_{I_j}(z)=s_j+2z.
\]

All coefficients are nonnegative. In the coefficient of \(z^2\) of their product, replace every \(A_i\) by \(4\) and every \(s_j\) by \(2\), retaining the other coefficients. This gives a lower bound. With \(q_i=L_i/8=1+\delta_i\), direct enumeration of the three ways to select a total codimension of two yields

\[
\frac{\Phi_{n-2}(P)}{2^n}
\ge\sum_i\frac{v_i}{4}
+4\sum_{i<j}q_iq_j
+2\ell\sum_iq_i+\binom\ell2.
\]

The corresponding cube coefficient is \(\binom n2=m+4\binom m2+2m\ell+\binom\ell2\). Subtracting this and using \(n=2m+\ell\) proves the first inequality, since \(4(m-1)+2\ell=2(n-2)\).

**Triangle compensation.** For a nontriangular factor, \(v_i/4-1\ge0\) and \(\delta_i\ge0\). For a triangular factor, \(v_i/4-1=-1/4\) but \(\delta_i\ge(3\sqrt3-4)/4\). Because \(n\ge3\), its contribution to the first two sums is at least

\[
-\frac14+2(n-2)\frac{3\sqrt3-4}{4}
\ge\frac{6\sqrt3-9}{4}>0.
\]

All products \(\delta_i\delta_j\) are nonnegative. Summing proves the second inequality.

**Equality and sharpness.** Equality in the ridge bound requires the absence of triangular factors, \(v_i=4\) and \(L_i=8\) for all planar factors, and interval lengths \(s_j=2\). Any quadrilateral containing the unit disk has perimeter at least \(8\), with equality only for the tangent square: move its four edge lines inward to the disk and apply Jensen to their consecutive normal gaps, with equality only at four gaps \(\pi/2\). Thus each planar factor is a centered side-\(2\) square; all intervals are \([-1,1]\). Conversely their product is a centered cube and gives equality. For the best universal triangular-factor coefficient, take \(n=3\), \(Q\) an inradius-one equilateral triangle and \(I=[-1,1]\). Its total edge length is \(2(6\sqrt3)+2(3)=12\sqrt3+6\), exceeding the cubical value \(24\) by \(12\sqrt3-18=2^3(6\sqrt3-9)/4\). All face-distance premises are met, because the triangle vertices lie at distance \(2\) from its center.

## Verification

The coefficient identity was reconstructed directly from the face-polynomial product. The independently executable file `verify.py` checks \(884\) products formed from tangent equilateral triangles, tangent squares and unit intervals, in dimensions \(3\) through \(18\), including the sharp triangular-prism coefficient and cube equality. A successful finite numerical run is a consistency test, not the proof for infinitely many products; the argument above establishes the universal quantifiers. Python 3 standard library is sufficient: run `python verify.py`.

## Relationship to prior work

Zwierzyński's 2026 surface-area theorem gives the planar \(L_i\ge8\) premise and formulates the general ridge-skeleton conjecture as Conjecture 5.2. Its Proposition 5.3 settles centered orthotopes and centrally symmetric admissible polytopes with every facet at distance exactly one. Its Section 5 uses the face polynomial for a different purpose, constructing counterexamples for skeleta of larger codimension. The present class permits arbitrary asymmetric planar factors and handles the fact that an admissible triangle has only three vertices, below the two-dimensional cubical vertex count. The three-dimensional case of the unquantified ridge bound also follows from the older Besicovitch–Eggleston edge-length theorem; the arbitrary-dimensional planar-product statement and its triangular-factor remainder are not stated by either cited result.

## Limitations

This does not prove Conjecture 5.2 for indecomposable polytopes or arbitrary higher-dimensional factors. The quantitative lower bound retains only the area/perimeter lower bounds of its factors and may be nonsharp for any fixed higher dimension. The uniform triangular-factor constant is sharp **across all dimensions**, at the three-dimensional triangular prism. Literature-priority uncertainty remains for earlier unindexed results about product polytopes; mathematical-record searches cannot establish global priority. Independent validation has not been performed.

## References

1. M. Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem* (2026), arXiv:2609.27798, Theorem 1.1, Proposition 5.3, and Section 5, https://arxiv.org/html/2609.27798.
2. R. Karasev, *Rogers's proof of Vaaler's theorem* (2026), Theorem 1.1, as cited in reference 1.
3. A. S. Besicovitch and H. G. Eggleston, *The total length of the edges of a polyhedron* (1957), as cited in reference 1.
