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

# Reproducibility

Run `python3 verify.py` with Python 3. The checker uses `fractions.Fraction`, constructs exact matrices, verifies the explicit five-power witness and the general downdate identity for rational examples, checks the beta-four polynomial reduction on rational parameters, and tests exact diagonal-power sampling at integer powers 0, 1, and 2. All-dimensional and all-real-exponent claims are established in RESULT.md by symbolic arguments, not by these finite checks. External independent audit has not been performed.
