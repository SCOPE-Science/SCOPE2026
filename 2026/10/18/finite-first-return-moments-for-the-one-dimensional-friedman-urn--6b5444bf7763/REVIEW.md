# Scientific review

**Correctness — PASS.** The urn has exactly \(n+1\) balls at time \(n\); its right-step probability at a positive state is \((n+2-x)/(2(n+1))\). This yields the exact killed first-moment recurrence. Uniform-in-time domination by a killed symmetric random walk supplies a reflection-principle bound. The resulting survival inequality bootstraps from order \(n^{-1/2}\) to order \(n^{-1}\), then to a summable logarithmically corrected bound, and finally to order \(n^{-3/2}\). Endpoint initial conditions, event boundaries, and the integer parity issue are addressed. A standalone script passes 889 finite tests, chiefly exact rational identities plus deterministic numerical bound checks, which supplement but do not replace the proof.

**Originality — PASS, subject to priority uncertainty.** Balaji and Mahmoud explicitly conjecture finite first-return mean for precisely this Friedman-urn process. Their one-time Eulerian recurrence argument does not imply summability of the first-return tail. Menshikov–Volkov analyzes drift criteria and Friedman-type outward-drift examples; Bercu–Bonnefont–Richou covers Eulerian marginal deviations. Source comparisons and mathematical searches identified no theorem covering this finite-mean and survival-tail claim. An unindexed general first-passage result remains possible.

**Value — PASS.** The result answers a named, naturally motivated first-passage question and improves it to a quantitative polynomial tail. It also implies all moments strictly below order \(3/2\), a feature not implied by mere recurrence. The cutoff is a proved sufficiency range, not claimed sharp.

**Scientific limits and closest literature.** The theorem is for one white initial ball and the one-dimensional opposite-color urn; no lower tail bound, exact tail constant, endpoint \(3/2\)-moment classification, stationary law, or multidimensional generalization is proved. Relevant full-text comparisons are Balaji–Mahmoud, arXiv:2504.14813; Menshikov–Volkov, arXiv:0711.2373; and the Friedman/Eulerian marginal treatment of Bercu–Bonnefont–Richou.

Self-review: passed. Independent audit: not yet performed.
