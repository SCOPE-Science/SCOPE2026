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

Set
\[
a=\frac1{d+1},
\qquad
b=\frac d{d+1}.
\]
Then
\[
a+b=1,
\qquad
\frac{a+b}{2}=\frac12.
\]
Consequently the geometric mean of the two source densities is
\[
\frac{\kappa^{1/2}}{\sqrt{I_aI_b}},
\]
which integrates to the claimed Hellinger affinity.

For the variance formula, put
\[
c=\frac{a+b}{2}.
\]
Integration by parts gives
\[
\int_a^c(t-a)F''(t)\,dt
=
(c-a)F'(c)-F(c)+F(a)
\]
and
\[
\int_c^b(b-t)F''(t)\,dt
=
-(b-c)F'(c)+F(b)-F(c).
\]
Since
\[
c-a=b-c,
\]
the midpoint derivative terms cancel. This proves the exact triangular-kernel second-difference identity used in the result.

Under the dilation \(K\mapsto sK\),
\[
I_t\mapsto s^{(d-1)(1-t)}I_t.
\]
The exponent in the numerator at \(t=1/2\) agrees exactly with the averaged denominator exponent, so the Hellinger gap is similarity invariant.

The bundled checker replays these exponent and midpoint-coefficient identities. It does not infer the arbitrary-body theorem from finite samples.
