# Independent mathematical audit — SCOPE-20260918-adcb7befe3ff

Final disposition: **PASS**.

## Correctness
**PASS** — A fresh Hamming-weight decomposition reproduces the finite bound: the zero slice differs from the signed intensity term by at most half the quadratic mass, the singleton slice differs from the coordinatewise l1 discrepancy by at most the full quadratic mass, and all multiple-success slices contribute at most another half, which yields the stated total-variation error after the factor one-half normalization. The proxy estimate follows by isolating exactly one disagreement and bounding two-or-more disagreements. For the sign-pattern family, swapping coordinates preserves every lambda_i and a_i exactly while changing only the net signed intensity. An independent exact enumeration on small rational examples reproduced the aligned and balanced first-order behavior.

## Originality
**PASS** — Smirnov's complete seven-page v2 was inspected. It proves a constant-factor proxy and the exact upper inequality but does not contain the signed rare-event expansion or the same-data factor-two obstruction. Avital-Kontorovich-Salafatinos give only constant-factor small-parameter descriptions. Searches for the signed-intensity correction and identical proxy-data obstruction found no stronger prior result. Thus the final claim is original to the best of current knowledge.

### Equivalent formulations
Equivalent rare-event and proxy formulations were checked; none of the inspected prior statements contains the signed correction.

### Broader coverage
The inspected broader results do not imply the finite additive expansion or the identical-proxy-data factor-two family.

### Exact database or table
This negative search is only supporting evidence; novelty rests on direct statement comparison with the full primary proxy paper.

### Claim versus prior implication
The final claim is not a corollary of the inspected proxy bounds.

## Value
**PASS** — The result identifies exactly which first-order statistic is lost by a newly proposed efficient proxy, gives a finite quantitative correction rather than only an asymptotic slogan, and constructs pairs with identical complete proxy data but asymptotically factor-two different true distances. Those are natural information-loss and approximation-boundary statements with direct relevance to the motivating problem.

## Source inspections
- **TV between Bernoulli products, up to constants** (https://arxiv.org/abs/2609.19222): complete seven-page arXiv v2 Assessment: NOT_COVERING_SIGNED_RARE_EVENT_REFINEMENT. Evidence: Theorem 1.1 compares TV to the proxy up to constants and proves the upper bound, but does not state the signed mass correction.
- **TV over Bernoulli products: the small parameter regime** (https://arxiv.org/abs/2602.21828): primary abstract Assessment: BROADER_SMALL_PARAMETER_CONTEXT_NOT_EXACT_REFINEMENT. Evidence: The abstract gives constant-factor tiny/small-regime formulas rather than the audited additive second-order expansion.

## Residual risks
- Older Poisson-binomial signed-measure asymptotics could contain related expansions under different terminology.
- The finite bound is most informative when the first-order discrepancy is not dominated by the quadratic remainder; no higher-order expansion is claimed.
