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

# Reproducible verification

Run `python verify.py` from the directory containing `quotient_models.json`. The program uses only Python's standard library. It builds the coned-square triangulation, identifies the full diagonal, enumerates group elements and all face-chain orbits, verifies uniqueness of simplex keys, and compares entire quotient face sets with the supplied certificate. It then checks each closed two-manifold link, connectedness, single boundary cycle and Euler characteristic, and replays the ordered elementary collapses by recomputing each free face's cofaces at that stage.

The recorded execution in `verification_output.txt` verifies the balanced representative with group order 16 and face vector (11,22,12), eight boundary edges and 22 collapses; and the unbalanced representative with group order 24 and face vector (19,42,24), twelve boundary edges and 42 collapses. Further runs at side sizes (3,3) and (3,4) match those quotient profiles. The terminal marker is `ALL_CHECKS_OK`. These finite checks support but do not replace the equality-pattern proof transferring the two orbit complexes to all side sizes at least two.

The source paper's first public posting date was verified on the arXiv record, rather than inferred from a later publication. The result remains subject to independent scientific validation and the risk of an equivalent unindexed source. No independent audit has been performed.
