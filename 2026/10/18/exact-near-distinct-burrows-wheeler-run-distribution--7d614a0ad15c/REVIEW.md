# Self-review

## Correctness — PASS
The proof explicitly partitions primitive near-permutation necklaces into cyclically adjacent and nonadjacent occurrences of the repeated letter. It counts all possible adjacent BWT rows by their unique first-letter ranks, including both endpoints of the alphabet and the binary boundary case. The sum is exactly \((q-1)!\) per repeated symbol, with \(q!/2\) total necklaces. An independent exhaustive checker builds and sorts rotations for alphabet sizes \(2\) through \(7\) and validates an independent last-to-first cycle construction; the checker output is packaged. Enumeration is corroboration, not the infinite proof.

## Originality — PASS within checked evidence
The open-access CPM 2026 full article by Fici et al. (Sections 3–6) proves nonbinary existence and a general lower bound for completely unclustered BWT outputs; it does not give a closed content-specific count for one duplicated character. The full arXiv:2606.01267v1 article (Sections 4–6) gives an unrestricted fixed-content primitive-necklace total and explicitly says this does not count completely unclustered BWTs. The present result supplies that missing refined enumeration and a letter-rank-independent structural classification. Public research-record and literature searches found no equivalent statement, but differently worded or unindexed prior enumeration remains a risk. Novelty is not inferred merely from different wording.

## Value — PASS
The single duplicated symbol is the minimal non-permutation Parikh class in which BWT run clustering is possible. Its full exact run distribution answers a natural counting question directly motivated by recent work on totally unclustered BWT images: both the near-maximum-run count and the probability of total unclustering are explicit, and surprisingly independent of the repeated letter's alphabet rank. The local successor criterion explains the cancellation between the adjacent-copy and separated-copy classes. This is a complete, infinite, self-contained natural enumeration, not an isolated short computational table.

## Limitations and closest literature
The statement does not extend to arbitrary fixed-content vectors. The literature comparison includes the full Fici et al. CPM article (2026) and the full arXiv:2606.01267v1 manuscript (2026); a differently indexed older count could exist. The BWT uses no sentinel and ordinary linear runs. Computations are finite corroboration. No independent scientific validation is claimed.

Self-review: passed. Independent audit: not yet performed.
