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

For the canonical vector field
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=\varepsilon(v+a-bw),
\]
it constructs
\[
\mathcal E
=
\frac12\dot v^2
+
\varepsilon
\left[
\frac{1-b}{2}v^2
+
\frac{b}{12}v^4
+
(a-bI)v
\right]
\]
and verifies exactly that
\[
L\mathcal E
=
(1-\varepsilon b-v^2)\dot v^2.
\]

It also checks the cleared residual identities behind the two conditional regressions and the abstract variance decomposition used in `RESULT.md`.

For
\[
\varepsilon=\frac{2}{25},
\qquad
b=\frac45,
\]
it confirms
\[
1-\varepsilon b
=
\frac{117}{125}
=
0.936.
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure and equality-rigidity arguments are analytic and are not inferred from finite trajectory simulation.
