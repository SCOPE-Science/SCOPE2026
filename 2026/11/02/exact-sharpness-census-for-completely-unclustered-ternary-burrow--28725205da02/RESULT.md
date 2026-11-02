# Exact sharpness census for completely unclustered ternary Burrows–Wheeler images through length 30

## Finding

Fix the ordered ternary alphabet \(\Sigma_3=\{0<1<2\}\). For each integer \(n\) with \(13\le n\le30\), let \(c_n\) be the number of length-\(n\) ternary words \(L\) with no consecutive equal symbols, with an \(n\)-cycle standard permutation, and with Hamming distance \(\lceil n/2\rceil\) from the sorted rearrangement of \(L\). Then the exact values of \(c_n\), and one explicit word witnessing positivity at every length, are:

| Length \(n\) | Sharp ternary BWT images \(c_n\) | Witness \(L_n\) |
|---:|---:|---|
| 13 | 28 | `1010101010120` |
| 14 | 4 | `10101210212021` |
| 15 | 88 | `101010101012021` |
| 16 | 22 | `1010101010120121` |
| 17 | 120 | `10101010101012020` |
| 18 | 30 | `101010101010121020` |
| 19 | 256 | `1010101010121202020` |
| 20 | 61 | `10101010101212102020` |
| 21 | 540 | `101010101010120212021` |
| 22 | 94 | `1010101010101210212021` |
| 23 | 1,084 | `10101010101012021012121` |
| 24 | 180 | `101010101010121021012121` |
| 25 | 2,148 | `1010101010101010101201020` |
| 26 | 330 | `10101010101010101210101020` |
| 27 | 3,956 | `101010101010101010121012020` |
| 28 | 595 | `1010101010101010101010101010` |
| 29 | 8,322 | `10101010101010101010101010120` |
| 30 | 1,072 | `101010101010101010121012012021` |


Consequently, for every ordered alphabet of size \(q\ge3\), the minimum cyclic number of runs in a primitive length-\(n\) necklace whose Burrows–Wheeler transform is completely unclustered satisfies

\[
U_q(n)=\lceil n/2\rceil\qquad(13\le n\le30).
\]

The count \(c_n\) applies **only to the fixed ordered ternary alphabet**, with no quotient by alphabet relabelings. Because the Burrows–Wheeler transform is injective on primitive necklaces, it also counts ternary primitive necklaces attaining equality. It is **not** asserted to equal the count over alphabets with more than three symbols.

At length \(n=14\), precisely four images attain equality, each with Parikh vector \((4,6,4)\). They are given in `n14_four.txt`.

## Assumptions and scope

The standard permutation \(\pi_L\) is the stable-sorting map on positions: the \(r\)-th occurrence (starting at zero) of symbol \(a\) in \(L\) maps to the \(r\)-th position in the block of symbol \(a\) in \(F=\operatorname{sort}(L)\). A primitive necklace is a rotation class of an aperiodic word. The cyclic run count of a nonconstant necklace is the number of adjacent unequal symbol pairs around the cycle. An \(n\)-letter BWT is completely unclustered when its linear list of symbols has \(n\) runs, or equivalently consecutive entries differ. This theorem concerns precisely the eighteen lengths \(13\) through \(30\), not any unbounded family.

## Proof

**Reduction to a finite exact predicate.** For a word \(L\) of length \(n>1\), its stable-sorting permutation is a single \(n\)-cycle if and only if \(L\) is the BWT of one primitive necklace (Fici et al., Lemma 3; Kumallagov, Section 2). For a single-cycle image, Kumallagov, Proposition 4.3 proves that its input cyclic run count is exactly \(d_H(L,\operatorname{sort}(L))\). Therefore the three tests in the definition of \(c_n\) are jointly necessary and sufficient for a sharp, unclustered primitive BWT image.

**Exhaustive generation.** A length-\(n\) ternary word with unequal adjacent symbols has exactly three possibilities for its first symbol and two independent choices at each later position; hence there are exactly \(3\cdot2^{n-1}\) such words. The independent successors are recursively visited by `verify_enumeration.cpp`, without repeats. For each completed word, the program computes its symbol counts, sorted-block offsets and stable permutation. It checks Hamming distance \(\lceil n/2\rceil\), and then walks the permutation orbit of position zero. Because the mapping is a permutation, that orbit has \(n\) distinct positions if and only if the permutation is a single cycle. Thus every accepted word satisfies the defining conditions and every eligible word is counted once.

