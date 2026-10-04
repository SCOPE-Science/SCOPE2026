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

Run `python3 verify.py` beside `maxima.json`. The verifier uses only the Python standard library. It reconstructs every binary word of length six, every one-deletion descendant set, the complete compatibility graph, and all maximal cliques. It then checks the exact stored maximum-code list, the universal core, the descendant coverage histogram, the unique perfect maximum, and all reversal/complement orbits.

Expected terminal line:

`VERIFY_OK vertices=64 maximal_cliques=62707 maximum=10 labeled_maxima=9 core=4 perfect=1 coverage=26x1,28x3,30x4,32x1 orbits=1x3,2x3 group_size=4`

The computation is finite and exhaustive. No timeout, random sampling, probabilistic certificate, or external solver is used. The classification is limited to binary length six and one deletion; the symmetry check is limited to the declared four-element group.
