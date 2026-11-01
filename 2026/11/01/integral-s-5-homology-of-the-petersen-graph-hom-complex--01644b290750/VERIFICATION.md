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

Run `python3 verify.py` using Python 3 (standard library only). It independently constructs the Petersen graph as disjoint two-subsets, its twenty-vertex bipartite double cover, the entire 120-element \(S_5\) action, and all Hom cells. It checks the exact nerve intersection pattern and the predicted character \((11,-1,-1,-1,-1,1,1)\).

The proof uses elementary topology of a finite contractible-intersection cover, the integral graph chain complex, and the Pieri rule. The checker is finite because the stated theorem concerns this one fully specified graph; it does not certify an equivariant homotopy splitting or an integral irreducible decomposition. No independent audit has occurred.
