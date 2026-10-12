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

Let
\[
\Delta=\sqrt{n(n-4)},
\qquad
R_n=\frac{n-\Delta}{2}H_1+\frac{n+\Delta}{2}H_2-E,
\]
and
\[
\gamma_q=qH_1+H_2-E.
\]
With \(2n\) exceptional curves collected in \(E\), the intersection form gives
\[
R_n\cdot\gamma_q
=
\frac{n(q-3)+(q-1)\Delta}{2},
\qquad
\gamma_q^2=-2(n-q).
\]

The exact checker applies
\[
s_{\gamma_q}(R_n)
=
R_n+\frac{R_n\cdot\gamma_q}{n-q}\gamma_q
\]
and verifies that after multiplication by \(2(n-q)\), the first two coefficients are
\[
A_q=n(n+q^2-4q)+(q^2-n)\Delta
\]
and
\[
B=n(n-3)+(n-1)\Delta.
\]

It then verifies symbolically that the determinant controlling rationality of \(A_q/B\) is
\[
2n(q-n)(q-n+2).
\]
For \(1\le q\le n-1\), the unique root is \(q=n-2\). The identity
\[
(n-2)^2-n(n-4)=4
\]
provides the elementary proof that \(\Delta\) is irrational for every integer \(n>4\).

The finite sweep through \(5\le n\le100\) is only a secondary sanity check. The mathematical claim rests on the symbolic identities and the parity argument. The saved replay output ends in `VERIFY_OK`.
