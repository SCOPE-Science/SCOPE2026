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
The packaged `verify.py` uses only exact rational arithmetic from the Python standard library.

It verifies the moment algebra underlying every state-slice variance defect. If
\[
\mathbb E[A]=\mathbb E[B]
\]
and
\[
\mathbb E[AB]=\mathbb E[B^2],
\]
then
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

It separately verifies the nuclear scaling
\[
\operatorname{Var}(k_1P_2)-\operatorname{Var}(k_2P_N)
=
k_1^2\operatorname{Var}(P_2)-k_2^2\operatorname{Var}(P_N).
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation steps, endpoint equality classification, crossing result, and exponential-memory representation are analytic arguments in `RESULT.md`; they are not inferred from finite numerical experiments.
