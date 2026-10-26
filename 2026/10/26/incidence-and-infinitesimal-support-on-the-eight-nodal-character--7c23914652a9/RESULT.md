# Incidence and infinitesimal support on the eight-nodal characteristic-three quartic

## Finding
Let \(X\subset\mathbf P^3_{\mathbf F_3}\) be the quartic
\[
\Psi(x_0,x_1,x_2,x_3)=\Psi(-x_1,x_0,-x_3,x_2),\qquad
\Psi(w,x,y,z)=wz(w^2+wx+x^2+y^2+yz+z^2).
\]
There are exactly \(48\) lines on \(X\) defined over \(\mathbf F_9\). Of these, eight contain no singular point of \(X\), 32 contain one, and eight contain two. Their ordinary projective intersection graph (two lines are adjacent when they meet, even at a singular point) is connected, with \(384\) edges and degree multiset \(14^8,16^{32},18^8\). Exactly \(120\) of the edges correspond to intersections at singular points; the remaining \(264\) correspond to smooth points.

The Zariski tangent space of the projective-line Fano scheme \(F_1(X)\) has dimension one at exactly seven of the eight two-node lines, and dimension zero at the remaining two-node line \(\ell_0=\{x_0=x_2=0\}\). All 40 other \(\mathbf F_9\)-rational lines have tangent dimension zero. Thus, **the seven tangent-obstructed lines form all but one of the maximum-degree class**, and the exceptional maximum-degree line \(\ell_0\) is infinitesimally reduced. The node-free, one-node and two-node statistics are finite-field assertions; no assertion about further geometric lines over larger fields is needed.

## Assumptions and scope
All arithmetic is in characteristic three. Write \(\mathbf F_9=\mathbf F_3[\tau]/(\tau^2+1)\), with the unique normalized reduced-row-echelon representatives of two-dimensional subspaces of \(\mathbf F_9^4\). The intersection graph uses intersections in the ambient projective space, not intersections of strict transforms on the minimal resolution. Its edges at singular points are retained. The singular points used in the computation are exactly the eight points over \(\mathbf F_9\) where the quartic and all four partial derivatives vanish, matching the previously published eight geometric nodes. Tangent spaces mean first-order line deformations in the Grassmannian cut out by the quartic restriction equations.

## Proof
The RREF forms for a two-dimensional subspace have pivot columns \(i<j\), with row \(u\) containing a leading one in column \(i\), row \(v\) containing a leading one in column \(j\), and only free entries strictly right of the respective pivots. Enumerating them gives
\[
{4\brack2}_9=(9^2+1)(9^2+9+1)=7462.
\]
For each basis, the degree-four restriction \(F(su+tv)\) vanishes identically precisely when it vanishes at all ten points \([s:t]\in\mathbf P^1(\mathbf F_9)\); a nonzero homogeneous binary quartic cannot vanish at ten distinct projective points. The exact independent coefficient/point evaluator in `verify.py` finds 48 qualifying RREF bases. Therefore the 48 count is exhaustive **over \(\mathbf F_9\)**.

The eight singular points are obtained by evaluating \(F\) and its four formal derivatives at all 820 points of \(\mathbf P^3(\mathbf F_9)\). Each of the 48 lines is represented by its ten distinct projective points. For a pair of distinct lines, intersection over the algebraic closure occurs if and only if their point lists share a point: the unique point of intersection of two lines defined over \(\mathbf F_9\) is Frobenius invariant. The program computes all unordered pairs of lines, yielding 384 edges. Each edge has exactly one intersection point, of which 120 are singular and 264 smooth. The line-by-line degree and node-incidence counts are respectively \(14^8,16^{32},18^8\) and \(0^8,1^{32},2^8\), with exact correspondence \(0\leftrightarrow14\), \(1\leftrightarrow16\), \(2\leftrightarrow18\).

For tangent spaces, choose the affine Grassmannian chart corresponding to each line's RREF pivots. In that chart the five coefficients of \(F(su+tv)\) define the Fano scheme. Their linearization in each free RREF coordinate is obtained from \(\sum_k (\partial F/\partial x_k)(su+tv)\delta x_k(s,t)\). The matrix over \(\mathbf F_9\) of these five coefficient equations has nullity \(0\) or \(1\). The exact finite-field rank calculation in `verify.py` yields 41 nullities zero and seven nullities one. Cross-tabulating with singular-node incidence yields \((0,14,0)^8\), \((1,16,0)^{32}\), \((2,18,1)^7\), \((2,18,0)^1\), where the entries are (nodes on line, graph degree, tangent dimension). In the final class the unique nullity-zero RREF basis spans \(\{x_0=x_2=0\}\). Since its tangent space has dimension zero at an algebraically closed geometric point, its local finite-type Fano scheme is reduced there; the seven tangent-dimension-one points have nonreduced local rings if the support is zero-dimensional, as is known for this geometric configuration, but no local multiplicities are determined here.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. It prints `VERIFY_OK` after checking all 7462 RREF lines, every restriction, all eight singular points, all pairwise incidences, Frobenius line cycles \(1^6 2^{21}\), all tangent nullities, and a second point-pair line enumeration. Source-code-based finite enumeration is a complete proof of the stated finite-field assertions because every ambient object is enumerated and evaluated with exact arithmetic. The last paragraph's implication from tangent dimension zero to reducedness uses the standard local Artin algebra fact for a zero-dimensional isolated scheme point.

## Relationship to prior work
Veniani's 2016 first version gives the same quartic equation and reports 48 geometric lines and eight singularities, but does not provide the complete intersection-graph/node-incidence/tangent cross-classification above. Its later revision discusses selected local line valencies and node incidences. The source reports eight lines through certain nodes and a different smooth valency for \(\ell_0\); the exact finite-field census here finds six \(\mathbf F_9\)-lines through each displayed node and eight smooth-point neighbors of \(\ell_0\). Therefore those local source statements are **not** used to establish the new claim; any additional geometric lines over larger fields or an unresolved comparison with the printed numbers must be examined independently. An earlier explicit computation established the seven tangent-obstructed support points and their Frobenius types; neither their existence alone nor the known total of 48 lines implies the present node-incidence/graph/tangent correspondence. Shimada–Shioda study the characteristic-zero model and certain reductions, without this finite-field intersection classification.

## Limitations
The counts and incidence graph are for the 48 lines **defined over \(\mathbf F_9\)**. No statement is made about the completeness of this set over algebraically closed extensions from the finite-field enumeration alone. The printed later-source local incidence numbers do not coincide with the finite-field counts and remain a comparison risk. The exact local nonreduced lengths and the geometric Picard lattice are not determined. No independent audit has been performed.

## References
- D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209v1 (first public version, 15 August 2016), Example 6.5; arXiv:1608.04209v4 (14 December 2020), Example 5.4. https://arxiv.org/abs/1608.04209
- I. Shimada and T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to a Kummer surface*, arXiv:1604.06265 (2016), on the characteristic-zero model and reductions. https://arxiv.org/abs/1604.06265
