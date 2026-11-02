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

# Verification and reproduction

Compile the included portable C++ source using `c++ -O2 -std=c++17 crown_check.cpp -o crown_check` and run `./crown_check`. The actual replay produced `VERIFY_OK exact_krylov_cases=5916` after exhaustively testing all nonempty vertex-absorber masks for crown graphs with \(n=3,4,5,6\), and 80 deterministic pseudorandom masks for each \(7\le n\le12\). The code forms the graph adjacency matrix independently and computes exact Krylov ranks modulo the prime \(1009\). For these particular small integers, the computed ranks agreed with the analytic real-field ranks; modular agreement alone would not prove a general characteristic-zero formula.

The optional `crown_numeric_audit.py` needs NumPy. It independently diagonalizes the real symmetric adjacency matrices, constructs the spectral spans of the marked-site projections, and checks sitewise diagonal bright-projector entries against the theorem. It returned `NUMERIC_OK checks=1357` for all nonempty patterns through \(n=5\) and selected masks through \(n=9\). Numerical tolerance is \(10^{-8}\), and no infinite proof is inferred from numerical checks.

The analytic certificate is the explicit eigenspace decomposition and rank/projection calculation in `RESULT.md`, with no reliance on a finite cutoff. Positive loss rates and a nonempty sink set are essential; coherent hopping is uniform and the quantum system is a single excitation. The result gives exact infinite-time capture only, not relaxation rates.
