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

# Reproduction

With Python 3 and SymPy available, run `python3 verify_primary.py`. Compile the independent C++17 check using `g++ -O2 -std=c++17 -o verify_secondary verify_secondary.cpp`, then run `./verify_secondary`.

The Python program directly constructs all spanning trees of \(K_{2,n}\) as edge sets, generates each allowed four-cycle-supported one-edge swap, and exhaustively checks pairwise distances, spheres, diameter, and Wiener index for \(2\le n\le5\). It uses exact SymPy matrices to check every Laplacian eigenvalue and its multiplicity for \(2\le n\le4\), and exact integer Laplacian cofactors for \(n=2,3\).

The C++ program independently enumerates wildcard-word configurations, constructs the exchange graph through its proved local rule, and checks all-pairs distances, spheres, and Wiener indices for \(2\le n\le7\). The local rule follows from the square-cycle enumeration in the mathematical proof; the Python program separately checks that rule directly against actual edge subsets.

These finite tests cannot prove infinitely many parameter cases. The all-parameter proof is given in `RESULT.md`, including a sharp distance lower bound, Walsh invariant-subspace decomposition, and application of the matrix-tree theorem. Independent scholarly audit has not been performed.
