# Complete volume spectrum and Bernoulli-thinning law of a regular icosahedron

## Finding

Let \(\varphi=(1+\sqrt{5})/2\) and let \(I\subset\mathbb R^3\) be the regular icosahedron of edge length \(2\) whose twelve vertices are all sign choices of the coordinate patterns \((0,1,\varphi)\), \((1,\varphi,0)\), and \((\varphi,0,1)\). For every subset \(S\) of these vertices define \(V(S)=\operatorname{Vol}_3(\operatorname{conv}S)\), taking \(V(S)=0\) for affine dimension below three.

Among all \(2^{12}=4096\) subsets there are **exactly 29 distinct volume values, including zero**. Every volume has the form \((a+b\varphi)/6\) with nonnegative integers \(a,b\), in fact both multiples of four. The following table is the complete joint census of retained vertex count and volume: an entry \((a,b;c)\) means that exactly \(c\) subsets of cardinality \(k\) have volume \((a+b\varphi)/6\). For \(k=0,1,2,3\), all \(\binom{12}{k}\) subsets have zero volume.

| \(k\) | Six-volume pairs and multiplicities \((a,b;c)\) |
|---:|---|
| 4 | \((0,0;75)\), \((4,0;30)\), \((0,4;180)\), \((4,4;180)\), \((4,8;30)\) |
| 5 | \((0,0;12)\), \((4,4;60)\), \((0,8;60)\), \((4,8;360)\), \((8,8;120)\), \((4,12;60)\), \((8,12;120)\) |
| 6 | \((8,4;12)\), \((4,12;90)\), \((0,16;10)\), \((8,12;350)\), \((4,16;30)\), \((8,16;260)\), \((12,16;132)\), \((16,16;40)\) |
| 7 | \((8,16;60)\), \((12,16;120)\), \((8,20;120)\), \((12,20;300)\), \((16,20;180)\), \((20,20;12)\) |
| 8 | \((16,20;30)\), \((12,24;90)\), \((16,24;255)\), \((20,24;120)\) |
| 9 | \((16,28;20)\), \((20,28;140)\), \((24,28;60)\) |
| 10 | \((24,32;36)\), \((28,32;30)\) |
| 11 | \((32,36;12)\) |
| 12 | \((40,40;1)\) |

Independently retain each vertex with the same probability \(p\in[0,1]\), and let \(V_p\) be the volume of the resulting hull (zero when its dimension is less than three). The displayed census specifies its entire law:
\[
 \Pr\!\left(V_p=\frac{a+b\varphi}{6}\right)
 =\sum_{k=0}^{12} c_{k,a,b}p^k(1-p)^{12-k},
\]
where all unspecified census coefficients \(c_{k,a,b}\) are zero. Its expectation is the explicit exact polynomial
\[
 \boxed{\mathbb E[V_p]=\frac16\sum_{k=4}^{12}(A_k+B_k\varphi)p^k(1-p)^{12-k}.}
\]

| \(k\) | \(A_k\) | \(B_k\) |
|---:|---:|---:|
| 4 | 960 | 1680 |
| 5 | 3840 | 6720 |
| 6 | 7680 | 12880 |
| 7 | 9600 | 15120 |
| 8 | 8040 | 11760 |
| 9 | 4560 | 6160 |
| 10 | 1704 | 2112 |
| 11 | 384 | 432 |
| 12 | 40 | 40 |

The exceptional lower-dimensional subsets have an exact geometric description: the twelve five-vertex planar subsets are precisely the five-neighbor rings of individual icosahedral vertices; the 75 planar four-vertex subsets are the 60 four-subsets of those rings and the 15 unions of two antipodal vertex pairs. Consequently **every subset of at least six vertices spans three-dimensional space**, and
\[
 \Pr(V_p=0)=\sum_{k=0}^{3}\binom{12}{k}p^k(1-p)^{12-k}
       +75p^4(1-p)^8+12p^5(1-p)^7.
\]
At \(p=1/2\), the three-dimensionality probability is \(3710/4096\) and
\[
 \mathbb E[V_{1/2}]=\frac{4601+7113\varphi}{3072},\qquad
 \frac{\mathbb E[V_{1/2}]}{\operatorname{Vol}(I)}
       =\frac{2089+2512\varphi}{20480}.
\]

## Assumptions and scope

All 4096 subsets of twelve **fixed** icosahedral vertices are included; repetitions are not allowed, and the empty set has volume zero by convention. Only ordinary Euclidean three-volume is used. The random model uses independent Bernoulli retention with a common parameter \(p\); the deterministic census holds without any probability assumption. Scaling all edge lengths from \(2\) to \(\ell>0\) scales every listed volume by \((\ell/2)^3\). The theorem concerns the full finite set of vertex-induced convex subpolytopes, not continuously sampled points on a surface.

## Proof

**Exact coordinate field.** Work in the ordered quadratic field \(\mathbb Q(\varphi)\) with the relation \(\varphi^2=\varphi+1\). Represent \(a+b\varphi\) by the integer pair \((a,b)\), so that addition, multiplication, determinants, and sign comparisons are exact. In mixed-sign cases the sign reduces to that of the integer \(a^2+ab-b^2\), with the inequality reversed when the \(\varphi\)-coefficient is positive and the integer part negative. Irrationality of \(\varphi\) eliminates nonzero equality ambiguities.

