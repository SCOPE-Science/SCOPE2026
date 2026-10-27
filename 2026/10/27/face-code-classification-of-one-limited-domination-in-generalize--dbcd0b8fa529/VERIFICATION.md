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

The proof in `RESULT.md` applies to all positive dimensions and all alphabet sizes at least two. Computational corroboration is supplied by `verify_hamming.py`, requiring Python 3, NumPy, and SciPy. Run `python verify_hamming.py` in a directory containing the file. The expected output is included in `verify_hamming_output.txt` and ends with `VERIFY_OK`.

The verifier checks the original domination and capacity conditions directly against a separate coordinate-component test for all vertex subsets in ten small graph profiles. Five larger profiles are checked with a binary integer program implementing both original conditions; a second program excludes all proposed minimum sets and searches for a different optimum. In every tested case, the predicted minimum and the complete list of minimum sets agree with these checks. The finite cases do not establish the theorem for all graph orders, and computational optimization does not serve as a substitute for the proof. No independent mathematical audit or external certification is represented.
