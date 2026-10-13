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

The symbolic proof in `RESULT.md` is the evidence for all odd prime powers. It reduces the simultaneous bad-unit intersection to quadratic-character sums and treats invertible nonscalar, scalar, rank-one, and zero matrices separately.

The bundled `verify.py` is an independent finite consistency check using only the Python standard library. It exhausts every matrix over \(\mathbb F_3\) and \(\mathbb F_5\), checking the minimum and equality characterization, then checks a representative of every nonscalar similarity type plus every scalar type over \(\mathbb F_7\) and \(\mathbb F_{{11}}\). It also checks the stated rank-one formulas. A successful run prints `VERIFY_OK`.

The finite replay does not prove the theorem for arbitrary prime powers and does not test characteristic two or dimensions above two. Those cases are outside the claim.
