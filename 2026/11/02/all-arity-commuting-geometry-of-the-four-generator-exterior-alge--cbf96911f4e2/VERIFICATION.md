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

# Computational verification

The executable `artifacts/check_exterior4.py` is a standalone Python 3 program using only the standard library. Run `python3 artifacts/check_exterior4.py`; the successful final line is `EXTERIOR4_COMMUTING_GEOMETRY_OK`. The actual captured output is embedded as `artifacts/verification_output.txt`.

The program computes original exterior products on all sixteen monomial basis elements. It exhaustively checks the adjoint-rank distribution of all 6561 odd elements over \(\mathbb F_3\), including the induced commuting-pair count. It exhaustively enumerates rank-one degree-one matrices and the ranks of their degree-three constraints for \((q,m)=(3,2),(3,3),(3,4),(5,2)\). It computes the tangent spans for each attainable rank at tuple lengths two, three and four over \(\mathbb F_3\). The program additionally verifies direct multiplication samples over primes two, three, five and seven, and over the genuine extension field \(\mathbb F_4\).

The tests do not exhaust arbitrary fields or tuple lengths. The general geometric and finite-field formulas rest on the algebraic proof, which specifies the reduced variety and does not claim radicality of the original equation ideal. Independent mathematical audit has not been performed.
