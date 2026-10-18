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

# Verification notes

`python check_section.py` (SymPy dependency, no network) passed the exact symbolic edge-intersection identities, 28-term nonnegative rational Bernstein certificate, and symbolic endpoint derivative conditions. Independent 2,000-direction polygon reconstructions matched the two formulas within \(9\times10^{-15}\) in Euclidean area.

The theorem is established by the exact symbolic identities and inequalities proved in `RESULT.md`, not by the numerical experiments alone. Boundary normals are obtained by continuity, and maximal/minimal equality orbits are explicitly classified. This is not an independent audit or an external certificate; full historical priority remains provisional.
