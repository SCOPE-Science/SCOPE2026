---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

**Reproduce.** Run `python3 check.py` with Python 3, NumPy and SciPy installed. The test script derives exact rational volumes by a binomial coefficient sum, evaluates original piecewise fibers by independent numerical quadrature, reconstructs convex hulls of small fractional stable-set polytopes, and compares scaled finite-volume and marginal CDF values to the gamma-limit formulas.

**Observed checks.** On the recorded run: 24 exact rational versus quadrature volume comparisons; eight independent convex-hull comparisons (four clique graphs and four clique windmills); twelve normalized Laplace convergence comparisons; nine scaled hub CDF comparisons. All numerical assertions passed. Complete-graph checks enumerate the zero vector, unit vectors and half-indicator points of subsets with at least three elements. Windmill checks enumerate all feasible half-integral points for the stated small graph cases.

**Proof-dependent claims.** For all integers \(m\ge1\) and fixed integers \(r\ge2\), the finite one-block fiber decomposition and the Cartesian-product volume identities are exact analytical facts. Dominated convergence, not simulation, proves the \(m\to\infty\) limits. Neither the code nor these experiments certify correctness or originality independently. No uniform-in-\(r\) convergence rates or claims about all literature are made.
