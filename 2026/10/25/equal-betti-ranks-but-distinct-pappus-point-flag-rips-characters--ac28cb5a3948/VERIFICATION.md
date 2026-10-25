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

## Executed checks
The complete `verify.py` file was executed against NetworkX 3.6.1. It checked both full simplex lists, exact mod-two simplicial boundary ranks, the Pappus graph automorphism count of 216, all twelve order/side/trace rows, and the 27 cases of point-versus-flag character inequivalence. Its stdout is embedded separately in `verify.out`.

## Mathematical scope
The mod-two computations bound rational ranks from above, and the Euler characteristic fixes rational second rank; they do not rule out integral torsion. Signed Lefschetz sums on the finite complexes give exact rational homology characters because other reduced rational homology vanishes. Every listed outcome is reproducible by the provided executable; no external expert or independent validation is claimed.
