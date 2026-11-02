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

# Mathematical verification and scope

The analytical argument in `RESULT.md` establishes (i) the exact product correlation for the static scenery, (ii) a uniform second-moment bound that implies its almost-sure spatial Cesàro law, (iii) the geometric holding-time transfer to a conditional bracket strong law, and (iv) the martingale functional invariance principle. All limit statements concern almost every fixed static environment and every finite time horizon.

`check.py` contains no network calls or external dependencies. The exact-rational check of 4,376 finite assertions is reported in `check_output.txt`. It tests the critical binary combinatorics and finite product moment identities; it does not establish an almost-sure or functional theorem by numerical extrapolation. The analytical proof is therefore essential.

No finite computational certificate or independent mathematical assessment is asserted for the infinite claims. The results do not include convergence rates, correlated coefficient arrays, or vanishing ellipticity.
