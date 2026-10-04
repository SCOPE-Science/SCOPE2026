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

It verifies the algebraic decompositions
\[
\dot X=(k_1A-k_2X)Y+k_3BX-2k_4X^2
\]
and
\[
\dot Z=k_3BX-k_5Z.
\]

For the historical 1974 parameter values
\[
k_3=8\times10^3,
\qquad
B=0.06,
\qquad
k_5=1,
\]
it verifies exactly
\[
k_3B=480,
\qquad
\frac{k_5}{k_3B}=\frac1{480},
\qquad
\frac1{(k_3B)^2}=\frac1{230400}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates algebraic certificates only. Conditional expectations and equality rigidity are analytic consequences of stationarity and bounded complete trajectories as proved in `RESULT.md`.
