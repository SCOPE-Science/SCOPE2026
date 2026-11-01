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

# Verification of the ternary counterexample

Run `python3 verify.py` with a standard Python 3 installation. Compare the standard output with `verification_output.txt`. The script independently enumerates cyclic shifts over alphabet sizes 2, 3 and 4 through lengths 12, 10 and 8, and verifies the two exchange pairs of the counterexample and common-block padding through length 39. The computation is a finite check only; no assertion of exhaustive verification for arbitrary length is made. The unrestricted proof is the indicator-vector argument in `RESULT.md`.

The primary full text of arXiv:2604.19504 was read, including Sections 2–4 and 7. The primary full text of arXiv:2507.04916 was read, including Section 6. The former treats pairs and explicitly leaves multiple words open; the latter also poses this question. Literature coverage may be incomplete; publication priority has not been independently established.
