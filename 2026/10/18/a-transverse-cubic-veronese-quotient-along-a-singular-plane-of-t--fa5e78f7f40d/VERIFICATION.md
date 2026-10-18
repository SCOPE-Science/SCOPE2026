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

# Reproducibility and limits

Run `python verify.py` using Python 3 with SymPy installed. The script evaluates the four proposed local equations on the original four-parameter cubic image and checks exactly the three Hankel-minor identities after adjoining a formal square root of the invertible parameter. It also checks the classical cubic Veronese parameterization. The observed output is `VERIFY_OK`.

The universal scheme identification additionally uses the mathematical argument in `RESULT.md`: both ideals are prime of dimension four and one contains the other. Symbolic substitutions alone do not prove ideal equality, global normality, or novelty. The calculation makes no assertion outside the chart \(x_2x_3x_7\ne0\). Independent audit has not been performed.
