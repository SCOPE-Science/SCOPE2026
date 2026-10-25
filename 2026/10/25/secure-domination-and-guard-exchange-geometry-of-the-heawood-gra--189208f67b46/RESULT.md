# Secure domination and guard-exchange geometry of the Heawood graph

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane. Its secure domination number is exactly \(\gamma_s(H)=6\). All \(84\) minimum secure dominating sets admit the following geometric description: choose a noncollinear triple of Fano points; among the seven Fano lines choose the unique line avoiding the triple and any two of the three lines meeting the triple in exactly one point. These are all the minimum sets, and they form one orbit under the natural \(\operatorname{GL}_3(\mathbb F_2)\) symmetry.

Join two minimum secure dominating sets if one selected vertex can be replaced by any unselected vertex without losing the secure-domination property. This *unrestricted one-vertex exchange graph* has \(84\) vertices, is connected and \(4\)-regular, has \(168\) edges, and has radius and diameter both equal to \(7\). From any minimum set its distance-layer sizes, at distances \(0\) through \(7\), are \((1,4,8,16,28,22,4,1)\).

## Assumptions and scope
The seven nonzero vectors of \(\mathbb F_2^3\) are points \(p_a\) and, separately, labels for the seven lines \(\ell_b\). Incidence means \(a\cdot b=0\) in \(\mathbb F_2\), where the dot product is the ordinary coordinate dot product. Vertices of \(H\) are the fourteen symbols \(p_a,\ell_b\), with edges exactly at incidences. This is the standard Fano-plane Levi graph; each vertex has degree three.

A set \(S\subseteq V(H)\) is *dominating* if \(N[v]\cap S\ne\varnothing\) for every vertex \(v\). It is *secure dominating* if it is dominating and for each \(u\notin S\) there exists an adjacent \(v\in S\) such that \((S\setminus\{v\})\cup\{u\}\) is dominating. This is one-defender, one-attack **ordinary secure domination**; it is not secure vertex-edge domination, simultaneous-move eternal domination, or a repeated-attack game. The exchange graph uses unrestricted replacement vertices, not an adjacency-constrained slide, and is defined **only on minimum secure sets**.

All statements concern this single fourteen-vertex graph. No assertion is made for larger projective planes or general cubic cages.

## Proof
**Exact finite lower bound and classification.** Label the fourteen vertices by integer positions \(0,\ldots,13\): positions \(a-1\) represent \(p_a\), and positions \(7+b-1\) represent \(\ell_b\), with \(1\le a,b\le7\) interpreted as nonzero three-bit vectors. For an integer mask \(s\), define \(\operatorname{Dom}(s)\) to mean
\[
\bigwedge_{w=0}^{13}\bigl(s\mathbin{\&}\operatorname{mask}(N[w])\ne0\bigr).
\]
Define \(\operatorname{Sec}(s)\) by \(\operatorname{Dom}(s)\) together with, for every unselected position \(u\), the condition
\[
\bigvee_{\substack{v\in N(u)\\v\text{ selected}}}
\operatorname{Dom}\!\bigl((s\setminus\{v\})\cup\{u\}\bigr).
\]
Here the set expressions are implemented as explicit bit deletions and insertions in `fano_secure_enum.py`; the formulas above specify the exact quantified property independently of the implementation.

There are exactly \(2^{14}=16384\) integer masks. The provided complete enumeration visits **every mask**, tests all fourteen domination conditions, and for each omitted vertex checks every adjacent selected defender. Its counts by secure-set size \(6,7,\ldots,14\) are respectively \((84,1444,2352,1862,987,364,91,14,1)\); no masks of cardinality below six pass. Among masks of size at most six, \(\operatorname{Sec}(s)\) is equivalent, *for every mask*, to the condition that \(s\) has exactly three point vertices, exactly three line vertices, and exactly two incidences between the chosen parts. All claims of nonexistence and exhaustiveness are therefore finite complete tests, not extrapolations from a range of graph orders. An independently coded C++17 test, `secure_fano_crosscheck.cpp`, constructs the Fano plane from the cyclic difference set \(\{0,1,3\}\subset\mathbb Z/7\mathbb Z\) and verifies the same predicate equivalence and full census, with separately implemented domination and defense tests.

**Geometric count and positive construction.** Three collinear points admit no line avoiding all three. Three noncollinear points form a triangle; its seven lines split into three two-point *sides*, three one-point *exclusive lines*, and one zero-point *avoiding line*. To select three lines and obtain exactly two incidences, one must take the avoiding line and exactly two of the exclusive lines. Conversely, the complete mask test shows every such six-set is secure. There are \(\binom73-7=28\) noncollinear point triples and three choices of the excluded exclusive line, giving exactly \(28\cdot3=84\) minima. A direct witness is \(S=\{p_1,p_2,p_4,\ell_3,\ell_5,\ell_7\}\). For its eight omitted vertices, legal defenders are respectively \(\ell_3,\ell_5,\ell_7,\ell_3,p_2,p_4,p_2,p_1\) for \(p_3,p_5,p_6,p_7,\ell_1,\ell_2,\ell_4,\ell_6\). The program checks each corresponding replacement dominates all fourteen vertices.

