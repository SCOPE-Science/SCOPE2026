# Degree-factorized synchronization of three-color cyclic dynamics on line graphs of pseudotrees

## Finding

Let \(H\) be a finite connected simple graph with at least one edge and cyclomatic number at most one, let \(L(H)\) be its simple line graph, and put \(d_v=\deg_H(v)\). Every vertex of \(L(H)\) initially receives one of three labelled colors, and evolves by the synchronous successor-contact cyclic cellular automaton (CCA). Write \(S(H)\) for the number of initial colorings eventually reaching a single uniform color.

**Tree case.** For every tree \(H\),
\[
 S(H)=3\prod_{v\in V(H)}(2^{d_v}-1).
\]
Among trees having exactly \(m\ge2\) edges, this gives the sharp bounds
\[
 3(2^m-1)\le S(H)\le 3^m.
\]
For \(m\ge3\), the lower equality holds precisely for the star \(K_{1,m}\), and the upper equality precisely for the path \(P_{m+1}\).

**Unicyclic case.** If \(H\) has a unique simple cycle \(C\) of length \(\ell\ge3\), define \(r_v=d_v-2\) for \(v\in V(C)\). Then
\[
 S(H)=3\left(\prod_{v\notin V(C)}(2^{d_v}-1)\right)
 [z^0]\prod_{v\in V(C)}
 \left((2^{r_v+1}-1)+2^{r_v}(z+z^{-1})\right).
\]
The coefficient \([z^0]\) means the constant Laurent coefficient. It can be evaluated by an elementary integer dynamic program in \(O(|V(H)|+\ell^2)\) arithmetic operations (no enumeration of \(3^{|E(H)|}\) colorings). Consequently, the count for unicyclic \(H\) depends only on the multiset of degrees on the cycle and the multiset of degrees outside it, not on their cyclic order or the arrangement of attached trees. Subdivision of any off-cycle bridge multiplies \(S(H)\) by three and therefore **leaves the synchronization probability unchanged**.

These formulas concern exact synchronized **initial configurations**, not the number of eventual uniform fixed configurations (which is three). The cycle criterion and finite-graph synchronization theorem used below were previously established; the degree-factorization, fast evaluation, and resulting structural invariances are the contribution assessed here.

## Assumptions and scope

A vertex of \(L(H)\) represents an edge \(e\) of \(H\); two such vertices are adjacent if the original edges share an endpoint. Let \(x_t(e)\in\mathbb Z/3\mathbb Z\). The synchronous update is
\[
 x_{t+1}(e)=\begin{cases}
 x_t(e)+1\pmod3,&\text{if some neighbor has color }x_t(e)+1\pmod3,\\
 x_t(e),&\text{otherwise.}
 \end{cases}
\]
No proper-edge-coloring restriction is imposed. Vertices and edges are labelled; all \(3^{|E(H)|}\) initial colorings are distinct. A synchronized trajectory is eventually monochromatic on the connected line graph. The tree formula assumes \(|E(H)|\ge1\); the unicyclic formula assumes a simple cycle, hence \(\ell\ge3\). Graphs with two or more independent cycles are not covered.

For a directed adjacent pair \(e,f\) in \(L(H)\), define the signed difference \(\delta_x(e,f)\in\{-1,0,1\}\) as the representative of \(x(f)-x(e)\pmod3\). For each directed cycle \(\gamma\), its winding is the **integer** sum \(\sum_{(e,f)\in\gamma}\delta_x(e,f)\), not merely the sum modulo three.

## Proof

