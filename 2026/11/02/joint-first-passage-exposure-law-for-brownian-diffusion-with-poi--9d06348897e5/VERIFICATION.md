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

# Reproducibility and verification

The included standalone `check_joint.py` uses NumPy, SciPy, SymPy, and mpmath. Execute with `python check_joint.py`. The following checks were actually performed against that file:

1. Four symbolic derivative identities, including the conditional subordinator's first two cumulant coefficients.
2. Five independently discretized two-region, three-argument backward equations using a sparse finite-difference solver. The relative discrepancies from the continuum transform were 0.00235326, 0.00141635, 0.00080848, 0.00159589, and 0.0000646653.
3. Two published marginal transform identities in each of those five parameter cases (completion-time and residence-time transforms), with the local-time marginal also visible algebraically in the analytic derivation.
4. Three high-precision Lévy integral comparisons and three correlation-identity calculations.

Finite-grid checks are not continuum proofs; consistency of symbolic expressions and numerical tests does not establish originality. The full continuum argument is provided in RESULT.md and is the basis for the correctness assessment. The public record does not assert that any independent audit has occurred.
