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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies
\[
L\left(\frac{y^2}{2}\right)=xy-y^2,
\qquad
L\left(\frac{z^2}{2}\right)=xz+\frac3{10}z^2,
\]
and
\[
L(yz)=xz+xy-\frac7{10}yz.
\]

It verifies both equilibria
\[
(0,0,0),
\qquad
\left(-\frac{10}{3},-\frac{10}{3},\frac{100}{9}\right),
\]
the exact mean–variance coefficient \(9/100\), and the RMS-gap coefficient \(7/13\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificates. The conditional laws use arbitrary one-variable test functions, and the equality classifications additionally use invariant-support tangency and bounded completeness.
