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

The standalone Python 3 standard-library program `artifacts/verify.py` independently constructs Fourier restriction matrices and their modular ranks, checks the exact pair-difference scalar action on selected layers, evaluates all proposed nonzero coefficients over a finite parameter census, and confirms the even-layer rank obstruction.

Run `python3 artifacts/verify.py` from the package root. An observed successful run printed `VERIFICATION_OK assertions= 25752 odd ranks n=3,5,7,9; harmonic identities; coefficient nonzero r<=50; even-rank obstruction`.

The finite computations check examples and algebraic identities; they do not replace the published harmonic-basis lemma or the general mathematical argument establishing the theorem for every odd dimension. No independent external audit was performed.
