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

# Reproducible verification

Run `python CHECK.py` from the directory containing the extracted files. Python 3 and NumPy are required. The script constructs both the waiting-time transform spectrum and the generator-resolvent spectrum for a fixed suite of positive heterogeneous rates, computes elementary-symmetric crossing polynomials, and checks crossing counts and sign changes. The recorded successful run produced 2,221 assertions with sizes 2 through 11 and six rate profiles each.

The strictly positive crossover count for every integer stage number and every positive-rate vector is established by the proof's stability and argument-rotation reasoning, not numerical root enumeration. No finite collection of tests establishes global novelty. No independent scientific validation has been performed.
