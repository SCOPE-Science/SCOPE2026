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

Install NumPy and run `python verify.py` in a directory containing this file and `verify.py`. The checker constructs Laplacians separately for each independently retained-edge subset, diagonalizes those matrices to form the associated unitary propagators, and builds the superoperator on vectorized matrices. It compares the limiting channel with matrix powers for connected paths, a cycle, and a star at two nonresonant step durations, verifies peripheral eigenvalue counts and modulus separation, and checks all three stroboscopic classes on the three-vertex path for multiple edge probabilities and finite iteration counts. A successful run prints `VERIFICATION_OK` and the number of assertion groups; observed result: 129.

Computational samples cannot establish convergence on arbitrarily large graphs or rule out additional resonant cases. The mathematical proof in `RESULT.md` uses exact commutants of edge transpositions, a weighted Hilbert--Schmidt variance identity, and the exact integer spectrum of the three-site path. Only the statement in `RESULT.md` is claimed. There is no independent audit.
