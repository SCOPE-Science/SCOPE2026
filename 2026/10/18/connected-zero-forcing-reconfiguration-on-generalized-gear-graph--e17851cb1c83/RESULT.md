# Connected zero-forcing reconfiguration on generalized gear graphs

## Finding

Let \(m\ge4\) and \(r\ge1\) be integers, write \(L=r+1\) and \(N=mL\), and let \(G=\operatorname{Gr}(m,r)\) be the generalized gear graph defined below. The minimum zero-forcing sets have size three. Their token-jumping reconfiguration graph \(\mathcal R(G)\) is connected and has
\[
 |V(\mathcal R(G))|=m(3r+2),\qquad
 |E(\mathcal R(G))|=m(6r+5).
\]
The entire vertex set of \(\mathcal R(G)\) is given explicitly by the three families \(H_x,A_{s,k},B_{s,k}\) below; distinct sets are adjacent exactly when they share two vertices. The graph contains an induced \(N\)-cycle on the minimum sets containing the hub, and every other minimum set is adjacent to that cycle. In particular,
\[
 \operatorname{diam}(\mathcal R(G))\le \left\lfloor\frac{N}{2}\right\rfloor+2.
\]
For \(r\ge2\) its complete degree distribution is
\[
 \#\{T:\deg_{\mathcal R}(T)=3\}=2m,\quad
 \#\{T:\deg_{\mathcal R}(T)=4\}=3m(r-1),\quad
 \#\{T:\deg_{\mathcal R}(T)=5\}=2m,\quad
 \#\{T:\deg_{\mathcal R}(T)=6\}=m.
\]
For \(r=1\) the nonzero degree counts are \(4m\) of degree four and \(m\) of degree six.

## Assumptions and scope

All graphs are finite, simple and undirected. Define the hub vertex \(v_0\) and rim vertices \(v_1,\ldots,v_N\), with rim indices taken cyclically modulo \(N\) in \(\{1,\ldots,N\}\). All successive rim vertices are adjacent; the hub is joined exactly to the \(m\) spoke vertices \(v_s\), where \(s\in\{L,2L,\ldots,mL\}\). Thus there are \(r\) intermediate vertices strictly between successive spokes. The standard zero-forcing rule lets a blue vertex with exactly one white neighbor color that neighbor blue. A *minimum zero-forcing set* is a blue starting set of minimum cardinality that colors every vertex. The reconfiguration graph has one vertex per minimum zero-forcing set, and two such sets are adjacent when exactly one selected vertex is exchanged.

With \(1\le x\le N\), \(s\) ranging over the spoke indices, and \(0\le k\le L-1\), define
\[
 H_x=\{v_0,v_x,v_{x+1}\},
\]
\[
 A_{s,k}=\{v_{s+1},v_{s-L+k},v_{s-L+k+1}\},\qquad
 B_{s,k}=\{v_{s-1},v_{s+k},v_{s+k+1}\}.
\]
All indices in these sets are cyclic. For each spoke \(s\), \(A_{s,L-1}=B_{s,0}=\{v_{s-1},v_s,v_{s+1}\}\), and these are the only duplicates across the displayed triples when \(m\ge4\).

## Proof

**1. Minimum cardinality and classification.** The minimum zero-forcing number \(Z(G)=3\) is already established in Anderton et al. [1, Theorem 2.3]. For completeness, a pair of initially blue vertices cannot color the hub: if the hub is blue, one rim vertex cannot initiate a forcing chain, and if it is white, the two rim seeds can propagate within at most one interspoke path but cannot color both rim neighbors of any spoke before the hub. Three vertices of the form \(H_x\) succeed, so the lower bound is tight.

Any \(H_x\) is forcing: the two successive blue rim vertices propagate in opposite directions around the rim, because every spoke already has its hub neighbor blue. Conversely, if a three-element forcing set initially contains the hub, its other two members must be adjacent on the rim to initiate a force; a nonadjacent pair leaves every blue rim vertex with at least two white rim neighbors and the hub with at least \(m-2\ge2\) white spoke neighbors. Thus all hub-containing minimum sets are the \(H_x\).

