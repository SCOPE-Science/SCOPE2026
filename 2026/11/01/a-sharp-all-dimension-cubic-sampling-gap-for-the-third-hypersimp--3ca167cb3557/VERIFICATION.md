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

# Reproducibility and verification
The standalone Python 3 file `CHECK.py` uses only the standard library. Run `python3 CHECK.py` in the same directory as the theorem statement. It reconstructs all three-subsets and exact rational Gram entries, evaluates the four Johnson incidence sectors, and checks Gram eigenactions on explicit alternating incidence vectors in dimensions \(6,7,8,9,10,11,12,13,15\). It also checks the exact rank at \(n=6\), the sharp rational equality at \(n=13\), and 94 supplementary dimension spot checks. The successful execution prints:

`HYPERSIMPLEX_CUBIC_SAMPLING_OK 1441 exact Gram rows; 94 extra dimension spot checks`

The finite code run corroborates algebra; it does not certify the infinitely many dimensions. The all-dimension argument is the rational Johnson decomposition, positivity of the three other spectral branches, and derivative sign analysis of the remaining branch, as written in `RESULT.md`. No independent audit or validation was performed.
