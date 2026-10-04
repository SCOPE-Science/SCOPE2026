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

For a positive smooth solution, \(P/x=d(\log x)/dt\) and \(Q/y=d(\log y)/dt\). Across the two smooth legs of the bilateral order-2 orbit,
\[
\frac{x_B}{x_A}\frac{x_D}{x_C}
=\frac{1}{(1+p_1)(1-p_2)},
\]
and
\[
\frac{y_B}{y_A}\frac{y_D}{y_C}
=\frac{y_B(y_A+\tau_1)}{y_A(y_B+\tau_2)}.
\]
Multiplying these endpoint contributions by the source quantities \(\Delta_1\Delta_2L_2\) gives the corrected multiplier in the finding.

`verify.py` uses exact rational arithmetic to replay these two endpoint identities, the printed-to-corrected quotient
\[
(1-p_2)^2\left(\frac{y_B+\tau_2}{y_B}\right)^2,
\]
and the equality condition \((1-p_2)(y_B+\tau_2)=y_B\). A successful replay prints `VERIFY_OK`.

The checker is a finite algebraic replay only. General validity comes from the symbolic logarithmic-derivative argument and the source's unsimplified Floquet formula; no numerical experiment is used to establish the theorem.
