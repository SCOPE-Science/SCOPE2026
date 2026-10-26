# A connectivity dichotomy for minimum zero forcing on powers of paths and cycles

## Finding

Let \(k\ge 2\) be an integer. For a finite graph \(G\), write \(G^k\) for the graph joining vertices at distance at most \(k\), and let \(\mathscr Z(G)\) be the token-jumping reconfiguration graph of its *minimum ordinary zero-forcing sets*: two distinct minimum sets are adjacent if their symmetric difference has size two.

**Theorem.** For every \(n\ge k+2\), the zero-forcing number of the path power is \(Z(P_n^k)=k\), and its reconfiguration graph has precisely \(2k\) vertices, with isomorphism type
\[
\mathscr Z(P_n^k)\cong
\begin{cases}
K_k\square K_2,&n=k+2,\\
\text{two copies of }K_k\text{ joined by one bridge},&n=k+3,\\
K_k\sqcup K_k,&n\ge k+4.
\end{cases}
\]
For every \(n\ge2k+3\), the cycle power has \(Z(C_n^k)=2k\), and \(\mathscr Z(C_n^k)\) is connected with exactly \(n(2k-1)\) vertices. It is covered by \(n\) cliques of order \(2k\), with consecutive cliques sharing exactly one vertex and all other pairs disjoint. For \(n\ge2k+4\), the *complete* reconfiguration graph, including edges between distinct cliques, has exactly
\[
|E(\mathscr Z(C_n^k))|=n(k+1)(2k-1).
\]
These conclusions determine a sharp connectivity transition for path powers and an opposite, persistent connectivity regime for cycle powers. The two numerical zero-forcing values are known and are not claimed as new.

## Assumptions and scope

All graphs are finite, simple, undirected and labeled. The path \(P_n\) has vertices \(0,1,\dots,n-1\) in order; the cycle \(C_n\) has vertices in \(\mathbb Z/n\mathbb Z\). Ordinary zero forcing starts with blue set \(B\). A blue vertex can turn a white vertex blue when that white vertex is its unique white neighbor. A zero-forcing set eventually blues every vertex; minimum means minimum cardinality, not inclusion-minimal. Edges of \(\mathscr Z(G)\) are *token jumps*, not adjacency-constrained token slides. Parameters are integers \(k\ge2\) and the stated lower bounds on \(n\).

The following explicit families are used in the theorem. On a path, for \(1\le j\le k\), set
\[
L_j=\{0,1,\dots,k\}\setminus\{j\},\qquad
R_j=\{n-1-k,\dots,n-1\}\setminus\{n-1-j\}.
\]
On a cycle, for each center \(c\in\mathbb Z/n\mathbb Z\) write
\[
I_c=\{c-k,c-k+1,\dots,c+k\}\pmod n,\quad
\mathcal F_c=\{I_c\setminus\{w\}:w\in I_c\setminus\{c\}\}.
\]

## Proof

**1. The first-force lemma.** Suppose \(G\) has minimum degree \(d\) and a forcing set of size \(d\). Any first force is made by an initially blue vertex \(u\) with exactly one white neighbor. Hence \(u\) has at most \(d\) neighbors, so its degree is exactly \(d\), and the initial blue set consists of \(u\) together with all but one vertex of \(N(u)\). This proves both \(Z(G)\ge d\) and the asserted necessary local form whenever a set of size \(d\) forces. Conversely, a full consecutive window on a power of a path or cycle can be extended one vertex at a time: with \(2k+1\) consecutive cycle vertices blue, the vertex \(k\) places back from the growing right boundary has exactly the next boundary vertex white among its neighbors. Analogously, a window beginning at a path endpoint can be extended from that endpoint. This gives the needed sufficient forcing constructions.

**2. Paths.** For \(n\ge k+2\), only vertices \(0\) and \(n-1\) have degree \(k\); all other vertices have degree at least \(k+1\). The first-force lemma therefore forces any size-\(k\) zero-forcing set to be one of the displayed \(L_j\) or \(R_j\). All these sets really force: the endpoint first forces its missing neighbor, completing the first \(k+1\) (or last \(k+1\)) path vertices; then the growing consecutive segment forces the rest. There are \(2k\) distinct sets, establishing minimality and the entire vertex set of the reconfiguration graph.

Two left sets differ in precisely one chosen vertex, so they induce \(K_k\); the right sets also induce \(K_k\). A left and right set can be adjacent only if their interiors agree in at least \(k-1\) vertices, since their distinct endpoint vertices contribute nothing to their intersection. For \(n=k+2\), both interior windows equal \(\{1,\dots,k\}\); matching omissions give exactly one cross edge per left vertex, producing \(K_k\square K_2\). For \(n=k+3\), the interiors overlap in exactly \(k-1\) vertices, and just one pair contains the entire overlap, producing exactly one cross edge. For \(n\ge k+4\), their interiors overlap in at most \(k-2\) vertices and no cross edge is possible. This proves the three cases.

