# Self-review: positive density of odd nonsquare counterexamples

## Correctness — PASS

For an odd abundant square \(a\), the sum \(C=\sigma(a)\) is odd and exceeds \(2a\). The change-of-sign condition gives an exact target \(H=(\sigma(am)-2am)/2\). For coprime odd nonsquare \(m\) with \(C(\sigma(m)-m)<m\), this target lies strictly between the largest possible subset sum whose \(m\)-multiple coefficient is at most \((C-2a-1)/2\) and the smallest sum with a larger coefficient. The argument covers **every** subset, not sampled subsets.

The density sieve is unconditional: inclusion-exclusion gives the fixed-prime-coprimality density, weighting by \(1/(p-1)\) bounds the mean divisor-sum excess, and the telescoping series \(\sum_{k>Y}1/[k(k-1)]=1/Y\) gives the claimed explicit loss. Perfect-square cofactors are negligible. An exact finite verifier confirms the representative anchor, positivity, interval bounds and explicit constant. It is not used as a substitute for the infinite proof.

## Originality — PASS

The strongest same-object source is Campbell, arXiv:2607.11043v1. Its Theorem 2.4 supplies positive density for an **even** counterexample family, while Theorem 3.1 supplies an **infinite sparse odd nonsquare** family with prime cofactors. Ross (2024) states Conjecture 17 for the odd nonsquares. Neither the even-density theorem nor infinitude from primes implies positive density of odd nonsquare counterexamples. Full relevant primary text, exact aliases, semantic prior records and own prior/current claim summaries were compared; no equivalent or dominating theorem was located.

The final publisher edition's full text was not accessible, although the complete initial preprint and the publisher abstract were reviewed. Unindexed results remain a residual literature risk, not grounds for declaring unique discovery.

## Value — PASS

This determines a meaningful qualitative density property in precisely the odd nonsquare class targeted by the conjecture, strengthening the sparse counterexample family to positive lower density. The theorem works for every fixed odd abundant square, with an explicit lower-density bound; it is not an arbitrary finite cutoff or a rewording of the even case.

## Scope and limitations

The positive lower bound need not equal the natural density; optimizing it, classifying all counterexamples, and proving existence of a natural density remain open. The computational artifact checks exact arithmetic in a representative case, while the paper proof handles all parameters.

Self-review: passed. Independent audit: not yet performed.
