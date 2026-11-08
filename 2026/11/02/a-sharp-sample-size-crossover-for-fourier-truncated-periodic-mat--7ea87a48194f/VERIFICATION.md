---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Let e=k-k_m and D=e(0)=T_m/Z, V=integral e(x)^2 dx=S_m/Z^2. Haar orthogonality gives exact E F=N D^2+N(N-1)V. For distinct unordered (i,j), squared offdiagonal terms sharing an index have zero covariance conditional on that shared point by translation invariance. Thus Var F=2N(N-1)(integral e^4-V^2)<=2N(N-1)D^2 V and rel Var <=2q/[N(1+q)^2]<=1/(2N), q=(N-1)V/D^2. Bounded N sequences concentrate because q=O(N m^-d), unbounded N via Chebyshev; full arbitrary oscillating N(m) follows. Lattice-tail Riemann sums yield T~t m^-2nu, S~s m^-(4nu+d), hence crossover N~m^d and ratio s/t^2=1/6 for d1,nu=.5.

## originality

PASS

Barnett–Greengard–Rachh study nonperiodic equispaced Fourier-grid kernel approximation with an N^2 Frobenius-error heuristic and a conjectured improved spectral convergence. That work does not state the exact periodic Fourier-truncation iid Haar Gram-tail mean, uniform sample-size concentration and finite diagonal/offdiagonal crossover. Periodic Matérn sampling theory covers a related underlying spectral construction but not this same random Gram-matrix statistic.

## value

PASS

The phase transition precisely diagnoses when diagonal spectral truncation bias dominates and when randomly sampled offdiagonal entry variance dominates. It gives exact constants and uniform sample-size convergence for a natural covariance approximation model, clarifying a known heuristic; the underlying Parseval/U-statistic ingredients are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
