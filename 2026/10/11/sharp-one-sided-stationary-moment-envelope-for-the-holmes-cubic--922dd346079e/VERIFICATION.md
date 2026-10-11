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

It verifies the invariant-mean algebra
\[
\mathbb E[x^3]
=
(a-b-1)m,
\]
the fixed-point identity
\[
\rho^2=a-b-1,
\]
and the sharp mixture formulas in a rational parameter test case with \(\rho=1\).

For the published pre-crisis parameters
\[
a=\frac{271}{100},
\qquad
b=\frac{18}{100},
\]
it verifies exactly
\[
\rho^2=\frac{153}{100}.
\]

The Cauchy-Schwarz step, its equality condition, forward-invariance support classification, and periodic-orbit side-visiting theorem are analytic proofs in `RESULT.md`; they are not inferred from finite numerical orbit sampling.

The stored output in `verification_output.txt` is `VERIFY_OK`.
