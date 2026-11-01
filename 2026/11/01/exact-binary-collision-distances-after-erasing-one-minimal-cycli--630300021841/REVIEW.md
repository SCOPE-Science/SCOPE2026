# Scientific review

## Correctness — PASS
For any binary pair the signed difference is a ternary vector and vice versa; its Fourier zeros at the sampled primitive roots extend to entire cyclotomic classes by rational Galois conjugacy. Prime-power order shells consist precisely of periodic sequences with zero-sum blocks, and their minimum supports are \(p^a\) at local order one and \(2p^{a-b}\) at positive order \(p^b\). The tensor-product argument proves the converse lower bound, and a product of signed two-site local witnesses attains it without exceeding the binary-difference alphabet. The corollary about worst deletion follows by minimizing the local factors. The included checker reproduces 103 exact shell checks, including exhaustive differences for lengths up to 10. Finite checks are not the infinite proof.

## Originality — PASS (provisional priority)
Pei--Chang's 2022 binary DFT uniqueness theorem and ambiguity-pair existence are prior results. Levinson--Viviano's arXiv:2510.11949, Lemma 2.2, supplies an explicit witness for the primitive shell, extended in Lemma 3.5; it does not, in the inspected text, rule out *shorter* shell-supported signed vectors. Iosevich--Mayeli's 2023 sparse-recovery bounds do not imply the sharp arithmetic distance formula. The current claim establishes the complementary lower bound for every omitted order. Searches found no exact database table covering this classification. The original 2022 full text could not be inspected, creating a meaningful historical-priority risk; nor does absence in a search certify novelty.

## Mathematical value — PASS
The distance is a natural robustness invariant of a minimal exact Fourier sampling design: after one coefficient is lost, it is the smallest number of binary pixels that can change invisibly. It depends sharply on the omitted character order and prime factorization, and the optimal guaranteed distance across all erasures is \(2^{\omega(N)}\), unlike the known qualitative statement that the design loses uniqueness. The theorem is a nontrivial exact minimum supported by a universal lower bound and an attaining construction, not an arbitrary finite slice or a mere rewording of a known nonuniqueness witness.

## Limitations and priority risk
No numerical-noise robustness, reconstruction algorithm, multi-erasure bound, or full classification of minimizing pairs is claimed. The full 2022 ambiguity-pair paper is materially relevant but was unavailable; an unindexed stronger theorem in cyclotomic coding may cover the sharp formula. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
