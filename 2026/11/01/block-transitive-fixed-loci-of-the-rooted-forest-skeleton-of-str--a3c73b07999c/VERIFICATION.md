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

# Reproduction and scientific boundaries

Run `python verify_block_fixed_forests.py` using Python 3 (standard library only). The program enumerates directed-arrow orbits and independently checks rooted-forest admissibility, comparing actual group-orbit simplices with the predicted join-face criterion for cyclic and full symmetric transitive block actions. The completed execution reported 490 classified edge orbits, 142,870 exhaustive face-subset checks and 46 finite action cases, with every comparison passing. To reproduce, run it alongside the other supplied files without external data.

The infinite-family proof is mathematical, not computational: transitivity and independence classify all directed-edge orbits, and the classical directed-tree homotopy theorem applies to the fixed-label part. The finite enumeration cannot prove the arbitrary-size assertion and is not presented as such. The statement is about geometric fixed points of the canonical vertex-edge-pair subcomplex, not the full strong Morse complex; no equivariant collapse for that larger complex is assumed. Independent audit has not been performed.
