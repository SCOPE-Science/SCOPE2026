# Six Euclidean inball phases of complementary chainlink sections

## Finding

Consider the planar Euclidean sections
\[
Q_t=\{(x_1,x_2,x_3)\in\mathbb R^3: x_1+x_2+x_3=t,\ 0\le x_i\le a_i,\ x_i-x_{i+1}\le a_i-2\},
\]
where \((a_1,a_2,a_3)=(4,5,6)\), indices are cyclic, and \(0\le t\le15\). Distances, areas, and perimeters are **intrinsic Euclidean** quantities in the affine plane of each section. Put
\[
 c=\frac{\sqrt6-\sqrt2}{4},\qquad d=\frac{3\sqrt2-\sqrt6}{12}.
\]
The exact Euclidean inradius is the following minimum of six affine functions:
\[
 \boxed{r(t)=\min\left\{\frac{t}{\sqrt6},\ c(t+2),\ d(t+7),\frac{3\sqrt2}{2},\ c(17-t),\frac{15-t}{\sqrt6}\right\}.}
\]
For increasing \(t\), the six expressions are active in the stated order, with the five exact interior change points
\[
 2\sqrt3,\quad\frac{1+5\sqrt3}{2},\quad2+3\sqrt3,\quad14-3\sqrt3,\quad15-2\sqrt3.
\]
The endpoint sections \(Q_0,Q_{15}\) are singletons, and their inradius in the ambient section plane is defined to be zero. All other sections have two-dimensional interior.

The complementary *integer-level* sections \(Q_6,Q_9\) have the same Ehrhart quasipolynomial (a previously established theorem), exactly six vertices each, the same intrinsic area \(43\sqrt3/4\), and the same intrinsic perimeter \(9(\sqrt2+\sqrt6)/2\). Yet their largest inscribed-circle radii are different:
\[
 \boxed{r(6)=\frac{13(3\sqrt2-\sqrt6)}{12}<2(\sqrt6-\sqrt2)=r(9).}
\]
In particular, Ehrhart equivalence **even together with equal Euclidean area, perimeter, and vertex count** does not determine the Euclidean inradius in this natural family. The precise positive difference is \((37\sqrt6-63\sqrt2)/12\).

## Assumptions and scope

This is the fixed chainlink polytope \(\mathrm{CL}((4,5,6),2)\) defined in Kantarcı Oğuz–Özel–Ravichandran. The primary claim is a complete exact formula for the inradius of every real-level section of this one chainlink polytope, with a derived concrete complementary-section counterexample. No claim is made for arbitrary parameters, all chainlink polytopes, Euclidean John ellipsoids, or the radii of sections in higher dimensions. The Ehrhart-equivalence conclusion applies to integer levels only. The source initially uses the cyclic order \((6,4,5)\); cyclic coordinate rotation is a Euclidean isometry and produces \((4,5,6)\).

## Proof

Write \(H_t=\{x\in\mathbb R^3:\sum_i x_i=t\}\). The orthogonal projection of a coordinate normal to its direction space \(H_0\) has length \(u=\sqrt{2/3}\); the difference normal \(e_i-e_{i+1}\) already belongs to \(H_0\) and has length \(v=\sqrt2\). Therefore the closed intrinsic disk of radius \(r\ge0\) centered at \(x\in H_t\) lies in \(Q_t\) **if and only if**, for \(i=1,2,3\) cyclically,
\[
 L_i:\ -x_i+ur\le0,\qquad U_i:\ x_i+ur\le a_i,\qquad D_i:\ x_i-x_{i+1}+vr\le a_i-2.
\]
Thus the inradius is a three-variable linear program on \(H_t\), without any smoothness approximation or inferred facet assumptions.

Six nonnegative linear combinations of triples of these nine constraints give universal upper bounds. In the table below, the names in the middle column are the three constraints summed in order; the three positive coefficients are displayed in the same order. In every row, the left-hand normal sums to a multiple of \((1,1,1)\), so \(\sum x_i=t\) removes the center coordinates. The last column is the resulting bound on \(r\).

| Row | Triple | Positive dual weights | Bound |
| --- | --- | --- | --- |
| 1 | \(L_1,L_2,L_3\) | \(1/\sqrt6,1/\sqrt6,1/\sqrt6\) | \(t/\sqrt6\) |
| 2 | \(L_1,D_1,L_3\) | \(2c,c,c\) | \(c(t+2)\) |
| 3 | \(L_1,D_1,D_2\) | \(3d,2d,d\) | \(d(t+7)\) |
| 4 | \(D_1,D_2,D_3\) | \(1/(3\sqrt2),1/(3\sqrt2),1/(3\sqrt2)\) | \(3\sqrt2/2\) |
| 5 | \(U_1,U_2,D_3\) | \(2c,c,c\) | \(c(17-t)\) |
| 6 | \(U_1,U_2,U_3\) | \(1/\sqrt6,1/\sqrt6,1/\sqrt6\) | \((15-t)/\sqrt6\) |

