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

The proof uses the exact two-eigenvalue RQI identity \(t_+=-t^3\) and the explicit positive-cone interval \(-\tan\theta<t<\cot\theta\). Endpoint comparison yields the universal condition \(\theta=\pi/4\), equivalent to equal diagonals.

The bundled `verify.py` checks the exact witness \(A=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\), \(x=(1,4)^{\mathsf T}\): positive definiteness, Rayleigh quotient \(25/17\), target-basin midpoint inequality \(25/17<3/2\), shifted determinant \(-361/289\), and mixed-sign solve \((-1309/361,255/361)^{\mathsf T}\). It also checks the projective identity on exact rational spectral examples.

The checker is a finite reproducibility aid; the universal theorem is proved symbolically in `RESULT.md`, not by enumeration. No higher-dimensional or floating-point claim is made.
