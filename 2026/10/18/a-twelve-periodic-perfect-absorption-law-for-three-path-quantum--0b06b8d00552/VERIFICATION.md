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

# Reproducibility and mathematical verification

The proof first establishes the contraction-to-dark-subspace identity for the specified non-Hermitian adjacency Hamiltonian. It then derives the two exact endpoint equations for the three arms, applies the second-kind Chebyshev invariant, solves the resultant \((\lambda^2-1)(\lambda^2-3)=0\), excludes the spurious eigenvalues \(\lambda=\pm1\), and uses the trigonometric recurrence at \(\lambda=\pm\sqrt3\) to obtain the length congruence. In the exceptional class, two normalized source-visible dark vectors contribute \(1/(2m+1)\) each. No finite set of cases is used in lieu of the algebraic argument.

Run `python verification/check_theta.py` with the versions constrained in `verification/requirements.txt`. The checker performs 81 exact symbolic endpoint tests, 63 dense spectral-projection comparisons, 10 constructed-vector eigenvalue and normalization comparisons, and eight direct non-Hermitian exponential evaluations of the unabsorbed state at long finite time. Expected summary:

```
VERIFY_OK exact_length_cases=81 spectral_projectors=63 dark_eigenvectors=10 finite_time_dynamics=8 max_projector_error=2.91e-16
```

Floating-point results may differ slightly by linear-algebra implementation; explicit numerical tolerances are in the checker. The long-time computation uses finite time and does not certify asymptotic convergence rates. Its role is a consistency check, not independent review, proof of priority, or a replacement for the displayed proof. The exact symbolic tests cover finitely many lengths only, while the proof covers every integer \(m\ge3\).
