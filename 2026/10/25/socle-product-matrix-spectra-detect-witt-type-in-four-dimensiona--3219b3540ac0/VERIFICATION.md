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

# Verification record

The independent audit channel is unperformed. The theorem is supported by the explicit decomposition and trace proof in `RESULT.md` and by direct finite computations in `verify.py`.

Run using `OPENBLAS_NUM_THREADS=1 python verify.py` with Python 3 and NumPy. Eight test cases were run: complete product matrices over fields of sizes 2, 3 and 4, each with two nondegenerate symmetric form types, and bilinear-incidence matrices over the prime field of size 5 with split and anisotropic forms. All assertions completed and printed `OK`.

For full matrices, construction uses the underlying four-coordinate algebra multiplication, not the predicted block decomposition. For \(q=4\) arithmetic uses the irreducible polynomial \(X^2+X+1\) over \(\mathbb F_2\). The real symmetric eigensolver checks eigenvalues rounded to six or seven decimal places. These are finite consistency checks, not exact symbolic certificates for all prime powers. The universal proof is supplied separately and does not rely on numerical tolerance.

The 12-page arXiv primary preprint (arXiv:2601.19301v1) was accessed and inspected, with page-image checks and comparisons against Theorems 3.1, 4.1, 4.4, 4.7, and 5.1. The full publisher page was not accessible; no independent external historical-priority review was conducted.
