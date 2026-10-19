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
# Reproduction

Run `python3 verify_tournament.py` (Python 3 standard library only). The checker independently enumerates all tournaments on 4 and 5 vertices and calculates exact rational moments of cyclic-triangle and four-cycle counts. It also checks the signed-monomial decomposition on 1000 additional six-vertex orientations.

The infinite-size proof is the product expansion and Walsh orthogonality in RESULT.md; finite enumeration is not offered as an exhaustive infinite certificate. The checker does not verify historical priority or an independent audit.
