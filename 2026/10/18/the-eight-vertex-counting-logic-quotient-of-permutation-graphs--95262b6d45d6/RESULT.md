# The eight-vertex counting-logic quotient of permutation graphs

## Finding

Let \(\mathcal P_n\) be the set of isomorphism types of finite, uncoloured, simple **permutation graphs** on \(n\) vertices, interpreted in the adjacency-only signature. Let \(p_n=|\mathcal P_n|\) and let \(q_n\) count the equivalence classes under two-variable first-order logic with counting \(C^2\), equivalently one-dimensional colour refinement. The exact finite profiles through order eight are:

| \(n\) | \(p_n\) | \(q_n\) | Non-singleton class multiplicities |
|---:|---:|---:|:---|
| 1 | 1 | 1 | none |
| 2 | 2 | 2 | none |
| 3 | 4 | 4 | none |
| 4 | 11 | 11 | none |
| 5 | 33 | 33 | none |
| 6 | 142 | 140 | two doubletons |
| 7 | 776 | 770 | six doubletons |
| 8 | 5699 | 5654 | 38 doubletons, two tripletons, one quadrupleton |

In particular, every two nonisomorphic permutation graphs on at most five vertices are distinguished by \(C^2\), and six vertices are **sharp** for first failure. There are exactly two indistinguishable nonisomorphic pairs at six vertices, with seven and eight edges respectively. The eight-vertex layer has exactly 41 non-singleton logical classes and 45 excess isomorphism types beyond its logical-class count.

## Assumptions and scope

A permutation graph has vertices indexed by \(1,\ldots,n\) and edges between \(i<j\) precisely when \(\pi(i)>\pi(j)\) for some permutation \(\pi\). The permutation is only a presentation: **only the uncoloured graph adjacency relation** is in the model-theoretic signature. Graph isomorphism can identify different permutation presentations. Two graphs are compared at the same order; distinct orders are distinguished by counting the domain. The classification makes no claim about larger graphs or about individual identification among all graphs outside the permutation-graph class.

## Proof

**Complete enumeration.** For fixed \(1\le n\le8\), list all \(n!\) permutations and form the corresponding symmetric, loopless inversion adjacency matrix. By the definition of permutation graphs, this generates every member of \(\mathcal P_n\), possibly repeatedly. Each graph is a tuple of binary adjacency masks. The program `verify_permutation.py` exhaustively groups these representations using exact graph isomorphism: a NetworkX isomorphism test searches adjacency-preserving vertex bijections. Graphs are partitioned by their refinement signatures first, an isomorphism-invariant necessary condition, and all collisions within a signature are tested against every retained isomorphism representative.

**Exact logic quotient.** The initial vertex colour is constant. At every round a new colour is the complete pair consisting of the previous colour and the multiset of neighbour colours. The program *globally interns these pairs across all generated graphs of fixed order*, without hashes. For each graph it records the multiset of vertex colours and groups all graphs with equal signatures. It compares the induced partitions after \(n\) and \(2n\) rounds and asserts equality; \(2n\) is sufficient for any pair of \(n\)-vertex graphs because their disjoint union has at most \(2n\) vertices. Standard finite-model-theoretic results identify stable ordinary colour-refinement equivalence with \(C^2\)-equivalence [1]. The exact enumeration yields every table entry and the multiplicity distribution.

**Explicit first obstruction layer.** To specify each exceptional graph unambiguously, number vertices \(0,\ldots,5\) and give the six adjacency bit masks (bit \(j\) denotes an edge to vertex \(j\)). The two unordered pairs are:

* Seven-edge pair: \((10,9,56,7,36,20)\) versus \((20,52,3,48,11,10)\).
* Eight-edge pair: \((24,56,56,7,7,6)\) versus \((42,9,56,7,36,21)\).

For each pair the exact shared-colour certificate shows \(C^2\)-equivalence and NetworkX graph-isomorphism testing establishes nonisomorphism. Each pair contains two **connected** graphs, so neither is an artefact of disconnected components. The first pair has vertex-degree multiset \((2,2,2,2,3,3)\), the second \((2,2,3,3,3,3)\); the pairs therefore occupy different logical classes. The distinct graphs have respectively seven and eight edges, as stated. Full uniqueness follows from the exhaustive isomorphism and logical-class partition, not just these example checks.

## Verification

Install the optional but precisely pinned dependency with `python3 -m pip install -r requirements.txt`. Then execute `python3 verify_permutation.py`, comparing its complete stdout with `verify_output.txt` and its terminal `EXACT_PERMUTATION_VERIFY_OK`. This authoritative certificate uses **exact**, globally shared, unhashed vertex colours and NetworkX's exact isomorphism routines. The separate implementation `verify_independent.py` uses another permutation enumeration and hashing-based WL signatures, with its output recorded in `independent_output.txt`; its probabilistic hashes are corroborative only. Both programs regenerate all permutations through length eight and require no downloaded input graph data.

## Relationship to prior work

The raw isomorphism counts \(1,2,4,11,33,142,776,5699\) are pre-existing data, documented in OEIS A123448 and the published permutation-graph catalog [2,3]. They are not claimed as new. The equivalence between \(C^2\) and colour refinement and the existence of regular/biregular obstructions are established by Arvind, Köbler, Rattan and Verbitsky [1]. Guo, Gavrilyuk and Ponomarenko [4] prove an 18-dimensional Weisfeiler–Leman *upper bound* for permutation graphs, rather than a one-dimensional small-order census. The contribution here is the exact quotient count and non-singleton class distributions, especially the complete sharp two-pair six-vertex layer. The inspected sources and targeted research searches did not state this particular finite classification, but an earlier specialist tabulation or a derivation from broader colour-refinement theory remains possible.

## Limitations

This is a fully reproducible finite computation for \(n\le8\), not an all-order formula, an independent expert audit, or proof that no historical account derives the same counts. The enumeration’s correctness relies on its disclosed code and the correctness of exact graph-isomorphism software; an independently coded variant reduces but cannot eliminate implementation risk. The known raw permutation-graph counts and the general logical framework remain prior art.

## References

[1] V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public 2015-02-04. https://arxiv.org/html/1502.01255v3

[2] OEIS A123448, *Number of permutation perfect graphs on n nodes*, initiated 2006-10-18. https://oeis.org/A123448

[3] R. Uehara, *Graph and Puzzle Catalogs*, nonisomorphic permutation graphs through order eight. https://www.jaist.ac.jp/~uehara/graphs/

[4] J. Guo, A. Gavrilyuk, I. Ponomarenko, *On the Weisfeiler–Leman Dimension of Permutation Graphs*, arXiv:2305.15861v1 (2023). https://arxiv.org/pdf/2305.15861
