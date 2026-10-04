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
The general result was checked algebraically from the reproduction number printed in the primary source.

Checks performed:
- Re-factored the published \(R_0(v)\) into the weighted endpoint form \((\mu R_S+vR_V)/(\mu+v)\).
- Differentiated the endpoint form and verified that the sign depends only on \(R_V-R_S\), equivalently \(\beta_2-\beta_1\).
- Recomputed the Table 2 endpoint values and confirmed \(R_V>1\).
- Solved the exact \(R_0=1\) boundary for \(\beta_1\) and computed its nonnegative-domain cutoff.
- Recomputed the Figure 1 \(R_0\) value from the displayed coefficients.
- Reconstructed the disease-free \((E,A)\) Jacobian block and computed its positive eigenvalue.
- Replayed all calculations using the bundled `verify.py` from its actual package path; it returns `VERIFY_OK`.

Limits:
- The analysis addresses only the printed equations and parameter values.
- No claim is made about unreported code, undocumented rescaling, or parameter values not present in the public article.
- No independent audit has been performed.
