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

The standard-library script `verify.py` is self-contained and checks the rational identities for the squared weights, both commuting two-step paths, outgoing and incoming summed-commutator coefficients, and telescoping grade traces. It evaluates dimensions \(2,3,4\) on three families of monotone grade sequences and compares exact small-threshold counts for constant-trace profiles to the independently computed beta-integral coefficient in dimensions \(2\) and \(3\).

Command: `python3 verify.py`

Observed result: `SPHERICAL_SUM_DEFECT_SPECTRAL_FINITE_CHECKS_OK assertionsets=231`.

The finite tests do not prove the weak Schatten equivalence, the positive trace result for infinitely many grades, or the Weyl limiting constant. The derivations in `RESULT.md` supply their infinite-dimensional proofs using monotone convergence, grade counting, and Riemann sums. No independent audit has been performed.