The symmetry group \(\operatorname{GL}_3(\mathbb F_2)\) maps points by \(a\mapsto Ta\) and line labels by \(b\mapsto(T^{-1})^{\mathsf T}b\), preserving incidence. It acts transitively on ordered bases of \(\mathbb F_2^3\), hence on noncollinear point triples with a distinguished excluded exclusive line. Therefore all \(84\) minima form one orbit. The provided Python certificate independently enumerates all \(168\) invertible binary matrices and confirms that the orbit of one minimum set has size \(84\).

**Exchange graph.** For a fixed selected point triple, its three admissible selected-line triples form a \(K_3\) under one-line replacement. Dually, for each fixed selected-line triple there are three admissible point triples forming a \(K_3\) under one-point replacement. Thus every configuration has two neighbours of each kind, giving degree four and \(84\cdot4/2=168\) edges. Both independent programs construct the complete adjacency list by checking that the two selected masks differ in exactly two bit positions. Breadth-first search from a representative returns distance layers \((1,4,8,16,28,22,4,1)\), whose sum is \(84\), proving connectedness and eccentricity seven for that representative. By the already proved transitivity, all vertices have eccentricity seven, hence both radius and diameter are seven. Both programs also independently run breadth-first search from *every* minimum configuration and confirm all eccentricities are seven.

## Verification
Run from the directory containing the provided standalone files:

```sh
python3 fano_secure_enum.py
c++ -std=c++17 -O2 secure_fano_crosscheck.cpp -o secure_fano_crosscheck
./secure_fano_crosscheck
```

The recorded UTF-8 outputs are `fano_secure_enum.out` and `secure_fano_crosscheck.out`. Their shared lines match exactly and include the complete cardinality distribution, the ordinary domination reference \(\gamma(H)=4\) (twenty-one minimum sets), the secure minimum and geometric classification, exchange edges, degree, distance levels, radius, and diameter. The first implementation additionally checks the full linear-symmetry orbit. Exhaustive enumeration is valid here because the domain has exactly \(2^{14}\) subsets; it would not by itself prove analogous assertions for arbitrarily larger incidence graphs.

## Relationship to prior work
Burger, de Villiers and van Vuuren (2013) introduce exact algorithms for the general secure domination number and define the same one-defender property. The accessible abstract describes general algorithms but contains no stated Fano-plane classification or optimal-exchange metric. Selected pages of their openly available scanned PDF were inspected; unchecked pages remain a specific comparison risk. Merouane and Chellali (2015) prove broad secure-domination bounds, including an upper bound by independence number for graphs of girth at least six; their accessible abstract does not give the present exact count or structural classification. Its full text was not available for inspection. Burger, de Villiers and van Vuuren (2015) investigate edge-removal stability, not the optimal-set exchange graph; its searchable full text contains no named Heawood theorem. Manrique, Ebadi and Ebrahimi (2015) study secure domination variants in *directed* graphs. A later Heawood-specific source by Sharmila (2024) concerns a distinctly defined *secure vertex-edge* domination invariant, not this one-step vertex secure-domination invariant.

The previously studied ordinary dominating sets of \(H\), or the general fact that many dominating configurations exist at size six, do not establish which of them survive every one-vertex attack, nor the exchange geometry of those that do. Mathematical-database searches and comparisons with accessible recorded claims did not reveal equivalent or stronger coverage, but unsuccessful searches are not proof of publication priority.

## Limitations
This is a finite, computer-assisted theorem for the specific Fano incidence graph. The complete enumeration is small and reproducible, and the geometric counting and orbit arguments give independent structural explanations, but there is no generalization to projective planes of arbitrary order. Incomplete full-text access to certain earlier papers and potentially unindexed finite tabulations leave a residual originality risk. No independent external scientific audit or publication-priority certification has been performed.

## References
1. A. P. Burger, A. P. de Villiers, J. H. van Vuuren, *Two Algorithms for Secure Graph Domination*, Journal of Combinatorial Mathematics and Combinatorial Computing 85 (2013), 321–339; publisher page https://combinatorialpress.com/jcmcc-articles/volume-085/two-algorithms-for-secure-graph-domination/ (dated 2013-05-31).
2. A. P. Burger, A. P. de Villiers, J. H. van Vuuren, *Edge stability in secure graph domination*, Discrete Mathematics & Theoretical Computer Science 17 (2015), 103–122, DOI: 10.46298/dmtcs.2120; open full text https://dmtcs.episciences.org/en/articles/2120/download.
3. H. B. Merouane, M. Chellali, *On Secure Domination in Graphs*, Information Processing Letters 115 (2015), 786–790, DOI: 10.1016/j.ipl.2015.05.006 (abstract available; full text not inspected).
4. M. Manrique, K. Ebadi, M. Ebrahimi, *Secure Domination in Digraphs*, arXiv:1503.04048 (first submitted 2015-03-13), https://arxiv.org/abs/1503.04048.
5. C. Ruby Sharmila, *Secure-Vertex-Edge Domination of Certain Named Special Graphs*, Communications on Applied Nonlinear Analysis 31(4s) (2024), DOI: 10.52783/cana.v31.950 (different invariant; relevant Heawood mention in accessible abstract/excerpts).
