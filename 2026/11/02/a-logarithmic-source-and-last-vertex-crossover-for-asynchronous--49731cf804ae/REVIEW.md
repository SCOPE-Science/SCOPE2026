# Scientific review

## Correctness — PASS

The finite-time law is derived from independently thinned Poisson contact processes on a tree, with rates \(r_a\), \(r_b\) and \(c\). The CDF, first moment and last-informed-side expressions follow from independent exponential maxima and their Laplace transforms. The source ordering follows from a nondecreasing ratio of the two maximum CDFs; the proof checks the direction of the inequality and preserves the required independence (a monotone coupling of the two maxima by itself would not justify the result). Gumbel convergence, the bridge exponential law, continuity away from the limiting atom, and uniform integrability support the exact statements of the three regimes. The standalone checker independently agrees with exact finite-state Markov recurrences for all \(1\le a,b\le9\), and performs additional CDF/source-order and scaling diagnostics. Numerical tests are not offered as proofs of the asymptotic claims.

## Originality — PASS, with historical-priority risk

Acan et al., arXiv:1411.0948 (first posted 2014-11-04), Proposition 13 already establish independent exponential edge contacts for asynchronous push-pull on any graph, and Section 2.4 gives first-order results for balanced double stars. This prior reduction **covers the foundational mechanism** and is credited. Giakkoupis et al., arXiv:2006.02368v1 (first posted 2020-06-03), Section 4.2 also uses a balanced double star to separate dissemination protocols, but analyzes order-of-growth rather than the unbalanced asynchronous hub-source and finishing-side laws. The inspected material did not give the source-order reverse-hazard criterion, exact rational finishing-side distribution or the \(b\asymp\log a\) critical limiting atom and mean difference. Explicit published-finding corpus semantic searches for this model, its transformations, hub-source ordering and limiting regimes returned no implication-equivalent finding; the accessible prior research records was checked for the same objects and conclusions. These negative searches are evidence of comparison, not a uniqueness certificate. Historical articles outside the inspected set and undiscovered equivalent formulations remain risks.

## Value — PASS

The result provides a complete finite distribution for a canonical communication bottleneck, proves a deadline-uniform ordering of possible hub sources, and identifies the natural point where the smaller community's hub delay first competes with the large community's extreme leaf waiting time. Its non-Gumbel critical law has an atom whose mass directly predicts which community finishes last; the exact mean difference quantifies the benefit of informing the higher-degree hub first. These questions arise from source selection and finishing-side uncertainty on highly heterogeneous networks, not an arbitrary parameter slice. The result is specialized and does not settle general-network broadcast optimization.

## Closest literature and limitations

- Acan, Collevecchio, Mehrabian and Wormald, *On the push&pull protocol for rumour spreading*, arXiv:1411.0948, Proposition 13 and Sections 2.2–2.4, https://arxiv.org/abs/1411.0948.
- Giakkoupis, Mallmann-Trenn and Saribekyan, *How to Spread a Rumor: Call Your Neighbors or Take a Walk?*, arXiv:2006.02368v1, Section 4.2, https://arxiv.org/abs/2006.02368.

The primary result assumes independent Poisson calls and exactly two hubs linked by a bridge, and it compares only hub sources. The asymptotic critical window requires one leaf class to be logarithmic relative to the other. No historical-priority or independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
