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
# Reproducibility

Execute `python3 verify_stern8.py` using Python 3 standard library only. The verifier enumerates all 48 primitive pairs modulo eight, computes the two possible successors from each, and checks the specified integer vector identities with complete exact arithmetic. These identities are finite, exhaustive algebraic certificates; the transition argument upgrades them to infinite generating-function claims. The script independently enumerates Stern values up to the dyadic depth 17, checks all eight histogram series against their proposed numerators, and checks the numerator-denominator gcd by rational polynomial division.

The spectral proof that all eight error exponents are sharp is given in `RESULT.md`; finite data alone do not establish it. Full archive literature coverage and independent audit are not claimed.
