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

`verify.py` is an executable, standalone Python 3 checker and `computation.txt` records actual stdout. A finite-ambiguity graph test identifies cyclic components and rejects reachable pairs of distinct cyclic components. For every Boolean unary transition relation on two, three, or four labeled states, the checker exhaustively verifies the bounded-ambiguity candidates and computes the observed maximum of accepted walks through 30 steps. It compares the entire maximizing graph set with the theorem's normal forms for three and four states. For each size from three to ten it then generates every claimed labeled extremizer and verifies finite ambiguity and optimal accepted-run multiplicity.

The exhaustive checks through four states and the construction checks through ten states passed. The infinite upper bound, structural equality theorem, and uniform walk multiplicity are proved mathematically in `RESULT.md`; these finite computations are not offered as infinite certificates. The comparison with literature is same-model-only and does not constitute independent verification.
