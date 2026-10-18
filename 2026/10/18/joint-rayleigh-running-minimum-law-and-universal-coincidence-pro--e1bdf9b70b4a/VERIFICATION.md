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

# Reproducibility and limitations

Run `python3 verify.py` from a directory containing this document and the standalone verifier. The script needs Python 3 and its standard library only. It independently generates exact overpartition counts using the coefficient product, enumerates all ordinary partition shapes through weight 12 with all overlining choices, and then checks exact joint-tail and coincidence formulas. Expected report: 13 enumerations, 78 joint-tail comparisons, 39 coincidence comparisons, and three finite asymptotic-trend checks.

The infinite results do not follow from the tests. They are established by the reversible counting identities in `RESULT.md`, the quantitative asymptotic of the overpartition coefficient from Sills–Engel, locally uniform exponential expansions, a Riemann sum, and a tail bound. No unrestricted computational search or external mathematical certificate is claimed. Fixed multiplicity thresholds are essential to the stated limiting argument; an independent audit has not been carried out.
