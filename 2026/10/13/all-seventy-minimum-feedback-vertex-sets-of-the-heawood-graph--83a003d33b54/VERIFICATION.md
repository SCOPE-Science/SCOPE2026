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

# Reproduction and limits

Run `python3 verify.py` with Python 3.9 or newer; it uses only the standard library. It independently builds the Fano plane as the seven nonzero three-bit vectors and the seven triples of zero vector-sum, then constructs the fourteen-vertex incidence graph. Exactly \(16{,}384\) subsets are visited. Every acyclic complement left by at most four deletions is checked to be a connected ten-vertex tree arising from one of the two structural types; conversely every predicted type is verified. All seventy optima and both induced degree signatures are checked.

The verifier also constructs \(168\) invertible maps on three binary coordinates, adds a verified point-line polarity, checks the resulting \(336\) maps preserve every neighborhood, and calculates the two optimizer orbits of sizes \(14\) and \(56\).

Expected terminal output:

```
VERIFY_OK vertices=14 edges=21 masks=16384 optimum=4 minimum_sets=70
VERIFY_OK orbit_types=A:14,B:56 group_order=336 tree_degrees=A:(1^6,3^4),B:(1^3,2^6,3^1)
```

The general proof for the fixed Heawood graph uses the forest edge identity and the Fano incidence axioms, not empirical inference. No claim is made for different incidence graphs or arbitrary graph order. Scientific priority remains subject to independently inspecting unavailable related literature; external mathematical validation was not performed.
