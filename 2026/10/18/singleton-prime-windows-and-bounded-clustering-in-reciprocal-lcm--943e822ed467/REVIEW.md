# Scientific review

## Correctness — PASS

The exact local prime-power formula and largest-at-a-tie maximization are stated precisely. The Taylor expansions near reciprocal prime zero are analytic (and differentiable), giving the correct coefficient \((\kappa-5)/12\) for the positive singleton-window width. Necessity compares exponent one to zero and two; sufficiency excludes all exponents three and above by the strict uniform local bound. Intersections of two singleton windows force adjacent transition slopes to differ by at most the order \(1/(p^2\log p)\), and the real-variable mean-value theorem gives diameter \((\kappa-5)/6+o(1)\). Fixed-prime positive second transition thresholds exclude finite primes when \(\varepsilon\to0^+\). Numeric checks in the companion script test finite cases only. Scientific risk: the proof is not independently validated.

## Originality — PASS, with residual risk

The closest inspected paper is Molnar, arXiv:2610.12816v1. Its Definition 4.1 and Lemma 4.2 give primewise endpoint optimization. Its Remark after Corollary 4.8 already gives the critical local expansion and the absence of exponent one when \(\kappa=5\). Its Lemma 4.5 gives repeated support on a broad fractional prime interval. The present claim is *not* novelty for those antecedents: it is the exact exponent-one interval, a global bounded common-parameter cluster diameter, and the at-most-one law for \(5<\kappa<17\). The nonreciprocal earlier family arXiv:2511.02106v1 does not share this normalized endpoint objective. A series of semantic searches of published mathematical findings and primary-text inspection did not reveal a dominating statement. Unindexed earlier statements, implicit stronger results, and the not-fully-inspected antecedent remain risks; a failed search is not evidence of uniqueness.

## Mathematical value — PASS

The original study relies on the arithmetic of canonical extremizers to transfer Robin-scale inequalities and highlights \(\kappa=5\) as a square-support boundary. This theorem describes what replaces square support above the boundary: positive singleton events occur infinitely often but are confined to uniformly bounded prime clusters. The clean cut at \(\kappa=17\) determines a nontrivial regime with at most one simultaneous singleton, a natural complete multiplicity assertion for late endpoints. This is an exact structural refinement of that specific motivated question, not an arbitrary numerical slice.

## Scope and limitations

Constants and asymptotic onset depend on a fixed \(\kappa>5\). The theorem does not provide a finite exception table, an effective uniform onset, endpoint counting asymptotics, or an RH consequence; other prime powers remain unrestricted. The high-precision examples do not prove the asymptotic or uniqueness statements. The comparison with the earliest nonreciprocal antecedent uses its primary abstract and the full later paper, not an inspection of that antecedent's complete text.

Self-review: passed. Independent audit: not yet performed.
