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

Run `python3 verify.py` in a directory containing the associated script. The script uses only the Python standard library, performs literal suffix/prefix comparisons, and fails by assertion if its finite tests disagree with the stated theorem. Expected final line: `VERIFY_OK`.

The runs completed for the accompanying code include all oriented subsets for length \(n=4,5,6,7,8,9\), whose respective optima were \(1,2,3,5,7,9\); direct pairwise criterion checks through \(n=21\); and construction checks through \(n=30\). This is finite corroboration only; the universal quantifier over all \(n\ge4\) is supported by the proof in `RESULT.md`, not by extrapolating experimental bounds. No external independent scientific audit is represented.
