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
The exact transformation is
\[
G=e^{X/\theta}-1,
\qquad
G\sim\operatorname{Gamma}(3,1).
\]

The bundled checker verifies the transformed CDF and the Gamma-quantile representation. It then evaluates the ML, MPS, LS, WLS, CvM, and AD criteria on a fixed positive sample before and after simultaneous scaling of sample and parameter.

Representative numerical optimizations verify optimizer scaling, and a finite-difference observed-information calculation verifies the \(c^{-2}\) information law.

The computations supplement the algebraic proof and do not replace it.
