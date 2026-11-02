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

Execute `python3 verify.py` using Python 3 (standard library only). This reconstructs the polynomial `R_(p^a)` coefficient by coefficient from independently evaluated Ramanujan sums and compares it to the displayed `p^(a-1)*(1-X^P)*E_(p,a)` product. For odd primes, it also computes all shifted coefficients and checks Eisenstein divisibility, including the constant term exactly divisible by `p` and the monic leading coefficient. Six polynomial discriminants are independently obtained from integer Sylvester determinants using fraction-free Gaussian elimination.

Actual execution output:

`VERIFY_OK: 14 exact prime-power cases; 417 independently computed Ramanujan coefficients; 265 shifted-Eisenstein coefficient divisibility checks; 6 independent resultant-discriminant checks.`

These checks are finite, not a proof for all prime powers. The symbolic proof in RESULT.md establishes the universal claims. Archimedean annulus and unique real root are proved analytically, not tested numerically. Discriminant comparisons are finite corroboration of the universal resultant proof. The script requires no network services, external data, or third-party packages.
