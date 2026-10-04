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

The proof in `RESULT.md` is symbolic and establishes the statement for every allowed pair of parameters. The executable checker is supplementary.

`verify_near_square.py` performs two finite checks using only the Python standard library:

1. It enumerates color-preserving isomorphism classes of bipartite graphs with no isolated vertices and exactly \(e\) edges for \(0\le e\le5\), recovering \((1,1,3,6,16,34)\).
2. It directly enumerates missing-edge orbits for the bouquet ranks \(9,8,7,13\), obtaining \(1,3,5,12\) homeomorphism classes.

The computation does not certify the infinite theorem by exhaustion. Its role is to check the first auxiliary counts, the orbit convention, and several concrete instances.
