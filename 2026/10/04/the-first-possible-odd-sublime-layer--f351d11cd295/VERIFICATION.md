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

The unrestricted proof is symbolic and appears in `RESULT.md`.

The checker independently verifies three finite components of the argument:

1. It enumerates every exponent partition with total multiplicity at most \(8\),
   computes the corresponding divisor count, and confirms that below \(8\) the
   only perfect divisor-count patterns are \((2,1)\) and \((5)\), while total
   multiplicity \(8\) has the unique perfect pattern \((6,1,1)\).
2. It checks the algebraic coprimality used in the \(p^5\) obstruction and
   searches finite odd-prime ranges for any direct counterexample in the two
   \(\tau=6\) shapes.
3. It verifies the modulo-\(8\) table for
   \(\Phi_7(p)\).

The finite checks are corroborative only. The lower bound and the equality
classification are proved for all integers by the divisor-count partition and
Euclid--Euler arguments.
