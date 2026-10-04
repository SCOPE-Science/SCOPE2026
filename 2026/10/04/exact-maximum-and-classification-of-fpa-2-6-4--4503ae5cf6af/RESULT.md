# Exact maximum and classification of \(FPA_2(6,4)\)
## Finding
For frequency permutation arrays \(C\subseteq\{0,1,2\}^6\) in which each symbol occurs exactly twice and every two distinct codewords have Hamming distance at least \(4\), the maximum size is exactly \(15\). Exactly \(12\) labeled maximum codes exist. In every maximum, forgetting symbol labels turns its codewords into exactly five perfect matchings of the six coordinate positions, with three codewords over each matching; those five matchings form a 1-factorization of \(K_6\). The six labeled 1-factorizations each support exactly two maxima. Under coordinate permutations and global permutations of the three symbols, all \(12\) maxima form one orbit, with stabilizer order \(360\).

One representative maximum code is:

```text
001122
010212
012021
021201
022110
100221
102012
112200
120102
121020
201210
202101
210120
211002
220011
```

Among the \(105\) unordered pairs of words in this representative, \(90\) pairs have Hamming distance \(4\) and \(15\) pairs have distance \(6\).

## Assumptions and scope
A frequency permutation array \(FPA_2(6,4)\) here is a subset of the \(90=6!/(2!)^3\) words of length \(6\) over \(\{0,1,2\}\) in which each symbol occurs exactly twice, with minimum Hamming distance at least \(4\). "Labeled" means that the six coordinate positions and the three symbols are fixed. The equivalence group used for the orbit statement is \(S_6\times S_3\), acting by coordinate permutations and one global symbol permutation.

## Proof
Construct the compatibility graph \(G\) on the \(90\) frequency-two words, joining two vertices exactly when their Hamming distance is at least \(4\). Codes in the stated class are exactly cliques of \(G\). The included verifier generates all \(90\) vertices from the multiset \(\{0,0,1,1,2,2\}\), builds \(G\) directly from Hamming distance, and enumerates every maximal clique by a deterministic bit-set Bron--Kerbosch search with pivoting. It finds the complete maximal-clique size distribution
\[
6:38895,\quad 7:20160,\quad 8:20520,\quad 9:10320,\quad 11:720,\quad 15:12.
\]
Hence no clique has more than \(15\) vertices, and the displayed clique proves attainability.

For the structural statement, associate to each word the perfect matching of the six coordinate positions obtained by grouping the two positions carrying each of the three symbols and then forgetting which pair has which symbol. For every one of the \(12\) maximum cliques, the verifier finds exactly five such perfect matchings, each occurring for exactly three codewords. Their \(15\) edges are pairwise distinct and therefore partition the edge set of \(K_6\); they form a 1-factorization. Across all maxima there are exactly six distinct labeled 1-factorizations, and each occurs for exactly two maximum codes.

Finally the verifier applies every element of \(S_6\times S_3\), a group of order \(4320\), to one maximum code. Its orbit is exactly the set of all \(12\) maxima, and exactly \(360\) group elements stabilize the representative, consistent with orbit--stabilizer.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `maxima.json`. A successful replay prints:

```text
VERIFY_OK words=90 maximum=15 labeled_maxima=12 factorizations=6 maxima_per_factorization=2 orbit_size=12 stabilizer=360 maximal_cliques=90627
```

The verifier reconstructs the words, Hamming graph, maximal cliques, 1-factorizations, and group action from definitions, then checks the packaged list of all \(12\) maxima.

## Relationship to prior work
Huczynska and Mullen introduced frequency permutation arrays and the notation \(M_\lambda(n,d)\), together with general constructions and bounds. Their first public arXiv version is dated 2005-11-07. The inspected full text defines the same Hamming-distance object and gives general bounds, but does not state the exact value \(M_2(6,4)\), enumerate the \(12\) maxima, or identify the 1-factorization structure.

Huczynska's later work studies equidistant frequency permutation arrays. The maxima classified here are not equidistant: their pair-distance multiset contains both \(4\) and \(6\), so an equidistant classification does not imply this result. The accessible portal record was inspected; the linked preprint was unavailable during comparison, so an unindexed statement there remains a residual literature risk.

Gillespie and Praeger study diagonally neighbour-transitive codes and frequency permutation arrays, with MSC classification including 94B60. Their inspected full text characterizes a symmetry-restricted family and group-generated permutation-code constructions; it does not enumerate all \(FPA_2(6,4)\) codes or imply the exact extremal census above.

## Limitations
This is a finite exact classification for the single parameter set \(\lambda=2,n=6,d=4\). The originality comparison cannot exclude an obscure unindexed table, thesis, or inaccessible preprint containing the same finite census. No claim is made for larger alphabets, larger lengths, or other distances.

## References
1. S. Huczynska and G. L. Mullen, "Frequency permutation arrays," arXiv:math/0511173, first public 2005-11-07; Journal of Combinatorial Designs 14 (2006), 463--478.
2. S. Huczynska, "Equidistant frequency permutation arrays and related constant composition codes," Designs, Codes and Cryptography 54 (2010), 109--120, DOI:10.1007/s10623-009-9312-0.
3. N. I. Gillespie and C. E. Praeger, "Diagonally neighbour transitive codes and frequency permutation arrays," Journal of Algebraic Combinatorics 39 (2014), 733--747, DOI:10.1007/s10801-013-0465-6.
