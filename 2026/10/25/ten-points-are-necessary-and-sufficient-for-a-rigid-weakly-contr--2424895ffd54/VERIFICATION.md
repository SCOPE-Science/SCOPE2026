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
# Reproduction and limits

Run `python3 verify.py` with standard-library Python 3; no packages or external data are needed. The script specifies all lower and upper cover incidences from Sections 4.1 and 5.1 of arXiv:2605.06155, enumerates the entire finite set of level permutations, and checks equality of transformed edge relations, including reverse-order mappings. It asserts group orders \(2,6,4,4,2,2,1\) and reverse-order bijection counts \(0,0,0,4,0,0,1\) in Type I--VII order. Each of the seven checks completed successfully. A separate directed-graph-isomorphism enumeration agreed with these counts. The final ten-point sharp cardinality step relies on the published nine-point classification and the cited group's nontriviality; `verify.py` does not enumerate all spaces with nine or ten vertices.
