# The Heawood locating-dominating exchange graph: four symmetry orbits and a one-move detour bound

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the seven-point Fano plane, and call \(S\subseteq V(H)\) a **locating-dominating set** when every vertex outside \(S\) has a nonempty, distinct open-neighborhood intersection with \(S\). It was previously proved that the minimum possible size is \(6\) [1, Proposition 24].

Define \(\mathcal L(H)\) to have as vertices all minimum locating-dominating sets, with an edge between \(S\) and \(T\) when \(|S\setminus T|=|T\setminus S|=1\). Then \(\mathcal L(H)\) has exactly **448 vertices and 3192 edges**, is connected, and has radius and diameter \(6\). Each vertex has eccentricity \(6\), although the graph is irregular. Its complete degree polynomial is
\[
28z^{6}+168z^{12}+168z^{14}+84z^{22}.
\]

Under the full group of \(336\) automorphisms of \(H\), the vertices form four orbits. With the two bipartition classes regarded as Fano points and lines, the orbits have these intrinsic descriptions and distance-layer profiles (distances \(0,1,\ldots,6\)):

| Selected point count / induced graph of selected vertices | Orbit size | Exchange degree | Distance-layer profile |
|---|---:|---:|---|
| 2 or 4 points; \(2K_2\sqcup2K_1\) | 168 | 14 | (1, 14, 68, 148, 143, 64, 10) |
| 3 points; \(2K_2\sqcup2K_1\) | 84 | 22 | (1, 22, 67, 144, 134, 66, 14) |
| 3 points; \(3K_2\) | 28 | 6 | (1, 6, 69, 162, 135, 66, 9) |
| 3 points; \(P_4\sqcup2K_1\) | 168 | 12 | (1, 12, 68, 140, 152, 69, 6) |

For any two minimum sets \(S,T\), put \(j(S,T)=6-|S\cap T|\). Then the **sharp one-extra-exchange bound** is
\[
 j(S,T)\le d_{\mathcal L(H)}(S,T)\le j(S,T)+1.
\]
Of the \(\binom{448}{2}=100128\) unordered distinct pairs, exactly \(2940\) require the extra exchange: \(1008\) pairs have \((j,d)=(2,3)\), \(1428\) have \((j,d)=(3,4)\), and \(504\) have \((j,d)=(4,5)\). Every other pair attains the set-difference lower bound. The complete unordered-pair distance distribution at distances \(1\) through \(6\) is
\[
(3192,15204,32508,32298,14868,2058).
\]

## Assumptions and scope
All graphs here are finite, simple, and undirected. The Fano plane has points represented by the seven nonzero vectors \(p\in\mathbb F_2^3\) and lines represented by nonzero normals \(\ell\in\mathbb F_2^3\), with incidence exactly when \(p\cdot\ell=0\) in \(\mathbb F_2\). The Heawood graph has 14 vertices and 21 incidence edges. The selected code vertices need not locate one another: the requirement concerns only vertices outside the selected set. The exchange is **unrestricted token jumping**, not token sliding along a Heawood edge, and every intermediate configuration must remain a minimum locating-dominating set.

## Proof
**Membership and optimality.** For a candidate \(S\), the signatures \(N_H(v)\cap S\) for \(v\notin S\) are computed exactly. Nonempty pairwise distinct signatures are by definition necessary and sufficient for locating domination. In the first standalone certificate, every \(\binom{14}{k}\) subset with \(0\le k\le5\) fails this test, and all \(\binom{14}{6}=3003\) candidates of size six are tested. Exactly \(448\) pass. The known independent proof of minimum size six is [1, Proposition 24]; the exhaustive check also proves this finite lower bound without relying on that paper.

**Exact exchanges.** Encode a selected subset by a 14-bit integer. For each passing size-six mask, try all six deletions and all eight insertions; retain the result precisely when it is one of the \(448\) passing masks. This produces every edge of \(\mathcal L(H)\), with no pruning by symmetry. The 448 row degrees sum to \(6384\), giving \(3192\) edges and the degree polynomial above. The standalone certificate `verify_cyclic.py` uses instead the Hamiltonian 14-cycle plus the seven chords \((0,5),(1,10),(2,7),(3,12),(4,9),(6,11),(8,13)\), independently of the point-line implementation.

