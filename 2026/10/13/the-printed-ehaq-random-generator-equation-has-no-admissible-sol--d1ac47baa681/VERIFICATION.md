---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The publisher PDF confirms the CDF in Eq. (3), the plus sign both in Eq. (10) and the line preceding it, and the later sampling instruction invoking Eq. (10). For L(x)=((1+tau)^2+tau*x+(tau*x)^2/2) exp(-tau*x), differentiation gives L'=-tau^2(2+tau+tau*x^2/2) exp(-tau*x)<0 on x>=0, tau>0. With L(0)=(1+tau)^2 and limit zero, the plus-sign target lies strictly above the range and the CDF's minus-sign target strictly inside it for 0<z<1, delta>0. The independent replay /workspace/replay_5.py bisects the CDF itself at 65-digit precision, confirms all 15 quoted computed quartiles and gives 0.238229040340517169 for the featured example. Agreement with Table 1 is numerical, not exact reproduction of every fourth decimal: at delta=0.5, tau=2 the computed first quartile 0.0364492753688223 is 0.0000507246311777 below the printed 0.0365 (within the checker’s stated numerical tolerance of 0.00006; it rounds to 0.0364). The other 14 displayed targets agree to four decimal places. The core range proof does not depend on Table 1. No uploaded code was executed or inference made about the sign used in unpublished code.

## originality

PASS

The CDF itself, the general power-CDF inversion and approximate tabulated quantiles are prior material. The supported distinct claim is the incompatibility of the printed generator with its own CDF and the uniform no-root result, not the inversion rule or a new distribution. No inspected distinct publication or matched catalogue statement establishes this diagnosis.

## value

PASS

Though the sign correction is elementary, the range obstruction rules out every sample under an instruction explicitly reused in the simulation study. This is a material reproducibility issue, not an isolated typo in unused notation. The valid monotone inversion makes the stated sampling procedure executable without implying the published code was wrong.

The dated certificate retains the supplied scientific assessment, sources and limitations.
