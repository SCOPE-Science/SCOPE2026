# Exact volume spectrum of antipodal vertex selections in the regular icosahedron

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(I\) be the regular icosahedron with vertex set
\[
\{(0,\pm1,\pm\varphi),\ (\pm1,\pm\varphi,0),\ (\pm\varphi,0,\pm1)\}.
\]
Its edge length is \(2\). Choose exactly one vertex from each of its six antipodal pairs and let \(P\) be the convex hull of the six chosen vertices. Across all \(2^6=64\) choices, \(\operatorname{Vol}(P)\) takes exactly four values:

| Representative signs \((\epsilon_1,\ldots,\epsilon_6)\) | Exact volume | Number of choices |
|---|---:|---:|
| \((+,+,+,-,+,+)\) | \((4+2\varphi)/3\) | 12 |
| \((+,+,+,+,+,+)\) | \((4+6\varphi)/3\) | 20 |
| \((+,+,+,+,+,-)\) | \((4+8\varphi)/3\) | 20 |
| \((+,+,+,+,-,-)\) | \((6+8\varphi)/3\) | 12 |

Here \(v_1=(0,1,\varphi)\), \(v_2=(0,1,-\varphi)\), \(v_3=(1,\varphi,0)\), \(v_4=(1,-\varphi,0)\), \(v_5=(\varphi,0,1)\), and \(v_6=(\varphi,0,-1)\); the sign pattern denotes the selected vertices \(\epsilon_i v_i\). The multiplicities sum to \(64\), and the minimum and maximum volumes are \((4+2\varphi)/3\) and \((6+8\varphi)/3\).

## Assumptions and scope

The coordinates above fix the scale (edge length \(2\)) and the center at the origin. A selection contains exactly one endpoint from each pair \(\{v_i,-v_i\}\). The claim concerns only this fixed regular icosahedron; it is not a statement about arbitrary centrally symmetric point sets or arbitrary antipodal polytopes.

## Proof

All coordinates lie in \(\mathbb Z[\varphi]\), with \(\varphi^2=\varphi+1\). Represent \(a+b\varphi\) by the integer pair \((a,b)\); addition, multiplication, determinants, and dot products then remain exact. The sign test is exact because
\[
2(a+b\varphi)=(2a+b)+b\sqrt5,
\]
so its sign is decided by integer sign comparisons and, when needed, comparing the squares of positive integers. Equality in the nontrivial squared comparison is impossible because \(\sqrt5\) is irrational.

For each of the \(64\) sign vectors, the verification program enumerates all \(\binom63=20\) triples. It tests each triple's plane against the remaining three points using exact signs, collects all coplanar points on every supporting plane, and thereby recovers every facet. Facet edges are identified as intersections of distinct facets in two vertices; each facet boundary is then ordered and triangulated by a fan. The signed tetrahedral-volume identity
\[
\operatorname{Vol}(P)=\frac16\left|\sum_{(a,b,c)}\det(a,b,c)\right|
\]
uses the outward-oriented boundary triangles. Summing these determinants in \(\mathbb Z[\varphi]\) gives the four exact values and multiplicities in the table. The program asserts the complete count map \(\{(8,4):12,(8,12):20,(8,16):20,(12,16):12\}\) for the coefficients of \(6\operatorname{Vol}(P)=A+B\varphi\). No floating-point decision is used in the proof computation.

## Verification

The standalone verifier uses only the Python standard library and exhaustively enumerates all \(64\) selections. It asserts that every selection is three-dimensional and that the exact coefficient pairs and multiplicities equal the displayed table. A separate floating-point convex-hull calculation was used only as a consistency check; it agreed with the exact results to within \(1.8\times10^{-15}\), but it is not part of the proof.

## Relationship to prior work

Aichholzer et al. study antipodal polygons and their higher-dimensional analogues. Their three-dimensional counterexample uses five antipodal pairs to show that the planar thin-versus-nonthin area ordering does not extend to higher dimensions; their final section leaves further questions about thick antipodal polytopes open. They do not give the exact volume spectrum for the six antipodal pairs of the regular icosahedron. Barba et al. study planar asymmetric \(k\)-gons with \(k<n\), which is a different dimension and parameter regime. The present result is a finite exact classification for one canonical three-dimensional point set, not a general resolution of the higher-dimensional problem.

## Limitations

The classification is specific to the regular icosahedron at the stated scale. It does not provide a formula for arbitrary antipodal sets, a general extremal-volume theorem, or a solution to the general existence problem for thick antipodal polytopes. The literature comparison is best-knowledge based; independent audit has not been performed.

## References

1. O. Aichholzer, L. E. Caraballo, J. M. Díaz-Báñez, R. Fabila-Monroy, C. Ochoa, and P. Nigsch, “Extremal antipodal polygons and polytopes,” arXiv:1301.6667 (2013), especially Sections 5–6.
2. L. Barba, L. E. Caraballo, J. M. Díaz-Báñez, R. Fabila-Monroy, and E. Pérez-Castillo, “Asymmetric polygons with maximum area,” arXiv:1501.07721 (2015), especially Sections 1–2.