**The exhaustive facet certificate.** Enumerate all masks \(m=0,\ldots,4095\). For the associated subset, first check all four-point affine determinants: if all vanish, its volume is zero. Otherwise, every facet of its three-dimensional convex hull has three affinely independent selected vertices. For each triple, form its plane normal using an exact cross product. It is a supporting facet plane exactly when all other selected vertices have signed dot products of one weak sign. Group equal facets by their complete sets of zero-sign vertices.

The arithmetic mean of each facet's vertices lies strictly inside its convex polygon. Thus its vertices can be ordered cyclically by their directions from that mean. The supplied checker sorts using **exact** half-plane and orientation comparisons in \(\mathbb Q(\varphi)\), and checks that all resulting oriented turns are strictly positive. Triangulating each outward-oriented facet gives the exact divergence-theorem volume identity
\[
 6V(S)=\sum_{F}\sum_{(i,j,k)\in\mathcal T(F)}
                  \det(v_i,v_j,v_k),
\]
where \(\mathcal T(F)\) is the oriented fan triangulation of facet \(F\). This identity is valid even when the origin lies outside the selected hull.

The exhaustive loop performs these operations on each of the \(4096\) masks with exact field arithmetic. Counting returned integer coefficient pairs produces the complete table above, whose multiplicities sum to \(\binom{12}{k}\) at each cardinality. It finds 29 distinct pairs, and exact positive volumes for all masks of cardinality at least six. The auxiliary exact checks identify all twelve planar five-sets as the five-neighbor rings and all planar four-sets as described above. These are finite exhaustive claims with a fully provided verifier; no sampling or heuristic cutoff is used.

**Probability laws.** A particular subset of cardinality \(k\) occurs with probability \(p^k(1-p)^{12-k}\). Summing over the census therefore proves the full mass function and the expectation polynomial. The zero-volume coefficient counts prove the displayed dimension probability. The values at \(p=1/2\) result from substituting into the exact integer coefficients; the full icosahedron has volume \(20(1+\varphi)/3\).

## Verification

Run `python icosa_exact.py` next to `volume_spectrum.json` using Python 3. The script enumerates all 4096 vertex masks from first principles, checks exact supporting facets and triangle turns, independently regenerates all census coefficients and checks every published row against the supplied table. It also checks the 12 planar neighbor rings, 15 antipodal-pair planes, expected subset multiplicities, and exact 29-level spectrum. The successful output terminates with `ALL_EXACT_4096_SUBPOLYTOPE_CHECKS_PASSED`.

As an independent algorithmic cross-check, `python crosscheck_numeric.py` (with `requirements-numeric.txt`) compares all 4096 exact volumes to SciPy/Qhull's independently constructed convex hulls. The performed run found zero discrepancies above \(10^{-10}\) and maximum absolute error \(1.07\times10^{-14}\). The exact proof does not depend on this floating-point check.

## Relationship to prior work

Newman's *Doubly random polytopes* (first public preprint June 12, 2020) treats independent vertex retention as a general random-polytope operation and analyzes large random circumscribed polytopes; it does not give this fixed icosahedron's finite volume spectrum. The prior published *Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron* gives all five possible **four-vertex** volume levels, which agree with the fourth row here; that layer is not claimed as new. Its four-vertex information does not alone determine the incidences, facet triangulations, or volumes of five-through-twelve-vertex hulls. Jacobson's 2026 work on progressive convex-hull simplification considers a related but different optimization problem involving removal of facet constraints and does not state the Bernoulli vertex-subset distribution. The novelty claim is the **full twelve-layer volume census and induced probability law**, not the general convex-hull algorithm, the pre-existing tetrahedral row, or the general vertex-thinning model.

## Limitations

This is a complete **finite** classification for one classical vertex configuration; it does not assert new complexity bounds or a higher-dimensional theorem. All labels are fixed and the Bernoulli parameters are equal; arbitrary unequal retention probabilities are recoverable from the individual-mask algorithm but are not tabulated. This same-source and literature comparison does not establish historical priority conclusively. In particular, the complete text of the published tetrahedron-spectrum record was inaccessible, although its detailed public synopsis concerns precisely four-vertex sets. Independent mathematical review has not been performed.

## References

1. Andrew Newman, *Doubly random polytopes*, arXiv:2006.07000 (initial version June 12, 2020); *Random Structures & Algorithms* 61 (2022), DOI 10.1002/rsa.21059. https://arxiv.org/abs/2006.07000 and https://doi.org/10.1002/rsa.21059.
2. *Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron* (published mathematical record, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-tetrahedron-volume-spectrum-and-continuous-maximum-fami--801a8f440668.
3. Alec Jacobson, *Progressive Convex Hull Simplification* (August 13, 2026), DOI 10.1111/cgf.70518, https://doi.org/10.1111/cgf.70518.
4. *Regular icosahedron*, standard coordinate and volume formulas, https://en.wikipedia.org/wiki/Regular_icosahedron.
