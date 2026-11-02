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

# Reproduction and verification

Run `python verify.py` using SymPy 1.14 or compatible. The script uses exact integer and \(\mathbb F_7\) polynomial operations, not floating point or finite sampling. Its saved output is `verification_output.txt` and terminates with `VERIFY_OK`.

The exact checks are: integer Hessian determinant identity; \(\mathbb F_7\)-resultant \(-x(x-2)^{21}\); affine lex leading terms \((u^2,uv^7,v^{15})\); local isolated primary component leading terms \((u^2,uv^7,v^{14})\); the length-21 standard basis; the local maximal-ideal filtration ranks and Hilbert--Samuel values; projective coordinate-vertex transversality and complete affine point support.

Flatness follows mathematically from the projective, zero-dimensional fibers of a relative complete intersection over a DVR. The verifier does not construct a stable or good reduction of the underlying curve and does not establish exhaustive historical novelty. The statement was reviewed internally; independent scientific validation was not performed.
