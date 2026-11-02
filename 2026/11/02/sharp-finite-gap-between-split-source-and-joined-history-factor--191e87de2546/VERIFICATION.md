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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and no third-party packages. The verifier constructs the full recursive reference/target family, independently computes longest admissible phrases in both parsing models, and checks the predicted greedy boundaries for \(1\le m\le7\). For \(1\le m\le5\), a separate backward dynamic program computes the genuine optimum over every admissible next phrase. It also validates the special-pair uniqueness conditions and exhaustively checks \(1764\) short binary reference/target instances against the exact bound and the greedy results. `verification_output.txt` preserves the expected stdout.

The arbitrary-parameter result is proved symbolically in `RESULT.md`; finitely many examples cannot certify its induction. No claim about fixed alphabets, minimal witness sizes, publisher priority, or independent mathematical validation is supported by this checker.
