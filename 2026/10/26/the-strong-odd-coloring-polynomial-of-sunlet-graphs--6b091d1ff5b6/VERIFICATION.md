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

# Verification of the sunlet strong odd coloring polynomial

Run `python3 verify.py` in the directory containing the included standalone verifier. The expected exact stdout appears in `verification_output.txt`.

The verifier exhaustively counts assignments for 11 small \((n,q)\) cases using the original degree-three neighborhood parity and properness conditions, totaling 488356 assignments that have a proper rim. Separately, it constructs the complete \(q(q-1)\)-state transfer and checks its exact trace against the polynomial recurrence for 84 cases. It also checks the specified low-palette specializations and reference values.

These are independently implemented finite sanity checks of the necessary combinatorial identities and the small cases; they are not a proof of the infinite theorem or an independent external audit. The unlimited parameter range follows from the invariant-space and incidence-rank proof in `RESULT.md`. All operations use Python's exact integers; there are no input files or third-party dependencies.
