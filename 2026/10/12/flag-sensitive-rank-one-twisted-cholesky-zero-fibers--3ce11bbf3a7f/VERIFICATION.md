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

The proof is symbolic and valid for every odd prime power in the stated diagonal setting. Its critical steps are: the projective factorization of a rank-one matrix; the equivalence between upper triangularity and the support inequality; the equivalence between the twisted zero equation and isotropy of the left factor; and the standard finite-field zero count for each nondegenerate prefix quadratic form.

`verify.py` performs independent finite checks over prime fields. It exhaustively enumerates all upper triangular matrices for the two four-dimensional examples over \(\mathbf F_3\), computes rank by modular Gaussian elimination, tests \(U^{{\mathsf T}}GU=0\), and recovers \(44\) and \(80\). It also checks smaller standard-form examples over \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\). The recorded output terminates with `VERIFY_OK`.

The finite enumeration is not an exhaustive proof for arbitrary field order or dimension. The infinite statement rests on the exact counting proof in `RESULT.md`; the verifier is a reproducibility and boundary check.
