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

The proof is symbolic and applies to every finite connected complete multipartite graph.

The accompanying `verify.py` independently builds each nondecreasing complete-multipartite profile of order \(2\) through \(9\). For every subset it checks the literal three-part definition: domination, connectivity of the selected induced subgraph, and connectivity of the complementary induced subgraph. It then compares that result with the stated profile criterion.

The same replay also compares the exact cardinality distribution with the closed polynomial formula. The checked range comprises \(87\) graph profiles and \(22{,}932\) vertex subsets.

The computation is a finite implementation check only. It does not certify the theorem beyond order \(9\), and no infinite conclusion is inferred from enumeration. The infinite claim rests on the proof in `RESULT.md`.

Bibliographic limits are separate from mathematical verification: the 2019 polynomial paper was available only through abstract/metadata during this check, so its unobserved full text remains an originality risk recorded in `AUDIT.json`.
