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

The bundled `verify_dual_dowker.py` uses only the Python standard library. It enumerates every binary matrix for the required small sizes, rejects matrices with an empty or repeated row/column neighborhood, canonizes relations under all independent row/column permutations, and canonizes each Dowker complex under all vertex permutations.

For every total side size below six, each ordered dual-Dowker signature has exactly one relation class. At \(3\times3\), the verifier checks 174 labeled bi-twin-free matrices, eight relation-isomorphism classes, seven ordered dual-Dowker signatures, and exactly one signature fiber of size two. It also checks the two witness canonical strings, their distinct row-degree multisets, and that both components of the common signature are full \(2\)-simplices.

A successful replay prints `VERIFY_OK`. The computation is exhaustive only for the finite ranges stated; it is not used to infer behavior for larger relations.
