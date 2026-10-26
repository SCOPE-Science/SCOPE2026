# Scientific review

## Correctness

**PASS.** For a binary word, the left-minimal mixed intervals beginning at a particular position exist precisely when the position is the last letter of a run followed by its opposite, and they end within the next run. This yields the finite-width formula \(L_w(h)=\sum_{i=2}^{m}\mathbf 1_{2\le h\le a_i+1}\). Its first differences uniquely recover the multiset of noninitial run lengths, except for the explicitly separated terminal run of length \(n-1\). Alternating-run constructions give surjectivity onto partitions of totals at most \(n-1\). Counting permutations proves every fiber size. Distinct-parts costs prove the exact maximal number of nonzero differences. Direct enumeration through length 15 checks the identities independently; it is not used as a substitute for proof.

## Originality

**PASS, subject to residual bibliographic risk.** Bille--Gørtz--Stordalen (arXiv:2206.10383, Lemma 1, Theorem 1, Section 4 and appendices) establishes sparse left-minimal profiles, general bounds and general interval decomposition, but not the binary partition census or its exact profile fibers. Sobel et al. (arXiv:2011.14460, Sections 1--4 and the gap-count bound) establishes the earlier co-occurrence model and gap-histogram algorithm, not this enumeration. Searches for binary left-minimal profiles, run lengths, partitions and difference support in the indexed research corpus did not expose an equivalent claim. OEIS A000070 already lists the same numerical values as cumulative partition numbers, but provides no left-minimal co-occurrence interpretation. The elementary binary specialization of the general interval lemma is relevant partial coverage, not a published implication giving the exact image and fiber count without the partition bijection. Unindexed equivalents and implicit gap-histogram variants remain risks.

## Mathematical value

**PASS.** Exact possible output vectors and exact fiber multiplicities are natural invariants of a prescribed query-answer observation model: they determine how many inputs can be distinguished without noise and quantify every ambiguity class, rather than merely estimating asymptotic storage. The partition bijection is structural, gives an exact infinite-family enumeration and generating function, and locates finite-length thresholds where the sparsity parameter's extremum jumps. The source literature studies data structures for these exact observations, so these invariants are motivated by its information-compression question; the statement does not claim a new general data structure.

## Closest literature and limits

The numerical integer-partition sequence is previously known. The source's general sparse-interval decomposition, when specialized to binary runs, provides part of the machinery; the exact bijection, all fiber sizes and sharp finite-length extremum constitute the additional conclusions. The result concerns left-minimal observations only, not unrestricted mixed-window observations or alphabets with nuisance symbols. Bibliographic and independent scientific validation remain incomplete.

Self-review: passed. Independent audit: not yet performed.
