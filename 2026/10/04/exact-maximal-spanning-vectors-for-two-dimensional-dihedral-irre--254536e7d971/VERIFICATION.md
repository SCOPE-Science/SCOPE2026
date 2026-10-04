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
The universal statement is proved analytically in `RESULT.md`. The executable replay is `verify.py`.

Running `python verify.py` constructs the rotation and reflection orbit projectors for every two-dimensional irreducible parameter \(k\) for every \(3\le n\le80\). It verifies complex span dimension \(4\) for the explicit working vectors and span dimension below \(4\) for representative failures of every necessary condition.

Expected output:

`VERIFY_OK irreps=1560 m2_cases=20 n_range=3..80`

The finite range is a consistency check only. It does not certify or substitute for the proof for arbitrary \(n\).
