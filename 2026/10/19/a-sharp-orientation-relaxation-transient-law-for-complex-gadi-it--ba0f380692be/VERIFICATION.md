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
# Reproduction notes

Run `python verify.py` with SymPy installed. The checker evaluates exact algebraic expressions, including direct reconstructions of both GADI substeps, rank-one eigenvalue and singular-norm formulas, the power identity, and rational amplification/relaxation examples. Expected output begins with `PASS:` followed by the number of successful comparisons.

Analytic limits in the accompanying proof require the explicit rank-one power formula and a uniform geometric-tail estimate. The finite checker does not claim to certify those limits by sampling. Bibliographic priority and broader-dimensional generalizations are not independently verified.
