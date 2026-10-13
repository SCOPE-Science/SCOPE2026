# Minimum total length of maximum-cardinality binary non-overlapping codes through order ten

## Finding

Let \(S\) range over finite nonempty binary variable-length non-overlapping codes, as defined below, whose codewords have lengths from two through \(n\). Write \(m_n\) for the largest possible cardinality and \(T_n\) for the smallest sum of codeword lengths among codes of cardinality \(m_n\). **For every integer \(2\le n\le10\)** the following values are exact:

| Maximum permitted length \(n\) | Candidate words after binary normalization | Maximum cardinality \(m_n\) | Least total length \(T_n\) |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 1 | 2 |
| 3 | 3 | 1 | 2 |
| 4 | 6 | 1 | 2 |
| 5 | 12 | 2 | 9 |
| 6 | 22 | 3 | 16 |
| 7 | 42 | 5 | 32 |
| 8 | 79 | 8 | 59 |
| 9 | 153 | 14 | 119 |
| 10 | 295 | 24 | 227 |

In particular, every 24-word binary non-overlapping code with lengths in \([2,10]\) has total length at least \(227\), and the bound is attained. The attaining code uses thirteen words of length nine and eleven of length ten; its mean length is \(227/24\), compared with length ten for a uniform-length 24-word code. Exact witnesses for all nine orders are in `WITNESSES.json`.

## Assumptions and scope

A non-overlapping code \(S\subseteq\bigcup_{j=2}^n\{0,1\}^j\) is a nonempty set of distinct finite words satisfying two requirements: (i) no nonempty proper prefix of any word is equal to a nonempty proper suffix of any (possibly the same) word; (ii) neither of two distinct codewords is a contiguous factor of the other. All lengths here are **bit lengths**, with every codeword counted once. The optimizing cardinality is the maximum available **with word lengths at most \(n\)**, not a prescribed count below that maximum. Neither the bounds nor the existence witnesses assert anything at \(n>10\).

## Proof

**Binary normalization.** The one-symbol case of condition (i) makes the set of starting symbols and the set of final symbols disjoint. Both sets are nonempty, so for binary words each is a singleton, and the two symbols differ. Simultaneously complementing every bit preserves both non-overlap conditions and every length. We may therefore require that every word starts with `0` and ends with `1`. Condition (i), applied to the same word, further requires each candidate to be unbordered (no proper prefix equals a suffix). Enumerating every binary word of each length from two through \(n\), retaining just those three properties, produces an exhaustive finite vertex set \(V_n\).

**Exact compatibility.** Put an edge between two distinct vertices \(u,v\in V_n\) precisely when no nonempty proper prefix of either equals a proper suffix of the other and neither word occurs as a contiguous factor of the other. These are all pairwise obstructions; because each vertex is already unbordered, non-overlapping codes correspond exactly to cliques. Hence the largest clique size equals \(m_n\), and minimizing the sum of vertex lengths over largest cliques equals \(T_n\). This reduction is reversible and loses no admissible code through the normalization.

**Exhaustive finite certificate and justified pruning.** The self-contained `verify.py` enumerates every vertex in \(V_n\), constructs all compatibility bitsets, and performs two complete ordered recursive clique searches. At a search node with candidate set \(U\), it greedily partitions the induced compatibility graph into independent color classes. A clique contains at most one vertex from each such class, so the number of colors is a certified upper bound on how many further vertices it can use. The maximization search discards a branch only if this bound cannot improve its incumbent. The length minimization first fixes the already-proved largest cardinality and discards a branch only if the coloring excludes an adequately large clique, or the sum of the lengths of the required number of shortest available candidates (ignoring conflicts) cannot beat its incumbent. Both are valid lower/upper bounds; the recursion branches on every possible first selected vertex in a fixed order and thus cannot omit a better solution. Empty candidate sets and completed cliques are handled explicitly. The source implements every operation without a heuristic stopping condition or solver dependency.

The numbers in the table are the exhaustive outputs; a complete witness for each row is included in `WITNESSES.json`. To see the final sharp equality concretely, the 24-word order-ten witness is:

```
000000111, 000010111, 000100111, 000110111, 001000111, 001010111, 001100111, 0100000111, 010000111, 0100010111, 0100100111, 010010111, 0100110111, 0101000111, 010100111, 0101010111, 0101100111, 010110111, 0110000111, 011000111, 0110010111, 0110100111, 011010111, 0110110111
```

Every listed word starts with `0`, ends with `1`, is unbordered, is pairwise compatible with all other listed words, and their combined bit length is \(227\). The recursive lower-bound certificate rules out both a larger code and a 24-word code of total length at most \(226\).

## Verification

Run `python3 verify.py` from the directory containing the attached source. The Python standard-library-only checker recomputes all candidate lists, every compatibility edge, both exact searches, all witness lengths, and all non-overlap conditions at orders two through ten. Its expected final line begins `VERIFY_OK binary lengths 2..10`; there are 295 candidates at order ten. An independent 0–1 mixed-integer linear optimization in SciPy/HiGHS found the same order-ten optimum with certified zero optimality gap. The standalone checker, not the external optimizer, suffices to reproduce the claimed finite result.

## Relationship to prior work

Wang and Wang, *On the maximum size of variable-length non-overlapping codes* (first submitted 2024-02-29), explicitly formulate the minimum-average-length optimization for prescribed code cardinality and prove general lower bounds. Their theorem bounding variable-length cardinality by the fixed-length maximum does not determine the optimum total lengths here. Wang and Wang's 2021 generating-function construction addresses attainable code sizes. Stanovnik, Moškon and Mraz's 2023 work addresses maximum non-overlapping code sizes and constructions, not these mixed-length minima. The new calculation is a finite exact solution of the length-optimization problem at maximal cardinality over nine successive binary order limits, not a new general capacity bound.

## Limitations

No exact formula for arbitrary order, no result for a fixed submaximal code size, and no classification of all optimal word sets is claimed. The finite recursive proof is exhaustive only for the stated range. Research-index and literature comparisons may not detect unpublished or unindexed equivalent computations; the full text of a potentially related 2025 construction article was unavailable, and priority regarding that article is unresolved.

## References

1. Y. Wang and Q. Wang, *On the maximum size of variable-length non-overlapping codes*, arXiv:2402.18896, first version 2024-02-29, https://arxiv.org/html/2402.18896v1 .
2. Y. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934 (2021), https://arxiv.org/abs/2108.06934 .
3. M. Stanovnik, M. Moškon, and M. Mraz, *In search of maximum non-overlapping codes*, arXiv:2307.12593 (2023), https://arxiv.org/abs/2307.12593 .
4. Qin and Luo, *A generalized construction of variable-length non-overlapping codes*, DOI:10.1007/s10623-025-01585-0 (2025). Full text not inspected; priority risk remains.
