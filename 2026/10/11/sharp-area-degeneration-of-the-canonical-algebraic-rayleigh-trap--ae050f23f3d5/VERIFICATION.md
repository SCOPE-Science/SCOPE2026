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

# Verification details

The direct Python reproducibility check (`python3 verify.py`) returns `CHECK_OK`. It uses only the Python standard library, evaluates discriminants derived algebraically from the two specified 2023 ovals, locates their positive turning points with bisection, and integrates the resulting chord-width quadratures by composite Simpson's rule. The checked finite cases include zero damping (geometric limiting circles), small damping (quadratic coefficient), and a large damping example (renormalized inner logarithmic term and outer area slope). The script's numerical comparisons are finite evidence, not a proof of an infinite-parameter limit.

The proof separately establishes the uniqueness of each turning point, the local lower and upper endpoint expansions, the cancellation of cutoff terms, and dominated convergence for the outer-area limit. The limiting outer coefficient is exact as a one-dimensional definite integral; printed decimals are not certified error enclosures. A later Rayleigh annulus improvement could only be inspected at abstract level; full publication priority is therefore not definitively resolved.
