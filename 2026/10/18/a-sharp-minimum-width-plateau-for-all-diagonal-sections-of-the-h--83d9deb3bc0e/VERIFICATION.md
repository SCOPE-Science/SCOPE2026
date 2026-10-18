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

Run `python3 checker.py` with the Python standard library. The direct checker enumerates all vertices for sample dimensions 4–8, performs exact Fraction computations for all cut supports, compares explicit candidate widths and sampled directions, and checks strict threshold inequalities in dimensions 4–89. Expected result: `PASS cuts=1130 random_directions=2968 threshold_dimensions=86 min_random_gap=0.012087365`. These checks are nonexhaustive with respect to dimension and continuous parameter; the all-dimensional statement relies on the proof in RESULT.md. Independent mathematical validation has not been performed.
