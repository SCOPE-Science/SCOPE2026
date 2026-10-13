# Scientific review: smooth copula tail-order reversal

## Correctness — PASS
The construction gives an explicit smooth conditional density whose row masses equal one. Subtracting its weighted column masses from one produces a positive corrective density: \(m(v)\le2H\sqrt\delta+\delta<1/4\), so there is no hidden negativity. Differentiation on compact interior sets is legitimate, both margins integrate to one, and no singular mass remains. The tail inequality follows from the uniform \(O(s^{3/2})\) bound at fixed rays. The exact curved-path identity leaves a super-polynomially small deficit, whereas any fixed positive Clayton parameter has a polynomial-order deficit. Two convexity bounds establish finite information. Representative high-precision checks passed; proof is analytic and covers the continuum. Residual limits concern boundary smoothness and parameter-uniform rates, which are not claimed.

## Originality — PASS, with priority risk
The principal comparison is Siburg–Strothmann (2022), Example 3: it does yield strict-tail/local-order reversal but uses a singular Marshall–Olkin copula. Their full-text Theorem 2 (positive ordering on interior cones) and Section 5 (restricted sufficient classes) do not imply a positive interior-\(C^\infty\), finite-information counterexample. The 2022 comparison-and-quantification study addresses tail dependence orders without this regularity-strengthened construction. Search comparisons examined alternative terms including absolutely continuous copulas, local lower orthant order, Clayton, smooth copula density, and curved-path tail behavior. Related published material was not found to cover this exact claim. A pre-existing independent smoothing construction under different terminology remains a residual bibliographic risk; this does not assert independent novelty certification.

## Value — PASS
A mathematically natural regularity question remained after the original singular counterexample: could strict positivity and smooth absolute continuity, or finite information, prevent the anomalous curved-path reversal? The theorem answers no without relaxing the strictness of the tail comparison. The shared construction works against the full one-parameter Clayton class and separates interior regularity from boundary-uniform regularity. This is a meaningful structural boundary for inference about extremal dependence, not a normalizing identity or arbitrary finite table.

## Limitations and context
The density is not claimed to extend boundedly or smoothly to the closed square. Fixed-ray order remains consistent with established cone results. Publication priority still requires independent assessment.

Self-review: passed. Independent audit: not yet performed.
