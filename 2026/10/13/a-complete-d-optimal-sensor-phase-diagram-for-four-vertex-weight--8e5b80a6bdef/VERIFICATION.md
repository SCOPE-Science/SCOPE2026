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
# Reproduction and mathematical limits

Run `python3 verify.py` from the directory containing `verify.py` with an ordinary Python 3 standard library. The completed checker prints `FOUR_NODE_UNIVERSAL_POLYNOMIAL_IDENTITIES_OK`, `ALL_26460_INTEGER_TRIPLES_BRANCHES_OK`, `EXACT_BOUNDARY_AND_REFLECTION_CASES_OK`, `LOWER_DIMENSION_MINIMALITY_OK`, and `VERIFY_OK`.

The determinant identities are exact polynomial statements. Every column of the Krylov matrix has homogeneous total degree equal to its exponent in the weights, so each determinant has total degree at most six. Seven distinct rational evaluation points in each of three variables and exact equality there certify a polynomial identity (successive univariate interpolation); this is not an extrapolation of numerical data. The phase inequalities, case boundaries, horizon independence, and positive-definiteness of the exponential Gramian are proved analytically in `RESULT.md`; the 26,460-point integral grid only guards against case mistakes. The checker does not independently assess source novelty, and it is not a general-purpose theorem prover or an external certification service.
