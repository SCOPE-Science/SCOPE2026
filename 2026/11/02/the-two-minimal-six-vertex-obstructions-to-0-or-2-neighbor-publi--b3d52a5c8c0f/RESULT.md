# The two minimal six-vertex obstructions to 0-or-2-neighbor public-goods equilibria

## Finding
Let \(G=(V,E)\) be a finite simple undirected graph. For every vertex \(v\), let \(s_v\in\{0,1\}\) be a binary action and \(k_v=\sum_{u\sim v}s_u\). All vertices have the **same strict best response**
\[
T(k)=\begin{cases}1,& k=0\text{ or }k=2,\\0,&\text{otherwise}.\end{cases}
\]
A pure Nash equilibrium (PNE) is an action vector \(s\) such that \(s_v=T(k_v)\) at every vertex. There is no tie in this best-response definition. Every graph with \(|V|\leq5\) has a PNE. Among graphs on exactly six labeled vertices, precisely \(300\) have no PNE, and all are connected. Up to graph isomorphism, exactly **two** PNE-free graphs exist at order six, represented (with vertex set \(\{0,1,2,3,4,5\}\)) by the following edge sets:

\[
E_A=\{01,02,04,05,12,23,25,34\},
\qquad E_B=\{01,02,04,05,12,13,14,34,45\}.
\]
Here, for example, \(01\) means the undirected edge between vertices \(0\) and \(1\). Their respective edge counts are \(8\) and \(9\). They have \(180\) and \(120\) labeled realizations, respectively, accounting for all \(300\) nonexistence instances among the \(26{,}704\) connected labeled graphs of order six.

## Assumptions and scope
The actions are deterministic, the graph is unweighted and undirected with neither loops nor parallel edges, and neighborhood counts exclude the vertex itself. The best-response pattern is homogeneous and defined at every nonnegative integer, including degrees above four, by the displayed formula. The first-obstruction census is for all graph isomorphism classes through six vertices, not for larger graphs and not for arbitrary best-response patterns. A PNE here is necessarily nonzero because \(T(0)=1\).

## Proof
**All graphs of order at most five admit an equilibrium.** More generally, suppose the maximum degree of \(G\) is at most \(3\). Write \(A\) for its adjacency matrix over \(\mathbb F_2\) and \(M=I+A\). For every \(z\in\ker M\), the symmetry and zero diagonal of \(A\) give
\[
0=z^{\mathsf T}Mz=z^{\mathsf T}z=\sum_{v\in V}z_v\pmod2.
\]
Consequently the all-ones vector is orthogonal to \(\ker M\), and, because \(M\) is symmetric, it lies in \(\operatorname{im}M\). Thus there is a solution \(s\in\mathbb F_2^{|V|}\) of \(Ms=\mathbf1\). Equivalently, \(s_v=1\) precisely when \(k_v\) is even. At degree at most three, the only even possibilities are \(k_v=0\) and \(k_v=2\); this is exactly \(T\), so the solution is a PNE. If instead \(G\) has a universal vertex, taking that vertex active and all others inactive is a PNE for any graph order. A graph on at most five vertices with no universal vertex has maximum degree at most three. The two cases prove the stated universal lower-order bound. For disconnected graphs, equilibria on components concatenate; this also covers every disconnected graph on six vertices.

**The eight-edge witness has no equilibrium.** In \(G_A\), call vertices \(0\) and \(2\) hubs \(a,b\); both have degree four and are adjacent. Vertices \(1\) and \(5\) are each adjacent to both hubs. Vertices \(4=e\) and \(3=f\) form the path \(a-e-f-b\). A degree-two vertex with neighbors taking values \(p,q\) must take action \(1+p+q\) modulo two. Therefore the path equations give \(e+f=1+a=1+b\), hence \(a=b\). If both hubs are zero, vertices \(1\) and \(5\) must both be one; an inactive hub then sees \(2+e\) or \(2+f\) active neighbors. To remain inactive it must see three rather than two, requiring \(e=f=1\); this contradicts \(e+f=1\) modulo two. If both hubs are one, vertices \(1\) and \(5\) must again be one, and each active hub sees at least three active neighbors, which is incompatible with acting one. Both possibilities contradict equilibrium.

