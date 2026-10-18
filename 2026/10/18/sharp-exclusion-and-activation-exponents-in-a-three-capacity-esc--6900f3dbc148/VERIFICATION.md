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
# Verification and limitations

Run `python verify_escort.py` with standard Python 3.9 or newer. The embedded program requires no external packages, internet, or persistent data.

The actual replay completed with these checks: (a) exact arithmetic for 199 rational budgets at order \(q=1/2\), including all three optimizer branches, affine constraints, and one-sided derivative signs; (b) 2,189 numerical root/active-set checks from 11 diversity orders and 199 interior budgets; (c) rational checks that \(b=1/4\) gives the potential abundance \((9/10,1/10,0)\) and Hill number \(8/5\); and (d) activation-coefficient comparisons in the regimes \(q=1/4\), \(q=1/2\), and \(q=3/4\).

These calculations corroborate the formulas at selected inputs. The infinite family and exact asymptotic exponent are established by the analytic escort-bijection, strict-convexity, KKT, and matched-asymptotics arguments in RESULT.md. The output is not an external proof certificate. The findings apply to theoretical maximum-diversity compositions under an exact three-score constraint; no empirical data were tested.
