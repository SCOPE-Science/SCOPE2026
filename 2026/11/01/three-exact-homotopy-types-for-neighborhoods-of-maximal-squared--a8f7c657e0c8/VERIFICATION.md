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

The included `verify.py` is a complete reproducible checker for all three finite cases. Run `python verify.py` with `sympy>=1.12` installed. It constructs every graph and face from the definitions rather than reading precomputed graph or complex files. Independent direct-distance and cyclic-gap enumerations agree. The checker verifies complete face vectors, exact matching cardinalities, a directed Hasse acyclicity topological sort, signed integral Morse boundaries, Smith normal forms over the integers, chain-square-zero identities, and reduced homology ranks.

Successful execution in the supplied environment:

```
VERIFY_OK k=2 n=8 vertices=12 faces=911 pairs=447 incidences=3700
VERIFY_OK critical={2: 9, 3: 8} smith={3: [1, 1, 1, 1, 1, 1, 1]} homology={2: 2, 3: 1} homotopy=S2veeS2veeS3
VERIFY_OK k=3 n=11 vertices=22 faces=16391 pairs=8182 incidences=89089
VERIFY_OK critical={2: 8, 3: 13, 4: 5, 5: 1} smith={3: [1, 1, 1, 1, 1, 1, 1, 1], 4: [1, 1, 1, 1], 5: [1]} homology={3: 1} homotopy=S3
VERIFY_OK k=4 n=14 vertices=35 faces=272861 pairs=136419 incidences=1913226
VERIFY_OK critical={1: 1, 2: 11, 3: 11} smith={2: [1], 3: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]} homology={3: 1} homotopy=S3
ALL_VERIFY_OK exact complete enumeration, Hasse acyclicity and integer Smith invariants
```

The `homotopy=` strings report the types derived in `RESULT.md` using the verified Morse data and standard cellular cancellation arguments. The checker independently establishes the finite chain and incidence data, but a code execution alone is not an independent audit of the topological arguments. The classification does not extend beyond the three stated parameters.
