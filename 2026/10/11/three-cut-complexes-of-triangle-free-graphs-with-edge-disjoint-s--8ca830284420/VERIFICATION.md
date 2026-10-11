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

# Verification of the graph-family result

`verify.py` is the complete standalone finite checker (Python 3, standard library only). Run `python3 verify.py` from the directory containing these files. It reconstructs four sample three-cut complexes, independently counts their disconnected triples, enumerates all nonempty faces, computes reduced mod-two homology by sparse bit-column elimination, checks square edge-disjointness, and compares with the symbolic formula evaluated on each graph. It also compares the independent number of connected induced triples with the graph degree-count identity. The checks completed with `VERIFY_OK`.

The four tested cases have \((n,q,B)=(8,1,13),(8,2,9),(9,1,19),(8,1,9)\). Mod-two agreement does not establish integral torsion-freeness or an all-parameter homotopy theorem; those claims follow from the explicit integral elementary collapses, Alexander duality, and the connectivity argument in `RESULT.md`. No independent audit has been performed.
