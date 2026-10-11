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

It checks the abstract conditional-regression variance identity
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B)
\]
under the moment consequences of a conditional projection.

It checks the exact algebra of the two stationarity steps used in the speed-slope proof and the branchwise sign structure of
\[
xh(x).
\]

For the classical slopes
\[
m_0=-\frac17,
\qquad
m_1=\frac27,
\]
it verifies exactly
\[
\frac{m_1-m_0}{m_1}=rac32
\]
and
\[
\frac{-m_0}{m_1-m_0}=rac13.
\]
It also verifies that the outer-branch expression for \(xh(x)\) changes sign precisely at \(|x|=3/2\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure conditional expectations, breakpoint lemma, and equality-rigidity arguments are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory simulations.
