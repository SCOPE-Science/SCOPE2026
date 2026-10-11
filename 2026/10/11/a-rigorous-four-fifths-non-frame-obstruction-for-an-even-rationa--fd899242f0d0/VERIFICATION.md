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

Execute `python3 verify_gabor_4_5.py` from the directory containing this text and the script. The script uses Python's standard-library exact fractions and integer outward interval operations. It proves rational enclosures of \(\pi\), \(e^{-x}\), and \(\cos x\) and asserts both determinant sign intervals, not just approximate signs. Its output includes `CERTIFIED` only if these two positive/negative enclosures pass.

The resulting non-frame statement follows from the explicit continuous fiber matrix and rank-deficiency proof in `RESULT.md`. A vanishing determinant at some point is established by continuity between rigorously opposite endpoint signs; the script does not enumerate roots or assert uniqueness. Numeric root estimates are non-probative background only. No independent audit or separate human verification has been performed.
