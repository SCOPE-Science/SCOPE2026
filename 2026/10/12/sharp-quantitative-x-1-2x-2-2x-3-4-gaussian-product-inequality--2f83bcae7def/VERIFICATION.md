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

The analytic proof has two independently replayable components.

First, Isserlis' formula for
\[
X_1^2X_2^2X_3^4
\]
contains \(105\) pairings. Grouping them by correlation monomial gives
\[
3,\quad
6a^2,\quad
12b^2,\quad
12c^2,\quad
48abc,\quad
24b^2c^2.
\]
The bundled script enumerates all pairings directly and verifies exactly these coefficients.

Second, define
\[
u_*=\frac{\sqrt{41}-5}{8},
\qquad
x_*=\frac{9-\sqrt{41}}4,
\qquad
C_*=\frac{7-\sqrt{41}}2.
\]
For the sign pattern
\[
a=-x_*,
\qquad
b=c=\sqrt{u_*},
\]
the script checks
\[
1+2abc-a^2-b^2-c^2=0
\]
and
\[
\frac{
6a^2+12b^2+12c^2+48abc+24b^2c^2
}{
6a^2+12b^2+12c^2
}
=
C_*.
\]

A deterministic grid over the negative-product positive-semidefinite region is included only as a replay check and is not used in the proof.

Expected successful terminal output begins with:
`VERIFY_OK constant=0.298437881284`.

The global lower bound and equality classification are established analytically in `RESULT.md`; finite computation is not used to certify an infinite statement.
