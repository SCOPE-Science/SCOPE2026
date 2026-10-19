# Optimal edge-colouring recolouring on the Petersen graph: two large components and frozen configurations

## Finding

Let \(P\) be the Petersen graph, realized as the Kneser graph \(KG(5,2)\): its vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with adjacency when the subsets are disjoint. Let \(\mathcal R_4(P)\) be the graph whose vertices are all proper edge-colourings \(c:E(P)\to\{0,1,2,3\}\), with two colourings adjacent precisely when they differ on one edge. The four colours are distinguished, and all four occur in every proper colouring since the Petersen graph has chromatic index four.

**Theorem.** The graph \(\mathcal R_4(P)\) has \(49{,}920\) vertices and \(109{,}440\) edges. It has exactly \(962\) connected components: \(960\) isolated colourings and two components of size \(24{,}480\) each. The isolated colourings form a single orbit under the natural action of \(S_5\times S_4\) (vertex-symbol permutations and palette permutations). Every palette permutation preserves each of the two large components; even symbol permutations preserve them, while odd symbol permutations interchange them.

The number \(49{,}920\) of proper edge-colourings was already recorded in OEIS A159233 and is included for normalization, **not** claimed as new. The contribution is the complete one-edge-recolouring component classification and the symmetry behavior.

## Assumptions and scope

All graphs are finite, simple, and undirected. A proper edge-colouring assigns different colours to incident edges. A recolouring step changes the colour of exactly one edge while maintaining propriety; switching two colours simultaneously on a Kempe chain is **not** a legal step. Colour names remain fixed along a path, though colour-name permutations act as automorphisms of the state graph.

One equivalent presentation is the generalized Petersen graph \(GP(5,2)\), with outer vertices \(u_i\), inner vertices \(v_i\), indices in \(\mathbb Z/5\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). An explicit isomorphism to the Kneser presentation is
\[
 u_i\longmapsto\{i,i+2\},\qquad v_i\longmapsto\{i+3,i+4\},
\]
with subscripts taken modulo five.

## Proof

**Missing-colour lemma.** For any proper four-edge-colouring of a cubic graph, each vertex \(v\) has one missing palette colour \(\mu_c(v)\). An edge \(uv\), currently coloured \(a\), can be recoloured if and only if \(\mu_c(u)=\mu_c(v)\). Indeed, three distinct colours occur at each endpoint and the only potentially admissible replacement colour is its missing colour. When the missing colours coincide, that common colour differs from \(a\) and from the colours of the four other edges incident with \(u\) or \(v\), so the replacement is valid. Consequently,
\[
 \deg_{\mathcal R_4(P)}(c)=\bigl|\{uv\in E(P):\mu_c(u)=\mu_c(v)\}\bigr|.
\]
In particular, an optimal edge-colouring is frozen exactly when its missing-colour vertex map is itself a proper vertex four-colouring.

**Complete finite enumeration.** The first executable certificate (`repro/verify_gp.py`) constructs \(GP(5,2)\) from the fifteen explicitly listed edges. It recursively assigns each of the four colours to each edge if the colour is absent from all earlier incident edges. Every proper assignment is obtained exactly once: a proper assignment follows a permitted branch at every step, while each final branch is proper. It builds every legal recolouring using the four incident-edge constraints and joins the endpoints using disjoint-set union.

A second, independent certificate (`repro/verify_kneser.py`) instead constructs the Kneser graph from the ten two-subsets, using bitmasks of colours already incident at each vertex. After complete backtracking, it forms a recolouring adjacency for each currently absent colour common to both endpoints. These conditions are necessary and sufficient by the missing-colour lemma. It independently computes the component-size distribution and checks the missing-colour degree count. No pruning by presumed symmetry or random sampling is used in either state enumeration.

Both exhaustive constructions give \(49{,}920\) legal colourings and \(109{,}440\) undirected recolouring edges. Exhaustive disjoint-set connectivity gives \(960\) components of order one and two of order \(24{,}480\), with no others. This proves the component count and the frozen count. The first certificate also computes the exact degree distribution
\[
 (n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7)
 =(960,1440,2880,10560,8640,12960,6720,5760),
\]
which has total \(49{,}920\) and degree sum \(218{,}880\).

