# Sequential edge orders from internal chords of alternating cycle factors
## Finding
Let \(G\) be any finite simple cubic graph, equipped with a fixed proper edge colouring \(c:E(G)\to\{B,H,R\}\). Let \(F\) be the spanning subgraph formed by the edges coloured \(B\) or \(H\). It is a disjoint union of even cycles. Suppose **each component cycle of \(F\) has a chord coloured \(R\)**: that is, an edge of colour \(R\) whose two endpoints belong to that same cycle. Then there exists a total ordering \(\prec\) of \(E(G)\) such that, for every edge \(uv\), the sequences of incident edge colours at \(u\) and \(v\), read in increasing \(\prec\)-order, differ.

In particular, this applies whenever the fixed proper colouring has a **bichromatic Hamiltonian cycle**. It includes an infinite nonbipartite family: for every integer \(k\ge 1\), the graph obtained by adding the antipodal matching to \(C_{4k}\), with the cycle edges alternately coloured \(B,H\) and matching edges coloured \(R\), has a distinguishing global edge order. The ordering can be constructed in time \(O(|V(G)|+|E(G)|)\) from the coloured adjacency lists.

## Assumptions and scope
All graphs are finite, simple, undirected, and cubic (all vertex degrees equal three); connectedness and bipartiteness are not assumed. A proper three-edge-colouring assigns different colours to the three incident edges at each vertex. A red chord is a red edge joining two **nonconsecutive** vertices of one of the alternating cycles. The hypothesis is sufficient, not claimed necessary. The edge ordering is chosen for the **specified fixed edge colouring**, not by recolouring.

For an edge order \(\prec\), write \(s_{\prec}(v)\) for the three-term word of colours encountered at vertex \(v\). The condition is \(s_{\prec}(u)\ne s_{\prec}(v)\) for all \(uv\in E(G)\). The two-factor contains no cycle of length two, by simplicity; its cycles have even lengths at least four. The red edges form a perfect matching.

## Proof
**Step 1: order each alternating cycle.** Since \(c\) is proper and \(G\) is cubic, each vertex has exactly one edge of each colour. Consequently the \(B,H\) edges form an alternating even cycle factor \(F\), and the \(R\) edges form a perfect matching. Take a cycle \(C\) of length \(\ell\), and select a red chord. Choose one endpoint of this chord to be \(v_0\). Enumerate the vertices cyclically as \(v_0,v_1,\ldots,v_{\ell-1}\), in whichever of the two directions gives the edge \(v_0v_1\) colour \(B\). Write \(e_i=v_{i-1}v_i\) for \(1\le i<\ell\) and \(e_\ell=v_{\ell-1}v_0\). List the cycle edges in order \(e_1,e_2,\ldots,e_\ell\); the colours alternate \(B,H,B,H,\ldots,H\).

**Step 2: insert internal red chords.** The chosen red chord joins \(v_0\) to some \(v_j\), with \(2\le j\le\ell-2\): adjacency to either cyclic neighbour would duplicate a cycle edge. Insert this chord **immediately after \(e_1\)** and before \(e_2\). Thus it is later than the \(B\) edge and earlier than the \(H\) edge at \(v_0\); at \(v_j\) it precedes both cycle edges.

Any other red chord has endpoints \(v_i,v_j\) with \(1\le i<j\le\ell-1\). Simplicity forces \(j\ge i+2\). Insert this chord in the gap immediately after \(e_{i+1}\) and before \(e_{i+2}\). This gap lies after both cycle edges incident with \(v_i\), namely \(e_i,e_{i+1}\), and before both edges incident with \(v_j\), namely \(e_j,e_{j+1}\), because \(j\ge i+2\). Insertions preserve the relative order of the cycle edges. If several chords share a gap, resolve their order arbitrarily; the endpoint inequalities remain true. Every vertex has exactly one red edge, so no vertex's red-edge position can be affected by another insertion.

**Step 3: insert red edges between cycles.** Perform Step 1 and Step 2 for every alternating cycle and concatenate the resulting cycle blocks in an arbitrary order \(C_1,\ldots,C_t\). For a red matching edge with endpoints on different cycles \(C_a,C_b\), say \(a<b\), insert it **between the whole block for \(C_a\) and the next cycle block**. It then occurs after both cycle edges at its endpoint in \(C_a\), and before both cycle edges at its endpoint in \(C_b\). The positions of different such edges within the same inter-block gap can be arbitrary. Every edge is now ordered exactly once.

