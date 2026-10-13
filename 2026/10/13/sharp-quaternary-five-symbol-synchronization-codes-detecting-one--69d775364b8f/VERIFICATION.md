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

The bundled verifier `artifacts/verify.py` regenerates both normalized vertex sets, checks every pair within every supplied clique and verifies complete vertex coverage, then checks all constructed codewords and every distinct pair. The independently implemented `artifacts/verify_independent.py` uses base-four integer encodings for the same mathematical objects; it also reconstructs the vertex sets and checks all certificate entries. Both were executed on the included files; the exact outputs appear in `artifacts/verification_output.txt`.

The finite clique covers prove the upper bound exhaustively for the declared parameters. No enumeration of optimizers, extrapolation to arbitrary block length, or independent external audit is asserted. Originality is assessed against the identified available primary full texts and public literature, subject to a documented inaccessible relevant publication.
