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
# Verification

The mathematical verification has two layers.

1. **Analytic identity.** At the published transition \(c_{*,d}\), set \(1-2\eta_dp_d^*=c_{*,d}\). Then the source formulas give
\[
U_d(p_d^*)-B_d(c_{*,d})=p_d^*(s_d\eta_d-\kappa_d)
\]
for all sufficiently large \(d\). Writing \(x=d-1\) gives the exact decomposition
\[
s_d\eta_d-\kappa_d
=3\eta_d\log(1+x^{-2/3})
-\frac{2x(x+2)}{(x+1)^2(x-1)}\log x.
\]
The first term is \((3/\ln2)x^{-2/3}+o(x^{-2/3})\), while the second is \(o(x^{-2/3})\). Also \(p_d^*\to1\) and \(d^{2/3}x^{-2/3}\to1\). This proves the matching lower limit. The published Corollary 13 supplies the upper limit.

2. **Reproducible numerical corroboration.** Run

`python3 artifacts/verify_asymptotic.py`

from the package root. The script evaluates the exact closed formulas for selected dimensions, verifies the witness lies in the affine \(U_d\) branch for the tested range, verifies witness gap does not exceed the published global upper bound, and prints the rescaled quantities approaching \(3/\ln2\).

The numerical run is not used to infer the infinite limit. No finite enumeration is presented as exhaustive evidence for the asymptotic theorem.
