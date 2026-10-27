# Scientific review

## Correctness — PASS
The analysis is a complete degree-wise proof. The variance identity and uniform first-derivative convergence restrict optimizers near the midpoint. For odd degrees, local strict concavity persists. For even degrees, splitting off the nonanalytic central binomial atom gives the exact curvature limit \(b_n+1/n\), a unique off-center critical point on each side below exponent two, and the logarithmic displacement and gain formulas. The numerical script checks representative finite-degree instances and is not presented as an infinite certificate.

## Originality — PASS with documented uncertainty
The closest primary work is Adell, Bustamante and Quesada (2015), which defines these Bernstein absolute moments and provides estimates, and Berend and Kontorovich (2013), which studies the exact first absolute binomial moment. Comparing mathematical statements, neither accessible result determines the parity-dependent optimizer splitting and essential singularity as \(r\uparrow2\). Broader searches for equivalent moment maximization, exponent-two cusp behavior, and asymptotic locations found no equivalent theorem. The complete 2015 primary paper was not accessible, so any unobserved ancillary conclusion there, or an unindexed earlier result, remains a residual originality risk.

## Mathematical value — PASS
Sharp Bernstein-moment envelopes are natural quantities in positive approximation theory. The result resolves a qualitative optimizer transition at the quadratic-moment exponent and its non-power-law scale for every fixed degree, with an exact rate for the tiny gain. The parity distinction and exponentially small displacement explain why ordinary numerical searches can misleadingly report a single centered maximizer.

## Limits
The neighborhood of exponent two depends on degree. The theorem does not solve the global exponent phase diagram, does not assert degree-uniform asymptotics, and has no independent validation. The proof, not the numerical test, supports the continuum assertion.

Self-review: passed. Independent audit: not yet performed.
