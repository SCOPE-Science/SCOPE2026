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

Run `python verify.py` using Python 3 (standard library only) from the directory containing this file. Successful completion prints `VERIFY_OK`. The finite cases and raw results are:

```
n=2 |GL|=6 nontrivial=2 tau_centralizer=2 orbits=4
n=3 |GL|=168 nontrivial=24 tau_centralizer=8 orbits=33
n=4 |GL|=20160 nontrivial=1344 tau_centralizer=192 orbits=908
VERIFY_OK
```

The script enumerates complete binary matrices of orders two through four, performs binary Gaussian elimination to test invertibility, and directly checks every simultaneous permutation of row/column indices. It independently confirms the exact number of invertible matrices fixed by a selected transposition and the integer Burnside orbit counts. This enumeration does not establish any infinite-dimensional asymptotic. The limiting proof relies on explicit centralizer formulas, uniform codimension bounds, and a controlled pairwise-overlap estimate, given in `RESULT.md`.
