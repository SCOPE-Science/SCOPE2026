# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Substituting the scalar quadratic family directly into the source paper's out-of-sample feedback definitions gives two convex quadratics in the proposed scalar stepsize. Their population minimizers are respectively \(1/\mathbb E[A]\) and \(\mathbb E[A^{-1}]\). The actual one-step squared-state multiplier is another convex quadratic with minimizer \(\mathbb E[A]/\mathbb E[A^2]\). The ordering follows from \(\mathbb E[A^2]\ge (\mathbb E A)^2\) and Jensen's inequality.

For support \([1,\kappa]\), the ratio threshold follows from the sharp Bhatia--Davis variance bound. The hypergradient threshold follows from two pointwise chord inequalities, both simultaneously sharp on endpoint-supported laws, followed by a one-variable maximization whose maximizer is \(\mathbb E A=\sqrt\kappa\). Solving the resulting equality with 2 gives the stated closed form \(\kappa_{\rm hyp}=3.546455444684995\ldots\). The null-step acceptance calculation follows directly from positivity of the independent evaluation curvature. The finite-batch lower bound uses only the positive contribution of the all-low-curvature batch. The published verification script reproduces the formulas and found no numerical violations in the stated checks.

Potential hidden assumptions were checked explicitly: \(A>0\) is needed for inverse moments; the evaluation curvature is independent and positive; the support thresholds concern raw unclipped population targets; and the null-step result is not presented as divergence of the published hypergradient algorithm.

## Originality

**PASS, to the best of our knowledge.** The motivating 2026 paper was inspected at the definitions of naive and out-of-sample feedback, the OSGM-SGD algorithm, and the discussion motivating large batches. It establishes stochastic OSGM convergence under its assumptions and already identifies same-batch feedback failure; those facts are excluded from the novelty claim. Its checked text does not state a mean-square random-curvature population target calculation or the sharp support-only thresholds reported here.

Prior hypergradient literature was searched, including Baydin et al. (2018), Almeida et al. (1999), and the deterministic online-learning analysis of Chu et al. (2025). Hypergradient adaptation, stochastic meta-descent, deterministic local stepsize optimality, and generic instability phenomena are prior art and are excluded. Classical random-recursion and adaptive-filter mean-square stepsize theory is also treated as background rather than a novelty claim.

Searches using the source identifier, the formulas involving \(\mathbb E[A^{-1}]\), mean-square stability terminology, coefficient-of-variation characterizations, and the exact threshold constants did not find an equivalent source-specific result. Existing SCOPE records were also searched by the source identifier and synonymous hypergradient/random-curvature terminology immediately before publication.

The principal residual originality risk is older adaptive-filter or stochastic-learning-rate literature that may contain equivalent scalar random-curvature calculations under different notation. Such coverage would reduce novelty of individual ingredients, but no checked source was found to combine the two 2026 out-of-sample feedback objectives with the exact target ordering, both sharp support thresholds, the null-step phase, and the finite-batch obstruction.

## Value

**PASS.** The result identifies a precise distinction that is hidden by the phrase “out-of-sample”: independence makes the evaluation unbiased, but does not make either feedback objective equal to the stochastic update's mean-square objective. The sharp condition-number thresholds quantify the robustness gap between ratio and hypergradient feedback, while the two-curvature calculation explains why the hypergradient null step can be essential. The batch-size expansion gives a concrete mechanism for why large batches make the three target stepsizes coalesce.

## Limitations

The theorem is scalar and quadratic, concerns one-step mean-square state contraction, and analyzes population feedback minimizers rather than the full online scheduler dynamics. Candidate-set projection can clip the displayed raw targets, and the hypergradient null step can reject unstable raw proposals. No claim is made that the published SOSGM algorithm diverges on these examples, nor that one-step mean-square optimality is the correct long-horizon objective in every application.
