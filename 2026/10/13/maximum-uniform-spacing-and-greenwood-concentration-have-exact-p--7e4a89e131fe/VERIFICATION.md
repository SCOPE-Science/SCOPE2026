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

The universal proof is analytic. The checker `verify_max_greenwood.py` uses only the Python standard library and exact rational arithmetic.

For every \(2\le m\le100\), it evaluates each \(k\)-fold threshold integral from beta integrals, reconstructs \(\mathbb E[L_mG_m]\) by inclusion-exclusion, and verifies the closed mixed-moment and covariance formulas exactly. It separately reconstructs \(\operatorname{Var}(L_m)\) and \(\operatorname{Var}(G_m)\) from exact simplex moments.

For every \(2\le m\le1000\), it checks \(F_m>0\), where \(F_m=H_m^2+H_m^{(2)}-2H_m\), and for \(m>2\) verifies exactly
\[
F_m-F_{m-1}=\frac{2(H_m-1)}m.
\]

Replay output:

`VERIFY_OK intersection_checks=5049 mixed_checks=99 covariance_checks=99 variance_checks=198 positivity_checks=999 increment_checks=998`

The finite replay does not establish the infinite theorem by enumeration; the proof in `RESULT.md` supplies the all-\(m\) argument. Independent audit has not been performed.
