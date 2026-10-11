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
The analytic proof establishes the theorem for every finite nonempty simple graph and every positive integer blow-up vector. The bundled `verify.py` is an exact-rational corroboration of the explicit complete-multipartite extremizers. It exhausts every Boolean character for six representative instances with unequal cluster sizes and both parities of the number of parts.

Replay command: `python verify.py`

Expected output:
`VERIFY_OK instances=6 cuts=356 min_fourier=0 formulas=6`

The finite replay does not certify the universal theorem; the expectation and symmetrization arguments in `RESULT.md` do.
