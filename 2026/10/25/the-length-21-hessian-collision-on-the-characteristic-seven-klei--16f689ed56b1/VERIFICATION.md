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

The accompanying `verify.py` uses exact arithmetic in \(\mathbb F_7\), via SymPy's finite-field polynomial and Gröbner-basis operations. It checks the global Hessian identity, the reduced affine lexicographic Gröbner basis, the only affine supported solutions, all \(14\) truncated local colengths, the maximal-ideal Hilbert function, and coordinate-tangent contact identities. It returned `VERIFY_OK` upon execution. In addition, the proof verifies the projective boundary charts directly, to avoid mistaking affine exhaustion for projective exhaustion.

The one singular point's type \(A_6\) comes from the cited literature; no part of the verification treats that classification as original. The finite field calculations concern exact finite-dimensional rings, not an inference from point samples to a universal theorem. No external independent audit has been performed. The verified output pertains only to the provided characteristic-\(7\) model and the ordinary Hessian.
