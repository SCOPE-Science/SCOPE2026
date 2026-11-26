---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the first collision and the unique length-ten class

Run `python3 verify.py` from the directory containing the unchanged companion script. The program enumerates each length-\(n\) factor for \(1\le n\le10\), using two consecutive aligned length-sixteen blocks and all allowed underlying binary pairs. It checks the factor counts and the complete third-order signature classes, with the first and only nonsingleton class in this range at length ten. The completeness of the finite cover follows from the proof in `RESULT.md`, not from the script's supplementary comparison to a finite prefix.

The script also checks order-four separation of the known seed pair and third-order equivalence after up to four substitution iterations. These are corroborative checks of the previously known witness and are not an infinite certificate. The corrected finding makes no new unbounded claim.
