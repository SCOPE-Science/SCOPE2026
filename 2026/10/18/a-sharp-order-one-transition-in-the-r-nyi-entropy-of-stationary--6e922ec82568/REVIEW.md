# Scientific review

## Correctness — PASS

The refresh projection identity gives the pair law exactly. The power-sum second derivative has a strict fixed sign, while the first derivative at independence is the Cauchy–Schwarz gap \(\alpha B_\alpha\). For subunit order and nonuniform marginals the endpoint derivative diverges negatively, forcing a unique interior maximum. The Shannon conclusion is an exact KL-divergence identity. Explicit Taylor expansion and the implicit-function theorem give the lag tail and the near-Shannon critical scale. The separate exact-matrix and finite numerical checks in `verify.py` passed 654 tests. Those tests do not certify the infinite statements; the analytic arguments supply their proof.

## Originality — PASS (bounded literature comparison)

The most relevant source, Judd–Esposito, arXiv:2610.10860v1, introduces the same lag-pair effective support and a lag envelope but establishes sample-complexity converses rather than the stated entropy monotonicity phase diagram. Wolfer–Alquier, arXiv:2402.10506v5, provides Rényi-related entropic terms and two-state mixing calculations but not the strict overshoot, unique maximizer, or order-one critical scaling. General Rényi entropic non-subadditivity is known and is **not** claimed as original; the original target is the exact characterization within a reversible Markov semigroup and its sharp critical asymptotics. Searches for equivalent couplings, time-lag entropy and dominant general results found no direct coverage. Unindexed special cases or indirect earlier implications are residual risks.

## Mathematical value — PASS

The effective-support factor is used as a statistical complexity parameter in recent average-mixing theory. This exact family proves why geometric decay of average mixing does not guarantee monotonicity of that factor and gives a complete uniform/nonuniform and Rényi-order classification. The critical coefficients quantify the vanishing overshoot and diverging optimal lag near Shannon order; these go beyond merely observing failure of subadditivity for an arbitrary joint distribution.

## Scope and residual risks

The theorem addresses only finite-state strictly positive refresh kernels. No inference is made about arbitrary Markov chains or every truncated lag envelope. The general prior landscape is broad, so a differently formulated result may remain unidentified. A source on the general structure of Rényi entropic inequalities was available at abstract level; its full text was not substantively examined, and its general feasibility statement is not asserted to be absent from the finding. The review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
