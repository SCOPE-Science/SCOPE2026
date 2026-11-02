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

Run `python3 verify_bounds.py` using Python 3 (standard library only). The script forms the complete joint-distribution linear program for three Bernoulli indicators, enumerates every basic feasible support of size at most five, and checks the sharp formula on all feasible three-coordinate quarter-grid inputs. The script prints 190 exact rational comparisons as passed and computes both heterogeneity examples. `CHECK_OUTPUT.txt` records the exact output. The formal all-dimension validity follows from the convex-hull proof in RESULT.md, not from the numerical test.

Research comparisons: Ansari's maximum-feasibility theorem, Bartl–Kupper–Lux–Papapantoleon's general maximum transport duality, Prékopa/Boros–Prékopa classical event-count linear programming, and Pinelis on exactly-one probabilities. Historical priority remains provisional. No independent audit or formal-machine proof has been performed.
