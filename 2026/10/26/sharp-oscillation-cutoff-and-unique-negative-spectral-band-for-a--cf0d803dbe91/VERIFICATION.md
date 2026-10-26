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
# Verification evidence and scope

The proof uses the standard curvature-\(-1\) spherical function \(\varphi_\lambda(r)=\sin(\lambda r)/(\lambda\sinh r)\), the stated \(4\pi/\lambda\) radial transform, and the \(L^2\)-Godement equivalence for a continuous radial \(L^2\) function with integrable transform. The theorem's actual hypotheses are verified by \(\int|K_\omega(o,x)|^2dx\le4\pi/3\) and exponential decay in frequency. The integration-by-parts boundary terms vanish at zero and infinity, including negative arguments in the sine-transform factor.

`verify_spherical_transform.py` runs direct original-integral quadrature at 50-digit precision, at 12 test pairs covering subcritical, critical and supercritical \(\omega\), checks the exact hyperbolic-addition identity with SymPy, and computes the cutoff \(\omega_*=0.7637391428751280204\ldots\). The analytic derivative \(h'(\lambda)>0\) is the proof of uniqueness of the spectral boundary; finite tests are not exhaustive. The checker is supplementary and has no role in proving the continuum sign theorem.

Independent audit and independent validation have not been performed. The scientific literature comparison cannot establish absolute priority.
