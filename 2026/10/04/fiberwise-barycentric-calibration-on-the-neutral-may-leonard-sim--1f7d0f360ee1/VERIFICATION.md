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

It verifies that for
\[
\alpha+\beta=2
\]
the total population
\[
N=x+y+z
\]
satisfies
\[
\dot N=N-N^2.
\]

After imposing
\[
N=1
\]
and
\[
\beta=2-\alpha,
\]
it verifies the exact pointwise per-capita identities
\[
\frac{\dot x}{x}=(\alpha-1)(z-y),
\]
\[
\frac{\dot y}{y}=(\alpha-1)(x-z),
\]
and
\[
\frac{\dot z}{z}=(\alpha-1)(y-x).
\]

It also verifies
\[
(x-y)^2+(y-z)^2+(z-x)^2
=
3(x^2+y^2+z^2)-(x+y+z)^2.
\]

Finally, exact rational linear algebra verifies that the cyclic mean equations induced by the barycentric conditional laws have the unique solution
\[
\mathbb E[x]=\mathbb E[y]=\mathbb E[z]=\frac13.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure conditional expectations are analytic consequences of stationarity against arbitrary logarithmic antiderivative tests and are not inferred from finite numerical sampling.