To prove **attainability**, for each row solve its listed three constraints with equality jointly with \(\sum x_i=t\), obtaining a unique pair \((x(t),r(t))\). The resulting values of \(r(t)\) are exactly the six affine bounds. Direct substitution shows that all nine constraint slacks are nonnegative at the two endpoints of the corresponding interval of the claimed partition. All those slacks are affine in \(t\), hence nonnegative throughout each interval. The six pairwise affine comparisons at their endpoints show that the indicated bound is the smallest of the six throughout that interval. This exhausts every real \(t\in[0,15]\) and proves the radius formula, including simultaneous contacts at the change points. `verify.py` carries out **exact symbolic**, not sampled, algebraic sign and dual-identity checks for all six rows, both endpoints, and every one of the nine inequalities. This is a finite exhaustive verification of the explicitly displayed algebraic certificate, not an attempt to infer a continuum theorem from numerical sampling.

For the complementary-level claim, eliminate \(x_3=t-x_1-x_2\). Exact pairwise intersections of the nine boundary lines, retaining only points that satisfy every halfspace, give the following planar coordinate vertices, listed in cyclic order:
\[
\begin{split}
Q_6:\quad &(1,0),(2,0),(4,2),(3,3),(0,9/2),(0,2);\\
Q_9:\quad &(2,1),(5/2,1/2),(4,2),(4,4),(2,5),(0,5).
\end{split}
\]
Here each pair represents \((x_1,x_2)\) and determines \(x_3\) by the section equation. The induced metric for differences \((p,q)\) is \(2(p^2+pq+q^2)\); the intrinsic area element is \(\sqrt3\,dx_1dx_2\). Applying the Euclidean polygon edge-length formula and the shoelace formula to these **exhaustive** vertices yields six vertices each, common perimeter \(9(\sqrt2+\sqrt6)/2\), and common area \(43\sqrt3/4\). The algebraic difference of the inradii is positive because \(37^2\cdot6>63^2\cdot2\). Finally, the original chainlink Ehrhart theorem applies since the parameters are integral and \(2\ell=4\le\min(4,5,6)\), giving Ehrhart equivalence at the integer complementary levels six and nine.

## Verification

Run `python verify.py` after installing the dependency in `requirements.txt`. The executable recomputes all six dual coefficient identities, all six exact center solutions, the six endpoint minimum-envelope comparisons, all 108 endpoint-by-facet feasibility inequalities, and both complementary polygon vertex sets with their exact Euclidean perimeter and area. SymPy evaluates algebraic numbers exactly. The checker is an independent mechanical reconstruction of the finite certificate from the specified halfspaces; the mathematical proof is the duality and affine-interpolation argument above. The source paper's Ehrhart theorem is cited rather than independently reproved.

## Relationship to prior work

Kantarcı Oğuz, Özel, and Ravichandran defined chainlink polytopes and proved equality of the Ehrhart quasipolynomials of integer-level complementary sections. Their paper also exhibits nonisomorphic complementary sections at levels four and eleven of this particular polytope and studies full-polytope faces, vertices, and volume. It does not determine this six-phase intrinsic Euclidean inradius profile, or the distinct inradii of the equal-area/equiperimetric level-six and level-nine polygons. A separate indexed finding titled *Cyclic interval barriers determine the Euclidean inradius of every chainlink polytope* concerns **full chainlink polytopes**, not their affine height sections; an inradius of a section cannot generally be deduced from the inradius of the ambient body. Standard linear programming duality gives a method but not the present classified exact parameter thresholds or paired-polygon invariant comparison.

## Limitations

The result concerns one fixed, previously motivated chainlink parameter vector; it does not classify which other Ehrhart-equivalent polytope pairs exhibit metric divergence. No implication about GL-equidecomposability is claimed. The volume/Ehrhart equivalence is imported faithfully from primary literature; the new geometric identities are derived directly from the nine inequalities and exact vertex enumeration. The six-phase disk-radius law holds for real levels; Ehrhart quasipolynomials are asserted equal only at integer complementary levels. No independent external mathematical audit is claimed.

## References

1. Ezgi Kantarcı Oğuz, Cem Yalım Özel, Mohan Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (first public 2022-11-15), especially Theorem 1, Definition 3.1, and Section 6. https://arxiv.org/pdf/2211.08382
2. Mathematical Subject Classification 2020, 52B15 (symmetry properties of polytopes). https://msc2020.org/