Suppose now that all three seeds lie on the rim. Before the hub first becomes blue, no blue spoke can force a white rim neighbor: the white hub would be an additional white neighbor. A spoke can force the hub only after that spoke and both its adjacent rim vertices are blue. A working process therefore requires an initially adjacent rim pair (or the three consecutive vertices centered at a spoke, which already contain such a pair). If the three seeds have no adjacent rim pair, no initial force can occur: an intermediate has two white rim neighbors, and a spoke cannot force without both rim neighbors blue. With an adjacent pair, the only active pre-hub propagation takes place in the interspoke path containing that pair, up to one or both endpoint spokes. A third seed elsewhere cannot start a second propagation on its own. For a spoke at an endpoint to acquire blue neighbors on both sides before the hub turns blue, this third seed must therefore be the rim neighbor immediately beyond that spoke, on the other interspoke path. The exceptional possibility that the spoke itself is one of the three seeds and both rim neighbors are the other two seeds is the common endpoint case \(\{v_{s-1},v_s,v_{s+1}\}\). This is precisely the \(A\)- or \(B\)-family above.

Conversely, every \(A_{s,k}\) or \(B_{s,k}\) works: start from its adjacent pair and force successively along that interspoke path until the designated boundary spoke \(v_s\) and its near rim neighbor are blue. The third seed already colors the rim neighbor on the far side of \(v_s\), so \(v_s\) forces the hub. Once the hub is blue, the existing adjacent rim pair propagates through all remaining rim vertices. This proves the classification and the stated minimum size.

For each spoke, the \(L\) choices of \(A_{s,k}\) and \(L\) choices of \(B_{s,k}\) have the sole overlap \(A_{s,L-1}=B_{s,0}\). The families belonging to distinct spokes are disjoint, since the unique first cross-spoke meeting pattern determines the spoke (with \(m\ge4\), the relevant paths are distinct). There are \(N=mL\) hub-containing sets and \(m(2L-1)\) other sets, totaling \(m(3r+2)\).

**2. Reconfiguration and connectivity.** All reconfiguration vertices are triples, so two vertices are adjacent exactly when they share two graph vertices. This, together with the preceding explicit set list, gives the entire reconfiguration graph without hidden choices. Among hub-containing sets the only exchanges are
\[
 H_x\longleftrightarrow H_{x-1},\qquad H_x\longleftrightarrow H_{x+1};
\]
these induce the cycle \(C_N\). Every \(A_{s,k}\) contains the adjacent rim pair \(\{v_{s-L+k},v_{s-L+k+1}\}\), and every \(B_{s,k}\) contains \(\{v_{s+k},v_{s+k+1}\}\). Replacing its remaining vertex by the hub reaches a corresponding \(H_x\) in one exchange. Hence all minimum sets lie in one connected reconfiguration component. Going from each endpoint to the hub cycle, traveling at most \(\lfloor N/2\rfloor\) cycle edges, and exiting proves the diameter bound.

**3. Degrees and edges.** For an unordered pair \(P\) of graph vertices let \(\mu(P)\) denote the number of classified minimum sets containing it. Then for any minimum triple \(T\),
\[
 \deg_{\mathcal R}(T)=\sum_{P\in\binom{T}{2}}\bigl(\mu(P)-1\bigr).
\]
No neighbor is counted twice because two distinct triples cannot share two distinct two-element subsets. Every rim edge occurs in exactly three listed triples, and every hub--rim pair in exactly two; hence each \(H_x\) has degree \(1+1+2=4\).

For \(A_{s,k}\), put \(a=v_{s+1}\), \(b=v_{s-L+k}\), and \(c=v_{s-L+k+1}\). Directly listing all occurrences of the three pairs \(\{a,b\},\{a,c\},\{b,c\}\) in the displayed \(H,A,B\) families gives the following *pair multiplicity* table (the columns are ordered as written):

