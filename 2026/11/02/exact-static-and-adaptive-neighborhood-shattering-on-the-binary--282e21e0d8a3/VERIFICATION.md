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

The local certificate consists of `grassmann35_cert.json`, `verify_grassmann35.py`, and its exact output `verification_stdout.txt`. The checker reconstructs all binary rank-two subspaces of \(\mathbb F_2^4\), rebuilds graph adjacency, verifies a four-query support with all sixteen label patterns, inspects every five-query support, and checks all 32 leaves of an explicit depth-five decision tree. The graph has 35 distinct concepts, so the depth-six obstruction is immediate from the required 64 distinct leaf witnesses.

Observed program output:

```
VC_LOWER_CERTIFICATE_PASS 4 support=0,1,3,7
FOUR_SUPPORT_CENSUS_PASS 41160
VC_UPPER_EXHAUSTIVE_PASS 324632
LITTLESTONE_DEPTH_FIVE_CERTIFICATE_PASS 31 nodes 32 leaves
LITTLESTONE_DEPTH_SIX_CARDINALITY_OBSTRUCTION_PASS 35<64
BINARY_GRASSMANN_35_ALL_CHECKS_PASS
```

Finite enumeration verifies the finite claim only; no higher-dimensional dimension formula, proof-assistant certification, external replication, or independent audit is asserted.
