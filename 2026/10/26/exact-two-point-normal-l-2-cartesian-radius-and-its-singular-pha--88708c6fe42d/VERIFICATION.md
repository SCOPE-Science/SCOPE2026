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

# Verification of the two-spectral phase law

The normal spectral theorem yields \(\|\operatorname{Re}(e^{-it}T)\|^2=\max\{(\operatorname{Re}(e^{-it}\lambda))^2,(\operatorname{Re}(e^{-it}\mu))^2\}\). The difference of the two scalar terms has average \(-A\) and oscillation amplitude \(B=\sqrt{A^2+U^2}\). Its positive part integrates over the single arc \(|v|<\arctan(U/A)\) to \((U-A\arctan(U/A))/\pi\). The zero and equal-radius boundary cases follow by taking the integrand directly rather than dividing by zero.

The derivative \(U^2/(A^2+U^2)\) of the correction for \(A>0\), and strict pointwise radial growth when \(U>0\), verify the phase and amplitude equality criteria. The series \(\arctan x=x-x^3/3+x^5/5+O(x^7)\) supplies the exact cubic leading coefficient; when \(A=0\), the correction is exactly \(U/\pi\), proving a linear onset.

The supplied `verify_two_spectrum.py` was executed successfully on 216 deterministic angular tests, with absolute discrepancies below \(1.7\cdot10^{-7}\). Its quadrature cannot establish a universal identity and does not replace the proof. The classification is restricted to normal operators with at most two spectral points; the same computation is not valid for arbitrary higher-rank or nonnormal operators without spectral reduction. No independent audit has been performed.
