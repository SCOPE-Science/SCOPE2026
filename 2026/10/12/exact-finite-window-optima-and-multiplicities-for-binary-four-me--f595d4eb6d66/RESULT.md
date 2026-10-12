# Exact finite-window optima and multiplicities for binary four-mer hitting sets

## Finding

Let \(\mathcal B_4=\{0,1\}^4\), and, for each integer \(L\ge4\), call \(U\subseteq\mathcal B_4\) an **\(L\)-hitting set** if every binary word of length \(L\) contains a contiguous length-four factor in \(U\). Define \(\tau(L)=\min_U|U|\) over all \(L\)-hitting sets and define \(N(L)\) as the number of labeled subsets attaining that minimum (the alphabet labels and factor positions are fixed; sets are not identified modulo reversal or symbol exchange).

**Theorem.** The exact finite-window size and multiplicity pairs \((\tau(L),N(L))\) are:

| Window \(L\) | Minimum \(\tau(L)\) | Number \(N(L)\) |
| --- | ---: | ---: |
| \(4\) | 16 | 1 |
| \(5\) | 10 | 2 |
| \(6\) | 9 | 50 |
| \(7\) | 7 | 8 |
| \(8\) | 7 | 52 |
| \(9\) | 6 | 10 |
| \(10\) | 6 | 14 |
| \(L\ge11\) | 6 | 30 |

More finely, precisely \(30\) of the \(128\) six-element cyclic-rotation transversals are unavoidable in all sufficiently long words. Among these \(30\), the maximum lengths of words avoiding the set are \(8\), \(9\), and \(10\), attained by respectively \(10\), \(4\), and \(16\) sets. The remaining \(98\) transversals admit avoiding words of arbitrary length. The known count of thirty minimum decycling sets and the known range of remaining path lengths are *background results*, not separate novelty claims here; the new component is the **joint finite-window optimum and exact multiplicities**.

## Assumptions and scope

All words are finite binary strings. Substrings are contiguous, not subsequences, and factors may overlap. There are exactly \(2^{16}=65{,}536\) possible labeled choices of \(U\), with all \(16\) distinct four-mers indexed by their ordinary four-bit binary values \(0,\dots,15\). All integer window lengths \(L\ge4\) are covered. No results for larger alphabets or a different four-mer length are asserted.

For each \(U\), define \(M(U)\) to be the largest length of a binary word with **no** factor in \(U\); put \(M(U)=\infty\) when avoiders exist at arbitrarily large lengths. Then \(U\) is \(L\)-hitting exactly when \(M(U)<L\).

## Proof

**Step 1: exact path/avoidance equivalence.** Construct a directed multigraph on the eight binary three-mers \(v\in\{0,1\}^3\). Every four-mer \(b_1b_2b_3b_4\notin U\) induces the edge from \(b_1b_2b_3\) to \(b_2b_3b_4\). An avoiding word of length \(L\) determines a directed walk of \(L-3\) edges. Conversely, any such walk uniquely spells the original three-bit starting state followed by each edge's last bit. Thus, the correspondence is exact, including repeated states and edges.

**Step 2: cycle test and longest paths.** If the remaining digraph has a directed cycle, arbitrarily long avoiding words follow by repeated traversal, so \(M(U)=\infty\). Otherwise the graph is acyclic, and its longest directed path has a well-defined number \(e(U)\) of edges, with length-zero paths allowed at any of its eight vertices. The exact maximum avoider length is \(M(U)=3+e(U)\). Kahn's topological algorithm detects a cycle when fewer than eight vertices are removed; otherwise the longest path is computed exactly in topological order by integer dynamic programming.

**Step 3: exhaustive finite optimum and counts.** The standalone `verify_graph.py` loops once over every integer mask \(s\in[0,2^{16}-1]\). Bit \(b\) of \(s\) is one precisely when the four-mer with integer value \(b\) belongs to \(U\). Steps 1 and 2 decide, exactly, whether each mask is \(L\)-hitting for every \(L=4,5,\ldots,11\). The code then minimizes the exact popcount and counts *all* attaining masks. Its actual asserted output is the first eight rows of the theorem. The independent program `verify_words.cpp` enumerates every length-\(L\) binary test word, computes its exact set of occurring four-mers, and tests the intersection property against every candidate \(U\); it reproduces every finite row through \(L=11\), without using graph topology.

**Step 4: reduction from all larger windows to necklaces.** Cyclic rotation partitions the sixteen four-mers into six disjoint rotation classes of sizes \(1,4,4,2,4,1\). Every class generates an infinite periodic binary sequence whose contiguous four-factors lie only in that class. Consequently any finite-window hitting set, regardless of \(L\), must intersect each of these six classes; therefore \(\tau(L)\ge6\) always. Every six-element hitting set is necessarily a choice of exactly one member of each class. There are exactly \(1\cdot4\cdot4\cdot2\cdot4\cdot1=128\) such choices.

