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

The exact theorem is proved by polynomial distance-algebra identities, the classical adjacency spectrum, a strict cubic upper bound, and uniqueness of the crossing of the only potentially positive nonconstant eigenvalue. No finite numerical calculation is used to prove an assertion about all real exponents.

The included `verify.py` requires Python, NetworkX and NumPy; run `python verify.py` from this directory. It reconstructs 36 vertices as the complement of two closed Hoffman--Singleton neighborhoods, verifies 90 edges and 1296 intersection relationships, compares exact integer distance-adjacency polynomial identities, tests five complete 36-by-36 powered-distance spectra, reconstructs all twelve size-six row/column maximal cliques of the distance-three rook graph, and checks ten linearly independent explicit row/column contrast eigenvectors. The printed success marker is `SYLVESTER_POWERED_DISTANCE_OK`.

At the computed endpoint the ten zero eigenvalues are verified numerically at tolerance \(10^{-9}\), while the exact ten-dimensional multiplicity follows from the analytic spectral decomposition. The numerical root is illustrative; the theorem defines the root uniquely and exactly.

The named graph's uniqueness and classical adjacency spectrum are accepted published inputs, separately cross-checked through explicit graph reconstruction. Independent mathematical audit has not been performed. The graph source's historic monograph reference has year-only bibliographic evidence and no fabricated day-specific initial date.
