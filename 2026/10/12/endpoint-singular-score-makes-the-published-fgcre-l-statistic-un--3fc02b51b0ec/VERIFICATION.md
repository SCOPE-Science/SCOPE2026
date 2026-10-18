---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Define v=-log(1-u)>0. Then J_beta(u)=v^(beta-1)(beta+1-v)/Gamma(beta+1), asymptotic -v^beta/Gamma(beta+1) -> -infinity as u->1^- for every beta>0. The paper explicitly defines 0<u<1, but Eq(7) evaluates i/n through i=n, leaving J_beta(1) undefined; if extended by left limit, the X_(n)>0 term is -infinity almost surely under exponential sampling. Eq(9) averages J_beta(i/n) through n in each coefficient b_(r,n), so no finite exact-null coefficients exist as printed. Derivative dJ/dv = v^(beta-2)(beta^2-1-beta*v)/Gamma(beta+1), so beta>1 is not monotonic, contradicting all-beta monotonicity in Remark 3.1. This is exact algebra, not a numerical inference. Crucially Remark 3.1 also mentions interior u_r=r/(n+1), but this is NOT the i/n endpoint rule printed in Eqs(7)/(9); the audit concerns literal formulas only.

## originality

PASS

Target 2026 FGCRE paper equations, theorem and remark were read directly, and targeted searches by DOI, J_beta(1), plotting positions, L-statistic endpoint and exact-null coefficients found no published correction of these precise inconsistencies. Classical L-statistic finite-sample results require finite deterministic coefficients and do not supply a singular J_beta(1). An undocumented author implementation or private erratum remains a genuine risk.

## value

PASS

This elementary endpoint diagnosis is consequential rather than a cheap cosmetic type check: it affects the primary proposed empirical test statistic and every spacing coefficient of the advertised exact finite-sample null law, so the published calibration cannot literally be applied as printed. It also identifies a distinct global monotonicity defect for beta>1; a valid correction requires a specified new interior or truncated weighting and re-proving its exact-null coefficient conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
