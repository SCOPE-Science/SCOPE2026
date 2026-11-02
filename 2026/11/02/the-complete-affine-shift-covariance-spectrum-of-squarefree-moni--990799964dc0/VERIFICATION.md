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

# Verification record

Run `python3 verify.py` with standard Python 3. The verifier builds finite fields from explicit irreducible polynomials and evaluates squarefreeness with a polynomial Euclidean gcd against the formal derivative. It directly enumerates 293 nonzero-shift cases over 11 base fields with 413,477 monic-cubic evaluations. Recorded output: `VERIFY_OK finite_fields=11 cases=293 tested_cubics=413477`. The finite list includes extension-field characteristic two and characteristic three, both central to the theorem. This is a numerical check only; the universal proof is the repeated-root bijection and inclusion--exclusion in RESULT.md. Independent audit status: not performed.
