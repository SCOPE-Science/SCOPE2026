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

The complete proof is in RESULT.md. The independent Gaussian blocks in the fixed orthonormal coordinates give the exact inverse-Wishart denominator \(\ell-r-1\). For Haar rows, the projector identity \(AA^{\mathsf T}=W^{-1}-I\) and an independent Gaussian representation of a Haar frame give the exact finite-population factor. Orthogonal three-block decomposition proves the two-sided law; the right-singular-vector construction proves sharpness of the realized-sketch operator norm.

Reproducibility: with Python 3 and NumPy, run `python CHECK.py`. The bundled code checks 36 deterministic shape cases and draws 6,000 independent Gaussian and 6,000 independent Haar sketch pairs. Outputs are shown and compared with proved expectations, with a deliberately loose finite-sample tolerance. Numerical experiments are not substituted for analytic finiteness or divergence proofs.

Scope: real, fixed independent sketches, finite-dimensional rank-\(r\) bases, exact arithmetic and one instantaneous projection. No time-evolution, sampling-without-replacement, structured sketch or independent external audit is asserted.
