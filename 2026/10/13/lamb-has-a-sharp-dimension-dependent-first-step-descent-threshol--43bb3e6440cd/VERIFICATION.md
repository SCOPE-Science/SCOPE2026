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
The package verifies LAMB's first-step dimension-dependent descent threshold on an isotropic quadratic.

`verify.py` checks the exact objective-ratio identity, the co-monotone cosine lower bound on randomized layer states, convergence of the explicit sharp family to \(1/\sqrt d\), and both sides of the \(2/\sqrt d\) objective-descent boundary.

The numerical checks are transcription guards. The universal cosine inequality and exact worst-case objective factor are proved analytically in `RESULT.md`.
