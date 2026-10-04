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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic.

It verifies directly from the Koper vector field that
\[
\ddot y
+
(2+\delta)\dot y
+
\delta y
=
k\dot x+\delta kx-\delta\lambda.
\]

It checks the abstract conditional-regression variance identity
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
from the required moment relations.

For
\[
\delta=1,\qquad
\varepsilon=\frac1{10},
\]
it verifies
\[
1+\frac{\delta\varepsilon}{3}
=
\frac{31}{30}.
\]
For
\[
\varepsilon=\frac1{100},
\]
it verifies
\[
1+\frac{\delta\varepsilon}{3}
=
\frac{301}{300}.
\]

It also checks the reported decimal strip radii to within \(10^{-6}\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure disintegrations, equality classification, and sign-to-strip argument are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory simulation.
