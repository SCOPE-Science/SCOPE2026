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

# Reproducible mathematical checks

Run `python3 verify.py` using the Python standard library. The script constructs the categorical-product host directly by coordinatewise inequality. It independently enumerates all induced forbidden cliques and every maximum-sized candidate subset for \((q,n,t)=(3,2,3),(4,2,3),(4,2,4)\), obtaining the exact theorem-predicted families of sizes \(6,12,8\). It also enumerates all Boolean solutions to the full-transversal saturation equations for \((q,n,t)=(3,3,3),(4,2,3)\), obtaining respectively \(9\) and \(12\) solutions; the solutions agree exactly with the expected coordinate cylinders. A finite algebraic swap-identity check confirms the rearrangement employed in the proof.

Observed standard output, ending in `VERIFY_OK`:

```text
DIRECT_EXHAUSTIVE_OK 3 2 3 6 sets 6 forbidden cliques
DIRECT_EXHAUSTIVE_OK 4 2 3 12 sets 96 forbidden cliques
DIRECT_EXHAUSTIVE_OK 4 2 4 8 sets 24 forbidden cliques
TRANSVERSAL_EQUATIONS_OK 3 3 3 9 sets 36 independently generated transversals
TRANSVERSAL_EQUATIONS_OK 4 2 3 12 sets 24 independently generated transversals
SWAP_IDENTITY_OK 3 2
VERIFY_OK
```

The finite tests check only the stated small cases. The proof's infinite quantifiers are established by exact clique partitions, an explicit transversal swap, the diameter-two connectedness of the disagreement graph for \(q\ge3\), and Boolean additive rigidity; they are not conclusions drawn from finite enumeration. No independent validation is asserted.
