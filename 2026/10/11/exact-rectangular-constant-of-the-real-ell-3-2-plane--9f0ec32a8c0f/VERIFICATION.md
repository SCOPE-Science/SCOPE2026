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

The file `verification_rectangular_l3.py` reconstructs the exact interior stationarity equations for the real \(\ell_3^2\) rectangular constant and checks the key algebraic certificate.

It verifies symbolically that eliminating \(s\) produces
\[
(t+1)^{18}(t^2+1)(t^2-t+1)^{18}(t^4-t^2+1)P(t^3),
\]
where \(P\) is the degree-fourteen polynomial in RESULT.md. Exact Sturm counts certify two and only two roots of \(P\) in \((0,1)\), one in each stated rational interval. The sign of the quadratic coefficient in the second stationary equation distinguishes the only branch with \(s>t\). High-precision evaluation of that already-isolated algebraic solution gives
\[
\mu=1.72853813848209303701779663029140740944800157\ldots.
\]

The computation is not used as a substitute for the analytic branch reduction: branches outside \(0<t<1\), \(s>t\) are bounded in the proof, and the exact resultant/Sturm calculation exhausts the remaining stationary possibilities. No claim is made about arbitrary \(p\) or about a radical expression for the isolated algebraic root.
