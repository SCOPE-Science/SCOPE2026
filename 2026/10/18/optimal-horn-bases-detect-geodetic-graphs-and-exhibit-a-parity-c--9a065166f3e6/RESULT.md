# Optimal Horn bases detect geodetic graphs and exhibit a parity census on cycles

## Finding
Let \(G=(V,E)\) be a finite, nonempty, connected, simple graph, with shortest-path distance \(d_G\). An implicational basis \(\Sigma\) is a set of rules \(A\to B\), where \(A,B\subseteq V\) and \(B\ne\varnothing\). A set \(S\subseteq V\) satisfies a rule when \(A\subseteq S\Rightarrow B\subseteq S\). Say that \(\Sigma\) represents the **geodesic convexity** when its models are exactly the sets containing every vertex on every shortest path between any two of their vertices. The cost of a basis is
\[
\operatorname{wt}(\Sigma)=\sum_{(A\to B)\in\Sigma} (|A|+|B|).
\]
Write \(M(G)=|\{\{u,v\}\subseteq V:d_G(u,v)\ge2\}|\), and let \(\operatorname{OPT}(G)\) denote the minimum cost over all bases.

**Tightness theorem.** For every such graph,
\[
\operatorname{OPT}(G)\ge3M(G),\qquad
\operatorname{OPT}(G)=3M(G)\ \Longleftrightarrow\ G\text{ is geodetic},
\]
where geodetic means that every pair of vertices has exactly one shortest connecting path. If \(G\) is geodetic, *all* optimum bases are obtained independently by assigning, to each nonadjacent pair \(\{u,v\}\), exactly one internal vertex \(w_{uv}\) of its unique shortest path and using the rule \(\{u,v\}\to\{w_{uv}\}\). Therefore the exact number of distinct optimum bases is
\[
\mathcal N(G)=\prod_{\{u,v\}:d_G(u,v)\ge2}(d_G(u,v)-1).
\]
The empty product equals one.

**Cycle census.** For \(r\ge1\), the odd cycle \(C_{2r+1}\) has
\[
\operatorname{OPT}(C_{2r+1})=3(2r+1)(r-1),\qquad
\mathcal N(C_{2r+1})=((r-1)!)^{2r+1}.
\]
For \(r\ge2\), the even cycle \(C_{2r}\) has
\[
\operatorname{OPT}(C_{2r})=2r(3r-4),\qquad
\mathcal N(C_{2r})=((r-1)!)^{2r}.
\]
In an even cycle an optimum basis has exactly one rule for each nonadjacent pair: the consequent is a singleton for nonantipodal pairs, but has **two distinct vertices, one on each open semicircle**, for antipodal pairs. All such choices are optimum, independently across unordered pairs. The counting treats each rule as a set-valued implication, not as an ordered string or a sequence of unit Horn clauses.

## Assumptions and scope
The graph is undirected, finite, connected, loopless, and has no parallel edges. Geodesic convexity is defined by *all* shortest paths, even where shortest paths are nonunique. A rule is charged for each literal in the premise and in the consequent, counted without repetition. The basis may have arbitrary premise and consequent sizes, but all its rules must be valid for geodesic convexity. Adjacent pairs and singletons are already geodesically convex. Empty-antecedent rules with nontrivial conclusion are not valid. There is no assumption that the closure system is a convex geometry (anti-exchange may fail).

## Proof
**1. Every nonedge forces an implication and a cost of three.** Fix \(u,v\) with \(d_G(u,v)\ge2\). The closure of \(\{u,v\}\) contains at least one other vertex. As \(\varnothing\), \(\{u\}\), and \(\{v\}\) are closed, no valid nontrivial rule can fire on those proper subsets. Hence any basis must contain a rule with **premise exactly** \(\{u,v\}\) and conclusion containing an element outside \(\{u,v\}\). Distinct unordered nonadjacent pairs require distinct rules; every such rule costs at least \(2+1=3\). Consequently \(\operatorname{OPT}(G)\ge3M(G)\). If equality holds, the only rules are one per nonedge, with premise that pair and a single new conclusion. Validity forces the new vertex to lie strictly within its geodesic interval \(I_G(u,v)\).

**2. A unique geodesic makes every such basis sufficient.** Assume every pair has a unique shortest path. Choose arbitrarily one interior vertex \(w_{uv}\) on this path for every nonedge pair. The rules are sound because \(w_{uv}\in I_G(u,v)\). Let \(S\) be a set closed under the chosen rules. We show that \(I_G(u,v)\subseteq S\) whenever \(u,v\in S\), by strong induction on \(d_G(u,v)\). For distances zero and one this is immediate. For larger distance, the rule adds \(w_{uv}\) to \(S\). Both subpaths from \(u\) to \(w_{uv}\) and from \(w_{uv}\) to \(v\) are unique geodesics of smaller length, so their vertices belong to \(S\) by induction. Their union is the full unique \(u\)-to-\(v\) geodesic. Therefore \(S\) is geodesically convex. Soundness and completeness yield a basis of cost \(3M(G)\). Conversely, part 1 describes every optimum basis; there are exactly \(d_G(u,v)-1\) independent choices for each rule, giving \(\mathcal N(G)\).

