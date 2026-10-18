# Self-review

## Correctness — PASS

The normalization of the Lindblad generator gives off-diagonal pure-dephasing rate \(\gamma\) and center population loss rate \(\kappa\), fixing all factors of two. The Hilbert–Schmidt dissipation identity excludes imaginary-axis spectrum for \(\gamma,\kappa,J>0\), and hence justifies integration to infinity. Four closed collective observables yield the exact mean. Completing a square gives global uniqueness of the positive optimizer when \(s<m\), while the bright/dark decomposition handles the singular \(\gamma=0\) boundary separately. Direct full-superoperator integration and numerical optimization passed 326 checks (maximum absolute discrepancy \(2.096\times10^{-13}\)). Computations corroborate, but do not replace, the analytic proof.

## Originality — PASS (same-model, with residual risk)

The 2018/2022 extended-star studies optimize coherent trapping and onsite energy defects. The 2023 dephased extended-star study fixes a uniformly delocalized peripheral input and uses the time to half absorption, plus a strong-noise approximation; it does not state the arbitrary-initial-density all-noise mean-time identity. The 2023 fully connected network study has additional leaf–leaf hoppings, so its coherence-dependent transport formulas do not imply those for the hub-only star by a direct parameter substitution. The 2022 star dephasing classicalization study has no absorbing hub. Exact-formula and model-alias searches found no equivalent recorded result. An implicit reduction from a more general full-resolvent theory remains possible, and the earliest coherent star primary paper was compared through its abstract rather than full text.

## Mathematical value — PASS

For a natural hub-and-spoke excitonic transport model, the optimizer is an explicit function of the preparation's bright overlap and graph size, yet entirely independent of the trap rate. The exact discontinuity for perfectly bright preparation makes the order of the vanishing-noise and infinite-time limits operationally consequential. The result distinguishes beneficial dephasing from bright-state degradation without assuming random disorder or restricting to localized states.

## Limitations

This is an infinite-time one-particle mean-absorption theorem for uniform hopping and dephasing. It does not show robustness to graph disorder, optimal finite-time transport, or automatic novelty relative to all possible unpublished or uninspected resolvent identities. Independent audit remains necessary.

Self-review: passed. Independent audit: not yet performed.
