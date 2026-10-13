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

# Reproducible verification of weighted-hypercube mixing

Run `python3 verify.py` with Python 3.10 or later and no third-party packages. Expected successful output:

```
VERIFY_OK exact_profiles=21 exact_entries=5124 integer_budget_profiles=3164 finite_window_modes=88 max_midpoint_error=7.772e-16
```

The program constructs the weighted cube's adjacency eigenvalue groups from all signed weights, builds each orthogonal spectral projector as an exact rational Walsh-character sum, and forms the projector Schur-square average. Independently it constructs the claimed signed-resonance Walsh eigenvalues, inversely transforms them to all matrix entries, and compares exact fractions. It checks ranks using exact elimination, row sums, and exact uniformity for 21 examples in dimensions one to five. It also enumerates all admissible positive integer tuples with budget no larger than \(2^d-1\), for dimensions one to five (3,164 profiles), and corroborates period integrals for 88 Walsh modes using independent midpoint quadrature. Executing the program from its **embedded file contents** is sufficient; no companion data files or external state are needed.

Finite tests do not prove the general theorem: signed-frequency averaging, Bézout's identity, the generating-polynomial budget induction, and the two-adic instantaneous criterion are proved analytically in `RESULT.md`. Finite-dimensional examples cannot exclude a hypothetical previously published equivalent theorem.
