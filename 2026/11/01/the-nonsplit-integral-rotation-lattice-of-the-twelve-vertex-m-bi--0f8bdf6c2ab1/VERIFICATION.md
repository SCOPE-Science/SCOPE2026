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

Run `python3 verify_mobius12.py`. The program uses only Python's standard library and performs exhaustive exact finite linear algebra on the specified twelve-vertex simplicial complex. Expected printed status: `VERIFY_OK`. It reports face counts \((12,48,76,48,12)\), binary boundary ranks \((11,37,36,12)\), three explicit octahedral homology generators, rotation columns \((3,5,1)\), mod-two nilpotent ranks \((2,1,0)\), and the repeating characteristic-zero signed Lefschetz trace pattern \((3,-1,-1,-1)\).

The program establishes all characteristic-two finite-chain claims and the signed face traces by complete enumeration. The integral rank and homology concentration are taken from the cited published nonequivariant theorem; the integral extension classification follows from the written algebraic argument. The program is not a substitute for an independent mathematical review. No claim about other ladder sizes is deduced from these computations.
