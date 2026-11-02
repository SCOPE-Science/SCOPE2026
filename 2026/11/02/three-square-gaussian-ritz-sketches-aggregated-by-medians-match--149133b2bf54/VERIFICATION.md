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

# Reproducibility notes

The analytic proof gives, for the real part of a standard circular complex-Gaussian ratio, \(F(x)=(1+x/\sqrt{1+x^2})/2\). The median-of-three density is \(3/[4(1+x^2)^{5/2}]\), and the change \(u=x/\sqrt{1+x^2}\) gives the exact moment \(\frac34\int_{-1}^1u^2\,du=1/2\). These are symbolic, nonasymptotic identities, checked again using rational polynomial integrals in `verify.py`.

The additional-row formula follows from a Schur-complement two-dimensional complex Gaussian projection and the shape-two Gamma inverse moment. The verifier uses separate seeded independent Gaussian draws to test two specific residual matrices at \(m=1\) and \(m=2\). Expected squared errors from the run were approximately \(1.600000\) and \(3.720000\), respectively; empirical median-of-three risks were \(1.586309\) and \(3.685232\), and empirical one-row-over risks \(1.587715\) and \(3.697470\). Acceptance tolerances were 7.5% and 10% relative error. These finite numerical tests only check implementation consistency; they cannot establish the all-dimensional theorem or rule out an undiscovered equivalent prior result. Standard-library only: `python3 verify.py`.
