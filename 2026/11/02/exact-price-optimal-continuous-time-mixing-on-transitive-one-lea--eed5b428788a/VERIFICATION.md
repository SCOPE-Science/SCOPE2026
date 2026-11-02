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

# Reproducible checks

The standalone `verify.py` requires only Python's standard library. Running `python3 verify.py` on the packaged file returned exactly `PASS: 1549 exact and independent spectral/budget checks`.

Its deterministic checks include 741 exact rational parameter identities; independently assembled continuous-time weighted Laplacians and Jacobi eigenvalues for every tested cycle size from 3 through 11, with four cost regimes and multiple randomized nonuniform allocations; spectral and budget checks for complete cores and the three-dimensional cube; and the three leading large-cycle asymptotics. Every finite computation is supplementary to the general analytic theorem: no finite range proves an infinite-parameter result. The script does not test independent publication priority or any nonuniform uniqueness on noncyclic cores.