**3. Cycles: all minimum sets and connectedness.** If \(n\ge2k+3\), every vertex of \(C_n^k\) has degree \(2k\). The first-force lemma says that every size-\(2k\) forcing set lies in at least one \(\mathcal F_c\). Every member of \(\mathcal F_c\) forces \(I_c\) at its first move and then forces the whole cycle by consecutive extension. This proves both \(Z(C_n^k)=2k\) and the equality
\[
V(\mathscr Z(C_n^k))=\bigcup_{c\in\mathbb Z/n\mathbb Z}\mathcal F_c.
\]
Each \(\mathcal F_c\) contains \(2k\) sets, any two adjacent by a single jump, hence spans \(K_{2k}\). Windows \(I_c\) and \(I_{c+1}\) intersect in \(2k\) vertices. Their only common minimum set is the intersection itself. Windows with centers separated by two or more cycle steps intersect in at most \(2k-1\) vertices, so the corresponding families have no common minimum set. There are no triple intersections. Therefore the union has \(2kn-n=n(2k-1)\) distinct members. The consecutive cliques share vertices around the whole cycle, so the complete reconfiguration graph is connected.

**4. Cycle edge enumeration.** Assume now \(n\ge2k+4\). An exchange edge joins two distinct \(2k\)-sets with exactly \(2k-1\) common vertices. The edges lying within a family \(\mathcal F_c\) contribute
\[
n\binom{2k}{2}=nk(2k-1).
\]
No edge lies within two such families, because two distinct families have at most one common *vertex* (configuration).

For any further edge select a first-force center for each endpoint. Their two windows must intersect in at least \(2k-1\) positions, so their center separation is one or two. For consecutive centers, the windows intersect in \(2k\) positions. The additional edges, not belonging to either clique, come from deleting the *same* vertex of this intersection other than the two centers: exactly \(2k-2\) choices for each of the \(n\) consecutive-center pairs. All other one-step exchanges across these windows use the shared configuration and have already been counted within a clique.

For center separation two, the windows meet in exactly \(2k-1\) positions. An adjacent pair must contain all these positions and one further position from each of the two windows. Each window has two positions outside the intersection, giving four candidate pairs. One pair is already an edge within the intervening center's clique, two have an endpoint with an additional adjacent first-force center and were counted with the consecutive-center pairs, and exactly one new pair remains. Thus this case adds \(n\) edges. Larger center separation has intersection at most \(2k-2\) and gives no exchange. Therefore
\[
|E|=nk(2k-1)+n(2k-2)+n=n(k+1)(2k-1).
\]
This completes the proof.

## Verification

The accompanying standalone `verify.py` constructs path and cycle powers directly from their graph distances, simulates both a simultaneous and a sequential ordinary forcing process, and independently enumerates *every* subset of the proposed minimum size in fifty small parameter cases (35 path pairs and 15 cycle pairs). It checks equality with the explicit families, rebuilds token-jump edges, counts components, and checks the cycle edge formula. Larger combinatorial reconstructions check parameters through \(k=7\) and \(n=45\). The final output is `ALL_VERIFY_OK`.

These tests are finite cross-checks only. The claims for arbitrary \(n,k\) follow from the preceding proof, not from extrapolation of a finite computation.

## Relationship to prior work

The zero-forcing process and its minimum-degree lower bound belong to the existing theory, including Amos, Caro, Davila and Pepper (arXiv:1401.6206, first posted 2014-01-23). Geneson, Haas and Hogben (arXiv:2009.00220, first posted 2020-09-01) introduced the token-jumping zero-forcing reconfiguration graph, and proved the base-cycle case \(\mathscr Z(C_n)\cong C_n\). Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker (arXiv:2610.03892, first posted 2026-10-02) explicitly determine the numerical values \(Z(P_n^k)=k\) and \(Z(C_n^k)=2k\). Those numerical values and the unpowered cycle case are not new. The present statement concerns the *complete minimum-set structure*, the path-family's sharp bridge-to-disconnection transition, the cycle-family's clique-cover connectivity, and its exact exchange-edge count. The inspected portions of these primary works do not provide that reconfiguration classification.

## Limitations

The cycle edge-count formula is asserted only for \(n\ge2k+4\), and the cycle minimum-set count only for \(n\ge2k+3\). No diameter formula or full graph isomorphism for the cycle-power exchange graph is claimed, beyond the explicit clique cover and edge enumeration. Earlier equivalently worded or unindexed classifications might exist; bibliographic novelty has not been independently certified. No independent mathematical audit has been performed.

## References

1. D. Amos, Y. Caro, R. Davila, R. Pepper, *Upper bounds on the k-forcing number of a graph*, arXiv:1401.6206v1 (2014-01-23), https://arxiv.org/abs/1401.6206.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020-09-01), https://arxiv.org/abs/2009.00220.
3. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892v1 (2026-10-02), https://arxiv.org/abs/2610.03892.