**1. Dynamical obstruction.** For any finite connected graph under three-color CCA, a coloring synchronizes if and only if every directed cycle has zero integer winding; this is the published irrotationality theorem [1, Theorem 3]. One can also verify its mechanism directly. If a vertex advances, denote its increment by \(\eta_e\in\{0,1\}\). On adjacent vertices, the signed differences obey
\[
 \delta_{x_{t+1}}(e,f)=\delta_{x_t}(e,f)+\eta_f-\eta_e.
\]
Indeed, if the old difference is \(1\), the lower-colored vertex must advance, and if it is \(-1\), the other must advance; for difference zero either increment is possible. Thus integer winding is conserved. Conversely, zero winding makes the signed difference an integer gradient \(h(f)-h(e)\). The update becomes an integer height update: a height increases by one if an adjacent height exceeds it by one. Adjacent heights remain at distance at most one. The set of sites at the initial maximum height expands by at least one graph edge each update, so after at most the diameter every site has reached that maximum and colors agree. This establishes the criterion in the finite setting used here.

**2. Line-graph local and global conditions.** For any vertex \(v\) of \(H\), its incident edges form a clique in \(L(H)\). All triangles in this clique have zero winding exactly when the colors on these incident edges occupy at most two of the three colors: three distinct colors yield a triangle winding \(3\) or \(-3\), whereas a one- or two-color clique admits an integer height lift. For a tree \(H\), the incident-edge cliques are glued at their shared single edge-vertices in a tree-shaped incidence pattern. One may align their integer height lifts successively, giving a global lift. Thus the no-three-colors-at-one-vertex condition is sufficient as well as necessary.

For unicyclic \(H\), gluing the clique lifts along a spanning tree leaves precisely one compatibility equation around the unique original cycle. Write the successive cycle edges as \(e_1,\ldots,e_\ell\); at their common original vertices let \(\Delta_i=\delta_x(e_{i-1},e_i)\in\{-1,0,1\}\), with cyclic indexing. The remaining compatibility condition is the integer equality \(\sum_i\Delta_i=0\). Equivalently: the coloring synchronizes exactly when every incident-edge clique uses at most two colors **and** this single winding is zero. This covers the case \(\ell=3\), when the base cycle itself produces a line-graph triangle.

**3. Tree enumeration.** Root a tree at any vertex of degree \(d\). The \(d\) incident edge colors may use at most two colors, which gives \(3(2^d-1)\) choices: three choices of a missing color, subtracting the extra double counts of monochromatic assignments. At each nonroot vertex \(v\), the parent-edge color is fixed, and each of the \(d_v-1\) child-edge colors must avoid using both of the other colors. There are
\[
 2\cdot2^{d_v-1}-1=2^{d_v}-1
\]
choices. Every descendant subtree has the same number of admissible completions for each prescribed parent color by global color-rotation symmetry. Multiplying these conditional counts proves the tree formula.

**4. Unicyclic enumeration.** Remove the cycle edges. All remaining parts are rooted trees attached to cycle vertices. For each vertex outside the cycle, conditional on its parent-edge color, the multiplier is \(2^{d_v}-1\), exactly as above. At a cycle vertex \(v\), there are \(r_v=d_v-2\) off-cycle child edges. If its two cycle edges have the same color, their extension count is \(a_v=2^{r_v+1}-1\). If those two cycle edges differ, their extension count is \(b_v=2^{r_v}\). Fixing the first cycle-edge color gives three choices. Advancing around the cycle, a transition of signed color difference \(\Delta_i\) has weight \(a_v\) when \(\Delta_i=0\), and weight \(b_v\) when \(\Delta_i=1\) or \(-1\). The zero-winding requirement is exactly \(\sum_i\Delta_i=0\); it simultaneously ensures closure in \(\mathbb Z/3\mathbb Z\). Therefore the weighted number of transition sequences is the indicated Laurent constant term, with factor three for the initial color and the independent off-cycle factors. Multiplication of all \(\ell\) three-term Laurent polynomials using coefficients supported between \(-\ell\) and \(\ell\) takes \(O(\ell^2)\) integer additions and multiplications.

**5. Degree invariance, bridge subdivision, and extrema.** The unicyclic product is commutative, so only the two specified degree multisets are relevant. Subdividing an off-cycle edge inserts a noncycle vertex of degree two; its new factor is \(2^2-1=3\), while other degrees and cycle weights stay unchanged. The total number of initial states also triples.

