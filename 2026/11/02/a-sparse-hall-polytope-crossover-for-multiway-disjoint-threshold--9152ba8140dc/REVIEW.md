# Scientific review

## Correctness — PASS

The claim is proved for independent Bernoulli subsets with fixed number of events and central-limit-scale thresholds. A capacitated Hall matching argument gives an **exact finite-dimensional** condition for mutually disjoint witnesses. The independent binomial central limit theorem controls the marginal surpluses, while explicit binomial-coordinate moment calculations give \(B_{J,n}/s_n-\binom{|J|}{2}\tau_n\to0\) in probability at bounded collision scale. Gaussian boundary continuity then identifies the full multivariate limit. A separate pair-intersection concentration argument handles divergent collision scale. The small- and large-parameter Gaussian laws follow from simplex integration and conditional Gaussian regression. All quantifiers, ceiling errors, subset constraints, and parameter regimes are stated in `RESULT.md`. Exhaustive matching, exact-rational probabilities, an analytic Gaussian integral, and seeded finite-size checks provide supplementary evidence, not infinite proof.

## Originality — PASS (subject to historical-priority risk)

Tesio's *How much do increasing events occur disjointly?* (arXiv:2610.32658v1, Section 6) gives the exact pair-union criterion and studies threshold witnesses explicitly at **fixed** Bernoulli parameter; it does not evaluate a sparse \(n^{-1/3}\) triangular-array crossover or multiway Hall-polytope limit. Cerf–Tesio's *The case of equality in BK* (arXiv:2607.02272, Definition 1.4 and Theorem 1.5) supplies the pairwise disjoint-testimony formalism, not this asymptotic law. published-finding corpus semantic searches for sparse threshold testimony, Hall matching, and Gaussian critical windows returned no same-object complete theorem. An accessible earlier mathematical record addressing fixed-bias two-event windows does not imply this sparse multiway limit. The closest general reductions (Hall matching and binomial CLT) do imply some ingredients but not directly the identified critical balance, subset-indexed Gaussian limit, or endpoint coefficient; these are explicitly proved here. A generic unpublished or differently phrased random matching limit could still contain the result.

## Mathematical value — PASS

Witness compatibility and the difference between eventwise occurrence and simultaneous disjoint certification are natural quantitative questions for increasing events. The theorem identifies a sharp sparsity exponent and a nontrivial continuum of multi-event collision laws; the full Hall-subset geometry, different marginal offsets, and the quadratic onset are not captured by pairwise overlap heuristics. The exact result remains meaningful even without a convergence-rate theorem, and supplies testable asymptotic benchmarks for product-space strengthened-BK questions.

## Residual limitations

No independence or third-party certification is claimed. The result does not characterize standard single-configuration BK gaps; it characterizes the product-space testimony defect. Only fixed event number and independent Bernoulli sampling are addressed. Publication-priority review should also consider general capacitated matching limit theorems.

Self-review: passed. Independent audit: not yet performed.