| Parameter | \(\mu(\{a,b\})\) | \(\mu(\{a,c\})\) | \(\mu(\{b,c\})\) | Degree |
|:--|--:|--:|--:|--:|
| \(L=2,\ k=0\) | 1 | 3 | 3 | 4 |
| \(L\ge3,\ k=0\) | 1 | 2 | 3 | 3 |
| \(L\ge4,\ 1\le k\le L-3\) | 2 | 2 | 3 | 4 |
| \(L\ge3,\ k=L-2\) | 2 | 3 | 3 | 5 |
| \(k=L-1\) | 3 | 3 | 3 | 6 |

The enumeration follows from three simple location rules: each adjacent rim pair occurs with its hub and with the two opposite-neighbor singleton choices at the adjacent spokes; a nonadjacent pair in different interspoke paths occurs only with a unique intervening spoke's near-neighbor pattern; and the near-boundary nonadjacent pair gains its third occurrence when one endpoint is at distance one from that spoke. The table may also be checked by substituting the displayed three families directly and solving the two-element containment equalities modulo \(N\), noting that \(m\ge4\) prevents a remote wraparound match. Rim reversal carries the \(A\)-cases into \(B\)-cases in reverse order; \(B_{s,0}\) is already the shared last \(A\)-case.

For \(L\ge3\), every spoke contributes one degree-six triple, two degree-five triples, two degree-three triples, and \(2(L-3)\) degree-four non-hub triples. Adding the \(mL\) degree-four hub triples gives \(3m(L-2)=3m(r-1)\) degree-four vertices. For \(L=2\), each spoke contributes two degree-four non-hub triples and one degree-six triple; with the \(2m\) hub triples this gives \(4m\) degree-four vertices. Summing degrees in either case gives \(2m(6r+5)\), whence \(|E(\mathcal R(G))|=m(6r+5)\) by the handshaking lemma. All statements follow.

## Verification

The standalone standard-library program `verify_gear.py` builds each graph from its adjacency definition, tests every two-vertex initial set and every three-vertex initial set under the ordinary color-change rule, constructs the exchange graph independently from shared two-element subsets, and checks all formulas, cycle adjacency and connectivity. It examines all \(\binom{m(r+1)+1}{3}\) triples for each \(4\le m\le8\) and \(1\le r\le6\). It checks 164,295 triples across 30 parameter choices; 2,250 are successful minimum sets. The output is recorded in `verification_output.txt`.

These finite tests are cross-checks of the constructive and algebraic proof above; they are not used to infer the unrestricted parameter theorem.

## Relationship to prior work

Anderton et al. [1] defined this generalized gear family and proved its zero-forcing number is three, with a discussion of possible initial configurations in their propagation-time analysis. Thus the scalar minimum and initial seed patterns are antecedents, not claimed as new. Geneson, Haas and Hogben [2] introduced the minimum-zero-forcing-set token-jumping graph and studied its connectivity for other graph families. Bong et al. [3] studied token addition/removal graphs using all feasible sets, a different state space and exchange rule. The present result is the explicit full token-jumping graph on minimum gear forcing sets, its connected hub-cycle backbone, complete degree distribution and edge formula. It is not a consequence of the already-known scalar zero-forcing number; it requires pairwise intersections among all optimal configurations.

## Limitations

The theorem is restricted to integer \(m\ge4\), \(r\ge1\), the ordinary zero-forcing rule, and one-vertex token exchanges among minimum sets. The three-spoke case is excluded: in the smallest case \(m=3,r=1\), the asserted degree and edge formulas do not hold. The diameter inequality is an upper bound, not an exact-diameter formula. No claim is made about token sliding, all-size forcing polynomials, or modified zero-forcing rules. Bibliographic searches cannot exclude unindexed equivalent results.

## References

[1] S. Anderton, R. Burden, M. Fontenot, N. Fredrickson, A. Kwon, S. Le, K. Mizozoe, E. Raign, A. Sangalli, H. Schuerger, A. Schwartz, *The zero forcing numbers and propagation times of gear graphs and helm graphs*, arXiv:2310.18513v1, first submitted 2023-10-27. https://arxiv.org/abs/2310.18513

[2] J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1, first submitted 2020-09-01. https://arxiv.org/abs/2009.00220

[3] N. H. Bong, J. Carlson, B. Curtis, R. Haas, L. Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668v1, first submitted 2022-05-19. https://arxiv.org/abs/2205.09668