**Step 4: check edges.** At each selected root \(v_0\), the resulting colour word is precisely \((B,R,H)\). At every nonroot vertex, its red edge appears either before both its cycle edges or after both; in particular, red is **not** the middle colour. Thus every edge of the \(B,H\) cycle factor incident with a root has distinct endpoint words.

At nonroot vertices \(v_i\), the order of the \(B\) and \(H\) entries is controlled by parity: for odd \(i\), the \(B\) entry precedes the \(H\) entry; for even \(i\), the \(H\) entry precedes the \(B\) entry. Therefore every cycle edge whose endpoints are both nonroots joins vertices with **opposite relative \(B,H\) order**, hence different complete three-colour words.

For a red matching edge, either it is the selected root chord, in which case its endpoints have red in the middle versus first position; or it is another internal chord or an inter-cycle red edge, in which case its endpoints have red last versus first. In all cases the endpoint words differ. Every edge has therefore been checked, so \(\prec\) is distinguishing. The construction uses lists and insertion buckets indexed by cycle-edge gaps, and requires linear work.

**Corollaries.** If \(F\) is Hamiltonian, all red matching edges have both endpoints in its unique cycle; hence the hypothesis holds. For the antipodal-matching family on \(C_{4k}\), every matching edge is such a chord, yielding the asserted order. These examples are genuinely nonbipartite: an antipodal edge and an arc of \(2k\) cycle edges form an odd cycle of length \(2k+1\).

## Verification
Run `python3 verify_sequential_chords.py` with Python 3 (standard library only). The supplied `verify_sequential_chords_output.txt` records the actual output. The verifier independently reconstructs the global edge order and checks that each vertex receives precisely the three distinct colours and that no edge has equal endpoint words.

For one alternating Hamiltonian cycle, every admissible chord matching is exhaustively tested for cycle lengths \(4,6,8,10,12\), giving respectively \(1,4,31,293,3326\) matchings. Among those, the numbers of nonbipartite instances are respectively \(1,3,29,280,3246\). A reproducible pseudorandom test also checks \(972\) matching configurations with two to four alternating cycles, with at least one chord per cycle. The Möbius ladder construction is checked for each \(1\le k\le25\). All produced orders passed the direct adjacency tests.

These finite computations corroborate the construction but are not an exhaustive proof for unbounded graphs; the argument in **Proof** handles all allowed orders and sizes.

## Relationship to prior work
Gorzkowska and Kwaśny [1] introduced the fixed-colouring global edge-ordering problem, proved a palette-distinction theorem (covering connected nonregular and class-two graphs), and established the assertion for regular degrees at least six. Their Conjecture 10 includes fixed proper colourings of cubic graphs; their inspected full text does not provide a theorem for the present coloured alternating-cycle/chord class. Every graph here is regular of degree three with the same three-colour palette at each vertex, so their established sufficient conditions do not imply this theorem.

An earlier published neighbourhood-block-order criterion [2] applies to a class of bipartite colourings and, in particular, regular bipartite degrees at least five; it gives no nonbipartite cubic result. Bipartite special instances of the present theorem may follow from broader bipartite constructions, but the new part includes infinitely many nonbipartite three-edge-coloured cubic graphs, already including \(K_4\). The proof provides a single constructive mechanism for an arbitrary number of alternating cycles with both internal and cross-cycle matching edges.

## Limitations
The alternating-factor chord hypothesis is sufficient and not asserted necessary. The proof does not settle all three-edge-colourings of all cubic graphs, all colourings of Hamiltonian cubic graphs, or cubic graphs requiring four edge colours. It does not establish the full Conjecture 10. Published-text comparison cannot exclude unindexed equivalent work. The verification program tests finite cases only; independent external validation has not been performed.

## References
1. A. Gorzkowska and J. Kwaśny, *Distinguishing adjacent vertices by ordering edges*, arXiv:2609.11832v1, September 10, 2026. https://arxiv.org/html/2609.11832v1
2. *A local-lemma criterion for sequential edge orderings in bipartite graphs*, September 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-sequential-edge-ordering-five-regular-bipartite--a144974e257a
