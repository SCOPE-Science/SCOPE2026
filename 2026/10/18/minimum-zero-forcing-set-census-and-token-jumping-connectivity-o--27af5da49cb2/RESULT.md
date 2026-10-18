# Minimum zero-forcing-set census and token-jumping connectivity of cycle powers

## Finding

**Theorem.** Let \(n\ge3\) and \(k\ge1\) be arbitrary integers. Write \(G=C_n^k\) for the graph on \(\mathbb Z/n\mathbb Z\) joining distinct residues of cyclic distance at most \(k\). Let \(\mathcal M_{n,k}\) denote the family of minimum ordinary zero-forcing sets of \(G\). Then all minimum sets, their number, and the optimum cardinality are as follows.

1. If \(n\le2k+1\), the graph is complete, \(Z(G)=n-1\), and \(\mathcal M_{n,k}=\{V(G)\setminus\{w\}:w\in V(G)\}\) has exactly \(n\) elements.
2. If \(n=2k+2\), the graph is the complete graph minus the perfect matching of antipodal vertex pairs, \(Z(G)=n-2=2k\), and \(\mathcal M_{n,k}\) consists of all sets \(V(G)\setminus\{a,b\}\) with \(a\ne b\) and \(a,b\) **not antipodal**. There are exactly \(nk\) such sets.
3. If \(n\ge2k+3\), then \(Z(G)=2k\) and
\[
\mathcal M_{n,k}=\{N_G[v]\setminus\{w\}:v\in V(G),\ w\in N_G(v)\},\qquad |\mathcal M_{n,k}|=n(2k-1).
\]
Here \(N_G(v)\) and \(N_G[v]\) are respectively the open and closed neighborhoods. Among these minimum sets, precisely the \(n\) sets consisting of \(2k\) cyclically consecutive vertices have two presentations in the displayed expression; the other \(2n(k-1)\) have one presentation.

In every regime, the **token-jumping reconfiguration graph** on \(\mathcal M_{n,k}\), adjacent when two distinct minimum sets exchange exactly one selected vertex, is connected. In the complete regime it is \(K_n\); in the perfect-matching-deletion regime it is the line graph of \(K_n\) with one perfect matching removed, viewed as the graph of admissible omitted edges.

## Assumptions and scope

All graphs are finite, simple, and undirected. Ordinary zero forcing starts with a blue set \(B\), repeatedly recoloring a white vertex when it is the **unique** white neighbor of some blue vertex. A minimum set is a forcing set having smallest possible cardinality; this is not the higher-threshold generalized forcing rule. The exponent \(k\) refers exclusively to taking a graph power. Cyclic intervals and residues are interpreted modulo \(n\). A token-jump replaces exactly one member of a minimum set by a previously unselected vertex. The theorem includes the complete and nearly-complete boundary cases rather than assuming \(n>2k+1\).

## Proof

**Universal first-force bound.** Suppose a blue set is not the entire vertex set and contains a vertex \(v\) making the first force, to \(w\). Since all neighbors of \(v\) except \(w\) must already be blue, \(B\) contains \(\{v\}\cup(N_G(v)\setminus\{w\})\), hence \(|B|\ge\deg(v)\ge\delta(G)\). Thus \(Z(G)\ge\delta(G)\) for every graph considered here. This statement concerns only successful sequences with an actual first force; the initially all-blue set is strictly larger in all our cases.

**Complete boundary.** If \(n\le2k+1\), all pairs are adjacent and \(G=K_n\). Its minimum degree is \(n-1\); every \(n-1\)-subset forces its unique white vertex. This proves the first regime, and all such subsets differ by one exchange.

