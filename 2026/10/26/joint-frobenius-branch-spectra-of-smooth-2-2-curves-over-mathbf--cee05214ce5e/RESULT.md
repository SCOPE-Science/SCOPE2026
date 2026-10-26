# Joint Frobenius branch spectra of smooth \((2,2)\) curves over \(\mathbf F_3\)

## Finding

For scalar-normalized geometrically smooth bidegree-\((2,2)\) curves in \(\mathbf P^1_{\mathbf F_3}\times\mathbf P^1_{\mathbf F_3}\), the unordered pair of Frobenius cycle partitions of the four branch points of the two degree-two projections takes precisely six values: \(((1,1,1,1),(2,2))\), \(((1,1,2),(1,1,2))\), \(((1,1,2),(4))\), \(((1,3),(1,3))\), \(((2,2),(2,2))\), and \(((4),(4))\), with respective numbers of scalar-normalized equations \(144,432,1728,2304,144,432\). These \(5184\) curves form exactly \(14\) polarized projective orbits; the overall smooth-form total \(5184\) is already known.

The joint spectrum is computed after identifying the two projection directions, but without quotienting forms by changes of coordinates. Each count is of equations normalized by the nonzero field scalars; over \(\mathbf F_3\) this identifies \(F\sim2F\). The complete distribution is:

| Unordered pair of Frobenius degree partitions | Equations | Polarized projective orbits |
| --- | ---: | ---: |
| \(((1,1,1,1),(2,2))\) | 144 | 1 |
| \(((1,1,2),(1,1,2))\) | 432 | 2 |
| \(((1,1,2),(4))\) | 1728 | 4 |
| \(((1,3),(1,3))\) | 2304 | 4 |
| \(((2,2),(2,2))\) | 144 | 1 |
| \(((4),(4))\) | 432 | 2 |
| **Total** | **5184** | **14** |

The corresponding rational-point-count distribution, also checked, is \(N=2,3,4,5,6,7\) with equation frequencies \(288,576,1152,1152,1440,576\), respectively. This is supporting classification data and not a separate discovery claim.

## Assumptions and scope

All fields and transformations are over \(k=\mathbf F_3\). An equation is a nonzero bihomogeneous polynomial \(F(X_0,X_1;Y_0,Y_1)\) of bidegree \((2,2)\), considered up to multiplication by \(k^\times\), with coefficients in the monomial order \((X_0^2,X_0X_1,X_1^2)\otimes(Y_0^2,Y_0Y_1,Y_1^2)\). The first nonzero coefficient is normalized to \(1\). There are \((3^9-1)/2=9841\) normalized equations.

A curve is **geometrically smooth** when no singular geometric point exists after extending to an algebraic closure. Such a curve is geometrically connected of arithmetic and geometric genus \(1\) by the genus formula for smooth bidegree \((2,2)\) divisors. Each projection to a factor is a finite separable degree-two morphism, with a reduced branch divisor of degree \(4\). A partition \((d_1,\ldots,d_r)\) records the degrees over \(k\) of the Frobenius orbits on the four geometric branch points; order within a partition is immaterial. The two projection partitions are recorded as an unordered pair because swapping factors is an allowed symmetry.

A **polarized projective equivalence** is induced by \((\operatorname{PGL}_2(k)\times\operatorname{PGL}_2(k))\rtimes C_2\), of order \(24^2\cdot2=1152\), acting on the fixed split quadric and allowing an exchange of factors. The orbit claim concerns this group, not all abstract isomorphisms of genus-one curves.

## Proof

**Discriminants and the smoothness criterion.** Write \(F=A(Y)X_0^2+B(Y)X_0X_1+C(Y)X_1^2\), with binary quadratic \(A,B,C\). Its first projection branch polynomial in the other coordinate is \(D_Y=B^2-4AC=B^2-AC\), a binary quartic over characteristic \(3\). Interchanging the factors gives \(D_X\). For a geometrically smooth \((2,2)\) curve, each projection is a separable double cover branched at four distinct geometric points, so its discriminant is squarefree. Conversely, if \(D_Y\) is squarefree, then \(A,B,C\) have no common geometric root (otherwise \(D_Y\) has a repeated root), so the projection is finite of degree two. Because the characteristic is not two, the local cover equation after completing the square has the form \(u^2=h(t)\); away from branch points it is étale, and at simple zeros of \(h\) it is nonsingular. Thus squarefreeness of either discriminant implies geometric smoothness. The other discriminant must then also be squarefree. These equivalences are independently checked against the Jacobian criterion below for all projective representatives.

