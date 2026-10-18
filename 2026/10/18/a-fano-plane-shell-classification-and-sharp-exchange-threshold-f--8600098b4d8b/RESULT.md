# A Fano-plane shell classification and sharp exchange threshold for Coxeter total domination

## Finding
Let \(G\) be the Coxeter graph, constructed as the disjointness graph on the \(28\) noncollinear three-point subsets of the Fano plane. Let \(S_j(x)=\{y\in V(G):d_G(x,y)=j\}\). A set \(T\) *totally dominates* \(G\) when every vertex, including every vertex in \(T\), has a neighbor in \(T\).

**Theorem.** The total domination number is \(\gamma_t(G)=10\), and the complete family of minimum total dominating sets is
\[
\mathcal T=\{T_x:x\in V(G)\},\qquad T_x=S_0(x)\cup S_1(x)\cup S_4(x).
\]
All \(28\) sets \(T_x\) are distinct. For distinct \(x,y\), let \(e(x,y)=|T_x\setminus T_y|=|T_y\setminus T_x|\) be the number of simultaneous selected-vertex replacements needed for a direct exchange. Then
\[
 e(x,y)=\begin{cases}6,&d_G(x,y)=1,\\9,&d_G(x,y)=2,\\7,&d_G(x,y)=3,\\4,&d_G(x,y)=4.\end{cases}
\]
Join two minimum sets when an exchange changes at most \(t\) selected vertices, with both endpoints minimum total dominating sets. For \(t\le3\) the exchange graph is edgeless, whereas at \(t=4\) it is canonically isomorphic to the distance-four graph of \(G\). It is connected, six-regular, has \(84\) edges, diameter \(3\), and the distance distribution \((1,6,15,6)\) from every vertex. The threshold of \(4\) is sharp.

## Assumptions and scope
Vertices of the Fano plane are the nonzero vectors \(1,\ldots,7\) of \(\mathbb F_2^3\) represented as three-bit integers; a three-subset \(\{a,b,c\}\) is a line exactly when \(a\oplus b\oplus c=0\). The graph vertices are all three-subsets that are **not** lines; two vertices are adjacent precisely when their three-subsets are disjoint. This is the standard 28-vertex Coxeter graph, not a Coxeter–Dynkin diagram and not the 30-vertex Tutte–Coxeter graph. There are \(42\) edges and every graph vertex has degree \(3\).

The distance shells use shortest-path distance in this graph. The exchange operation permits replacement of at most \(t\) selected vertices in one step; no condition is imposed on intermediate states within a simultaneous replacement. The theorem classifies every minimum set, not arbitrary nonminimum sets or subdivision parameters.

## Proof
**Lower bound.** Every selected vertex has three neighbors. Thus if \(T\) totally dominates all \(28\) vertices, then \(3|T|\ge28\), so \(|T|\ge10\).

**Explicit geometric upper bound.** The Coxeter intersection array is \(\{3,2,2,1;1,1,1,2\}\). Equivalently, its distance shells about each \(x\) have sizes \((1,3,6,12,6)\). For each shell index \(j\), the numbers of neighbors in shells \(j-1,j,j+1\), respectively, are \((0,0,3)\), \((1,0,2)\), \((1,0,2)\), \((1,1,1)\), and \((2,1,0)\). These data follow directly from the stated Fano-plane disjointness construction and are rechecked for every vertex by the accompanying geometry program. The set \(T_x=S_0(x)\cup S_1(x)\cup S_4(x)\) contains \(1+3+6=10\) vertices. Every vertex in shell \(0\) has a neighbor in shell \(1\); a vertex in shell \(1\) has one in shell \(0\); a vertex in shell \(2\) has one in shell \(1\); a vertex in shell \(3\) has one in shell \(4\); and a vertex in shell \(4\) has one **within** shell \(4\). Hence \(T_x\) totally dominates \(G\), proving \(\gamma_t(G)=10\).

For this set, the number \(|N_G(v)\cap T_x|\) equals \(3\) at \(v=x\) and \(1\) at every other vertex. Thus \(x\) is recoverable from \(T_x\), proving that the \(28\) constructed minima are distinct.

**Exhaustiveness (finite exact-cover lemma).** There are \(\binom{28}{10}=13{,}123{,}110\) labelled vertex subsets of size \(10\). The self-contained program `verification_enumerate.cpp` visits each one exactly once using the next-combination recurrence and tests total domination by taking the bitwise union of its ten open-neighborhood masks. Exactly \(28\) pass. This is independently checked by `verification_branch.py`, which branches on the smallest currently uncovered vertex and adds each of its three possible adjacent defenders. Its only nontrivial pruning rule is that \(u>3r\) uncovered vertices cannot be covered with \(r\) remaining selections. The branch search visits \(2{,}281\) nodes and returns the same \(28\) masks. The branching is complete because any eventual total dominating set must include a neighbor of the selected uncovered vertex. A set of fewer than ten vertices cannot totally dominate by the preceding lower bound. The two output mask lists are identical. Since the \(28\) explicitly constructed \(T_x\) are already among those minima, this verifies exhaustiveness without treating a random sample as proof.

