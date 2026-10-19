# Optimal identifying codes of the ternary affine-plane incidence graph form four Pappus components and an incidence cone

## Finding

Let \(\Pi=\operatorname{AG}(2,3)\) be the affine plane of order three, with nine points \(P\) and twelve lines \(L\), and let \(H\) be its point-line incidence (Levi) graph. A *closed-neighborhood identifying code* is \(C\subseteq V(H)\) such that the sets \(C\cap N_H[v]\), for all \(v\in V(H)\), are nonempty and pairwise distinct. The optimal size \(\gamma_{\mathrm{ID}}(H)=9\) follows already from the general degree bound of Karpovsky--Chakrabarty--Levitin, as recorded by Gravier et al.; the contributions here are the complete optimizer classification and the exact optimum-code exchange graph.

**Complete classification.** Precisely \(109\) nine-vertex identifying codes exist, with three disjoint types:

1. The full point set \(P\) (one code).
2. \((P\setminus\{p\})\cup\{\ell\}\), for a point \(p\) incident with a line \(\ell\) (\(36\) codes).
3. \((P\setminus T)\cup\mathcal{L}_d\), where \(T\) is a noncollinear triple of points and \(\mathcal{L}_d\) is the unique complete parallel class of three lines whose direction does not occur among the three joins of pairs of points of \(T\) (\(72\) codes).

There are exactly three orbits under the affine collineation group \(\operatorname{AGL}(2,3)\), with sizes \(1,36,72\).

**Exchange decomposition.** Let \(\mathcal E\) have these \(109\) optimal codes as vertices, with two adjacent exactly when one vertex of \(H\) is removed and another is inserted. If \(L(H)\) denotes the ordinary line graph of \(H\), \(K_1\vee L(H)\) its cone (one universal vertex joined to all vertices), and \(\mathsf{Pa}\) the eighteen-vertex Pappus graph, then
\[
\mathcal E\cong \bigl(K_1\vee L(H)\bigr)\;\sqcup\;4\mathsf{Pa}.
\]
The cone has \(37\) vertices, \(126\) edges, radius \(1\), and diameter \(2\). Each Pappus component has \(18\) vertices, \(27\) edges, radius and diameter \(4\). Thus the full exchange graph has \(109\) vertices, \(234\) edges, and five components.

## Assumptions and scope

All arithmetic is in \(\mathbb F_3\). Points are ordered pairs \((x,y)\in\mathbb F_3^2\). The twelve lines are the nine sets \(\{(x,mx+b):x\in\mathbb F_3\}\) for \(m,b\in\mathbb F_3\), and the three vertical lines \(\{(a,y):y\in\mathbb F_3\}\). The incidence graph has one vertex for every point and every line, with edges only for incidence. Identifying always uses *closed* neighborhoods and must separate *both* point and line vertices. The reconfiguration move preserves cardinality nine and the identifying-code property after each individual exchange. This is a theorem about this finite affine plane, not a claim for all orders.

## Proof

**1. The minimum is nine, and the optimizer list is exhaustive.** The incidence graph has \(21\) vertices and maximum degree \(4\). The established identifying-code degree bound \(\gamma_{\mathrm{ID}}(G)\ge 2|V(G)|/(\Delta(G)+1)\) gives \(\gamma_{\mathrm{ID}}(H)\ge\lceil42/5\rceil=9\). The nine points themselves identify every vertex: a point has its own singleton trace, while a line has its own three-point trace. Hence the minimum is nine. This minimum-value argument is **not claimed as new**.

To classify all minima, the finite complete enumeration in the supplied \(\texttt{verify.py}\) is a proof by exhaustive cases. It constructs the twelve lines from the displayed equations, then the exact twenty-one closed-neighborhood bitmasks \(N_i\). For a nine-element subset encoded by a bitmask \(s\), it tests
\[
\forall i:\ (s\mathbin{\&}N_i)\ne0,\qquad
\forall i<j:\ (s\mathbin{\&}N_i)\ne (s\mathbin{\&}N_j).
\]
It visits **all** \(\binom{21}{9}=293930\) nine-subsets, not a sample or a symmetry-restricted subfamily. A separate logically equivalent implementation verifies that each candidate meets all \(21\) nonempty-neighborhood constraints and all \(210\) pairwise symmetric-difference constraints. Both give exactly \(109\) identical nine-subsets. The script also checks all \(\binom{21}{8}=203490\) eight-subsets by both tests (none succeeds); this redundancy does not replace the prior general lower bound.

Independently of enumerating valid codes, the same script constructs the claimed geometric family: one full point set; \(9\cdot4=36\) incident point-line pairs; and the \(\binom93-12=72\) noncollinear triples, each possessing a unique unused fourth direction. These \(109\) masks are distinct and agree *setwise* with the complete enumeration. Therefore the three descriptions characterize every optimum, with no assumption about a guessed orbit or completeness of a search partition.

**2. The thirty-seven-vertex component.** Map \((P\setminus\{p\})\cup\{\ell\}\) to the incidence edge \(p\ell\) of \(H\). One-swap adjacency of two such codes occurs exactly when the incidences share point \(p\) or line \(\ell\). Thus their induced graph is \(L(H)\). The all-point code is adjacent to every one of these \(36\) codes. It is not adjacent to any third-type code because a single exchange cannot change the selected-point count from nine to six. This proves the cone description. As \(H\) has \(36\) edges, each joining a point of degree four to a line vertex of degree three, \(L(H)\) is five-regular on \(36\) vertices and has \(90\) edges. Coning adds \(36\) edges, giving \(126\). The apex is universal, and nonadjacent incidence edges exist, so radius and diameter are respectively one and two.

