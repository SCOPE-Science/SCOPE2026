---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For the exact recurrence x[n+1]=-x[n]+G(x[floor(n/m)]) with even m>=2, each m-block alternates c and G(x[k])-c and returns to c; recursive stripping of least-significant odd base-m digits proves x[n]=Q_c^{t_m(n)}(c) for every n. The residue histogram has probability 2^(-r-1), giving TV convergence by uniform tail truncation even for unbounded Q-orbits. For linear G=delta*u, the explicit affine iterates give boundedness delta in [-1,1) union {2}, full-time p-moment threshold |delta|^p<2 or delta=2, critical BK/2 and supercritical geometric growth on m^K horizons. Positivity and m^K<=N<m^(K+1) yield full-time divergence; convergence below threshold requires bounded tails. These are all-index arguments, not numerical extrapolation.

## originality

PASS

The exact flip resonance supplies an even-block cancellation mechanism, nonlinear digit representation, full physical-time occupation TV convergence and sharp moment phase diagram. The closest 2026 pantograph manuscript studies the same broad family but its general sufficient stability statements and purely delayed nonlinear plateau analysis do not imply this critical nonhomogeneous law. No stronger covering digital-sequence formulation was established in inspected sources. Originality is best-of-knowledge, not historical certification.

## value

PASS

The bifurcation between pointwise unbounded trajectories, a geometric occupation law in total variation, and divergent time moments is a substantive intermittency classification for a naturally selected critical parameter line; it applies uniformly to arbitrary nonlinear feedback and all even reciprocal bases, not an arbitrary isolated numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
