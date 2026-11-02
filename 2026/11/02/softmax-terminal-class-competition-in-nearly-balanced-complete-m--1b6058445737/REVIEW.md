# Scientific review

## Correctness
**PASS.** An exact conditional coupon-stream construction separates within-part labels from a finite class Markov chain. Its stationary law is verified by detailed balance; for at least three parts, a uniform two-step Doeblin minorization bounds variance of class visits by the time horizon. The standard missing-coupon factorial-moment limit combines with these clock estimates to prove the joint Gumbel law. The softmax follows from the exponential representation. Mean-value comparison of deterministic coupon clocks proves dominance above the critical imbalance window. The standalone exact-state and stochastic checker passed all its assertions. Finite checks corroborate, but do not replace, the asymptotic proof.

## Originality
**PASS, qualified.** The relevant 2021 random-regular-graph paper studies global cover-time distributions, and the 2022 last-new-vertex paper proves a uniformity characterization, not the multipartite terminal-class softmax. The 2015 Chang–Xu multipartite paper concerns hitting-time formulas according to its available abstract; its full text was not accessible. A previous complete-bipartite two-part logistic law cannot imply the nonbipartite Markov-clock competition or attenuation by \(1/(k-1)\). Targeted research-record and external searches found no equivalent or stronger statement. Residual historical-priority risk remains, particularly from inaccessible full text and potentially uncatalogued results.

## Value
**PASS.** The last discovered community of a cover tour is a natural localized extreme statistic. In complete multipartite graphs, class visit frequencies change with part sizes and oppose the straightforward coupon-load effect. Their exact competition produces a nontrivial scale \(n/\log n\) and a parameter-free sensitivity coefficient \(1/(k-1)\), quantitatively distinguishing nonbipartite from bipartite cover tours. The joint limit also determines all joint late-cover exceedance probabilities, not just an expectation or a scalar cover time.

## Closest literature and limitations
Tishby–Biham–Katzav, arXiv:2110.13592; Buchanan–Horn–Rombach, arXiv:2209.08079; Chang–Xu, DOI:10.4310/PAMQ.2015.v11.n3.a1 (abstract only); Rivera–Sauerwald–Sylvester, DOI:10.4230/LIPIcs.ICALP.2021.107 (abstract only). The result assumes fixed \(k\), nearly balanced part sizes, and simple random walk. Broader heterogeneity, quantitative rates, and historical priority beyond the inspected material remain open.

Self-review: passed. Independent audit: not yet performed.
