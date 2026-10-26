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

# Reproducible exact verification

Run `python3 verify.py` with a standard Python 3 interpreter. For every one of the twelve transient count vectors, the script reconstructs all transitions of the two-channel process and verifies the harmonic equations as exact polynomial identities of degree at most five. It checks the factorization of the majority gain, the classical voter-model value at rate one, and the one-sided zero-rate limit with exact fractions.

The computation is finite algebra, but the conclusion covers all real rates in \(0<\gamma\leq1\) because the polynomial residuals vanish identically and the denominator has positive coefficients. The proof that hitting consensus occurs almost surely, and hence that these equations identify the hitting probabilities, is in `RESULT.md`. The claim makes no assertion at exactly zero rate or for a different scheduling convention. Independent auditing has not been performed.
