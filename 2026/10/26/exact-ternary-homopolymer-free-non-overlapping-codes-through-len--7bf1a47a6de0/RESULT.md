# Exact ternary homopolymer-free non-overlapping codes through length nine

## Finding

Fix the alphabet \(\Sigma=\{0,1,2\}\). A length-\(n\) word is **homopolymer-free** if successive symbols differ. A fixed-length code \(C\subseteq\Sigma^n\) is **non-overlapping** (cross-bifix-free) if for every ordered pair \(u,v\in C\), including \(u=v\), no proper nonempty prefix of \(u\) is equal to a suffix of \(v\). Let \(H(n)\) be the largest cardinality of a code satisfying both conditions. Let \(E(n)\) count *labeled* codebooks of size \(H(n)\): codebooks are unordered sets, but their alphabet symbols and coordinate positions are distinguished. Let \(O(n)\) count their orbits under simultaneous permutation of the three alphabet symbols and reversal of all codewords.

For every integer \(2\le n\le9\), the following values are exact:

| \(n\) | Self-bifix-free homopolymer-free candidate words | \(H(n)\) | \(E(n)\) | \(O(n)\) | Sizes of symmetry orbits |
|---:|---:|---:|---:|---:|---|
| 2 | 6 | 2 | 6 | 1 | 6 |
| 3 | 6 | 2 | 6 | 1 | 6 |
| 4 | 12 | 2 | 18 | 2 | 6, 12 |
| 5 | 24 | 4 | 6 | 1 | 6 |
| 6 | 42 | 5 | 24 | 2 | 12, 12 |
| 7 | 90 | 8 | 48 | 5 | 6, 6, 12, 12, 12 |
| 8 | 162 | 16 | 6 | 1 | 6 |
| 9 | 342 | **24** | **12** | **2** | **6, 6** |

In particular, among length-nine ternary words without adjacent equal symbols, the largest cross-bifix-free code has precisely 24 codewords. There are exactly 12 maximum labeled codebooks and exactly two inequivalent classes under global alphabet permutations and word reversal. Two explicit representatives, one for each class, appear in `OPTIMA_N9.txt`. Each class consists of six labeled codebooks.

The run constraint is imposed within each codeword. The prefix/suffix separation also forces the final symbol of every codeword to differ from the initial symbol of every codeword, so concatenating arbitrary codewords preserves the no-equal-neighbors constraint across boundaries.

## Assumptions and scope

All words are linear, with a distinguished first and last position; there is **no quotient by cyclic rotation**. Cross-bifix matching is tested at every length \(k\) with \(1\le k<n\). Self-comparisons \(u=v\) are forbidden just as cross-comparisons are. Reversal acts simultaneously on all words; symbol relabeling applies one *common* permutation to all positions and words. The integers \(n=2,\ldots,9\) exhaust the asserted scope. Empty and length-one words are outside the definition here.

The word "homopolymer-free" means a maximal constant-symbol run has length one, not that a word uses every alphabet symbol or satisfies a balance constraint. No lower bound on Hamming distance is imposed. The table is an exact finite classification, not a claim about arbitrary \(n\) or alphabets of other sizes.

## Proof

**Lemma 1 (compatibility graph).** Let \(V_n\) be the set of homopolymer-free length-\(n\) words with no proper nonempty prefix equal to their own suffix. Form a simple undirected graph \(G_n\) on \(V_n\), joining distinct words \(u,v\) exactly when neither has any proper prefix equal to a suffix of the other. Then the allowed codebooks are precisely the cliques of \(G_n\).

**Proof.** Self-overlapping words cannot lie in any permissible code, hence every codeword is in \(V_n\). For two distinct vertices, the absence of an overlap in both ordered directions is exactly their adjacency condition. A set of vertices is pairwise adjacent exactly when all the required ordered pairs satisfy cross-bifix avoidance. The homopolymer condition is already built into \(V_n\). This proves the equivalence. \(\square\)

**Lemma 2 (complete ordered search).** Suppose vertices are indexed in lexicographic order and an integer bitmask \(A\) contains precisely the as-yet-eligible vertices whose indices exceed all previously chosen indices and which are adjacent to every previously chosen vertex. At each recursion node, branch in increasing order over the least set bit of \(A\), choose that vertex, and intersect the residual bitmask with its neighbor bitmask. If the current clique has \(r\) vertices, discarding the node when \(r+|A|<B\), where \(B\) is the largest clique size already observed, cannot remove any larger clique or any clique of size \(B\).

**Proof.** Any clique containing the chosen vertices can add only vertices in \(A\); therefore its size is at most \(r+|A|\). Branching on the least eligible bit and then deleting that bit before considering the next branch partitions all increasing vertex sequences into disjoint recursion branches. Every global maximum clique is encountered: along its increasing sequence every required vertex remains eligible, and after its last vertex no higher-index compatible vertex is possible (otherwise it would not be maximum). The strict inequality in pruning retains ties. Thus the terminal records include *every* maximum clique exactly once. \(\square\)

