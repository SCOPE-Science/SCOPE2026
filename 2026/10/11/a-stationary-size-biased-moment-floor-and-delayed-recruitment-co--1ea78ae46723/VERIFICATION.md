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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic for the algebraic stationary consequences.

It checks that
\[
p\mathbb E[B]=\delta\mathbb E[X]
\]
and
\[
p\mathbb E[XB]=\delta\mathbb E[X^2]
\]
imply
\[
\operatorname{Cov}(X,B)
=
\frac{\delta}{p}\operatorname{Var}(X).
\]

It also verifies the Cauchy--Schwarz variance consequence
\[
\operatorname{Var}(B)
\ge
\left(\frac{\delta}{p}\right)^2\operatorname{Var}(X)
\]
for a rational test moment set satisfying the exact covariance law.

A symbolic equilibrium check uses an exact ratio
\[
p/\delta=4
\]
and confirms the relation
\[
e^{-aK}=\delta/p
\]
through the defining formula
\[
K=a^{-1}\log(p/\delta).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The time-translation marginal argument and strict Jensen equality case are analytic proofs in `RESULT.md`; no finite delay simulation is used.
