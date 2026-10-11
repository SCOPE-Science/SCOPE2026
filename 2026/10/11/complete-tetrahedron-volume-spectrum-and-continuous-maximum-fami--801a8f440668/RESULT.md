# Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(I\) be the regular icosahedron with edge length \(2\) and vertex set
\[
V=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
For any unordered four-element subset \(S\subset V\), put \(\delta(S)=6\operatorname{vol}_3(\operatorname{conv}S)\). The **entire volume spectrum** is

| \(\delta(S)\) | \(0\) | \(4\) | \(4\varphi\) | \(4\varphi^2\) | \(4\varphi^3\) |
|:--|--:|--:|--:|--:|--:|
| Number of subsets | 75 | 30 | 180 | 180 | 30 |

For **all** tetrahedra \(T\subseteq I\), including tetrahedra with vertices anywhere in \(I\),
\[
\max_{T\subseteq I}\operatorname{vol}_3(T)=\frac{2\varphi^3}{3},\qquad
\frac{\max_T\operatorname{vol}_3(T)}{\operatorname{vol}_3(I)}=\frac{\varphi}{10}.
\]
There are precisely 30 maximizing tetrahedra whose four vertices belong to \(V\). The full (uncountable) maximizing locus comprises 20 two-dimensional families, described precisely below.

## Assumptions and scope

Throughout, a tetrahedron is a nondegenerate convex hull of four points in Euclidean three-space. The containing regular icosahedron is the closed convex polytope \(I=\operatorname{conv}(V)\). The normalization is edge length \(2\); scaling all lengths by \(\lambda>0\) multiplies tetrahedral volumes by \(\lambda^3\) and leaves the sharp volume fraction unchanged. Distinct maximum tetrahedra are identified by their geometric vertex sets, independently of ordering.

For deterministic indexing, enumerate the 12 vertices as follows: for \((a,b)\) in lexicographic order \((-1,-1),(-1,1),(1,-1),(1,1)\), append \((0,a,b\varphi)\), \((a,b\varphi,0)\), then \((a\varphi,0,b)\). Indices in the family table start at zero. Thus every indexed coordinate and every exact certificate condition can be regenerated without additional input.

## Proof

**1. Exact ordered-volume computation.** In \(\mathbb Z[\varphi]\), use \(\varphi^2=\varphi+1\). Represent \(a+b\varphi\) by the integer pair \((a,b)\), multiply by
\[
(a,b)(c,d)=(ac+bd,ad+bc+bd),
\]
and compare signs exactly using \(2(a+b\varphi)=(2a+b)+b\sqrt5\). For each increasing four-tuple \(i<j<k<\ell\), calculate
\[
D_{ijkl}=\det(v_j-v_i,v_k-v_i,v_\ell-v_i).
\]
Enumerating the finite domain of exactly \(\binom{12}{4}=495\) choices by the included full exact checker gives precisely the five levels and multiplicities in the displayed table. The checker uses two separately coded determinant formulas and checks equality for every choice. It confirms that the largest absolute determinant is \(4\varphi^3=4+8\varphi\) and is attained at 30 quadruples. One explicit witness is the indexed vertex set \((0,1,4,11)\); its signed determinant is \(-4\varphi^3\). Hence the claimed maximum for vertex-supported tetrahedra is \(4\varphi^3/6\).

**2. Reduction from arbitrary contained tetrahedra.** The signed determinant \(D(x_0,x_1,x_2,x_3)=\det(x_1-x_0,x_2-x_0,x_3-x_0)\) is affine separately in each argument. Given \(x_i\in I\), write each point as a convex combination of elements of \(V\). The resulting signed determinant is a convex combination of signed four-vertex determinants. Thus \(|D(x_0,x_1,x_2,x_3)|\le4\varphi^3\); the witness proves sharpness. Equality for a chosen orientation requires **every** four-tuple appearing with positive coefficient in the product convex combination to have the same extremal signed determinant. This equality condition is crucial below.

**3. Exact combinatorial equality certificate.** Let \(\mathcal E\) be the 30 maximizing unordered vertex quadruples. For every unordered triple \(B\subset V\), form \(A(B)=\{v\in V\setminus B:B\cup\{v\}\in\mathcal E\}\). The checker exhaustively confirms
\[
\#\{B:|A(B)|=0\}=140,\quad
\#\{B:|A(B)|=1\}=60,\quad
\#\{B:|A(B)|=3\}=20.
\]
For each of the 20 triples with \(|A(B)|=3\), these three apex vertices form one of the 20 triangular facets of \(I\), and the 20 associated facets are all different. The three oriented determinants with the fixed ordered base \(B\) have the same sign and exactly the same value. Consequently, for every \(z\in F_B:=\operatorname{conv}A(B)\), \(\operatorname{conv}(B\cup\{z\})\) is maximizing.

To exclude **two or more** movable vertices, fix two vertex choices in the positive convex expansions of two of the tetrahedron's other vertices. Two distinct positive-support vertices for each of two movable arguments would yield four maximizing distinct vertex quadruples on a Cartesian \(2\times2\) grid, all containing that fixed vertex pair. The checker exhaustively verifies that no such grid exists in \(\mathcal E\). A repeated vertex would instead give a zero determinant, contradicting maximality. Hence every maximizing tetrahedron has at least three vertices in \(V\). If its fourth vertex is not in \(V\), its positive vertex expansion must lie entirely in \(A(B)\) for its fixed three-vertex base \(B\); the 0-, 1- and 3-element classification forces \(z\in F_B\). The same certificate confirms that each of the 30 vertex-supported maximizers appears in precisely two families. This proves the complete equality classification.

For direct reproduction, here is the full list \(B\mapsto A(B)\) of the 20 families, with triples presented as deterministic vertex indices:

| \(B\) | \(A(B)\) | \(B\) | \(A(B)\) |
|:---:|:---:|:---:|:---:|
| (0,3,4) | (8,10,11) | (0,3,10) | (2,4,5) |
| (0,4,11) | (1,3,5) | (0,5,10) | (3,7,11) |
| (0,5,11) | (4,6,10) | (1,4,8) | (3,9,11) |
| (1,4,11) | (0,6,8) | (1,6,9) | (7,8,11) |
| (1,6,11) | (4,5,9) | (1,8,9) | (2,4,6) |
| (2,3,8) | (4,9,10) | (2,3,10) | (0,7,8) |
| (2,7,9) | (6,8,10) | (2,7,10) | (3,5,9) |
| (2,8,9) | (1,3,7) | (3,4,8) | (0,1,2) |
| (5,6,7) | (9,10,11) | (5,6,11) | (0,1,7) |
| (5,7,10) | (0,2,6) | (6,7,9) | (1,2,5) |

**4. Volume fraction.** The standard volume formula for an edge-two regular icosahedron is \(\operatorname{vol}_3(I)=\frac{20}{3}\varphi^2\). It also follows by summing 20 origin-apex pyramids of equal triangular facets: each facet has area \(\sqrt3\), and the distance from the center to a face is \(\varphi^2/\sqrt3\). Thus \(\operatorname{vol}_3(I)=20\sqrt3(\varphi^2/\sqrt3)/3\). Dividing the sharp tetrahedral volume by this quantity gives \(\varphi/10\).

## Verification

The included self-contained `verify.py` uses only Python's standard library. Execute `python3 verify.py` from the directory holding the file. It validates all 495 four-vertex determinants using two separately implemented exact formulas in \(\mathbb Z[\varphi]\); exact sign comparison; the 20 actual supporting triangular facets; the 220 three-vertex base multiplicities; the 20 facet-to-base bijections; equality of the three oriented determinants on each facet; membership counts of all 30 maximizing quadruples; and the absence of any forbidden two-by-two grid. It additionally checks the numerical ordering of the exact levels at 60-digit decimal precision. Expected final line:

`VERIFY_OK vertex_sets=495 volume_levels=5 histogram=75,30,180,180,30 maxsets=30 families=20 facets=20 grids=0 witness=(0, 1, 4, 11)`

The finite configuration space is fully enumerated, **not sampled**. The universal claim for continuous tetrahedra is established by the separate multilinearity and equality arguments above; executing the checker alone without these arguments would not establish that conclusion.

## Relationship to prior work

Horváth and Lángi, *Maximum volume polytopes inscribed in the unit sphere* (first arXiv version 26 February 2014, `arXiv:1402.6496`), analyze volume maxima of spherical polytopes and the unconstrained regular-simplex extremum. Their circumsphere problem allows vertices anywhere on the sphere; its unconstrained bound does not determine this discrete golden-ratio spectrum or the movable-facet equality locus inside a fixed icosahedron. The paper's main dimension–vertex cases also concern polytopes with a prescribed total number of vertices, rather than the volume spectrum of tetrahedra within one given twelve-vertex polytope.

Conway and Torquato, *Packing, tiling, and covering with tetrahedra* (PNAS, 2006, DOI `10.1073/pnas.0601389103`), Appendix, calculate how 20 **regular** tetrahedra with a prescribed centroidal shared vertex fit into an icosahedron. That constrained packing problem is distinct from optimizing the volume of one arbitrary tetrahedron at arbitrary placement, and does not give the stated 30 vertex extremizers or 20 moving-apex families.

The displayed finite spectrum and continuous equality classification were not identified in the inspected works; absence from a small set of literature is not proof of historical priority. An older equivalent classification, particularly in regular-polytope geometry, remains possible.

## Limitations

The theorem concerns the regular Euclidean icosahedron and the volume functional; it does not classify maximal tetrahedra for distorted icosahedra, higher-dimensional polytopes, or other objectives such as surface area or minimal width. The proof of the finite classification depends on a complete, executable exact-arithmetic certificate whose bounded search is justified by the 12-vertex coordinates. Publication priority and independent checking of the argument have not been established. The spectrum includes zero determinants for coplanar quadruples; these are not nondegenerate tetrahedra.

## References

1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, `arXiv:1402.6496`, original public version dated 2014-02-26, https://arxiv.org/abs/1402.6496; full open text https://arxiv.org/html/1402.6496v3.
2. J. H. Conway and S. Torquato, *Packing, tiling, and covering with tetrahedra*, *Proceedings of the National Academy of Sciences* **103** (2006), 10612–10617, https://pmc.ncbi.nlm.nih.gov/articles/PMC1502280/, DOI `10.1073/pnas.0601389103`.
3. H. S. M. Coxeter, *Regular Polytopes*, Macmillan, 1963, historical geometrical background; complete priority comparison with this work was not performed.