For the tree bounds, set \(f(d)=2^d-1\). The adjacent ratio \(f(d+1)/f(d)=2+1/(2^d-1)\) strictly decreases with \(d\). Thus transferring one unit of degree from a larger positive degree to a smaller one (when they differ by at least two) strictly increases \(\prod_v f(d_v)\). Positive tree degree sequences sum to \(2m\), and both the star sequence \((m,1,\ldots,1)\) and the path sequence \((2,\ldots,2,1,1)\) are realizable. Repeated balancing, or equivalently majorization, proves that the former uniquely minimizes and the latter uniquely maximizes the product for \(m\ge3\); their formulas yield the asserted bounds.

## Verification

Two separately implemented exhaustive simulators check the full synchronous update, not just the winding criterion. Run `python3 verify/spot_checks.py` for every labelled connected tree or unicyclic simple graph on at most five vertices, and `c++ -std=c++17 -O2 verify/labelled_graphs.cpp -o /tmp/line_cycle_check && /tmp/line_cycle_check` for all such labelled graphs on at most six vertices. Their exact recorded outputs are in `verify/spot_checks_output.txt` and `verify/labelled_graphs_output.txt`. The C++ program reports 5,339 graphs and 3,048,843 labelled initial configurations; the Python program reports 383 graphs and 65,775 configurations. A separate non-independent check using the unlabelled graph atlas through seven vertices (78 graphs, 92,838 initial configurations) agreed. These are finite tests; the all-size conclusion follows from the proof.

As a further structural check, two simple unicyclic graphs with degree multiset \(\{1,1,2,2,3,3\}\), unique cycle of length three, and cycle-degree multisets \(\{2,2,3\}\) versus \(\{2,3,3\}\) have respective synchronization counts 357 and 369. This illustrates why the **cycle/noncycle degree partition** is necessary: the total degree multiset and cycle length alone do not determine the count.

## Relationship to prior work

Gravner, Lyu, and Sivakoff [1] established the general finite-graph synchronization/irrotationality equivalence, which is explicitly used and not claimed as new. General exact cycle-winding summation methods already determine synchronization populations in principle for arbitrary finite graphs; the specialization here is distinguished by a closed multiplicative degree formula, one-variable constant term, quadratic-time exact integer evaluation, and sharp tree extrema. The central-trinomial coefficient count of a bare cycle is a known special case, not a claimed discovery.

Cutler and Radcliffe [2] study extremal counts for graph homomorphisms into the looped three-vertex path (the Widom–Rowlinson model). That is not the local three-color no-rainbow constraint coupled to zero integer winding used here. Zhang [3] studies additive modular All-Colors update rules on trees and unicyclic graphs, which are not successor-contact CCA. A line-graph-specific factorization matching this statement was not identified in the inspected sources; an unindexed earlier treatment remains possible.

## Limitations

The result does not classify recurrent non-synchronizing orbits or transient-time distributions. The degree-factorized formula is restricted to trees and connected unicyclic base graphs; graphs with two independent cycles generally have coupled winding constraints and are outside its scope. The exact formula and extremal conclusions are proved; computational checks alone do not establish the infinite-family theorem. Some older literature was accessible only through abstracts, so historical novelty is subject to further independent literature review.

## References

[1] J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first publicly posted 2016-10-24, Theorem 3 and Section 4. https://arxiv.org/html/1610.07320v1

[2] J. Cutler and A. J. Radcliffe, *Extremal graphs for homomorphisms*, Journal of Graph Theory **67** (2011), 261–284, DOI:10.1002/jgt.20530. https://doi.org/10.1002/jgt.20530

[3] *Solutions to All-Colors Problem on Graph Cellular Automata*, Complexity (2019), article 3164692, DOI:10.1155/2019/3164692. https://doi.org/10.1155/2019/3164692
