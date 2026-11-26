# The first crown whose perfect-matching switch diameter exceeds its part size

## Finding

Let \(C_n\) be the simple bipartite graph obtained from \(K_{n,n}\) by removing the matching \(\{ii':1\le i\le n\}\). Let \(F_n\) be the graph whose vertices are the labelled perfect matchings of \(C_n\), with adjacency given by one alternating four-cycle switch. Among \(n\ge4\), the least part size at which \(F_n\) is connected with diameter greater than \(n\) is \(n=9\).

The finite exclusion of smaller part sizes is given by these exact results; every listed graph is connected.

| \(n\) | Order | Size | Radius | Diameter |
|:---:|---:|---:|---:|---:|
| 4 | 9 | 12 | 3 | 3 |
| 5 | 44 | 120 | 4 | 4 |
| 6 | 265 | 1,260 | 5 | 6 |
| 7 | 1,854 | 13,440 | 6 | 7 |
| 8 | 14,833 | 152,040 | 7 | 8 |

At \(n=9\), the connected graph has diameter ten. That endpoint and the complete inverse-antipode classification at nine are also given in [1]. The contribution considered here is the first-occurrence conclusion, supported by the exact smaller-order calculations, not a separate claim of novelty for the nine-symbol antipode census.

## Assumptions and proof

The forbidden matching is fixed and both parts are individually labelled. A state assigns column \(\pi(i)\) to row \(i\); the bijection \(\pi\) must have no fixed points. All switch paths are in this labelled graph. Given two rows \(i<j\), replacing their occupied columns with those columns exchanged is a switch precisely when \(\pi(i)\ne j\) and \(\pi(j)\ne i\). Those inequalities are exactly the absence of a forbidden diagonal edge after the swap. Every alternating square switch acts on two rows in this way, so there are no other edges to consider.

Conjugation by \(\sigma\in S_n\) corresponds to simultaneous row and column relabelling and preserves switch adjacency. Thus every derangement of a given cycle type has the same eccentricity. Relabelling is used only to select sources before searching, never as a move.

For each \(4\le n\le8\), exhaust the \(n!\) labelled permutations, discarding fixed-point states. For every retained state generate neighbors using the two-row rule above; count each edge once, or divide the degree sum by two. The degree at \(\pi\) can also be counted as \(\binom n2-n+c_2(\pi)\), since the \(n\) forbidden ordered pairs \((i,\pi(i))\) correspond to distinct unordered pairs except for the double counts of the \(c_2(\pi)\) two-cycles. Then run breadth-first search from a representative of every distinct sorted cycle-length list in the retained states. For clarity, the following are the exact maximum reached distances by source type, with a breadth-first traversal of the entire order shown in the preceding table in each case.

| \(n\) | Cycle type → eccentricity |
|:---:|:---|
| 4 | \((2,2)\to3\), \((4)\to3\) |
| 5 | \((2,3)\to4\), \((5)\to4\) |
| 6 | \((2,2,2)\to5\), \((2,4)\to5\), \((3,3)\to6\), \((6)\to5\) |
| 7 | \((2,2,3)\to7\), \((2,5)\to6\), \((3,4)\to7\), \((7)\to6\) |
| 8 | \((2,2,2,2)\to7\), \((2,2,4)\to7\), \((2,3,3)\to8\), \((2,6)\to7\), \((3,5)\to8\), \((4,4)\to7\), \((8)\to7\) |

Breadth-first expansion labels a state at its shortest-path length upon discovery: the queue processes the layers of increasing distance, and every edge out of each layer is examined. Conjugation and exhaustive permutation enumeration therefore make the minima and maxima of these representative eccentricities the exact radii and diameters in the first table. For \(n=9\), the same switch graph is connected of diameter ten by [1, Finding and Complete shortest-path certificate]. It is also recomputed as an endpoint check in the bundled programs. The five smaller diameters are all at most their part sizes, proving the minimum part size claim without any inference about larger orders.

## Reproduction and relationship to existing results

The bundled `verify_python.py` and `verify_cpp.cpp` enumerate the full finite spaces and perform breadth-first searches, respectively using adjacency lists and on-demand switch generation. The Python output gives the summary rows for all six sizes and the nine-symbol profiles. The C++ output also gives the smaller per-type profiles: its `results` entries for \(n=4,\ldots,8\) contain the `types` rows tabulated here. Neither program uses random sampling or identifies states along paths up to relabelling.

Dyer, Jerrum and Müller [2, Lemma 2] prove a diameter bound of \(n\) for the chordal bipartite case. The crown family is outside that hypothesis: selecting three corresponding row and column labels induces a chordless six-cycle. The finite calculation locates the first failure of the same numerical bound within crowns. Bonamy et al. [3] study the same type of switch on general matching spaces without providing this finite exclusion. Other derangement graphs use different adjacency: for instance Moshtagh and Shaveisi [4] join derangements that differ at every position, not derangements related by a legal transposition. Jain's *Transpositions in Derangements* is a relevant same-object comparison; its full text was not available for inspection, so historical priority is not claimed. The result does not address asymptotic diameter, adjacent-position swaps, or mixing time.

## References

1. *Unique antipodes in the nine-symbol derangement switch graph*, Finding and Complete shortest-path certificate. https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-unique-antipodes-in-the-nine-symbol-derangement-switch-graph--6d5778bc7d5d/RESULT.md
2. M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725, Lemma 2. https://arxiv.org/abs/1501.07725
3. M. Bonamy et al., *The Perfect Matching Reconfiguration Problem*, MFCS 2019, DOI:10.4230/LIPIcs.MFCS.2019.80. https://arxiv.org/abs/1904.06184
4. H. Moshtagh and F. Shaveisi, *Some results on the graph of derangements*, DOI:10.22034/as.2025.22570.1763, Abstract. https://as.yazd.ac.ir/article_3888.html
