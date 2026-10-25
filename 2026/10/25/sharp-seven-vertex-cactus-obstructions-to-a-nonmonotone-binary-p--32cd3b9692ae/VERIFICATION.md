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

Run `python3 verify.py` with Python 3.9+; standard library only. The program reconstructs each graph from its exact edge set, tests exact adjacency and integer action profiles, checks the two explicit obstruction types, and exhausts all connected cacti on up to seven vertices. On successful completion it reports 6,075 connected labelled cacti through six vertices, and 111,982 seven-vertex cacti including 3,150 labelled failures in two isomorphism classes. It verifies a finite classification, not the analytical unrestricted-order lemma or novelty relative to inaccessible literature. No independent audit has been performed.
