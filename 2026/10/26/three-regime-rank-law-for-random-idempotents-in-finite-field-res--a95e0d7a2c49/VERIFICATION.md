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

# Reproducible mathematical checks

Run `python3 verify.py` using Python 3.9 or newer; it depends only on the standard library. Success outputs `VERIFY_OK` after all checks. The program enumerates all matrices of the form with bottom \(m\) rows zero, multiplies matrices directly to impose \(E^2=E\), computes ranks by modular elimination, and compares all resulting rank strata with the explicit projection count for thirteen small prime-field cases. It also verifies integer product identities for prime powers \(q=2,3,4,5,7,8,9,11\) and compares critical-window ratios against their limiting weights for several fixed offsets.

Exhaustive tests cover only selected small dimensions and prime fields. The other prime-power tests are arithmetic checks of finite formulas, not exhaustive extension-field enumeration. The total-variation and free-energy statements are mathematically proved in `RESULT.md` using finite-product bounds and dominated convergence, not certified solely by the program. No independent audit has been performed.
