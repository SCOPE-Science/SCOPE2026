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

The coefficient comparison was checked symbolically. With \(\delta=d_0-2r_0\), \(L_0=c_1^{-2}\), and \(x_0=2c_1\delta/r_0\), the source assumptions imply \(x_i=\kappa_i d_i\theta_i\ge x_0\). For \(\beta>L_0\ge L_i\),
\[
\frac{a_i}{\widetilde a_i}=\frac{\beta}{L_i}\ge\frac{\beta}{L_0},
\qquad
\frac{b_i}{\widetilde b_i}=\frac{1+\beta x_i}{1+L_ix_i}\ge\frac{1+\beta x_0}{1+L_0x_0}.
\]
Thus the common factor \(q\) is strictly larger than \(1\).

For \(p=(1+\delta q)/(1+\delta)\), direct algebra gives
\[
p-1=\frac{\delta(q-1)}{1+\delta},\qquad q-p=\frac{q-1}{1+\delta},\qquad \frac{p-1}{q-p}=\delta.
\]
These identities close the two recurrence inequalities exactly. The proof uses the source's positivity comparison \(\widetilde\Delta^{(4)}_i\ge\widetilde\Delta^{(2)}_i\) and its identification of exponent growth rates with the product components.

The published proof was also checked internally for boundary consistency. The stated free-flight lower bound is \(d_i\ge d_0-2r_0\), not \(d_i\ge d_0\). The final proof cannot replace an induction rate by a larger auxiliary rate without a new argument, and a minimum cannot be lower-bounded by one of its defining entries in the direction used there. The repaired proof avoids those steps.

Limits: no claim is made that \(\log p\) is sharp, and no conclusion is drawn about whether the stronger printed bound can be proved by another method.
