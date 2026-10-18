# Three colours detect every bicyclic obstruction to robust dependence splitting

## Finding
Let \(X\) and \(Y\) be finite nonempty, disjointly tagged attribute domains, and let \(G\subseteq X\times Y\) be an arbitrary simple bipartite graph (isolated domain values allowed). For a nonempty finite set \(C\) and a function \(c:G\to C\), form the *functional team* \(T_c=\{(x,y,c(x,y)):(x,y)\in G\}\). Write \(\Phi=\operatorname{dep}(x,z)\vee\operatorname{dep}(y,z)\), with lax splitting disjunction. Call \(G\) robust for \(C\) if \(T_c\models\Phi\) for **every** edge coloring \(c\).

**Theorem.** If \(|C|=1\) or \(|C|=2\), every finite simple bipartite graph is robust for \(C\). If \(|C|\ge3\), then \(G\) is robust for \(C\) exactly when every connected component has at most one cycle (equivalently, \(G\) is a pseudoforest). For every non-pseudoforest graph a falsifying coloring exists using just three colors. Thus the alphabet transition from two to three is sharp, and robust validity for at least three colors is decidable by a linear-time graph traversal.

## Assumptions and scope
A dependence atom \(\operatorname{dep}(a,b)\) holds of a team when assignments agreeing on \(a\) also agree on \(b\). Lax disjunction means \(T\models\psi\vee\chi\) exactly when \(T=T_1\cup T_2\) for subteams satisfying the respective atoms; they may overlap. Every \((x,y)\) occurs at most once because \(c\) is a function. No restriction is imposed on degrees, number of components, or the cardinality of \(X,Y\) beyond finiteness and nonemptiness. All colorings are quantified over; this is **not** a claim that a particular given team satisfies the formula.

## Proof
**1. Semantic reduction.** A coloring \(c\) satisfies \(\Phi\) if and only if there exist (total) vertex-label maps \(f:X\to C\) and \(g:Y\to C\) such that for every \((x,y)\in G\),
\[
 c(x,y)=f(x)\quad\text{or}\quad c(x,y)=g(y).
\]
Indeed, a satisfying split has a unique \(z\)-value at each \(x\) in the first part and each \(y\) in the second; extend these partial maps arbitrarily on unused vertices. Conversely, assign each edge to a corresponding part, using either part when both conditions hold.

**2. At most two colors.** For a singleton alphabet every edge has the one color. If \(C=\{a,b\}\), choose \(f(x)=a\) for every left vertex and \(g(y)=b\) for every right vertex. Every edge is covered regardless of \(G\).

**3. Pseudoforests.** In each tree component orient every edge away from a chosen root. In a unicyclic component orient the unique cycle cyclically and orient all attached tree edges away from the cycle. Each vertex receives at most one oriented edge. Label each vertex with the color of its incoming edge, if any, assigning an arbitrary default color otherwise. Every edge is covered by its head. By step 1 every coloring of a pseudoforest satisfies \(\Phi\), for arbitrary \(C\).

**4. Bicyclic obstructions.** If a finite connected graph has at least two independent cycles, it contains a connected bicyclic subgraph of one of three types: (i) a theta graph (three internally disjoint paths between a pair of vertices), (ii) two vertex-disjoint cycles joined by a path, or (iii) two cycles meeting in exactly one vertex. This follows by taking a minimal connected subgraph containing two distinct cycles, removing pendant branches, and considering their first intersection (a shared path, no intersection, or a single vertex). Suppressing degree-two vertices yields the three possibilities. All cycles in our bipartite graph are even.

In types (i) and (ii), the bicyclic subgraph \(H\) has maximum degree three and \(|E(H)|=|V(H)|+1\). By the bipartite edge-coloring theorem, \(H\) admits a proper edge coloring using at most three colors. Under any vertex-label maps, each vertex could cover at most one incident edge, since incident edges have different colors. Hence at most \(|V(H)|\) edges could be covered, contradicting \(|E(H)|=|V(H)|+1\).

In type (iii), let the shared vertex be \(v\). Color the two edges incident to \(v\) on the first cycle with color \(a\), and the two incident to \(v\) on the second cycle with distinct color \(b\). Color remaining edges of each even cycle alternately with two colors chosen from the three-color palette other than the cycle's central color. As the paths between the two central incidences have even numbers of edges, this makes the two incident edge colors *different at every noncentral vertex*. Each of the two cycles has one more edge than it has noncentral vertices, so each demands that \(v\) cover at least one edge from that cycle. Yet \(v\)'s single label cannot cover an incident edge of both cycles: their incident labels at \(v\) are \(a\) and \(b\), distinct. Contradiction.

Extend the three-color obstruction arbitrarily from \(H\) to the other edges of \(G\). Any satisfying vertex labels for the larger graph would restrict to satisfying labels for \(H\). Therefore every non-pseudoforest fails robustness for every alphabet with at least three colors, completing the proof.

## Verification
The standalone file `robust_dependency_check.py` independently tests satisfaction by enumerating all vertex labelings and tests pseudoforest structure by connected-component edge/vertex counts. It exhausts every edge subset and every three-coloring of \(K_{1,1}\), \(K_{1,3}\), \(K_{2,2}\) and \(K_{2,3}\), and verifies an eight-edge figure-eight counterexample on \(K_{3,4}\). The expected output ends in `ROBUST_DEPENDENCY_CHECK_OK`. These checks corroborate but do not establish the arbitrary-graph theorem, whose proof is above.

## Relationship to prior work
Fröhlich, Kolaitis and Meier classify model-checking complexity and coherence for disjunctions of two dependence atoms. Their Theorem 12 establishes NL-completeness for \(\operatorname{dep}(x,z)\vee\operatorname{dep}(y,z)\), and Theorem 24 constructs families of incoherence witnesses. Their Lemma 14 identifies the pseudoforest condition for the *different*, uncolored formula \(\operatorname{dep}(x,y)\vee\operatorname{dep}(y,x)\). The present criterion instead quantifies **over all colorings of one fixed support graph** and proves that exactly three consequent values suffice to detect every bicyclic obstruction, including degree-four figure-eight cores. The standard bipartite edge-coloring theorem is used, not newly asserted.

## Limitations
No classification of individual labeled instances beyond the semantic reduction is asserted; individual-team model checking remains governed by the established complexity theory. The new robust characterization concerns functional teams (at most one consequent per input pair) and finite bipartite supports, not arbitrary ternary teams or hypergraphs. Historical subsumption by a differently named graph-coloring theorem remains a residual priority risk. No independent audit has been performed.

## References
1. Nicolas Fröhlich, Phokion G. Kolaitis, and Arne Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, initial public release August 22, 2025. https://arxiv.org/abs/2508.16146 (PDF: https://arxiv.org/pdf/2508.16146).
2. Dénes König, classical bipartite edge-coloring theorem: a bipartite graph of maximum degree \(d\) has a proper edge coloring with \(d\) colors. (Used only as established supporting mathematics.)
