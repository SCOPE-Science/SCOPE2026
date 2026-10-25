# Self-review

**Correctness — PASS.** The fixed-size differential equation follows from the cited source's total payoff and Fermi update formula. The Bernstein coefficients for sizes two and three have exactly one sign variation under \(1<r<g\); Descartes' rule and endpoint signs prove exactly one globally attracting root, including simplicity. For four players, all five Fermi weights become exact rationals at the specified noise, and four exact rational vector-field signs force three simple roots of the quartic with alternating attraction. The executable standard-library rational certificate independently recomputes the polynomial and the signs. General results follow analytically, not from finite enumeration.

**Originality — PASS (qualified).** The motivating 2024 preprint studies variable-size groups from \(1\) to \(3\) or \(1\) to \(5\) and numerically demonstrates bistability; it does not supply the exact minimum **constant** group size under the strict social-dilemma constraints. General nonlinear-public-goods Bernstein and group-size-diversity work gives methods and adjacent phenomena, but no inspected primary statement implying both the all-parameter impossibility and exact four-player witness was located. There is residual risk from unindexed or inaccessible literature, and priority is not independently established.

**Value — PASS.** The sharp cutoff isolates interaction order from group-size heterogeneity and provides a small, exact example of two stable mixed-population states under positive noise, avoiding claims based on a numerical phase diagram. This is a motivated model-specific structural boundary rather than an arbitrary parameter enumeration.

Closest literature: Zhang–Tang (arXiv:2402.16317), Archetti (Games 2018, 9:17), Peña (Evolution 2012, 66:623–636). Scope limitations: well-mixed deterministic Fermi model; the threshold need not hold for other payoff aggregation, update or finite-population rules. Remaining publication-priority uncertainty does not amount to independent verification.

Self-review: passed. Independent audit: not yet performed.
