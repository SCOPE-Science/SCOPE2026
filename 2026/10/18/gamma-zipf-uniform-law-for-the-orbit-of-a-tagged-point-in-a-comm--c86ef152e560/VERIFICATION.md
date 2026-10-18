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

# Analytical and computational checks

The proof identifies each transitive component with a Hermite-normal-form index subgroup of the integer plane. Its exact finite probability is verified by independent exhaustive enumeration of commuting pairs through five labels; the checker derives each twist from the permutations rather than assigning subgroup parameters by fiat.

Run `python3 verification/commuting_tagged_verify.py` from the extracted package root. Observed result: 162 exhaustive pointed-orbit assertions, 175 exact normalized coefficient assertions and 8 finite asymptotic diagnostics passed.

The checker uses rational arithmetic for the finite exact identities and floating-point arithmetic only in explicitly labeled diagnostics. Finite enumeration is not an infinite proof. The analytic chain uses the eta-product asymptotic, a one-saddle coefficient estimate, a uniform bounded-square-root coefficient ratio, a fixed-height Riemann sum, the normalization identity using the zeta value, and conditional discrete-uniform twist convergence. No independent audit or independent certification has been performed.
