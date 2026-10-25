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
# Verification details

Running `python3 verify.py` with the standard Python library generates every regular cell by monotone extension of oriented-triangle zero-cells, checking all required tournament arcs independently. It also generates the cells by the theorem's anchored Boolean subsets and checks **equality of the complete cell sets**, not merely their sizes, for \(n=5,7,9,11,13,15\). The command terminates with `BOOLEAN_CELL_ENUMERATION_OK` after checking the complete face vectors. The infinite-family statements use the separate, explicit circular-order proof; finite verification does not prove all cases. No integer homology, homotopy equivalence or independent review is certified.
