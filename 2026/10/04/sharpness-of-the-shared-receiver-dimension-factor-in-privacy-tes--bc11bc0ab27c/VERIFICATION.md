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

The analytic proof gives an exact all-dimension construction. The accompanying `verify.py` independently constructs the permutation decoders and the two decoded privacy-test range isometries for representative cases with \(d<M\), \(d=M\), and \(d>M\). It checks that the range bases are orthonormal, that the designated range vectors have overlap \(\min\{1,d/M\}\), and that the largest singular value of the full range-overlap matrix has the same value.

The packaged script was replayed from the packaged bytes and returned `VERIFY_OK`.

The finite replay is not an exhaustive proof over all dimensions; the general proof is the basis-extension and range-vector argument in `RESULT.md`. No claim is made about optimality of the later steps in the full strong-converse theorem.
