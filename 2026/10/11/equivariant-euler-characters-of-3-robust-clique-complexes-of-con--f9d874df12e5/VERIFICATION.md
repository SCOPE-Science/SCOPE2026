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

# Verification
The standalone `verify.py` uses only the Python standard library and reconstructs graph automorphisms, complex faces, orientation signs, simple four-cycles, and the symmetric-square cycle-space traces independently of the proof presentation. Execute `python3 verify.py`; the program must report `VERIFY_OK` with 232 connected bipartite graphs, 858 automorphism-character comparisons, and the separately enumerated grid and cube actions. The computation is finite and does not certify the general theorem; the symbolic equivariant kernel argument in `RESULT.md` is the proof.

The four-cycle and adjacent-edge-pair module maps, virtual symmetric-square substitution, bipartiteness restriction, and the distinct nonconcentration caveat were examined directly. The literature search may miss equivalent unindexed sources. No independent audit has been performed.
