# A sharp twelve-to-thirteen Rips collapse transition in generalized Petersen graphs

## Finding
Let \(G_n=GP(n,2)\), with its unit-edge shortest-path metric, and let \(\mathrm{VR}_{\le}(G_n;2)\) consist of all nonempty sets of vertices of pairwise graph distance at most two. For every integer \(n\ge13\), the complex \(\mathrm{VR}_{\le}(G_n;2)\) **simplicially collapses onto the outer cycle** \(C_n\). In particular,
\[
\mathrm{VR}_{\le}(GP(n,2);2)\simeq S^1\quad(n\ge13).
\]
The threshold is sharp for this stable statement: at \(n=12\),
\[
\widetilde H_2\!\left(\mathrm{VR}_{\le}(GP(12,2);2);\mathbb F_2\right)
 \cong (\mathbb F_2)^3,
\]
and all other reduced mod-two homology groups vanish. Thus the preceding complex cannot collapse onto a circle.

## Assumptions and scope
The vertex set of \(G_n\) is \(\{u_i,v_i:i\in\mathbb Z/n\mathbb Z\}\), with precisely three families of undirected edges: \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). Graphs are simple. The asserted simplicial collapse is for **all** integers \(n\ge13\); the \(n=12\) computation is an exact finite boundary obstruction. The metric is the combinatorial shortest-path metric, and scale two is inclusive; no claim is made for Euclidean embeddings or for other values of the graph-power exponent.

Writing \(H_n=G_n^2\) for the graph joining pairs at distance one or two, we have the exact identity \(\mathrm{VR}_{\le}(G_n;2)=\mathrm{Cl}(H_n)\). Every index in the proof below is understood modulo \(n\), but the stages of vertex deletion are ordered by representatives \(0,1,\ldots,n-1\).

## Proof
**1. Square-graph adjacency.** Every length-at-most-two walk in \(G_n\) is obtained either by walking within the outer ring, within the inner step-two ring, or through one spoke. Consequently the edges of \(H_n\), for \(n\ge13\), are exactly
\[
\begin{aligned}
 u_i\!\sim u_j&\iff j-i\in\{\pm1,\pm2\},\\
 v_i\!\sim v_j&\iff j-i\in\{\pm2,\pm4\},\\
 u_i\!\sim v_j&\iff j-i\in\{0,\pm1,\pm2\},
\end{aligned}
\qquad(\bmod n).
\]
In each case the alternatives are distinct for \(n\ge13\).

**2. A local fold lemma.** Let \(H\) be a finite graph and \(a,b\) distinct vertices with \(N_H[a]\subseteq N_H[b]\). Deleting \(a\) induces a simplicial collapse \(\mathrm{Cl}(H)\searrow\mathrm{Cl}(H-a)\); a sequence of such deletions ending at one vertex makes \(\mathrm{Cl}(H)\) collapsible. If a vertex \(w\) of a simplicial complex has collapsible link, its closed star is a cone on that link, and the elementary collapses of the link can be coned and completed by a final free face pair to delete \(w\) while fixing the subcomplex not containing \(w\). Thus an induced vertex link that is dismantlable can be used to delete the vertex by a simplicial collapse.

**3. Explicit inner-vertex elimination.** Delete \(v_0,v_1,\ldots,v_{n-1}\) in this order. Immediately before deleting \(v_i\), its link in the remaining flag complex is the clique complex of the graph induced by
\[
\{u_{i-2},u_{i-1},u_i,u_{i+1},u_{i+2}\}
\ \cup\ \{v_{i+d}:d\in\{-4,-2,2,4\},\ (i+d)\bmod n\ge i\}.
\]
The inequality refers to the standard residue in \(\{0,\ldots,n-1\}\); it records exactly which inner vertices have not yet been deleted. Put \(U_j=u_{i+j}\) and \(V_j=v_{i+j}\). In the following five lines, each expression \(A\to B\) means fold/delete vertex \(A\) because its **closed** neighborhood in the current link graph is contained in that of \(B\). The order within each line is essential.

| Indices \(i\) | Surviving inner offsets | Link fold sequence |
|---|---|---|
| \(0,1\) | \(-4,-2,2,4\) | \(U_1\to U_0;\ U_2\to V_2;\ U_0\to V_{-2};\ U_{-2}\to V_{-2};\ U_{-1}\to V_{-2};\ V_4\to V_2;\ V_2\to V_{-2};\ V_{-4}\to V_{-2}\) |
| \(2,3\) | \(-4,2,4\) | \(U_{-1}\to U_0;\ U_1\to U_0;\ U_2\to V_2;\ V_4\to V_2;\ V_2\to U_0;\ U_0\to U_{-2};\ U_{-2}\to V_{-4}\) |
| \(4\le i\le n-5\) | \(2,4\) | \(U_{-2}\to U_{-1};\ U_{-1}\to U_0;\ U_0\to U_1;\ U_1\to U_2;\ U_2\to V_2;\ V_2\to V_4\) |
| \(n-4,n-3\) | \(2\) | \(U_{-2}\to U_{-1};\ U_{-1}\to U_0;\ U_0\to U_1;\ U_1\to U_2;\ U_2\to V_2\) |
| \(n-2,n-1\) | none | \(U_{-2}\to U_{-1};\ U_2\to U_1;\ U_{-1}\to U_0;\ U_1\to U_0\) |

