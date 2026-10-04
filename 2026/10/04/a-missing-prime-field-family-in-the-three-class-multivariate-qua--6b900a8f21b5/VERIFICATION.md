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
# Verification

For the two tags, write \(A_{ij}=T_{ij}\) and \(B_{ij}=1-F_{ij}\). Expanding right self-distributivity and comparing the coefficients of the two input variables and the translating variable gives
\[
B_{ij}(A_{ik}-A_{jk})=0,
\qquad
B_{ik}(1-A_{ij})=B_{ij}B_{jk}.
\]
With diagonal values \(A_{00}=A_{11}=2\) and \(B_{00}=B_{11}=-1\), these identities have exactly two branches.

If \(B_{01}=B_{10}=0\), then \(A_{01}=A_{10}=1\). Otherwise, the first identity forces \(A_{01}=A_{10}=2\), and the second reduces to
\[
B_{01}B_{10}=1.
\]
Requiring the off-diagonal entries of \(F\) to be units excludes \(B_{01}=1\). Writing \(B_{01}=r\) therefore gives the stated family with \(r\in\mathbb F_p^\times\setminus\{1\}\).

The bundled verifier independently enumerates every unit coefficient quadruple for \(p=5,7,11\), compares it with this closed form, and checks all quandle axioms on every element triple. Its output is:

`VERIFY_OK primes=5,7,11 unit_solution_count=p-1 p5_solutions=4 p5_extra=2 family_missing_choices=p-3`

The finite computation is only a regression and transcription check; the all-prime result is the symbolic argument above.

The independent-audit channel has not been performed.