**Exchange geometry.** Exhaustive pairwise intersections of the \(28\) explicit shell sets, checked independently by `verification_geometry.py`, give replacement counts \(6,9,7,4\) at respective graph distances \(1,2,3,4\). The pairwise histogram is \(42\) pairs of cost \(6\), \(84\) of cost \(9\), \(168\) of cost \(7\), and \(84\) of cost \(4\), accounting for all \(\binom{28}{2}=378\) pairs. Therefore the first possible nontrivial exchange threshold is \(t=4\). At that threshold the edges are exactly the pairs of graph vertices at distance four. A breadth-first search on this explicitly defined 28-vertex distance-four graph verifies connectedness, degree \(6\), and profile \((1,6,15,6)\) from each of its \(28\) vertices. In particular, its diameter is exactly \(3\).

## Verification
The Fano-plane vertex list is sorted lexicographically by its three nonzero integers. Bit \(i\) in a mask denotes the \(i\)-th vertex under this ordering. `certificate.json` records this list, every optimum mask and the full exchange-distance data.

Compile `verification_enumerate.cpp` with `c++ -std=c++17 -O2 verification_enumerate.cpp -o verify_exact` and run `./verify_exact`. Run `python3 verification_branch.py` and `python3 verification_geometry.py` with `certificate.json` in the working directory. The three embedded output files are `enumeration_output.txt`, `branch_output.txt` and `geometry_output.txt`. The C++ and Python branch programs independently derive all \(28\) minimum masks; the geometry program verifies each geometric shell condition and all \(378\) pairwise exchange costs. All checks passed when replayed from these exact embedded sources.

The finite exhaustiveness argument uses \(\binom{28}{10}\) possibilities, which is every candidate at the provably minimum size, and the independent branch search. No extrapolation to an infinite family is made.

## Relationship to prior work
The Coxeter graph and its intersection array are classical; see the Coxeter graph entry in Wolfram MathWorld and its cited graph-theory references. Total domination is a standard graph invariant, and earlier work including Henning (2000) and Henning–Yeo (2007) establishes general bounds rather than the optimum configuration classification here.

Jeyanthi and Hemalatha, *New results on total domination number and subdivision number of some families of graphs* (2016), Lemma 2.2, state that the Coxeter graph has total domination number \(14\), exhibiting a fourteen-vertex witness. Their displayed argument does not establish a sharp lower bound. The explicit ten-vertex total dominating sets here contradict that stated value, and the degree bound shows ten is sharp. The \(28\)-set shell classification and the sharp four-exchange connectivity threshold are additional, strictly stronger structural statements. This finding does not evaluate the paper's other graph families or subdivision claims.

A targeted comparison with mathematical research records, graph databases, alternate Fano-model terminology and available primary literature found no prior statement covering the complete shell and exchange classification. Such searches do not independently establish worldwide publication priority.

## Limitations
The theorem is specific to this finite Coxeter graph and the stated simultaneous exchange rule. The completeness claim depends on the transparent, finite enumerations and exact program source supplied here; the programs are evidence of a finite proof, not an external or independent formal certification. A published database or unindexed paper could contain an equivalent classification not located in the targeted search. Independent external scientific audit has not been performed.

## References
1. P. Jeyanthi and G. Hemalatha, *New results on total domination number and subdivision number of some families of graphs*, International Journal of Mathematics Trends and Technology (2016), Lemma 2.2. Author-uploaded full text: https://www.researchgate.net/publication/304170270_New_results_on_total_domination_number_and_subdivision_number_of_some_families_of_graphs .
2. Wolfram MathWorld, *Coxeter Graph*, https://mathworld.wolfram.com/CoxeterGraph.html .
3. M. A. Henning, *Graphs with large total domination number*, Journal of Graph Theory 35 (2000), 21–45. First available online 2000-08-09; https://doi.org/10.1002/1097-0118(200009)35:1%3C21::AID-JGT3%3E3.0.CO;2-F .
4. M. A. Henning and A. Yeo, *A New Upper Bound on the Total Domination Number of a Graph*, Electronic Journal of Combinatorics 14 (2007), R65, https://doi.org/10.37236/983 .
5. A. Godbole, J. Jamieson and W. Jamieson, *Maximum Number of Minimum Dominating and Minimum Total Dominating Sets*, arXiv:1308.3178 (2013), https://arxiv.org/abs/1308.3178 .
