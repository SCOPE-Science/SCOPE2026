---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 16 Bernoulli weighted vertices, each 5-set normalized simplex determinant is integer. Vanishing at each p_i=0,1 factors e4=∏p_i(1-p_i); degree at most 5 per bias, reflection p_i↦1-p_i and coordinate permutations force the quotient to be symmetric multiaffine in q_i and hence Σa_j e_j(q). An independently implemented exhaustive census of all 4368 five-sets found determinant multiplicities 1360/2672/320/16 for 0/1/2/3 and exactly the claimed 13 nonzero diagonal coefficient counts. This determines R=1-4e3+18e4 on all biases, rather than extrapolating a finite sample. Separate exact rational summation at biases (1/2,1/3,1/4,1/5) gave ratio 1613/1800. Because 4Σ1/q_i-18≥46, the deficit is ≥46e4² with sharp equality at all q_i=1/4. Only the product-distribution subfamily, not all 16 weights, is proved.

## originality

PASS

The complete independent-coordinate Bernoulli four-parameter identity, not the already known unrestricted formulation or symmetric uniform value, is the proposed new claim. A fully read Resultary sharp symmetric gap result has a disjoint positive interior parameter family except at uniform biases and cannot imply the new coefficients. The initiating arXiv full text remained unavailable, a genuine residual priority risk.

## value

PASS

Independent Bernoulli probabilities form a natural probabilistic slice of an explicitly open four-cube inequality. The exact expectation and sharp variance-square deficit are independently useful quantitative invariants, rather than an arbitrary few data points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
