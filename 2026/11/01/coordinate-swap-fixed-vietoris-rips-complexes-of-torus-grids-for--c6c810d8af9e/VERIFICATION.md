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

The orbit-barycenter construction is proved in RESULT.md. The main infinite-family step is the exact metric classification of admissible orbits and pairwise compatible orbits, after which the list of all triangles and the annular PL homeomorphism follow directly.

Run `python3 verify.py` using Python 3 without external libraries. It enumerates original torus-grid point pairs, swap orbits, admissibility and compatibility at scales one and two for each integer \(7\le n\le25\), and verifies every face up to size four. The expected face vector is \((n,0,0)\) at scale one and \((2n,4n,2n)\) at scale two, with no faces containing four vertices. No finite enumeration is represented as an all-size proof.

The integral homology is deduced from the explicit PL annulus model, without relying on rational rank computations. The source arXiv:2502.07134v1 was publicly available 2025-02-10. No external independent audit or scientific certification has been carried out.