**Exhaustive arithmetic computation.** Enumerate every \(9\)-tuple in \(k^9\setminus\{0\}\) with its first nonzero component equal to \(1\). Dehomogenize each binary quartic at \(Y_0=1\), keeping a degree-one factor at infinity if the affine degree is \(3\). Test squarefreeness by Euclidean gcd with the formal derivative, then factor the quartic into monic irreducibles of degrees \(1\) to \(4\) by exact trial division over \(k\). For each smooth equation, compute and sort the two degree partitions. The direct enumeration in `biquad3_independent.py` obtains exactly the six counts displayed above and \(5184\) smooth forms.

**Independent geometric and orbit computation.** Enumerate the orbits of all \(9841\) normalized equations under elementary transformations of the two projective factors and their swap. The resulting \(41\) disjoint orbits exhaust all normalized equations. For each orbit representative, form its four bihomogeneous partial derivatives and compute their Gröbner ideals on the four standard affine charts \(X_i=Y_j=1\). Exactly \(14\) orbits, representing \(5184\) equations, have unit Jacobian ideal on every chart; hence they are geometrically smooth. The branch factors and their orbit-weighted frequencies agree with the independent direct enumeration. A further independent check enumerates all \(1152\) automorphisms using evaluation/interpolation and recovers all \(14\) orbit sizes and their mutual disjointness. The \(14\) representatives and their sizes are tabulated in `REPRESENTATIVES.csv`.

## Verification

The embedded standalone programs are `biquad3.py` (symbolic Jacobian/orbit computation), `biquad3_independent.py` (independent exact full-form discriminant and factor-degree computation), and `biquad3_groupcheck.py` (all group elements by evaluation/interpolation). `biquad3_groupcheck.py` reads `biquad3_results.json` generated by the first script; other programs are independent. All use exact modular arithmetic. Run from the directory containing them with Python 3.10 or later and SymPy 1.14: `python -W ignore biquad3.py`, `python biquad3_independent.py`, then `python biquad3_groupcheck.py`. The three accompanying `*_reference.txt` files record successful runs. The two direct counts of all smooth equations and all six joint branch types agree, and the third computation confirms group orbit sizes.

`biquad3_results.json` contains all \(41\) projective representatives, with coefficient mask, orbit size, smoothness flag, branch partitions, equation and rational-point count (for smooth representatives). `biquad3_independent.json` records the independently recomputed frequencies. No finite extension cut-off is used to assert geometric smoothness: the first computation uses exact Gröbner ideals, while the second uses the squarefree discriminant criterion over the algebraic closure.

## Relationship to prior work

Fisher and Radičević [1, Section 2] associate two binary quartics to a bidegree \((2,2)\) genus-one form. Fisher, Ho and Park [2, Remark 3.6] already give the total number of smooth \((2,2)\) forms up to scaling over \(\mathbf F_q\) as \(q^4(q+1)^2(q-1)^2\), which specializes to \(5184\) for \(q=3\). **That total is prior work, not the new claim.** Their broader counts do not specify how the Frobenius permutations on the two branch divisors occur jointly. The classification here adds the precise unordered six-profile distribution and its orbit refinement, including asymmetric branch behavior that aggregate smooth-form counts do not determine.

## Limitations

The theorem concerns the single field \(\mathbf F_3\) and the specified polarized models; it is not a formula for all finite fields and does not identify abstract elliptic curve isomorphism classes. The point-count distribution is auxiliary. Exact enumeration certifies the finite statement but cannot establish global publication priority. Earlier unindexed small-field databases or classifications might already imply individual profiles; a comprehensive independent literature audit is not claimed.

## References

[1] T. Fisher and L. Radičević, *Some minimisation algorithms in arithmetic invariant theory*, arXiv:1703.01940, first posted 2017-03-06, especially Section 2. https://arxiv.org/abs/1703.01940

[2] T. Fisher, W. Ho and J. Park, *Everywhere local solubility for hypersurfaces in products of projective spaces*, arXiv:1911.09623, first posted 2019-11-21, especially Remark 3.6 and Section 6.2. https://arxiv.org/abs/1911.09623
