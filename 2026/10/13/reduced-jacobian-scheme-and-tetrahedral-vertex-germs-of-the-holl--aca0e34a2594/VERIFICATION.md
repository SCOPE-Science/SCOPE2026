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

The original matrix, coordinate-chart transformation, and five displayed partial derivatives were checked with exact symbolic polynomial calculations in `verify.py`. The computation also exhaustively checked the squarefree monomial support criterion and the Hilbert functions in degrees \(0\) through \(8\), and printed the output stored in `verification_output.txt`.

The exact mathematical proof—not finite enumeration—establishes that the Jacobian ideal is the intersection of six prime ideals on every affine coordinate chart; the six charts cover all projective points. The local Hilbert--Samuel multiplicity follows from the all-degree Hilbert-series identity by face enumeration. No claim is made about positive characteristic or larger matrix formats.
