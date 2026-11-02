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

Run `python3 verify_coupled_sylvester.py` from the directory holding this file. It uses exact `fractions.Fraction` matrix arithmetic and prints `EXACT_CHECKS_OK 1035` when the tests pass. The recorded checks span n=2,...,11; tau=1/8,1/2,1; and every k=1,...,n-1. They test the signed-shift powers, the two rank-one forcing norms, exact coupled equations, weighted shift power, trial residuals, termwise component norms, and relative error counts. Their dimension coverage is finite and cannot certify the universal theorem; the universal identities, uniqueness, and singular-value assertions have complete symbolic derivations in RESULT.md. Independent review is not performed.
