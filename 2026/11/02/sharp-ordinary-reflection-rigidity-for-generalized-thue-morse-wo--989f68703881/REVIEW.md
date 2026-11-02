# Mathematical review

## Correctness — PASS

The digit-carry identity \(\Delta_j\equiv1-(b-1)\nu_b(j+1)\pmod m\) holds at every nonnegative position, including exact powers and trailing carries. Every two successive transitions include \(+1\). Mutual occurrence of an ordinary triple and its reverse therefore forces its endpoint symbols to agree, and any longer mutually reversible factor must be two-periodic. The double \(-1\) obstruction within three consecutive transitions, including the special base-two valuation argument, eliminates both orientations of a nonpalindromic alternating four-factor. The congruence-witness construction proves the exact two-factor language for all \(b,m\); all three greatest-common-divisor cases have the correct orbit counts. The finite verifier returned `VERIFY_OK 3477 finite assertions`. The infinite assertion follows from the proof, not the tests. No hypotheses or boundary cases in the stated range are omitted.

## Originality — PASS, with residual risk

Section 7 of Allouche et al. (arXiv:2406.09302) raises generalized Thue–Morse reflection complexity, reports the \(b=2,m=3\) instance, and only observes analogous behavior at higher alphabets. Thus that published special case is covered and is **not** claimed new. Starosta (arXiv:1104.2476, pp. 364–369) calculates factor complexity and proves closure under antimorphisms that reverse order while also transforming each letter by \(k\mapsto x-k\); this is not letter-preserving reversal for \(m\ge3\). Allouche–Shallit (DMTCS 2000, Theorem 8) establishes absence of long *palindromes*, not absence of distinct mutually reversed factors. The later generalized-reflection literature studies a different group action and does not establish the present uniform plain-reversal assertion on the inspected material. No duplicate was identified in the targeted mathematical searches and available earlier claims. An unindexed equivalent or indirect derivation from a stronger result remains a genuine risk, and this assessment is not independent.

## Value — PASS

The work resolves the named 2024 family-wide reflection-complexity question in one structural theorem, across every integer base and every alphabet size at least three, rather than extending a numerical table. It gives a sharp factor-length cutoff, a base-two/multiple-base uniform mechanism, and the previously unaccounted length-two gcd phase diagram. The known \(b=2,m=3\) special case and existing ordinary factor complexity are explicitly excluded from the novelty claim.

## References and limitations

Primary comparison: https://arxiv.org/abs/2406.09302 (Section 7); https://dml.cz/dmlcz/142943 (Proposition 3.1 and factor-complexity section); https://dmtcs.episciences.org/en/articles/282/download (Theorem 8); https://arxiv.org/abs/2610.14637 (distinct group actions). No independent validation is claimed. Incomplete indexing of mathematical literature leaves a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
