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

The proof is exact and does not depend on bounded computation.

The attached checker supplies an independent finite stress test. It generates every prime
\[
\ell<20000
\]
by integer trial division, sets
\[
b=\ell+1,
\]
and directly evaluates
\[
T_b(x)
=
\left\lfloor\frac{x^2}{b}\right\rfloor
+
(x^2\bmod b)
\]
for every positive one-digit state.

It separately predicts the cycle set from the theorem:
if
\[
\ell\not\equiv1\pmod3,
\]
the predicted set is empty; otherwise it finds the two roots of
\[
z^2+z+1\equiv0\pmod\ell
\]
and applies
\[
u^2-(3\ell-1)u+(\ell-1)^2\le0.
\]
The directly observed and predicted sets must agree exactly.

The checker also asserts:
\[
\ell=7:\quad 2\leftrightarrow4,
\]
\[
\ell=13:\quad \text{no cycle},
\]
\[
\ell=19:\quad 7\leftrightarrow11,
\]
and
\[
\ell=67:\quad 29\leftrightarrow37.
\]

Finite agreement is corroborative. The universal proof rests on the transition congruence, the prime-field cubic-root classification, and the exact quotient-and-remainder condition.
