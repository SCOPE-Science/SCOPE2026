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

Run `python3 verify.py` in this directory. The verifier uses only the Python standard library. It reconstructs \(\mathbb F_4\), the sixteen ambient codewords, all IPP1/IPP2 forbidden subsets, all \(65536\) candidate subcodes, and the twenty affine lines. It asserts the exact maximum, number of maximizers, and both line-profile counts before printing `VERIFY_OK`.

The verification proves only the finite claim stated in `RESULT.md`. It does not test unrestricted quaternary codes outside the ambient MDS code and does not infer novelty from computation.
