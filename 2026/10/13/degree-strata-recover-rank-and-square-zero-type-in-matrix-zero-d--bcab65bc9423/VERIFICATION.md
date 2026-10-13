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

The proof has three independent ingredients: annihilator-subspace dimensions, separation of the resulting degree values, and a flag count for square-zero matrices.

For a rank-\(r\) matrix \(A\), the checker confirms in the complete graph on nonzero singular matrices of \(M_3(\mathbb F_2)\) that the actual neighborhood size is
\[
2q^{n(n-r)}-q^{(n-r)^2}-1-\mathbf 1_{A^2=0}.
\]
It separately checks representative vertices over \(\mathbb F_3\), verifies the closed rank and square-zero counts for small parameters, and checks that distinct pairs \((r,\mathbf 1_{A^2=0})\) never share a proposed degree in the tested range.

The computations are finite corroboration only. The arbitrary-prime-power theorem rests on the exact linear-space dimensions and the image-kernel flag count given in the proof.

Reproducibility requires Python 3 only; no external package is used by `verify.py`.