**Lemma 3 (independent maximal-clique check).** Standard Bron--Kerbosch recursion with pivoting, maintaining a chosen clique \(R\), possible extension vertices \(P\), and previously excluded vertices \(X\), enumerates each inclusion-maximal clique once. Branching over \(P\setminus N(p)\) for a pivot \(p\in P\cup X\) does not omit any maximal clique: a clique extending \(R\) either contains a nonneighbor of \(p\) from \(P\), or can be extended by \(p\). Records at \(P=X=\varnothing\) are precisely the maximal cliques. Consequently the largest recorded size and all cliques of that size must match Lemma 2 independently of its pruning.

**Proof of the finding.** The standalone Python program `check.py`, provided in full, enumerates exactly \(3\cdot2^{n-1}\) homopolymer-free words at each asserted length by traversing \(\Sigma^n\) and discarding adjacent repeats. It removes the self-overlapping words to form \(V_n\), constructs \(G_n\) by explicitly checking all \(k=1,\ldots,n-1\) in both ordered directions, and runs the independent complete searches of Lemmas 2 and 3.

The programs agree on the maximum size and the **complete sets** of maximizing cliques at each of the eight lengths. Their exact integer outputs are the first four numerical columns of the displayed table. At \(n=9\), \(G_n\) has 342 vertices; the Bron--Kerbosch pass visits exactly 121728 inclusion-maximal cliques, only 12 of which have the maximum size 24. Every maximum codebook is checked again by comparing each ordered pair of its actual strings, rather than merely trusting graph adjacency.

For the symmetry count, the program applies all \(3!\) alphabet permutations and optional reversal to each maximum codebook, deduplicates the resulting sets, checks they are among the enumerated optima, and partitions all optima into these orbits. The orbit sizes sum to \(E(n)\) at every length. At \(n=9\) this produces two orbits, both of size six, with the canonical representatives supplied in `OPTIMA_N9.txt`. The self-contained, terminating computation, the exhaustive-search lemmas, and the directly validated witnesses jointly prove all claims in the table. \(\square\)

## Verification

From the extracted standalone files, run `python3 check.py`; the standard library is the only dependency. The final success marker is `TERNARY_RUN_ONE_NONOVERLAP_PASS`. The checker reports both exact algorithms' optimum sets, vertex counts, maximum-codebook counts, orbit partitions, and the 121728 maximal cliques at length nine; any disagreement raises an assertion. Each of the two length-nine representatives has 24 explicitly printed codewords, whose pairwise overlaps can also be checked manually. `OPTIMA_N9.txt` is a convenience copy of these exact word sets.

The exhaustive certificate is finite: every candidate is drawn from all ternary length-\(n\) words, and no extrapolation beyond \(n=9\) is used.

## Relationship to prior work

Wang and Wang (arXiv:2108.06934, first public version 2021-08-16) formalize \(q\)-ary non-overlapping codes and give generating functions for construction families; the source's fixed-length code tables do not impose the absence of equal neighbors and do not give this constrained optimum/census. Stanovnik, Moškon and Mraz (arXiv:2307.12593, first public version 2023-07-24) solve numerous **unconstrained** maxima: their Table 1 gives \(S(3,9)=656\), compared with the constrained value 24 here. The two maxima are not interchangeable.

The particularly close paper *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths* (Stanovnik, Moškon and Mraz, 2025; DOI 10.1007/s40314-024-03055-0) studies the same conjunction of synchronization and run restrictions. Section 4 gives constructions and structural coverage for run-limited maximal codes, while Section 5 addresses additional balance restrictions. Those constructions provide a general route to deriving particular constrained optima, but the inspected treatment does not state the present complete ternary length-two-through-nine optimum and symmetry census. The new contribution is the **evaluated exact finite profile and all maximizing codebooks**, not the invention of either constraint or the general maximal-code characterization.

Published related records on unrestricted length-five and length-six non-overlapping maxima also concern different alphabets or omit the homopolymer condition. This comparison does not prove bibliographic uniqueness; a previously unindexed computation of these exact constrained optima remains possible.

## Limitations

Only the eight lengths \(2\le n\le9\), alphabet size three, and maximum run length one are resolved. The proof is a fully reproducible finite exhaustive classification; it supplies no closed formula or asymptotic characterization beyond that domain. Counting maximizing codebooks under a different equivalence group (e.g., individual coordinate permutations) is not part of the claim. Although the constraints are motivated by frame synchronization and avoidance of homopolymers, no statement about actual error rates, physical DNA synthesis, or distance under other channels is made. Novelty is assessed against searched and accessible literature, not certified independently.

## References

1. G. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934v1 (2021-08-16), https://arxiv.org/abs/2108.06934.
2. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, arXiv:2307.12593v1 (2023-07-24), https://arxiv.org/abs/2307.12593.
3. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, Computational and Applied Mathematics 44, 109 (2025), https://doi.org/10.1007/s40314-024-03055-0.
