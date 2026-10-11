# Scientific same-model review

## Correctness — PASS

The statement is valid for all nonconstant one-variable real rational Herglotz--Nevanlinna inputs with positive residues and nonnegative linear coefficient, including the zero-pole positive-slope case and all finite pole counts. The published graph representation has precisely the factor \(\pi\) and the weights \(1/J'\); their inverse-graph Jacobians cancel. The \(t\)-root sums are the Vieta sums of a degree-\(N+1\) polynomial for positive slope and a degree-\(N\) polynomial for zero slope away from its exceptional value. Differentiating the complete real inverse-root sets gives exactly \(1/a\) or \(\Gamma/(b-s)^2\). The exceptional inverse value and \(y=0\) carry no atoms; the quadratic blow-ups are genuinely nonintegrable. Rational-function identity and graph separation complete the common-marginal and mutual-singularity proofs. Symbolic leading-coefficient checks and fifteen numerical inverse-root traces and twenty-four finite-difference graph Jacobians corroborate the algebra, without replacing the proof.

## Originality — PASS

The closest directly relevant source, Fagrell--Luger [1], already proves extremality and supplies the two-graph weights; the first coordinate marginal is an immediate consequence and is not claimed as new. Neither its Theorem 3.1 nor its characterization in Proposition 3.4 states the **second-coordinate projection**, its precise local-finiteness transition, or the **if-and-only-if classification of cross-parameter marginal equivalence**. Those require collecting *all inverse roots in the first coordinate*, a second Vieta calculation that is not part of the source's two-graph construction. Nedic--Saksman [2] analyzes hyperplane-supported measures and cannot directly give this curved two-sheet classification. The general Clark structure formula of Anderson et al. [3] is related under Cayley transforms, but does not supply the explicit rational-parameter equivalence classes. The residual risk is an unindexed or differently formulated earlier inverse-root-trace result; no search can establish absolute novelty.

## Value — PASS

This is a complete exact classification of a natural invariant of a newly identified extreme family, not an arbitrary finite parameter computation: it distinguishes a locally finite Lebesgue second marginal from a nonlocally finite one by the single analytic datum \(a=0\), determines exactly which coefficients survive both coordinate projections, and proves that arbitrarily many mutually singular nonlinear extreme measures can have identical coordinate data. It gives a rigorous and fairly sharp negative result for inverse reconstruction from coordinate projections, while expressly not claiming a general theorem for all Nevanlinna measures.

## Sources and boundaries

Primary proof input: [1] arXiv:2610.02476v1, Section 3.2, Theorem 3.1, equations (20)--(24). The neighboring [2] is *On the structure of Nevanlinna measures*, DOI 10.1002/mana.202200135, Sections 2--3. The broader Cayley-related structural source [3] is *Clark measures for rational inner functions II*, arXiv:2303.11248v1, Section 3. The nonrational case, arbitrary two-variable measures, and independent validation are not addressed. The original two-variable extremality theorem is cited, not reproduced or independently certified.

Same-model review: passed. Independent audit: not yet performed.
