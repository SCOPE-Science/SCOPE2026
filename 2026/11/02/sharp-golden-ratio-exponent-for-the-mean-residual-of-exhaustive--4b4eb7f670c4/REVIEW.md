# Review: sharp golden-ratio exponent for mean exhaustive-Peres residuals

## Correctness — PASS

For fair binary input, the XOR sequence is uniformly distributed and the retained equal-pair bits are independent fair bits conditional on the XOR sequence. This proves both recurrences, including the odd final bit. The exponent is exactly the solution to \(2^{-\alpha}+4^{-\alpha}=1\). The lower induction does not approximate the binomial child by its mean: the proof bounds the actual Jensen gap by \(d_n<4\) using Taylor curvature and the standard binomial Chernoff tail. With the zero-binomial atom accounted for, the lower and upper barriers hold at every positive integer input length. The corresponding expected number of residual ones is exactly half by recurrence and the base cases. An independent direct recursive enumeration through length 12 and exact rational recurrence calculations through length 90 agree. These finite checks are not substituted for the proof.

## Originality — PASS, with residual priority risk

Garivier's October 2026 work presents the exact recurrence and specifically identifies the golden-ratio mean exponent as a heuristic in the discussion of the open worst-case residual-growth problem. Its proved deterministic upper exponent is larger and does not supply the all-length mean estimate. Peres's original asymptotic-rate proof, Pae's recursive extraction treatment, and Prasitsupparote–Konno–Shikata's finite-length conditional maximum-redundancy bound do not imply this two-sided sharp fair-source mean statement. Semantic mathematical-record searches and overlap comparisons with accessible prior scientific claims found no matching theorem. Recurrence asymptotics may be implicit in unindexed divide-and-conquer analysis, so this assessment is not independent priority certification.

## Value — PASS

The exponent of the expected number of unextracted bits determines the finite-length loss scale of an explicit lossless randomness extractor. The motivating paper singled out the same exponent heuristically, leaving a quantitative gap between numerical behavior and the established worst-case estimate. Proving positive universal lower and upper constants directly on the exact recursion identifies the mean scale at every length and gives a power-law lower obstruction to reducing the worst-case exponent below \(\log_2\varphi\). This does not settle the conjectured sharp maximum-residual exponent or the limiting prefactor.

## Closest literature and limitations

The closest source is A. Garivier, arXiv:2610.26396, Section 8 and Appendix A: mean recursion and heuristic exponent, different rigorous worst-case upper bound. Y. Peres (1992) proves asymptotic extraction rates; S.-I. Pae (2018) treats recursive extraction; A. Prasitsupparote et al. (2018) give a different, heuristic-dependent maximum-redundancy lower bound. The theorem only concerns independent fair input and the specified exhaustive transform. No independent publication-priority or mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
