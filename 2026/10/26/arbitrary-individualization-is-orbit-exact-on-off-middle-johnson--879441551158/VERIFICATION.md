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

Two ordinary Python programs accompany the theorem: `check_refinement.py` and `check_moments.py`. Run each with Python 3 from the directory containing the files. The saved output files `check_refinement_output.txt` and `check_moments_output.txt` give the expected outputs. The first computes refinement directly on seven finite graph families; the second checks the crucial odd-moment cancellation and leading-term identities exactly. All reported tests passed. The general all-parameter statement relies on the symbolic multilinear proof in `RESULT.md`, not a finite enumeration. The case \(n=2k\) is outside the theorem.