**3. The four Pappus components.** Third-type codes select the three lines of one complete parallel class; any single exchange preserving third type must keep that class fixed, because different complete classes are disjoint. After an affine coordinate change, write the class as \(y=0,1,2\). Its omitted noncollinear triple is uniquely
\[
T=\{(x_0,0),(x_1,1),(x_2,2)\},\qquad x_0+x_1+x_2\ne0 \quad\text{in }\mathbb F_3.
\]
There are \(27-9=18\) such triples per class. Two configurations within the class are adjacent precisely when one \(x_i\) changes, while the coordinate sum remains nonzero. The sums are \(1\) and \(2\); from a sum-one triple there are exactly three neighbors obtained by adding one to one coordinate. Hence the component is the bipartite graph with two copies \(A,B\) of \(\mathbb F_3^2\), whose edges are
\[
A(u,v)B(u,v),\quad A(u,v)B(u+1,v),\quad A(u,v)B(u,v+1).
\]
This is a standard bi-Cayley model of the Pappus graph. For a fully explicit incidence identification, put \(x=v-u\) and \(f(u,v)=-u^2-u-v^2-v-uv\) in \(\mathbb F_3\). Send \(A(u,v)\) to the point \((x,f(u,v))\), and \(B(u,v)\) to the nonvertical affine line \(y=xz+f(u,v)-x^2\) (here \(z\) is the varying first coordinate). These two maps are bijections onto nine points and the nine nonvertical lines, respectively, and direct substitution proves incidence exactly for the three displayed edge types. The resulting Levi graph is the Pappus graph. The two maps and all \(81\) point-line incidence tests are checked independently in \(\texttt{verify.py}\). Each component is connected, has \(18\) vertices and \(27\) edges, and direct all-source breadth-first search gives eccentricity four at every vertex.

**4. Orbit statement and completeness of exchange.** The group \(\operatorname{AGL}(2,3)\) has \(9\cdot|\operatorname{GL}(2,3)|=432\) elements. It is transitive on the set of points, flags, and noncollinear triangles. The structural descriptions therefore form orbits of sizes \(1,36,72\). Independently, the supplied checker constructs all \(432\) affine permutations and verifies those exact orbit sizes and every exchange edge. Its component calculation agrees with Steps 2 and 3.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3.10 or newer; only the standard library is needed. The program lists all \(203490\) eight-subsets and \(293930\) nine-subsets, using two exact identification predicates; constructs the three geometrical families; generates every one-swap edge; checks orbit sizes under all affine maps; checks the cone and the four Pappus coordinate models; and independently recomputes every vertex eccentricity. The recorded output in \(\texttt{verification_output.txt}\) is reproducible. No random sampling, numerical optimization, or conjectural generalization enters the proof.

## Relationship to prior work

The closed-neighborhood code concept dates to Karpovsky, Chakrabarty and Levitin (1998). Gravier, Parreau, Rottey, Storme and Vandomme (arXiv:1411.5275, first public 2014-11-19) explicitly state the general degree lower bound used here. Thus the inequality yielding minimum nine is established prior work, and this finding **does not** claim it as original. Their full paper studies vertex-transitive and strongly regular adjacency graphs, particularly generalized quadrangles, and does not classify the minimum codes of this irregular bipartite affine-plane incidence graph or their exchange adjacency.

Bousquet, Lagoutte, Li, Parreau and Thomassé (arXiv:1407.5833) give broad structural and approximation results for identifying codes in hereditary graph classes; those do not yield this exact \(109\)-code geometry or the Pappus-component decomposition. Foucaud et al. study identifying codes **of line graphs**, whereas the code problem here is on the original bipartite Levi graph; the line graph \(L(H)\) appears only in the *derived* exchange graph. Published incidence-graph constructions identify the underlying affine plane but supply no comparable optimum-code table in the materials inspected. The novel claim is confined to the complete optimizer structure and its exact reconfiguration graph.

## Limitations

The classification applies to the unique affine plane of order three, with closed-neighborhood identification and one-for-one vertex swaps of *minimum-cardinality* codes. It does not describe other affine orders, arbitrary code sizes, or open-neighborhood locating codes. Exhaustive finite enumeration constitutes a proof only because all relevant labeled subsets are covered; the checker is not an infinite-family argument. The originality comparison is based on the stated primary sources, targeted searches, and accessible published records, not a proof that no unpublished or unindexed equivalent computation exists. The work has not undergone an independent audit.

## References

1. S. Gravier, A. Parreau, S. Rottey, L. Storme, E. Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, Electronic Journal of Combinatorics 22(4) (2015), P4.6; preprint arXiv:1411.5275 (2014-11-19), https://arxiv.org/abs/1411.5275 .
2. N. Bousquet, A. Lagoutte, Z. Li, A. Parreau, S. Thomassé, *Identifying codes in hereditary classes of graphs and VC-dimension*, SIAM J. Discrete Math. 29 (2015), 2047-2064; preprint arXiv:1407.5833 (2014-07-22), https://arxiv.org/abs/1407.5833 .
3. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying Codes in Line Graphs*, J. Graph Theory 73 (2013), 425-448, https://doi.org/10.1002/jgt.21686 .
4. Magma Computational Algebra System, *Planes, Graphs and Codes*, documented affine-plane incidence example, https://docs.magma-maths.org/Geometry/FinitePlanes/graph-code.html .
