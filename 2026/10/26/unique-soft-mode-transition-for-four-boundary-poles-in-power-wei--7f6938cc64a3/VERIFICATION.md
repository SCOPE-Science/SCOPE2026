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

# Reproduction and mathematical limitations

Run `python3 check_transition.py` using an ordinary Python 3 interpreter. The script verifies exact partial-fraction identities by rational evaluation at twelve distinct points after clearing a known degree-at-most-ten numerator; it then bounds \(\pi\) by alternating rational arctangent series and \(\log2\) by a positive rational atanh series. The resulting fully rational inequalities prove \(F(2)<0<F(3)\). The script also displays a Simpson-quadrature estimate of the sole transition value; that estimate is noncertifying.

The full spectrum and uniqueness for every \(\alpha>2\) follow from the beta-moment expansion, the root-of-unity generating identities, positivity of the rational integrals, and a strict single-crossing monotonicity argument, all written in `RESULT.md`. Finite calculations alone would not prove those universal assertions. The endpoint integral value at \(\alpha=2\) is not claimed to be an actual twice differentiable energy Hessian. No independent scientific audit has been performed.
