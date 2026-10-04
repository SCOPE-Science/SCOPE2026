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
The proof is symbolic and uniform in n. The accompanying `verify.py` is an exact-rational consistency checker. For n=4,...,8 it constructs the Cauchy--Binet numerator N, denominator D, rank-one factor S, and derivative numerator J=N'D-ND'. It verifies the denominator identity D=(n-1)(P')^2-nPP'', the generic degree pattern in the chosen specializations, coprimality, divisibility J by S, and quotient degree 3n-8. It also checks squarefreeness/separation in those finite examples.

The finite replay is not an exhaustive proof for arbitrary n. The all-n argument is the algebraic proof in RESULT.md, especially the Cauchy--Binet identity, Riemann--Hurwitz count, Lagrange-basis count of the rank-one parameters, and the published identification of the smooth and singular resectioning strata.

Run with Python 3 only:

`python3 verify.py`

Expected final line: `VERIFY_OK`.
