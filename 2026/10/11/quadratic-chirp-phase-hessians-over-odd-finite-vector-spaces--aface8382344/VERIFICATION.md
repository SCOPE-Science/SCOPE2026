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

The real phase autocorrelation energy is computed using every nonzero additive shift. An analytic differentiation gives \(D^2\mathcal E_Q(0)[\varphi,\varphi]=8N^2\sum_h\sin^2(2\pi Q(h)/p)|\widehat\varphi(h)|^2\) with \(\widehat\varphi(h)=N^{-1}\sum_x\varphi(x)e^{-2\pi i B(h,x)/p}\); this yields Euclidean Hessian eigenvalues \(8N\sin^2(2\pi Q(h)/p)\). The Gauss-sum count and exact flat families are separately proved in `RESULT.md`.

Execute the provided complete standalone script, from this directory, as `python3 verify.py`. It uses only Python 3 standard-library modules. The completed run returned exactly:

`VERIFY_OK quadratic_zero_counts=140 hessian_directional=10 flat_families=7 maximum_relative_hessian_error=1.794e-10`

The \(140\) checks enumerate diagonal nondegenerate forms over selected small odd prime fields and compare their isotropic zero counts with the stated discriminant formula. The \(10\) Hessian checks compare a direct double finite difference of independently evaluated correlation energies with the Fourier multiplier formula. The \(7\) phase-family checks directly evaluate correlations after nonconstant isotropic-line phase deformations. The calculations use floating-point tolerances; infinite-parameter correctness follows from the stated character-orthogonality, differentiation and quadratic Gauss-sum proof, not from these finite tests. No external independent audit or global perfect-sequence certification has been performed.
