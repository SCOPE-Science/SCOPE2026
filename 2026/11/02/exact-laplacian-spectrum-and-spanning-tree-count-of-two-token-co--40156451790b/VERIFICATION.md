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

The theorem is symbolic for every pair of integers \(m,n\ge3\), using a complete invariant-subspace decomposition of the combinatorial Laplacian. Its spanning-tree formula uses the exact matrix-tree theorem.

The direct Python test `verify_primary.py` generates all two-token configurations from the base biclique, constructs all legal moves, and compares exact characteristic polynomials as well as reduced-Laplacian determinants for five parameter pairs: \((3,3),(3,4),(3,5),(4,4),(4,5)\). It requires Python 3 and SymPy. Recorded output ends in `DIRECT_EXACT_CERTIFICATE_OK`.

The independently constructed C++17 test `verify_alt.cpp` enumerates each base edge and chooses a stationary third token, then checks predicted modular eigenvalue nullities and matrix-tree cofactors modulo \(1000000007\) on \((3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(5,6),(6,7)\). Recorded output ends in `ALTERNATE_CERTIFICATE_OK`. These modular checks can miss coincidences at the chosen prime; the primary exact computation does not rely on modular nullities.

Neither finite implementation alone proves any general statement. No independent scholarly audit has been performed.