**Safe parity pruning.** To speed up the full finite enumeration, the C++ program applies Kumallagov, Proposition 9.2 before its Hamming and cycle checks: in an even-length sharp image all nonzero symbol multiplicities are even; in an odd-length sharp image exactly one multiplicity is odd. The proposition is necessary for every single-cycle sharp image, so this pruning loses no accepted word. The second verifier uses a different enumeration and does not use this pruning.

**Upper and lower bounds.** Each table witness is independently reconstructed into a primitive necklace and checked by a direct BWT algorithm in `verify_witnesses.py`; each has exactly \(\lceil n/2\rceil\) cyclic input runs. This proves \(U_3(n)\le\lceil n/2\rceil\). The reverse inequality for all alphabet sizes follows from the Mantaci–Restivo–Rosone–Sciortino–Versari factor-two bound, as applied by Kumallagov, Proposition 3.2. Every ternary construction remains valid over an ordered alphabet with \(q\ge3\), so equality holds for all such alphabets in the stated interval.

## Verification

Compile the complete enumerator with `g++ -O3 -std=c++17 verify_enumeration.cpp -o verify_enumeration` and invoke `./verify_enumeration 13 30`; its `sharp` field gives the eighteen values in the table. To reproduce the independent mask-based enumeration, compile `verify_bitmask.cpp` analogously and invoke it with arguments `13 26`; this separately reproduces every exact count for lengths \(13\) through \(26\) without parity pruning. Run `python3 verify_witnesses.py` in the same folder as `witness_table.tsv`; this reconstructs a primitive input and independently recalculates the actual transform and input cyclic runs for every listed length. A separate direct ternary enumeration checks all four \(n=14\) images. Recorded outcomes are in `verification_output.txt`.

The complete enumerator's candidate-count identity \(3\cdot2^{n-1}\) is a coverage certificate for the enumerated finite domain. These finite checks do not resolve any length outside the specified interval. No proof uses an unverified extrapolation from the table.

## Relationship to prior work

Kumallagov (arXiv:2606.01267v1, May 31, 2026) introduced \(U_q(n)\), proved the universal lower bound, established values and witnesses through length \(12\), and posed the all-length sharpness conjecture (Conjecture 7.1). Its arithmetic family in Proposition 8.1 already covers the **numeric sharpness** statements at lengths \(13,28,29\) via primes \(13\) and \(29\). Those cases are included here only to give a continuous **new count table**, not as independent new numeric optima. The previously unresolved numerical lengths in the interval are \(14\) through \(27\) and \(30\). The earlier paper does not present the eighteen values of \(c_n\) or the complete four-word census at length \(14\).

Fici, Gabory, Romana and Sciortino (arXiv:2508.20879v1, August 28, 2025) proved existence of completely unclustered BWT images at every length over at least three letters. Their existence theorem does not give the minimum input cyclic run count or the exact sharp image census.

## Limitations

This is a **finite exact census**, not a proof of Kumallagov's conjecture for arbitrary lengths. The result is computationally exhaustive conditional only on the stated elementary enumeration argument and cited known identities. The high-length counts use the full primary C++ enumeration, while the independently implemented complete recount covers lengths through \(26\); every witness through \(30\) is separately checked by direct inverse-and-forward BWT. Relevant older, possibly differently phrased classifications cannot be excluded without broader independent priority review. No independent mathematical audit has been performed.

## References

1. David Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267v1, publicly submitted May 31, 2026. Sections 3, 4, 6–10.
2. Gabriele Fici, Estéban Gabory, Giuseppe Romana, and Marinella Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879v1, publicly submitted August 28, 2025. Lemma 3, Theorem 15.
3. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, and L. Versari, *Measuring the clustering effect of BWT via RLE*, Theoretical Computer Science 698 (2017), 79–91; factor-two bound as quoted and used in reference 1.
