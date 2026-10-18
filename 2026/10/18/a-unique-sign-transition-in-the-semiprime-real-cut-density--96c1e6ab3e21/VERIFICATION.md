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

# Reproducibility and limits

The proof in `RESULT.md` is analytic and self-contained apart from standard zeta continuation and Euler-product logarithmic-derivative identities. Its decisive checks are: the exact fractional-part integral for \(\zeta\); the sign of \(F(z)\) on \((0,2^{-1/2}]\); local uniform convergence for \(n\ge2\); the logarithmic endpoint asymptotics; and the derivative of the exponentially renormalized integral. These demonstrate universal statements, not merely tested cases.

`verify.py` independently evaluates the specified real Möbius-log branch and the upper-cut integral numerically at selected points. Floating evaluations are neither interval certificates nor proofs of uniqueness. The reported approximate density root is an illustration only and not a theorem assumption. No independent mathematical audit or external certification has been performed.