Each asserted containment follows by intersecting the adjacency lists in Step 1 with the link vertices remaining at that particular stage. These are finite symbolic offset computations: all possible differences among the listed offsets lie between \(-8\) and \(8\), and the only possible modular identifications influencing the inequalities are excluded by \(n\ge13\) (the listed offset classes and adjacency tests are valid also at \(n=13\)). In each row the number of folds is exactly the number of link vertices minus one. Hence every link dismantles to one vertex, and Step 2 removes each \(v_i\) without changing the collapse type.

**4. The surviving outer complex.** After all inner vertices are removed, the induced square graph on \(\{u_i\}\) is \(C_n^2\). For \(n\ge13\), its maximal cliques are precisely the triangles \(\{u_i,u_{i+1},u_{i+2}\}\). Each distance-two edge \(u_iu_{i+2}\) belongs to exactly one of these triangles, so removing this triangle together with its free distance-two edge is an elementary collapse. Performing this for all \(i\) leaves only the outer cycle edges. This proves the stated **simplicial collapse** and its homotopy consequence.

**5. The sharp boundary \(n=12\).** Enumerate all cliques of the exact shortest-path square graph, retaining their faces. The simplex counts in successive dimensions are \((24,108,160,84,12)\). Over \(\mathbb F_2\), with the augmentation as the reduced degree-zero boundary, the boundary ranks are \((1,23,85,72,12)\). The rank-nullity identity \(\widetilde\beta_k=f_k-\mathrm{rank}(\partial_k)-\mathrm{rank}(\partial_{k+1})\) therefore gives \((0,0,3,0,0)\), proving the non-circle obstruction. The complete finite computation is supplied as independently reproducible code; it is not used to deduce Step 3 for all \(n\).

## Verification
The companion `verifier.py` uses only the Python standard library. It rebuilds each graph from the original three edge families, constructs distance-at-most-two adjacency without relying on the symbolic formula, compares every pair against Step 1 for all \(13\le n\le40\), and replays each containment of all five families of link folds (\(742\) vertex-link instances). Separately it exhausts all maximal cliques and faces for \(n=12\), performs exact binary boundary elimination, and reproduces the stated face counts, ranks, and reduced Betti numbers. The package includes `verification_output.txt`. Finite checks support but do not replace the all-parameter symbolic link argument.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers*, arXiv:1104.0433, Proposition 2.2, proves collapse for graph squares when the original graph has girth at least seven. That hypothesis fails here: \(GP(n,2)\) has five-cycles \(u_i,u_{i+1},u_{i+2},v_{i+2},v_i,u_i\). Its Theorem 3.1 assumes that **every** clique of the square graph lies in the closed neighborhood of a vertex of the original graph; the five vertices of the displayed cycle form a clique of the square graph, whereas \(GP(n,2)\) is cubic and its closed original neighborhoods have just four vertices. Theorem 3.2 forbids induced five-cycles, so its conditions fail as well. That work's cycle-power classification determines Step 4 but does not perform Step 3.

Adamaszek–Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first public version 2015-03-12; primary MSC including 55U10), classifies Rips complexes for metric circles and cyclic graphs. The graph-metric structure of the two-ring generalized Petersen family is not covered by its circle classification. Published results about the independence, matching, or cut complexes of individual generalized Petersen graphs concern different complexes and do not imply a collapse for the flag complex of the graph square.

## Limitations
This theorem covers only the specified graph family and scale two; it does not classify the full filtration, all generalized Petersen parameters, or the integer homology of the exceptional \(n=12\) complex. The boundary computation establishes mod-two homology only. The proof is self-contained apart from the standard dominated-vertex simplicial-collapse lemma. Previously unindexed publications under graph-power, flag-complex, or generalized-Petersen terminology remain a potential originality risk; unsuccessful literature searches are not proof of absolute novelty.

## References
- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (first public 2011-04-03), especially Sections 2, 3, and 6. https://arxiv.org/abs/1104.0433
- M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669v1 (first public 2015-03-12); *Pacific Journal of Mathematics* **290** (2017), 1–40. https://arxiv.org/abs/1503.03669
- R. Nedela and M. Škoviera, *Which generalized Petersen graphs are Cayley graphs?*, *Journal of Graph Theory* **19** (1995), 1–11, for standard generalized-Petersen conventions. https://doi.org/10.1002/jgt.3190190102
