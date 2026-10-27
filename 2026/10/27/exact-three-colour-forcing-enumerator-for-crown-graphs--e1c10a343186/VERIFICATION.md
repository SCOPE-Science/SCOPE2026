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

# Verification summary

The ordinary Python 3 program `verify_crown.py` enumerates all \(4^{2n}\) initial partial assignments for \(n=4\) and \(n=5\). It derives the graph's edges directly from the deleted-matching definition, rejects improper partial colourings, applies an immediately forced vertex when exactly two distinct neighbour colours are present, and checks the terminal properness and seed counts. Its independent coefficient calculation uses binomial coefficients, not the forcing simulator. It also explicitly checks the excluded \(n=3\) boundary.

Invocation: `python3 verify_crown.py`.

Observed result (from this exact program before packaging): `VERIFY_OK exact_cases=2 checked_assignments=1114112 matching_polynomials=True boundary_case_n3=True`.

The infinite proof depends on the three terminal-colouring types and the legal forcing sequence for the shared-colour type. Exhaustive checking of two finite graphs is not an infinite-case proof. No independent mathematical audit has been carried out.
