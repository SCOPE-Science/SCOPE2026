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

- Executed `python3 verify_quadratic_spline.py` from the current record's standalone file. Python `fractions.Fraction` arithmetic verifies the Gram inverse, each kernel polynomial by exact polynomial identities, all 29 Bernstein-control norm comparisons, and the endpoint lower bound.
- The proof checks every \(x\in[0,1]\) by nonnegative Bernstein blending on ten intervals, followed by reflection. It does **not** infer the general theorem from finite grid sampling.
- The four sign switches in the endpoint kernel are shown by explicit quadratic roots and give the claimed distinction between measurable attainment and continuous nonattainment.
- The statement is restricted to the specified fixed midpoint and continuity class. Unindexed historical variants could remain; independent validation has not been performed.
