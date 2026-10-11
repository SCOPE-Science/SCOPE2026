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
The packaged `verify.py` uses only the Python standard library and exact rational sparse-polynomial arithmetic.

For the vector field
\[
\dot x=v,\qquad
\dot v=\mu(1-x^2)v-x,
\]
it verifies, for monomial test functions through degree eight, the generator decomposition
\[
L\!\left(\frac{x^{k+1}v}{k+1}\right)
=
x^kv^2
+
\frac{\mu x^{k+1}(1-x^2)v}{k+1}
-
\frac{x^{k+2}}{k+1}.
\]
This is the exact polynomial identity used after the conditional damping term is shown analytically to have zero stationary mean.

It also verifies
\[
L\!\left(\frac{x^2+v^2}{2}\right)
=
\mu(1-x^2)v^2.
\]

Finally, exact rational arithmetic verifies that the \(k=0\) and \(k=2\) hierarchy identities together with the energy balance imply
\[
\mathbb E[x^4]=3\mathbb E[x^2].
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The all-test-function conditional identity, distributional reconstruction of the kinetic-energy projection, and strict equality cases are analytic arguments in `RESULT.md`; they are not inferred from finite numerical experiments.
