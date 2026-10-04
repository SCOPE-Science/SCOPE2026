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

Run `python3 artifacts/verify.py` from the package root. The verifier uses only the Python standard library and exact integer arithmetic.

It performs four exhaustive checks: it reconstructs the ten orbits of all 81 ternary length-four targets under symbol permutations and reversal; it verifies that the dual numerators total 468 and that every one of the 243 ternary length-five deletion balls has numerator at most 23; it generates the 21 codewords from seven cyclic-translation representatives; and it confirms that their deletion descendants cover all 81 targets. A successful execution prints `VERIFY_OK`.

The computation proves only the finite parameter \(q=3,n=5,R=1\). It does not prove uniqueness of optimal codes, a formula at other parameters, or absence of an equivalent statement in literature not inspected. The 2026 same-topic preprint was available only through abstract/preview material during the literature comparison.
