# Scientific review: Uniform forest collision law

**Correctness (PASS).** Conditional on the Stam box count, all edge-equality indicators in a forest are independent Bernoulli variables; this is verified by calculating each edge-subset product moment. The ratio of successive weights for the box count has an explicit decreasing logarithm, giving a moderate-deviation tail smaller than the smallest avoidance main term. The proof then uses uniform Taylor bounds and binomial-to-Poisson total-variation coupling. Exhaustive finite computations in `checker.py` corroborated 75 forest histograms and the cycle boundary; the asymptotic proof is analytic, not an extrapolation from finite data.

**Originality (PASS within inspected sources; priority risk remains).** Galvin--Thanh's graphical Stirling identities account for finite forest counts, and Chern--Diaconis--Kane--Rhoades' box method accounts for the conditional construction and known adjacent-edge binomial phenomenon. Those are not claimed as new. The inspected sources did not establish the uniform moving-target Poisson *total-variation* law and *relative* vanishing event asymptotic across all forests. An older graph-Bell or occupancy formulation might still imply this result, so this is not a uniqueness certificate.

**Value (PASS).** The probability of a concrete first-order compatibility property can be as small as \((W(n)/n)^r\) for spanning trees. A uniform relative estimate, not only a probability tending to zero, resolves its natural quantitative scale while revealing a sharp structural forest-versus-cycle boundary.

Closest primary literature: Koponen, arXiv:2610.16163 (first public 2026-10-12), Chern et al., arXiv:1502.00938, and Galvin--Thanh, arXiv:1206.3591. Important limitations: fixed \(r\), deterministic forests only, no general first-order convergence-law assertion, and incomplete global priority coverage. Full source comparisons and residual risks are recorded in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
