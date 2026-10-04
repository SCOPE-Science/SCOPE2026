# Review

## Correctness
PASS. The source's model gives the asymptomatic and recovered right-hand sides as \(F_4\) and \(F_5\), and its own Eqs. (5.4)–(5.5) use those fields. Eqs. (5.10)–(5.11) then use \(F_3\) and \(F_4\), and the correctors (5.15)–(5.16) repeat those substitutions at every quadrature term. The exact rational witness gives three distinct initial field values \(1/2,1,0\). The standard Caputo-to-Volterra identity then yields nonzero leading differences of order \(t^\alpha\), independently of any finite experiment. The proof only concludes that the printed scheme cannot have the claimed convergence to the target equations; it does not infer what unavailable code did.

## Originality
PASS. Exact-title, formula-alias, predictor–corrector, and semantic published-finding searches did not locate an earlier statement of the repeated component shift or its implication for the claimed \(A\)- and \(R\)-error orders. The motivating paper is the decisive source: it contains both the correct component definitions and the contradictory printed scheme. Garrappa's 2018 full text gives the general system method with a single vector field evaluated componentwise and therefore does not cover the source-specific indexing defect. A closely related 2022 Sene chapter was identifiable bibliographically but its full text was not reliably available for comparison; that access gap is retained as a residual originality risk.

## Value
PASS. The defect is repeated in the pre-discretization relations, both final correctors, and the recovered predictor, and it directly invalidates two displayed convergence estimates and the article's blanket convergence conclusion for the formulas as written. This matters for reproducibility of the numerical section and interpretation of the asymptomatic and recovered trajectories. The result also gives a minimal exact witness and the precise leading discrepancy, making the issue mathematically diagnostic rather than a typographical observation.

Closest literature: Sene and Mansal (2026), Sec. 5; Garrappa (2018), general vector fractional multistep methods; Garrappa (2010), predictor–corrector stability; Sene (2022), related Caputo SEIR numerical methods.

Limitations: no public implementation was located, so the figures are not claimed to be wrong; a repaired component mapping is outside the claim.

Same-model review: passed. Independent audit: not yet performed.
