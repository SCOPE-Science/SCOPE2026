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

For
\[
F_{a,b}(x)=(1-e^{-ax})(1-e^{-bx}),
\]
the verifier solves
\[
F_{\theta_1,\theta_2}(Q(x))=F_{\lambda_1,\lambda_2}(x)
\]
by bisection and then evaluates derivatives from
\[
Q'(x)=\frac{f_X(x)}{f_Y(Q(x))}
\]
and
\[
Q''(x)=\frac{f_X'(x)-f_Y'(Q(x))(Q'(x))^2}{f_Y(Q(x))}.
\]

For the source example \((\lambda_1,\lambda_2)=(2,3)\) and \((\theta_1,\theta_2)=(3/2,7/2)\), the predicted constants are
\[
e^x\left(Q(x)-\frac43x\right)\to-\frac23,
\]
\[
e^x\left(Q'(x)-\frac43\right)\to\frac23,
\qquad
e^xQ''(x)\to-\frac23.
\]
At the origin,
\[
Q''(0+)=\frac52\sqrt{\frac87}\left(\sqrt{\frac87}-1\right).
\]

The standalone `verify.py` checks these constants directly from the exact formulas. Expected final line:
`VERIFY_OK tail_q=-0.666554373 tail_qp=0.666438679 tail_qpp=-0.666213879 local_qpp=0.184816890`.

Finite numerical checks do not establish the asymptotic theorem; they only replay it.