The standalone graph checker exhausts this Cartesian product of \(128\) choices. Exactly \(98\) yield a directed cycle; the remaining \(30\) have maximum avoiding lengths \(8\) (ten choices), \(9\) (four choices), or \(10\) (sixteen choices). This is exhaustive since all six-element candidate hitting sets belong to this product. In particular some six-element set hits every word of length \(9\), and all \(30\) acyclic transversals hit every word of length at least \(11\). Any set that hits all length-\(11\) words also hits all longer words: take the first length-\(11\) factor. Thus \((\tau(L),N(L))=(6,30)\) for every \(L\ge11\), and the finite threshold counts are exactly those listed.

## Verification

Execute `python3 verify_graph.py`. The program asserts the full histogram of sizes and counts, the number of masks enumerated, the six necklace sizes, and the \(128\)-choice distribution, before emitting the word `PASS` in JSON.

As a logically distinct check, compile and execute `c++ -O2 -std=c++17 verify_words.cpp -o verify_words && ./verify_words`. It enumerates all \(2^L\) words at every \(L\in\{4,\dots,11\}\) and independently checks the optimal size/count pairs, ending with `DIRECT_WORD_CENSUS_PASS`. Both executed successfully from the accompanying source files. The exhaustive nature of the *finite* verification is proved by explicit closed loop bounds and the graph correspondence above; no experiment is extrapolated to arbitrary graph parameters.

## Relationship to prior work

The binary finite-window hitting-set problem is a specialization of the universal \(k\)-mer hitting set framework introduced and investigated by Orenstein and collaborators. Their 2016 public conference abstract and expanded 2017 full article describe finite-window universal hitting sets, heuristics, and integer programming, but do not report this binary four-mer window-by-window exact cardinality-and-count profile. Champarnaud, Hansel and Perrin (2004) proved the minimum size of an unavoidable constant-length word set through cyclic-rotation classes; this gives the lower bound of six for the infinite-window problem, not the values \(10,9,7,7\) or the number of *all* optimizers for shorter windows. Zheng, Kingsford and Marçais (2021) explicitly report **thirty** minimum decycling sets for binary four-mers: that total is known. Marçais, DeBlasio and Kingsford (2024), Table 2, report the exact **range** of remaining-node-path lengths \(5\) to \(7\) over those minimum decycling sets, equivalent to the avoider-length range \(8\) to \(10\) here. That range is also known. The specific distribution \((10,4,16)\), the exact first six-set window \(L=9\) with ten optimal sets, and the complete profile of labeled optimizers for \(L=4,\dots,10\) are not implied by merely knowing the thirty-set total or two endpoints of the path-length range, and were not stated in those inspected articles.

## Limitations

The finding is finite in the four-mer parameter and does not supply a symbolic formula for arbitrary \(k\) or alphabets. It depends on the integrity and exhaustive loop coverage of the two supplied short programs; no separate formal machine-checked certificate is asserted. The cited 2024 paper substantially overlaps in model and in the **extremal range**, but not in the finer exact multiplicity statistics. An unavailable supplementary document associated with the 2021 article, or unindexed code/data, could contain comparable small-instance counts; this residual bibliographic uncertainty is not a novelty proof. The exact date printed in the 2016 proceedings establishes an archival source-date anchor, not a proven earliest worldwide posting date.

## References

1. Orenstein, Pellow, Marçais, Shamir, and Kingsford, “Compact universal k-mer hitting sets,” HiTSeq 2016 Proceedings, pp. 63–64, Orlando, 8–9 July 2016, https://www.hitseq.org/abstracts/abstracts-2016.pdf .
2. Orenstein et al., “Designing small universal k-mer hitting sets for improved analysis of high-throughput sequencing,” *PLOS Computational Biology* (2017), DOI: 10.1371/journal.pcbi.1005777, https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005777 .
3. Champarnaud, Hansel, and Perrin, “Unavoidable sets of constant length,” *International Journal of Algebra and Computation* 14 (2004), pp. 241–251; accessible author-uploaded text: https://www.researchgate.net/publication/220169546_UNAVOIDABLE_SETS_OF_CONSTANT_LENGTH .
4. Zheng, Kingsford, and Marçais, “Lower Density Selection Schemes via Small Universal Hitting Sets with Short Remaining Path Length,” *Journal of Computational Biology* 28 (2021), pp. 395–409, DOI: 10.1089/cmb.2020.0432, https://pmc.ncbi.nlm.nih.gov/articles/PMC8066347/ .
5. Marçais, DeBlasio, and Kingsford, “Sketching Methods with Small Window Guarantee Using Minimum Decycling Sets,” DOI: 10.1089/cmb.2024.0544, https://journals.sagepub.com/doi/10.1089/cmb.2024.0544 .
