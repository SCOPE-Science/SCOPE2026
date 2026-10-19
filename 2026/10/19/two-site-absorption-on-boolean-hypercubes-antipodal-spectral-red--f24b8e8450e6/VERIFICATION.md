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
# Reproducible mathematical checks

Execute `python artifacts/verify_two_sink.py` with Python 3, NumPy and SciPy. It should print `checks= 739`, and the dimension-five mean absorption fractions `0.3125` (nonantipodal) and `0.1875` (antipodal). The script checks exact Krawtchouk formulas against independently constructed Walsh projections for every initial site in dimensions two through six, checks spectral ranks and traces, and compares asymptotic survival against matrix-exponential evolution with unequal sink rates for dimensions two through five. These are finite corroborative checks. The proof's strict Gram-rank argument and dissipative spectral-convergence argument establish the unbounded-dimensional result without assuming exhaustive experimental evidence.

Independent audit has not been performed.
