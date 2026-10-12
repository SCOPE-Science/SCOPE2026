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

For the order-four three-state boundary law, write
\[
N=t^4+t^3+t^2+t+2,
\qquad
Q=t^3+t^2+t.
\]
Then \(\theta=N/Q\). The exact reductions used in the proof are
\[
N-Q=t^4+2,
\qquad
N-tQ=t+2,
\]
and, with \(D=t^3+t^2+t+1\),
\[
((t^4+1)Q+N)=(t^4+2)D.
\]
These identities produce the two nontrivial eigenvalues in the stated rational forms.

The branch-ordering identity is
\[
t^3(t+2)-(t^4+2)=2(t-1)(t^2+t+1).
\]
For the \(t>1\) Kesten–Stigum exclusion, the exact gap polynomial shifts as
\[
(t+1)(t^2+1)(t^4+2)-2t^3(t+2)
=
 s^7+8s^6+28s^5+54s^4+59s^3+36s^2+14s+6
\]
under \(t=1+s\). Every coefficient is positive.

The verifier also reconstructs the quotient-rule numerator of \(\theta'(t)\), checks the divisibility identity
\[
N-2(1+t)Q=-(t+2)(t^3+t^2+t-1),
\]
and numerically isolates the unique root \(\rho\in(0,1)\) only for the displayed decimal.

`verification/verify.py` uses only standard-library exact integer polynomial arithmetic for the identities. The floating-point bisection is informational and is not used to certify any infinite statement.

The verification does not establish a converse to Kesten–Stigum or a true reconstruction threshold.
