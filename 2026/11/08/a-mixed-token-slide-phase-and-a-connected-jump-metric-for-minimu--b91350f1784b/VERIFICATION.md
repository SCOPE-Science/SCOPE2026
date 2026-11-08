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

# Reproduction

Use `node direct_check.js` and `node cycle_check.js` from the folder containing the four evidence files. No third-party libraries or external datasets are required. The scripts independently generate the graphs, minimum decycling sets, token-slide and token-jump transition graphs, connected components and all-sources distances.

The first script checks all candidates with a union-find forest test; the second generates simple cycles and tests the defining cycle-hitting property. They independently prove the finite enumeration and move counts by exhaustive search, not random sampling. The expected final markers are `DIRECT_CHECK_PASS` and `CYCLE_CHECK_PASS`; all detailed counts are in the paired output text files. The proof of the four-vertex lower bound and of the induced-tree property is given in `RESULT.md`.

The verified parameter range is \(n=5,6,7\) only. Only the fourteen-vertex \(GP(7,2)\) has asserted jump radius and diameter. Full scholarly and historical-priority reviews have not been performed.
