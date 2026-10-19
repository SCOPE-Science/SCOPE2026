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

# Reproducibility and mathematical limits

Run `python verify.py` with Python 3 using only its standard library. In the recorded execution, the program passed 50,139 counted verification checks: matrix trace/determinant identities, characteristic-root comparisons, model-specific Schur limits, rate-optimal relaxations and exact rational nilpotence. The verified special values \(q=3/2\), \(c=1\), \(\tau=7/24\), \(\rho=25/7\) produce a nonzero two-by-two rational matrix with exact zero square.

The proof's global quantifiers, positive-parameter uniqueness, phase boundaries and exclusion of universal finite termination at \(q\ge2c\) follow from the symbolic discriminant and Cayley--Hamilton argument, **not** from the numerical cases. No independent external mathematical audit has been performed. Finite precision and actual block-ADMM behavior are outside the verification scope.
