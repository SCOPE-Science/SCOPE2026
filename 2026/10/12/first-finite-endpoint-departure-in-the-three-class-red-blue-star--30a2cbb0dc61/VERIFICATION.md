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

Run `python3 verify.py` next to `RESULT.md` and inspect `verification_output.txt` for the saved run output. The verifier exhausts all \(1767\) integer class-size triples with \(2\leq n\leq20\) and all exact finite endpoint comparisons. The loops enumerate every such triple by setting \(c=n-a-b\); all assertions are exact integer computations. The two order-20 witnesses are checked separately by direct edge construction and the literal four-vertex ordered embedding count; all profiles through order eight receive the same direct check. The finite result concerns only this graph family, not all graphs or future orders. The run output is evidence of execution, while the code and its elementary loop-exhaustion argument provide the finite proof.
