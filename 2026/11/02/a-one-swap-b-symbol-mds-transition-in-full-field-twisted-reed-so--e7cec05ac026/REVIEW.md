# Scientific review

## Correctness — PASS
The claim is quantified over prime \(p\ge5\), dimension \(2\le k\le p-1\), nonzero twist \(\eta\), every cyclic permutation and all window lengths \(1\le b\le p\). The root-sum equivalence follows directly by Vieta's formula in degree \(k<p\) and the converse product construction. The zero-run count is exact and its unique extremal shape is a single block of exactly \(k\) zeros. An invertible Vandermonde minor supplies the needed reverse bound when no length-\(k\) zero block exists. In the explicit swap, exactly two window sums change; the only potential replacement of the forbidden sum would require \(k^2=1\pmod p\), excluded by \(2\le k\le p-2\). The codimension-one obstruction is a direct complement count. Direct enumeration confirms the formulas and minimum-layer multiplicities in the indicated finite cases. Remaining limit: finite computation cannot prove the infinite family; the written argument does.

## Originality — PASS with specified risk
Compared with arXiv:2610.16283 (2026-10-12), the published claims concern ordinary generalized Hamming weights and subcode support distributions, rather than ordered cyclic windows. arXiv:2107.06945 develops the twisted polynomial family but not its \(b\)-symbol reordering transition. arXiv:1211.1728 gives the symbol-pair Singleton bound and broad constructions; arXiv:2103.16299 gives general \(b\)-MDS rank criteria, but neither supplies the explicit simultaneous one-swap construction or the sharp dimension boundary here. Targeted published-record searches did not identify an equivalent formulation. Risk: the result could follow implicitly from an unindexed specialization of the general rank criterion or from an older polynomial-evaluation design not inspected; a search failure is not proof of global uniqueness.

## Value — PASS
The invariant is operational for overlapping-read channels: the same non-Hamming-MDS linear code is one unit below optimal for every short window in an arithmetic order, and becomes optimal for every window length after only an adjacent coordinate transposition. The theorem provides an explicit all-parameter ordering, a necessary-and-sufficient exact window-sum test for arbitrary orderings, extremal word multiplicities in the defective case, and a sharp impossibility boundary. The group-arithmetic mechanism is not a renaming of the general Singleton bound. This is a useful finite-field coding-geometry phenomenon; no improved Hamming distance or decoding algorithm is claimed.

## Closest literature and limitations
Liu et al., arXiv:2610.16283; Liu–Pan, arXiv:2103.16299; Chee et al., arXiv:1211.1728; Beelen–Puchinger–Rosenkilde, arXiv:2107.06945. The proof is specific to prime fields, full evaluation, highest hook, and unit twist. Priority remains subject to additional external literature checks and independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
