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

For \(a=\pi/(2\sqrt3)\), define
\[
H(c)=\tanh(ac)-2\Phi(c)+1
\]
and
\[
R(c)=\log\frac{a\,\operatorname{sech}^2(ac)}{2\varphi(c)}.
\]
The proof shows that \(R'(c)=c-2a\tanh(ac)\) has exactly one positive zero after initially decreasing, so \(R\) first decreases and then increases. The separated signs \(R(0)>0\), \(R(1)<0\), \(R(2)<0\), and \(R(c)\to\infty\) give exactly two zeros of \(H'\).

The standalone `verify.py` recomputes the numerical sign certificates, the Mills-bound comparison at \(c=2\), and the unique root on \((1,2)\). Its terminal line is of the form:
`VERIFY_OK cstar=1.744471617747319 R1=-0.101500505268434 R2=-0.165702102485606`.

The mesh checks are regression tests only. Global uniqueness follows from the analytic derivative-shape argument.
