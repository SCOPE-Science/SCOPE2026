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
# Reproducible checks

Run `python checker.py` in a directory containing the accompanying script. The script invokes the exact recursive hare map on every ternary input of lengths \(0\) through \(10\), independently computes image membership and every fiber size via a decomposition dynamic program, and checks the proposed rational recurrence. On replay it reports `PASS`, with exact output preserved in `computation.txt`.

This finite computation supports but does not prove an infinite-language claim. The proof supplied in `RESULT.md` uses structural decomposition, constructive inverse, a Myhill–Nerode separation, and formal generating functions, and does not infer infinite results from enumeration. Full text of the 2026 motivating manuscript was unavailable for direct inspection; the 2020 originating primary paper was examined. No independent audit was performed.
