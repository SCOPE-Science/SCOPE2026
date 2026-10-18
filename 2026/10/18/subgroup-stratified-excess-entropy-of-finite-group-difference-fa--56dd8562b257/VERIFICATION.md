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

# Verification evidence and limits

The complete analytic argument appears in `RESULT.md`. The proof verifies the group action and its orientation posterior, the conditional independence of observed halves given their recoverable coset vector, and the finite-subgroup perturbation argument. Infinite statements depend on the strong law of large numbers and finite-group elementary facts, not on exhaustive numeric enumeration.

Run `python3 verify.py` using only the Python standard library. It independently enumerates group-valued source words, applies the noncommutative operation \(Y_i=X_i^{-1}X_{i+k}\), and compares the resulting exact rational output distributions to the separately evaluated finite orientation-entropy identity. Actual execution returned:

`VERIFY_OK: 38 independent group-valued finite-cylinder entropy identities across cyclic and nonabelian examples`

The models cover \(\mathbb Z/3\mathbb Z\), \(\mathbb Z/4\mathbb Z\), and \(S_3\), both tested lags \(k=1,2\), and full, proper nonnormal, and trivial stabilizers. The program checks only finitely many words and does not prove the full theorem, asymptotic reconstructibility, or uniqueness of the research claim.

The available literature was compared at the level of claims; the well-known binary Rule-60 excess-entropy discontinuity is credited to Lindgren and Nordahl (1988). Independent audit and certification have not been performed.
