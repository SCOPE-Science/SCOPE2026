# Self-review

## Correctness
PASS. Conditional on the directing vector, every adjacent change indicator has mean equal to \(D=1-\sum_jP_j^2\). The mixed covariance follows by the tower property. Symmetric Dirichlet moments give the closed \(\operatorname{Var}(D)\); separating adjacent from disjoint edge pairs gives the stated \(\operatorname{Var}(T_n)\) and hence the exact correlation. An exact rational checker independently verifies 45 parameter cases and 20,007 complete sequence states.

## Originality
PASS. The closest full-text source, DOI 10.1239/jap/1231340230, develops the same multicolor Pólya/Dirichlet run framework but integrates out the directing vector and does not state a mixed run–latent-diversity moment. Claim-specific searches over aliases such as total runs, changes, switches, Gini–Simpson diversity, homozygosity, and Dirichlet directing measure located no equivalent formula. The closest inaccessible source is DOI 10.1016/j.spl.2008.01.002; its abstract covers marginal run distributions, so its unread full body remains a residual risk.

## Value
PASS. The result connects a canonical local path statistic with a canonical latent diversity parameter, giving both an exact finite-sample correlation and its approach to one. It quantifies how reinforcement-induced exchangeability still lets transition frequency recover latent diversity and is not implied by existing fixed-probability coverage/run covariance results.

## Closest literature and limitations
The explicit formulas assume a symmetric finite-color Dirichlet directing law. The universal conditional-unbiasedness identity itself is broader. No optimal-estimation claim is made. The complete body of the 2008 Statistics & Probability Letters paper on exchangeable multi-state runs was not available for inspection.

Self-review: passed. Independent audit: not yet performed.
