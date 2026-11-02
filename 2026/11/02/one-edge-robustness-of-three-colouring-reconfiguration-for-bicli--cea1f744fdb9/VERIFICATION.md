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

# Finite verification and proof limits

Run `python verify_direct.py` and `python verify_structural.py` from the folder containing the extracted artifacts. Both scripts use the standard Python library only. The first enumerates assignments and all legal one-vertex changes; the second builds the hypercube-plus-ear model directly and checks its neighbour lists against the graph constraints. Their assertions establish the enumerated cases and no larger range. The proof of the theorem for arbitrary positive integers \(m,n\ge2\) is the mathematical argument in `RESULT.md`.

The complete theorem is about exact distances in an unweighted proper three-colouring graph. It does not claim a statement for four colours, multiple deleted original edges, or stars. Relevant historical literature is partially available only as indexed text; bibliographic coverage and independent validation are not certified.
