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

Run `python checker.py` with SymPy and NumPy installed; expected output is included in `checks.txt`. It checks exact polynomial identities and all-weight Rayleigh certificates, plus numerical spectral reconstructions. Infinite-weight optimality follows from the analytical Rayleigh quotient argument in RESULT.md, not sampling of weights. The rank-two global stability inequality follows from the rank-two Frobenius trace bound; no exhaustive rank-two numerical testing or independent audit is asserted.
