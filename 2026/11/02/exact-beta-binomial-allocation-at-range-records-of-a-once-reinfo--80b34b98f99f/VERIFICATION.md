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

To reproduce the finite tests, place `check.py` and `check_output.txt` together and run `python3 check.py`. The checker uses Python's standard-library `fractions.Fraction` and solves the original weighted finite-state exit equations with exact Gaussian elimination. It then propagates all joint record-direction probabilities through 30 levels for six rational reinforcement weights, verifies the beta-binomial mass function, conditional final direction, mean and variance, and checks two nonexchangeable three-record paths. Expected output is recorded in `check_output.txt`.

The proof in `RESULT.md`, not this finite test, establishes the theorem for arbitrary real \(c>0\), all levels, and the weak beta limit. The nonexchangeable paths rule out a process-level Pólya-urn representation, not the beta-binomial identity in a single marginal.

Literature inspection included the entire publicly served HTML of arXiv:2602.10721v2 and arXiv:1903.05234. For the closely related Serlet (2018) chapter, only bibliographic headings and abstract could be read; the full chapter was unavailable, and equivalent prior results remain a material historical-priority risk. There was no independent audit.
