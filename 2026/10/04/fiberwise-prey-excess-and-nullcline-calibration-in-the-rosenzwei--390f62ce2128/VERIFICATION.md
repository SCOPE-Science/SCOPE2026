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
The packaged `verify.py` uses only the Python standard library and exact rational algebra.

It checks the coexistence-prey identity
\[
N_*=rac{mh}{1-m},
\qquad
\frac{N_*}{h+N_*}=m,
\]
and the factorization
\[
\frac{N}{h+N}-m
=
\frac{h(N-N_*)}{(h+N)(h+N_*)}.
\]

It checks that
\[
\frac{(N-N_*)^2}{h+N}
=
(h+N)-2(h+N_*)+rac{(h+N_*)^2}{h+N},
\]
which is the algebra behind the conditional harmonic defect.

It also verifies the abstract conditional-regression variance identity
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
from
\[
\mathbb E[A]=\mathbb E[B],
\qquad
\mathbb E[AB]=\mathbb E[B^2].
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure conditional expectations, strict support bound, and equality classification are analytic arguments in `RESULT.md`; they are not inferred from finite simulations.
