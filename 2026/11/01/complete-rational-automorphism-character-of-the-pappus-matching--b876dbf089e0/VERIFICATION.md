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

# Verification of the Pappus automorphism character

The two exact, executable witnesses in this package are `verify_pappus_mod2.py` and `verify_pappus_character.py`. Run each with Python 3.9+; no optional libraries, network connections, or outside certificates are used.

The first exhaustively reconstructs all 35,368 graph-edge matchings, computes every augmented simplicial boundary matrix by elimination over \(\mathbb F_2\), and checks ranks \((1,26,271,1448,4195,6362,4335,984,42)\). This verifies rational homology concentration using universal coefficients together with the exact Euler characteristic, **not** by assuming mod-two ranks equal rational ranks.

The second completely enumerates the 216 adjacency-preserving vertex permutations. Each character value is independently obtained from (i) a direct signed trace on *all* fixed matching simplices and (ii) an edge-orbit independence sum. All 216 comparisons pass. The full character-value distribution is \(40:1,4:32,1:12,0:81,-1:36,-2:36,-4:18\), and its weighted sum is zero. The machine-readable stdout witnesses are supplied as `verification_character.log` and `verification_mod2.log`.

No external validation, integral lattice decomposition, or contractibility assertion is included. The finite computations verify only this exactly defined 18-vertex graph.
