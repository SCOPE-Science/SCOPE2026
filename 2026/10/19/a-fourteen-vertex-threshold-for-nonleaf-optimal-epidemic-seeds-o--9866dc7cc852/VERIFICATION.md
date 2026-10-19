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

# Reproducible exact verification

Run `python3 verify.py` and `python3 crosscheck.py` with Python 3 standard library in the same directory. Both report success and use exact rational arithmetic.

The first program generates one canonical representative of each unlabeled tree up to order \(13\), using all leaf attachments from every representative, and compares every vertex score with the best leaf score. Counts at orders \(1\) through \(13\) are `1,1,1,2,3,6,11,23,47,106,235,551,1301`. The second program independently computes the witness scores as sums of all rooted simple-path-prefix probabilities (instead of directed-edge recursion), and asserts agreement with the first method at all \(14\) vertices.

The witness maximum is \(49/16\) at internal vertex \(0\); the largest leaf value is \(1763/576\), giving strict difference \(1/576\). The finite lower bound depends on the completeness of the tree-generation and canonicalization arguments given in `RESULT.md`; a successful run without that argument would not prove exhaustiveness. No independent external audit or infinite-order classification is claimed.