**3. Any geodesic ambiguity makes the lower bound strict.** Suppose \(G\) is not geodetic. Choose a pair \(u,v\) of *minimum distance* \(\ell\ge2\) admitting two distinct shortest paths. Every pair at distance strictly less than \(\ell\) has a unique geodesic. Suppose a basis achieved \(3M(G)\). By part 1, its one rule on \(\{u,v\}\) has singleton conclusion \(w\) in \(I_G(u,v)\). Fix one shortest \(u\)-to-\(v\) path \(P\) through \(w\). Starting with \(\{u,v\}\), the rule adds \(w\). Thereafter, whenever the current set is contained in \(P\), all its nontrivial rules except the already-used pair \(\{u,v\}\) have premises formed by two vertices of \(P\) at distance strictly less than \(\ell\). Their unique shortest paths are subpaths of \(P\), so their conclusions remain in \(P\). Thus the entire rule closure stays in \(P\). But \(I_G(u,v)\) contains a vertex of another shortest path outside \(P\), contradicting the assumed basis. Hence the optimum exceeds \(3M(G)\).

**4. Even and odd cycles.** In \(C_{2r+1}\), every pair has a unique shortest path; for each distance \(d\in\{2,\ldots,r\}\) there are exactly \(2r+1\) unordered pairs at distance \(d\). Part 2 gives the stated optimum and product \(\prod_{d=2}^r(d-1)^{2r+1}=((r-1)!)^{2r+1}\).

In \(C_{2r}\), exactly the \(r\) antipodal pairs have two shortest paths, each of length \(r\), and every other pair has a unique shortest path. Any basis requires a rule per nonedge. For an antipodal pair \(\{u,v\}\), if no rule on this premise adds a vertex from one of the two open semicircles, then, starting with \(\{u,v\}\), all subsequent rules whose endpoints lie on the other semicircle remain there: any nonantipodal pair of vertices on that semicircle has its unique shortest path there. Hence both open semicircles must be hit by the conclusions of rules on \(\{u,v\}\). This costs at least four literals for an antipodal premise and at least three for any other nonedge premise. Conversely, give every nonantipodal pair a single interior consequence and every antipodal pair one rule with exactly two consequences, one from each open semicircle. By induction along each shorter arc, every rule-closed set contains each complete geodesic interval, so this is a basis meeting the lower bound \(3M(C_{2r})+r\), where \(M(C_{2r})=r(2r-3)\). The equality case forces precisely the displayed form. Each of the \(2r\) pairs at distance \(d\in\{2,\ldots,r-1\}\) has \(d-1\) choices, and each of the \(r\) antipodal pairs has \((r-1)^2\) choices. The product is \(((r-1)!)^{2r}\).

## Verification
The standalone script `verify.py` independently calculates graph distances, all geodesic intervals, fixed points of the full shortest-path closure, and fixed points of each candidate Horn rule set. It exhaustively checks all optimum choices for cycles through seven vertices and deterministically samples further optimum choices for cycles with eight through ten vertices. It tests every subset of vertices for every sampled basis. It also exhaustively considers all connected labelled graphs on two through five vertices, checking geodetic cases against the explicit construction and nongeodetic cases against a minimal-distance ambiguous pair. Running `python3 verify.py` returns:

`VERIFY_OK cycles_bases=231 cycle_subsets=42040 all_connected_labelled_graphs=771 geodetic=357 nongeodetic=414 graph_subsets=21672`

The computed optimum costs for cycle sizes three through ten are respectively \(0,8,15,30,42,64,81,110\), matching the proved formula. These finite computations do not establish the universal statements by themselves; the proofs above do.

## Relationship to prior work
Bichoupan's *Complexity Results for Implication Bases of Convex Geometries* (arXiv:2211.08524, 2022), in its introduction and Theorem 3, formulates literal-count optimum bases and proves general NP-hardness for convex geometries; it does not supply a graph-geodesic optimum-cost characterization or a parity-dependent count of all optimum bases. Chepoi's *Separation axiom \(S_3\) for geodesic convexity in graphs* (arXiv:2405.07512, 2024), especially §4.3.1, treats implicational representations as input to semispace enumeration but does not determine optimum Horn bases. The 2026 paper *Characterizing the optimum bases of a convex geometry using quasi-closed hypergraphs* (arXiv:2603.14615) does provide a broader optimum-basis method for **convex geometries**, including order-convex subsets of posets; the present cycle systems need not satisfy anti-exchange. For example \(\{0,1\}\subset C_4\) is closed, while adding either vertex \(2\) or \(3\) forces the other, so \(C_4\)'s geodesic closure fails anti-exchange. The theorem here distinguishes geodetic graphs by optimum cost and counts optimum bases on both parity classes of graph cycles, outside that convex-geometry-only coverage. No categorical claim of publication priority is made.

## Limitations
The tightness theorem is for connected simple graphs and the stated literal-weight cost, not arbitrary weighted constraints or prime-CNF-length conventions. The factorial formulas count labelled-vertex bases, not orbits under graph automorphisms. The theorem does not determine optimum costs on arbitrary nongeodetic graphs beyond the strict lower bound; the exact nongeodetic calculation is for even cycles. The available full-text comparison is not a proof that the result was never previously published under another terminology, such as transit-function bases or graph betweenness Horn compression. No independent mathematical audit has been conducted.

## References
1. T. Bichoupan, *Complexity Results for Implication Bases of Convex Geometries*, arXiv:2211.08524v1, first posted 2022-11-15, https://arxiv.org/abs/2211.08524.
2. V. Chepoi, *Separation axiom \(S_3\) for geodesic convexity in graphs*, arXiv:2405.07512, first posted 2024-05-13, https://arxiv.org/abs/2405.07512.
3. A. Meunier, L. Nourine, S. Vilmin, *Characterizing the optimum bases of a convex geometry using quasi-closed hypergraphs*, arXiv:2603.14615, 2026, https://arxiv.org/abs/2603.14615.
