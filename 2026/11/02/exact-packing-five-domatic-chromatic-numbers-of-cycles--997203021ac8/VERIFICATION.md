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

Extract `witnesses.json` and `verify.py` into the same directory and run `python3 verify.py` with Python 3. The checker has no third-party dependencies.

Observed output:

```
BASE_WITNESSES_OK 35
EXHAUSTIVE_NEGATIVE_FOUR_PALETTE_OK 21186
ELEVEN_VERTEX_K6_OBSTRUCTION_OK 44
SPLICING_CONSTRUCTION_TEST_OK 191
VERIFY_OK
```

The first check reconstructs every cycle from its vertex count and verifies all packing constraints and all broadcast-layer coverage inequalities directly. The second enumerates every permissible four-palette packing word for the eight exceptional orders, with a complete cyclic wraparound check. The eleven-vertex obstruction derives six-cliques in the forced-distinct relation whenever all broadcasting-depth requirements pass. The last check constructs and directly checks 191 instances in the unbounded ten-step family; the all-orders conclusion additionally requires the nine-window splicing proof in `RESULT.md`, not finite extrapolation.

The explicit six-color lower bounds at the two smallest orders and the universal four-color lower bound are written mathematical arguments. Historical novelty remains subject to outside confirmation. Independent mathematical audit has not been performed.
