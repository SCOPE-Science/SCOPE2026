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

The analytic proof reduces the full parameter-and-deviation statement to the one-dimensional function
\[
f_b(t)=\log\!\frac{b+1}{b}-\log(1-t)-\frac{b+2}2t^2.
\]
The derivative identity
\[
f_b'(t)=\frac{1-(b+2)t(1-t)}{1-t}
\]
shows that for \(b\le2\) the function is nondecreasing, while for \(b>2\) its only interior minimum is at \(t_b=(1+\sqrt{(b-2)/(b+2)})/2\). At that point the envelope derivative of \(H(b)=f_b(t_b)\) is
\[
H'(b)=-\frac1{b(b+1)}-\frac{t_b^2}2<0.
\]
This proves the infinite classification without numerical enumeration.

The bundled checker uses high-precision decimal arithmetic to verify the sign change
\[
H(3.75347721)>0>H(3.75347722),
\]
the critical-point equation, and representative finite-grid stress tests. Those computations certify the quoted decimal bracket and implementation consistency only; they are not used as a substitute for the analytic global proof.
