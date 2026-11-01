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

# Reproducibility and limits

Run both standard-library Python 3 scripts in the same extracted directory:

```
python3 verify_paley13_four_cut.py
python3 crosscheck_paley13_mod2.py
```

The first script reconstructs the ordinary four-cut complex from its exact graph definition, cross-checks a second face-enumeration method, verifies an explicit 3,484-pair acyclic matching by testing every one of 42,393 directed Hasse incidences, and checks all 78 signed affine Lefschetz traces. Its expected marker is `PALEY13_FOUR_CUT_MORSE_AFFINE_VERIFIED`.

The second, separately written script enumerates allowed simplices directly using four-subset connectivity in the complement. It reduces all simplicial boundary matrices over \(\mathbb F_2\). Its expected marker is `PALEY13_FOUR_CUT_MOD2_CROSSCHECK_OK` and it finds Betti vector \((1,0,0,0,0,0,25,0,0)\).

Both actual execution outputs accompany the scripts. The nonaugmented Hasse matching is verified by a complete topological sort, not by an unverified appeal to the order of the pivot steps. The acyclic matching, not the mod-two boundary ranks, proves the integral homotopy type. The rational character is determined by signed simplicial traces; no integral module isomorphism is claimed. No external or independent audit has been performed.
