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

The claim is verified analytically from the explicit coordinate model.

For \(A=(-1,0)\), \(B=(1,0)\), \(C=(0,2)\), and \(P=(0,y)\), perpendicular projection gives the three pedal vertices recorded in `RESULT.md`. The resulting exact formulas are
\[
R_p(y)=\frac{1+y^2}{1+2y}
\]
and
\[
r_p(y)=\frac{2(2-y)\bigl(\sqrt{5(1+y^2)}-2+y\bigr)}{5(1+2y)}.
\]
At \(y=1/100\), the reversal \(R_p+\sqrt2\,r_p>5/4\) is reduced to an exact integer comparison after two rigorous rational lower bounds for the radicals. The script `verify_counterexample.py` replays those identities and comparisons using exact rational arithmetic for every non-radical step.

The script also prints a high-precision decimal excess as a diagnostic. That decimal value is not used to prove the sign. The proof does not claim a complete classification of counterexamples or an optimal replacement coefficient.
