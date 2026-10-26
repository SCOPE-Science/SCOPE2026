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

# Verification notes

The package contains `verify.py`, an executable exact symbolic check using SymPy. Running `python verify.py` from the package directory returned:

`PASS: general rank-one derivative, complete weighted three-path coefficients, two exact witnesses, unweighted three-path boundary`

The checker verifies the rational expressions for both concrete graphs, their derivatives and three limit/minimum values, the general three-vertex weighted coefficient on every standard-basis opinion vector, and the unit-weight small-order exclusion. The analytical proof in RESULT.md separately establishes the general response for all eligible connected positive graphs, nonnegative innate opinion vectors, and all real strengths \(t\geq0\). The checker does not exhaust larger graphs or establish novelty. The result is reviewed but has not received independent validation.