**Symmetries.** Every permutation of the five underlying symbols permutes the ten Kneser vertices and fifteen edges, so it preserves recolouring adjacency. Similarly, each permutation of the four palette colours acts on states. The second certificate explicitly enumerates all \(5!\) symbol permutations and \(4!\) palette permutations. The orbit of one frozen colouring has exactly \(960\) distinct states; each is confirmed frozen, and the preceding exhaustive count shows that this is the entire frozen locus. For each of the two large components, the same certificate takes a representative state and checks all \(24\) palette permutations and all \(120\) symbol permutations: the palette action and the \(60\) even symbol permutations remain in the original component; the \(60\) odd symbol permutations land in the other large component. Since these permutations are state-graph automorphisms, their action on one representative determines their action on the whole connected component. Thus the claimed orbit and interchange statements follow.

## Verification

From the directory containing this file, run both standard-library-only programs with Python 3:

```sh
python3 repro/verify_gp.py
python3 repro/verify_kneser.py
```

Their captured reference outputs are `repro/verify_gp_output.txt` and `repro/verify_kneser_output.txt`, respectively. Both programs independently assert the vertex total, edge total, full component histogram, and frozen-state total before printing `VERIFY_OK`. The second independently asserts the group-orbit and component-interchange results. The mathematical proof of completeness is the finite search-space argument above; the outputs are only checkable traces of this complete computation. No assertion is made about other snarks, palettes, or simultaneous Kempe moves.

## Relationship to prior work

The one-edge reconfiguration model is that of Osawa, Suzuki, Ito, and Zhou, *The Complexity of (List) Edge-Coloring Reconfiguration Problem*, arXiv:1609.00109v1 (public 2016-09-01). Their theorems classify computational hardness for classes of input graphs; they do not give the fixed Petersen graph's optimal-palette component census. Ito, Kawamura, and Zhou, *An Improved Sufficient Condition for Reconfiguration of List Edge-Colorings in a Tree* (2012), treat trees, so their connectivity hypotheses cannot be specialized to this cyclic cubic graph.

OEIS A159233, originally entered 2009-04-06, already tabulates \(49{,}920\) proper four-edge-colourings of the Petersen graph, equivalently proper vertex four-colourings of its line graph. The raw count does not determine which states are mutually reachable or which are frozen. In a later graph-recolouring survey (Bousquet, habilitation manuscript, Chapter 3, Figure 3.11), a **five**-edge-colouring of the Petersen graph is exhibited as frozen. That different-palette example does not establish the four-colour frozen-state count or the two nontrivial components here. The reconfiguration problem also differs from Kempe interchange, which may recolour multiple edges at once.

## Limitations

This theorem concerns only the Petersen graph with the minimal four-colour edge palette and single-edge updates. It does not characterize analogous graphs for larger snarks, allow lists of permitted colours, or determine component diameters. The count \(49{,}920\) is prior knowledge. The new reachability and symmetry claims were checked by exhaustive finite computation with independently constructed graphs but have not received independent external scientific audit. The literature comparison cannot exclude an unindexed equivalent finite census.

## References

1. H. Osawa, A. Suzuki, T. Ito, and X. Zhou, *The Complexity of (List) Edge-Coloring Reconfiguration Problem*, arXiv:1609.00109v1, submitted 2016-09-01. https://arxiv.org/abs/1609.00109
2. T. Ito, K. Kawamura, and X. Zhou, *An Improved Sufficient Condition for Reconfiguration of List Edge-Colorings in a Tree*, IEICE Trans. Inf. Syst. E95.D (2012), 737–745, https://doi.org/10.1587/transinf.E95.D.737
3. OEIS Foundation, A159233, *Number of edge colorings of the Petersen graph*, originally entered 2009-04-06, https://oeis.org/A159233
4. N. Bousquet, habilitation manuscript, Chapter 3, Section on line graphs and Figure 3.11, https://perso.liris.cnrs.fr/nbousquet/Habilitation_defense.pdf
