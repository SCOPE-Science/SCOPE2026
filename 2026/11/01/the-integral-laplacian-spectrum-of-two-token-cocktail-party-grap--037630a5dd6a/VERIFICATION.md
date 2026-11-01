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

The exact formula is proved by a complete invariant-space decomposition in RESULT.md. The proofs and programs refer to the same simple, unweighted, collision-free, two-token configuration graph on \(K_{2,\ldots,2}\).

To replay, run `python3 verify_numeric.py` (requires NumPy and SymPy) and `c++ -std=c++17 -O2 verify_modular.cpp -o verify_modular && ./verify_modular` in a directory containing those files.

The first method builds all allowable token steps and compares complete floating-point spectra to their *integer* predictions for \(2\le m\le9\), also checking exact reduced-Laplacian determinants for \(m=2,3,4\). The second independently constructs allowed exchanges, verifies exact nullities of \(L-\lambda I\) over two prime fields, and checks the spanning-tree identity modulo both primes for \(2\le m\le8\). Both separately test graph row sums and symmetry. Coincident theoretical eigenvalues are combined before comparison.

These tests are finite evidence and do not prove the infinite family by themselves. The all-parameter proof is the incidence/signed-square decomposition in RESULT.md; no external scholarly audit has been performed.
