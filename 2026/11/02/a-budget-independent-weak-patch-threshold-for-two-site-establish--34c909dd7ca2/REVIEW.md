# Review of the three-site seeding threshold

## Correctness

**PASS.** With Poisson mean \(a x_i\) for the first two sites and \(b x_3\) for the third, site-failure probabilities are exactly exponential. Conditional on third-site establishment, the strong-site failure product is fixed under equal-sum allocations while the failure-probability sum is uniquely minimized by balancing. The remaining scalar failure objective has derivative \(u[u(1-v)+(1-2h)v(1-u)]\). Its sign proves the zero-third-site regime, the sharp equality at \(h=1/2\), and the unique strictly interior root when \(h>1/2\). Root logarithms prove the two limits. The embedded checker passed 18,898 assertions. Continuum validity rests on the proof, not the sample checks.

## Originality

**PASS on accessible scientific evidence, with residual risk.** Comparison of published mathematical records and primary literature did not identify an equivalent three-site unequal-Poisson-efficiency threshold. Derman–Lieberman–Ross (1974) is the closest abstract-level antecedent: it treats general \(k\)-out-of-\(n\) allocation with a common resource-to-reliability function, so its stated hypotheses do not directly supply the heterogeneous efficiency classification. The Derman complete text and a related 1975 chapter were unavailable; they remain named priority risks. The full Eriksson et al. (2014) article concerns rescue and dispersal dynamics, not this constrained two-site establishment probability; the Leung et al. (2004) PDF was accessible only on its first page.

## Value

**PASS.** A requirement that two geographically distinct introductions establish is a natural minimal redundancy criterion for a conservation-reintroduction program. The exact half-efficiency cutoff is budget-independent, and the weak site's large-budget share differs substantially from its small-budget share. These facts give a checkable allocation benchmark and explicit regime boundaries, without asserting that ecological field systems satisfy the independence assumption.

## Risks and limits

The biological model is deliberately one-shot; stochastic dispersal, site dependence, Allee barriers beyond one successful founder, and long-term viability are not treated. A general reliability allocation result may already imply this specialized threshold; direct full-text comparison to the most relevant older work was unavailable. No external scientific or historical priority audit is claimed.

Self-review: passed. Independent audit: not yet performed.
