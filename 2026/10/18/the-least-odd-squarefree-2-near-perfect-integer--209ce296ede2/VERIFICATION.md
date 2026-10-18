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

# Reproducibility and limits

Run `python3 verify.py`. The program uses only the Python standard library; it recomputes the relevant exact rational abundancy bounds, enumerates the twelve five-prime candidates, tests all complete proper-divisor sets, and separately scans all odd integers not exceeding \(39585\). The saved `verification_output.txt` is the actual successful output.

The global reduction from arbitrary odd squarefree numbers to the finite candidates is proved in `RESULT.md` using prime-support and monotonicity inequalities. Computation verifies only the finite list and is not presented as an infinite argument. No independent audit or external certification has been performed.