**The four orbits.** Every invertible binary linear transformation of the three-dimensional point space induces a permutation of its seven points and the contragredient permutation of lines. The \(168\) such transformations, together with point-line duality, give \(336\) graph automorphisms. The second certificate constructs these as explicit 14-vertex permutations, verifies every incidence edge and nonedge, and computes complete orbits of the \(448\) passing sets. Exactly four orbits occur, with sizes \(28,84,168,168\). Direct inspection of all selected induced subgraphs gives the four descriptions in the table; no fifth selected-set type occurs. The original 14-vertex graph has no additional automorphisms: an automorphism preserving points induces a collineation of the Fano plane and therefore is one of the \(168\) binary linear transformations; any automorphism exchanging the bipartitions is a collineation composed with duality.

**Distances and detours.** A single exchange replaces one selected vertex, so every transformation from \(S\) to \(T\) uses at least \(j(S,T)\) exchanges. In `verify_cyclic.py`, ordinary breadth-first search is performed from *each* of the \(448\) states over the complete constructed edge set. Every search reaches all 448 states and has greatest distance six. The certified pair-distance histogram and pairwise values of \(d-j\) are precisely those displayed above; none exceeds one. For a separate calculation, `verify_fano.py` runs BFS from one representative of each of the four orbits and multiplies the resulting all-target counts by orbit size. Graph automorphisms preserve distances, so this weighting gives the exact ordered-pair histogram; subtracting the \(448\) diagonal pairs and dividing by two gives the unordered histogram. Both routes give the same distance counts and the same \(2940\) exceptional pairs. Each orbit representative has eccentricity six, hence all 448 vertices do.

These are complete finite proofs by explicit deterministic enumerations with fully specified domains and predicates, not estimates from random search or extrapolation to other incidence graphs.

## Verification
Run the two attached Python 3 scripts without external packages:

```sh
python3 verify_cyclic.py
python3 verify_fano.py
```

The first prints `CYCLIC_HEAWOOD_EXHAUSTIVE_PASS`; the second prints `FANO_GL3_SYMMETRY_CERTIFICATE_PASS` when all assertions succeed. The scripts use independent graph presentations, subset representations, and shortest-path counting strategies. The first exhausts the \(448\) BFS roots, while the second exhausts the \(336\) explicit automorphisms and four orbit representatives. Each verifies the full exchange metric and the precise detour census.

## Relationship to prior work
Balbuena, Foucaud, and Hansberg [1] proved \(\gamma^{LD}(H)=6\) by a direct contradiction argument; they display an optimal six-vertex set. The earlier minimum value is not proposed as new. The inspected full-text section containing Proposition 24 supplies neither the 448-set census nor an exchange-graph distance analysis. Haas and Seyffarth [2] study reconfiguration of ordinary dominating sets, including single-vertex exchanges and addition/removal models; their feasibility condition is weaker than locating domination, so their results do not imply these counts or distances. Suzuki, Mouawad, and Nishimura [3] examine addition/removal reconfiguration of ordinary dominating sets, likewise not the fixed-size locating-dominating exchange graph. The novelty asserted here is confined to the exact 448-state classification, four-orbit structure, and complete metric/detour results. An equivalent unindexed historical computation is possible.

## Limitations
The theorem concerns the Heawood graph alone, not all incidence graphs of projective planes, all cubic graphs, or all locating-dominating exchange graphs. Its claims are exact finite combinatorial statements supported by exhaustive executable certificates; they do not establish an asymptotic or general structural theorem. The full literature cannot be exhaustively certified, and an equivalent result in unindexed work remains possible. No evidence about token sliding, identifying codes, or nonminimum locating-dominating sets is inferred.

## References
[1] C. Balbuena, F. Foucaud, A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, Electron. J. Combin. 22(2), P2.15 (2015). First publicly posted 2014-07-27, arXiv:1407.7263. https://arxiv.org/abs/1407.7263 .

[2] R. Haas, K. Seyffarth, *The k-Dominating Graph*, Graphs Combin. 30 (2014), 609–617. arXiv:1209.5138. https://arxiv.org/abs/1209.5138 .

[3] A. Suzuki, A. E. Mouawad, N. Nishimura, *Reconfiguration of Dominating Sets*, Lecture Notes in Computer Science 8497 (2014). arXiv:1401.5714. https://arxiv.org/abs/1401.5714 .
