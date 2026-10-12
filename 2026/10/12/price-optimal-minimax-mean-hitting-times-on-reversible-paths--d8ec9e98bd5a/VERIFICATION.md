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

# Reproduction and limits

Run `python3 verify.py` with Python 3 using the standard library. The checker derives finite hitting times independently by solving the generator Poisson equations with exact rational arithmetic, then compares every ordered pair against the endpoint identities. It verifies budget normalization, the extremal multiplier and directional active-constraint conditions numerically, checks arbitrary feasible alternatives, and tests all three regimes of the three-state price frontier.

Before package assembly, the checker produced: `VERIFY_OK 220 independent exact generator/hitting-time cases; 5940 ordered hitting entries; 800 arbitrary-mass/price optimizer cases; 8000 feasible perturbations; eight exact three-state phase probes`.

Exact matrix identities apply only to the tested finite cases. Float comparisons and sampled alternatives cannot establish an infinite-dimensional family of inequalities, uniqueness, completeness of a classification, or originality. The proof of those claims is in `RESULT.md`, Steps 1–4, using direct Poisson flux identities, weighted Cauchy–Schwarz equality, and strict scalar concavity. The only historical full-text limitation most relevant to the claim is the unavailable 1996 Palacios–Tetali article.
