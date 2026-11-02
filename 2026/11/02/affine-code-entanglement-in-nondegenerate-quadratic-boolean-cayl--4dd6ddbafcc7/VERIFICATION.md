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

# Reproducible mathematical checks

Run `python verify_quadratic_cuts.py` with Python 3.9+ and NumPy. It constructs quadratic Cayley graphs directly from Boolean quadratic functions with randomly chosen invertible linear substitutions and optional linear terms; it computes binary cut ranks using bit-vector Gaussian elimination, independently predicts them by the restriction of the polar form, and checks eight exact small-graph spectra by preparing the entire sixteen-qubit graph state and tracing out the opposite qubits.

The recorded successful checker output was:

```text
exact_cut_ranks {4: 6336, 6: 2520, 8: 96}
direct_graph_state_spectra 8 max_abs_error 4.1633e-17 graph_degrees [6, 10]
PASS
```

The total \(8952\) binary-rank comparisons are exact calculations; the direct spectral diagonalizations use floating point with the reported maximum discrepancy. The checker covers all subspace directions and offsets for sampled quadratic forms in dimension four, randomized directions and offsets for dimensions six and eight, and both valence types in dimension four. These tests do not exhaust all ambient dimensions or all quadratic forms. Universal correctness depends on the explicit finite-field proof in `RESULT.md`, not the test counts.

The relevant literature-comparison risk is possible earlier specialized work on modular affine-cut ranks; this is not resolved by numerical checks. No independent audit has been performed.
