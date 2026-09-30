# Independent Audit — 2026/09/17/heterogeneous-bernoulli-exact-chernoff-envelope--40d55355f1a6

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `ed14325f59ea436424aa4ed50fd3ff57b360395a`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact cgf reduction is correct. The centered Horvitz-Thompson error is a sum of independent terms d_i(Z_i-p_i)/[p_i(1-p_i)], with d_i ranging over the full interval [a_i-m_i,b_i-m_i]; convexity of the Bernoulli log-mgf makes the endpoint maximum exact unit by unit. The two-sided envelope is convex in the center vector, and reflection m -> 2c-m swaps upper and lower tails, so midpoint centering is pointwise minimax. The g_q formula follows from selecting the larger endpoint according to min(p,1-p). The Hoeffding and Bernstein specializations have the stated support/variance scales, and at Y_i(0)=Y_i(1)=b_i the variance is exactly V_n, while M_n/sqrt(V_n)->0 gives Lindeberg and the matching Gaussian lower-rate obstruction. A random numerical stress test of the midpoint inequality over heterogeneous propensities found no violations.

## Originality

**PASS** — Freidling's September 2026 randomization-inference paper develops Hoeffding/Bernstein finite-sample intervals, while Aronow-Lopatto prove midpoint-differenced Horvitz-Thompson minimaxity for worst-case squared error. Older survey-sampling work gives exponential inequalities for rejective/conditional-Poisson schemes. Targeted searches did not locate the combined exact bounded-outcome cgf envelope for arbitrary independent unequal propensities, its pointwise midpoint minimaxity for exponential loss, and the resulting aggregate heterogeneous effective-sample-size lower/upper scale. The ingredients are elementary, but the theorem package appears distinct.

## Scientific value

**PASS** — The result sharpens a current finite-sample inference problem exactly where unequal propensities make worst-unit Hoeffding bounds unattractive. It gives a separable exact envelope requiring only one-dimensional Chernoff optimization, connects the same midpoint center to a second minimax criterion, and identifies a matching heterogeneous sum_i[p_i(1-p_i)]^-1 scale. Those features are directly reusable in design-based treatment-effect inference.

## Sources

- Randomization Inference with Concentration Inequalities (Tobias Freidling): https://arxiv.org/abs/2609.18586 — Closest current concentration-based SATE source; develops Hoeffding and Bernstein-type intervals.
- Minimax unbiased estimation for finite populations with bounded outcomes (P. M. Aronow; Patrick Lopatto): https://arxiv.org/abs/2605.20572 — Proves midpoint-differenced Horvitz-Thompson minimaxity for worst-case squared error, a different loss criterion.
- Bernstein-type exponential inequalities in survey sampling: Conditional Poisson sampling schemes (Patrice Bertail; Stephan Clémençon): https://doi.org/10.3150/18-BEJ1101 — Older exponential-inequality literature for rejective/conditional-Poisson sampling; not the exact independent-Bernoulli endpoint envelope.

## Limitations

- The theorem requires independent Bernoulli assignment and known deterministic outcome bounds.
- Midpoint minimaxity is only for the two-sided cgf envelope within the centered Horvitz-Thompson family, not for all unbiased estimators.
- The exactness is for the worst-case cgf; Chernoff inversion and the union bound are not exact-tail or shortest-interval results.
- Residual originality risk remains from older survey-sampling literature under different notation.

## Independent exact check

```json
{
  "implementation": "symbolic derivation plus randomized numerical convexity/reflection stress test",
  "random_cases_checked": 1000,
  "midpoint_violations": 0,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
