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

# Reproducibility and boundaries
Run `python3 verify_hypercube.py` with Python 3 and no third-party packages. The script constructs the polar vertices by normalized integer potentials with unit gradients on all graph edges. For dimensions \(d=2,3,4\) it checks all \(6,38,990\) polar vertices using exact fractions, respectively; every squared norm is bounded by \(d2^{d-2}\), with precisely \(2^d\) equality cases. It compares all equality vectors to explicit degree-one Walsh sign combinations, checks the rank \(d\) of their span, and verifies a genuinely displaced ball of the same radius using exact squared facet inequalities for each dimension.

The all-dimensional spectral inequality, its equality characterization, integer squared-norm gap and displaced-center margin are proved in `RESULT.md`. Finite exhaustive experiments are not proofs for arbitrary dimensions. No complete enumeration for larger dimensions or independent external validation is asserted.