**Deleted-matching boundary.** If \(n=2k+2\), exactly the antipodal vertex pairs are nonedges, so \(\delta(G)=n-2\). Any \(n-2\)-set omits two vertices \(a,b\). If \(a,b\) are antipodal then each blue vertex is adjacent to both white vertices and no force can begin. If they are not antipodal, the antipode \(a'\) of \(a\) is initially blue and adjacent to \(b\) but not \(a\), so it forces \(b\); thereafter any blue neighbor of \(a\) forces the one remaining white vertex. Consequently the optimal omission pairs are precisely the edges of \(G\), counted by \(\binom n2-n/2=nk\). Two admissible pairs sharing one endpoint can be exchanged; their line graph is connected because deleting a perfect matching from \(K_n\), \(n\ge4\), leaves a connected graph, and the line graph of a connected graph with edges is connected.

**Sparse-enough power: necessity and sufficiency.** Assume \(n\ge2k+3\). The graph is \(2k\)-regular, so \(Z(G)\ge2k\). Each closed neighborhood \(N_G[v]\) is a cyclic interval of \(2k+1\) consecutive vertices. The proposed \(2k\)-set \(B=N_G[v]\setminus\{w\}\) initially lets \(v\) force \(w\). After this step all of \(N_G[v]\) is blue. A blue interval \(\{a,a+1,\ldots,a+L-1\}\) of length \(L\ge2k+1\), and length less than \(n\), can be expanded one vertex to the right: its vertex \(a+L-k\) is blue and all its forward \(k\) neighbors except \(a+L\) are already in the interval; its backward neighbors are in the interval as well. Hence it forces \(a+L\). Repeat until all vertices are blue. (When the interval has length \(n-1\), the remaining white vertex is still the only white neighbor of that blue vertex, so the same conclusion holds.) Thus the displayed family consists of zero-forcing sets and \(Z(G)=2k\).

Conversely, a minimum forcing set \(B\) has size exactly \(2k\). At the first force \(v\to w\), the first-force bound is an equality; therefore \(B=N_G[v]\setminus\{w\}\). This is the full classification.

**Multiplicity of neighborhood presentations.** There are \(n(2k)\) ordered center–deleted-neighbor presentations. Two distinct closed neighborhoods of length \(2k+1\) can contain a common \(2k\)-subset only when their centers differ by one step in the cyclic order: since their complements are cyclic intervals of length \(n-2k-1\ge2\), distinct complements have union size at least \(n-2k\), with equality exactly when the intervals are shifted by one step. Equivalently, for a direct elementary check, intersect the two shifted cyclic intervals and observe that their intersection has size \(2k\) only for adjacent shifts (and is at most \(2k-1\) otherwise). Each adjacent pair intersects in exactly \(2k\) consecutive vertices, giving one set with two presentations, and different adjacent center pairs give distinct sets. Thus there are exactly \(n\) double presentations and no higher multiplicities. The unique-set count is \(2kn-n=n(2k-1)\); precisely \(n\) are cyclic blocks and the remaining \(2n(k-1)\) have one presentation.

**Token-jumping connectivity.** In the third regime take an arbitrary optimum \(B=N_G[v]\setminus\{w\}\). If \(w\) is one endpoint of that closed-neighborhood interval, \(B\) is a consecutive block of size \(2k\). Otherwise, exchange either endpoint \(u\) of that interval that belongs to \(B\) for \(w\), producing the consecutive block \(N_G[v]\setminus\{u\}\). Each such exchange is between minimum sets. The consecutive blocks \(\{i,i+1,\ldots,i+2k-1\}\), indexed by \(i\pmod n\), connect cyclically via one-vertex exchanges. Hence every minimum set connects to the common cycle of blocks. Connectivity in the other regimes was established above. \(\square\)

## Verification

The supplementary self-contained verifier, `verify_cycle_powers.py`, constructs the adjacency relation from cyclic distance, iterates the color-change rule directly, enumerates every subset of the claimed optimum size for \(3\le n\le15\) and \(1\le k<n\), and compares the resulting exact collection to the theorem's family. It independently checks that the smallest degree equals the claimed optimum and that the token-jumping graph of the enumerated minimum sets is connected. It also checks 25 larger parameter pairs nonexhaustively. The recorded check is `VERIFICATION_OK exhaustive_parameter_pairs=104 candidate_subsets=33331 enlarged_cases=25`.

These finite tests verify the specified finite instances, not the infinite theorem; the proof above supplies the arbitrary-parameter argument.

## Relationship to prior work

Premodkmuar, Dominic and Chacko (2020), Proposition 27, computed the **connected** zero-forcing number for the square of a cycle. This overlaps the known optimal-cardinality question at power two but does not enumerate minimum sets, treat all powers, or determine the token-jumping graph. Geneson, Haas and Hogben (2020), Proposition 2.2, proved the zero-forcing reconfiguration graph of the ordinary cycle is a cycle, and their Proposition 2.3 treats complete graphs. These are the \(k=1\) and complete boundary cases recovered here, not new claims at those boundaries. Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker (2026), Proposition 8, prove the ordinary zero-forcing number of powers of cycles; the scalar \(2k\) portion of this theorem is therefore **not independently new**. The contribution is the complete minimum-set classification and counts across the two sharp boundary transitions, together with connectivity of their reconfiguration graph in every regime.

## Limitations

The main theorem is about **ordinary** zero forcing of undirected powers of cycles only, and token jumps, not token slides or higher-threshold forcing. The original scalar bound and ordinary-cycle cases already appear in the cited literature. An equivalent full census may exist outside the inspected, indexed sources; bibliographic priority is not guaranteed. Computational checks end at finite parameters and do not replace proof. Independent scientific review has not been performed.

## References

1. K. P. Premodkmuar, C. Dominic, B. Chacko, *Connected k-forcing sets of graphs and splitting graphs*, Journal of Mathematical and Computational Science 10 (2020), 656–680. Published 2020-03-06. DOI: 10.28919/jmcs/4446. Open text: https://scik.org/index.php/jmcs/article/download/4446/2155.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020-09-01), https://arxiv.org/html/2009.00220v1.
3. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (2026-10-02), https://arxiv.org/abs/2610.03892.
