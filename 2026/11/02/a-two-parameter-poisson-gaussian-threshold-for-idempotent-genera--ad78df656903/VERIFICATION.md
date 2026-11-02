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

# Computational checks and mathematical limits

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` in the folder containing this file. It independently multiplies elements of a finite Rees zero-matrix semigroup, starts from its literal nonzero idempotents and absorbing zero, and closes the set under products until no new element appears. For separate comparison it computes component sizes and cycle-gain ranks from a spanning forest, then checks the exact cardinality and full-generation event.

The four binary-group exhaustive censuses cover \((a,b,d)=(2,2,1),(2,2,2),(2,3,1),(2,3,2)\), with 81, 625, 729, and 15,625 possible zero/nonzero labelings. Their numbers of fully generated semigroups are 8, 0, 144, and 1536 respectively. Three independent prime-field dimension-one censuses cover \((a,b,p)=(2,2,3),(2,3,3),(2,2,5)\), with 256, 4096, and 1296 possible labelings. All seven exhaustive configurations passed. In particular, the full-support rank histograms agree with exact Gaussian finite-field rank counts; the verifier also checks disconnected supports and those with isolated index vertices.

The asymptotic normal/Poisson independence and threshold limit are proved analytically in `RESULT.md` and are not asserted to be established by these small censuses. This work has not undergone independent mathematical audit or independent priority verification.
