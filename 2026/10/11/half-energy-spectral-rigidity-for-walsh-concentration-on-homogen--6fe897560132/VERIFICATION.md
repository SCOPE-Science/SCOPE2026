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
# Verification of the concentration spectrum claim
The proof is analytic: parity of the compressed sign operator, strict positivity of the quadratic pairing with the defining linear form, and the binomial alternating sum give the complete result. No finite experiment is taken as proof for arbitrary dimension.

## Reproducible checks
Run `python verify.py` with standard Python 3.9+ from this directory. It constructs Fourier coefficients of multiple no-tie linear-threshold functions on cubes of dimensions one through seven, checks all cutoffs, the absence of forbidden same-parity blocks, the predicted parity dimension difference, and full rectangular rank modulo the prime `1000003`. A rank equal to the column count modulo this prime proves the corresponding rational matrix has full rank for each tested sample. It also checks the exact integer quadratic-form bounds for explicit nonzero Walsh vectors.

The tested source emitted:

`VERIFY_OK exact_cutoff_cases=443 dimensions=1..7 rank_mod_prime=1000003 parity_and_margin=checked`

This finite testing cannot exclude failure outside the tested cases; that exclusion is provided by the proof. The gap \(m/(2M)\) is a universal lower bound, not a claim of universal optimality.
