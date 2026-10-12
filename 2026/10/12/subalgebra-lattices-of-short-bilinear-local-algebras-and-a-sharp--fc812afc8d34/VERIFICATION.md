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

# Reproduction and limitations

Run `python3 verify.py` using Python 3 and the standard library. The checker implements its own finite-field operations, including \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\); enumerates every reduced-row-echelon subspace of the radical as a vector space; tests the products of every pair of basis vectors for membership in that subspace; and compares the dimension histogram to the exact formulas in RESULT.md. It also tests degenerate positive-rank forms and collision patterns among nonisomorphic bilinear forms.

The nondegenerate checks cover the listed ranks and types over \(q=2,3,4,5,7\), including even-characteristic alternating and nonalternating forms. Additional degenerate cases exhaust the parameter families for \((q,n)=(2,3),(2,4),(3,3),(3,4),(4,3)\). Successful execution prints `VERIFY_OK` and `VERIFY_GENERAL_OK`.

Finite verification is not a substitute for the full symbolic proof and cannot establish bibliographic uniqueness. No external independent audit has been performed.
