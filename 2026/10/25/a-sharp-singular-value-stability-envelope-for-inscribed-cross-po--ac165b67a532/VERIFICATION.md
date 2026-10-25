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

Run `python verify.py` with Python 3, requiring no third-party libraries. The program uses exact `fractions.Fraction` arithmetic and Gaussian elimination. It constructs rational inscribed paired vertices, certifies all chosen-facet support inequalities and the positive origin barycenter, and reproduces determinant and profile equalities for dimensions two through six. The unrestricted dimension proof is contained in `RESULT.md`; finite checks are not a substitute for its quantifiers. Originality is based on substantive comparisons of mathematical statements and is not independently certified.
