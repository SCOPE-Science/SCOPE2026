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

The exact graph, perfect matchings, reflection permutation and signed-chain orbit convention are defined in `RESULT.md` and implemented in `verify_reflections.py`. Run with Python 3 and the standard library:

```sh
python3 verify_reflections.py
```

Successful execution checks the exact pairwise conflict criterion through even width 14; complete maximal faces of the independently constructed flag graph through width 10; full reflection-orbit quotient identities, open-twin reductions and alternating character values through width 32; and eight independent signed fixed-face calculations from actual perfect-matching facets, with widths 4, 6, 8 and 10. The unbounded proof is the symbolic graph classification and triangular-chain recurrence, not the numerical samples. No independent audit or integral lattice classification is asserted.
