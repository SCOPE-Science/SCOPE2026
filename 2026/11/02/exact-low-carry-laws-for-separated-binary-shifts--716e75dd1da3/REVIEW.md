# Review of the separated-shift low-carry law

**Correctness: PASS.** The digit-sum identity follows by counting binary carries. On any event with at most \(h\) carries, distinct carry chains are confined to disjoint digit intervals because the nonzero digits of the shift have gaps at least \(h+1\). The probability of a particular weak composition of the carry count is exactly \(2^{-(h+j)}\), and the central-binomial-tail identity closes the formula. An exact rational independent finite-state checker and direct dyadic enumerations support the proof. The proof covers all positions and all positive weights, not just the verified finite cases.

**Originality: PASS, with residual priority risk.** Earlier full-text work of Spiegelhofer and Wallner contains the general digit-sum distribution recurrence and a many-block Gaussian theorem. Recent work of Cheng establishes general positive bias and sharp *minimum* fixed-weight bias, not the explicit carry probability distribution in the public materials inspected. The exact uniform sparse family was not found in the targeted searches; the general recurrence and the uninspected complete recent preprints leave genuine implicit-coverage risk. Two claim-specific published-finding corpus searches completed without matching records; a later request temporarily failed and is not counted as a negative search.

**Value: PASS.** The formula is an infinite exact classification of the low-carry law for a natural family of noninteracting binary shifts; it gives a precise \(h^{-1/2}\) positive-bias benchmark against the recently studied much smaller extremal fixed-weight biases. The gap requirement matters, as the two-weight shift \(t=5\) has a different density from \(t=9\).

Limitations: no law is claimed for carry counts above the weight, no optimization over shifts of fixed weight is claimed, and the primary full texts of the 2026 papers could not be inspected. A prior implicit version remains possible and independent priority review has not occurred.

Self-review: passed. Independent audit: not yet performed.