**The nine-edge witness has no equilibrium.** In \(G_B\), vertices \(0,1,4\) form a triangle of degree-four hubs. Each hub pair has a unique degree-two common leaf, respectively \(2,3,5\), and these three leaves are independent. Every leaf must act one exactly when its two adjacent hubs take the same action. By symmetry it suffices to consider the number \(r\in\{0,1,2,3\}\) of active hubs. If \(r=0\), all leaves act one and each hub sees exactly two active neighbors, so must act one. If \(r=3\), all leaves act one and each hub sees four active neighbors, so must act zero. If \(r=1\), the leaf between the two inactive hubs acts one and the other leaves act zero; each inactive hub sees two active neighbors and should act one. If \(r=2\), the leaf between the two active hubs acts one, while the inactive hub sees two active core neighbors and should act one. Each case contradicts its defining number of active hubs.

**Completeness of the six-vertex classification.** The included deterministic exhaustive checker traverses exactly one integer edge mask for every labeled simple undirected graph, for each order \(n\in\{1,\ldots,6\}\). For each graph it constructs the correct adjacency bit masks and tests connectivity by fixed-point reachability. For each connected graph it exhaustively tests all \(2^n\) binary action profiles, checking the defining best-response equality at every vertex. For each equilibrium-free six-vertex graph, it computes the minimum edge mask over **all** \(6!\) vertex permutations; two graphs have the same canonical mask exactly when they are isomorphic. The complete run reports \(0\) failures for orders one through five, \(300\) at order six, and only the two canonical masks \(957\) and \(1915\), with multiplicities \(180\) and \(120\). The code independently checks that the displayed witnesses map to these two masks, have no equilibrium, and collectively exhaust the failures. This finite exhaustive process is a complete proof for the finite classification because all graphs, profiles and relabelings are traversed, not sampled. The two witnesses' direct contradictions additionally establish nonexistence without relying solely on the computation.

## Verification
Run `python3 verify.py` using Python 3.8 or newer; no external packages, data downloads, randomness or solver are needed. The expected connected-graph counts, paired with their equilibrium-free counts, for \(n=1,2,3,4,5,6\) are respectively \((1,0),(1,0),(4,0),(38,0),(728,0),(26704,300)\). For six vertices the equilibrium-free canonical-mask multiset is \(\{957:180,1915:120\}\). The code includes the edge lists and asserts all of these numerical statements. The parity argument and the two witness contradictions can be checked independently by hand; enumeration certifies only the finite six-vertex census, not any claim about larger orders.

## Relationship to prior work
Gilboa and Nisan (2022, arXiv:2207.04238v1, p. 3) explicitly posed the computational complexity of this exact 0-or-2-neighbors pattern as an open problem, while separately recognizing that infinite alternating parity patterns are decidable by linear equations over \(\mathbb F_2\). The degree-three parity argument above uses this familiar linear-algebraic observation, not a claimed new general algebraic method. Klimm and Stahlberg (2023, arXiv:2301.11849) prove NP-hardness for the broader nonmonotone family including this pattern. Gilboa (2023, arXiv:2301.11580v1; revised 2024) proves the finite-pattern complexity classification and explicitly illustrates nonexistence for 0-or-2-neighbors with a **nine-vertex chain of four triangles** (Fig. 4). None of these inspected treatments states the sharp six-vertex cutoff or both first-obstruction isomorphism classes. NP-hardness in itself does not imply the finite-order classification; conversely, the finite classification does not improve the published NP-hardness bounds.

## Limitations
This is a first-order, finite structural classification for one strict homogeneous best-response function. It does not classify equilibrium-free graphs at larger orders, give a forbidden induced-subgraph characterization, or provide an efficient decision algorithm for arbitrary input graphs. Other unindexed studies or unpublished machine-generated graph censuses may already contain an equivalent minimal-obstruction classification, so publication priority needs external confirmation. The explicitly supplied checker must be rerun in a trusted environment if a different computing platform is used.

## References
1. M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238v1, 9 July 2022, https://arxiv.org/pdf/2207.04238v1 .
2. M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849v1, 27 January 2023, https://arxiv.org/pdf/2301.11849v1 .
3. M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580v1, 27 January 2023, https://arxiv.org/pdf/2301.11580v1 .
