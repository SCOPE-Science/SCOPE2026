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

The cap localization matrix is diagonal at the unperturbed cap; its eigenvalue gaps are positive binomial tail partial sums. Second-order perturbation of its simple top eigenvalue produces a negative boundary-integral diagonal term and positive couplings from Fourier modes j<=N, yielding explicit d_{N,j} and a plateau d=1 for j>N. Binomial consecutive ratios imply d_1=0<d_2<...<d_N<1 and the sharp minimum d_2=(2−p)/(2+(N−2)p). The N to infinity p=s/N limit uses binomial-to-Poisson convergence and dominated Fourier sums, not a uniform nonlinear remainder. Independent exact rational arithmetic across 45 (N,p) pairs, N=2..16 and p∈{1/4,1/2,3/4}, verified ordering, null mode and d_2 identity; source eigenmatrix checker inspected, not treated as proof.

## originality

PASS

Frank’s SU(2) coherent-state cap optimizer and García-Ferrero–Ortega-Cerdà’s polynomial stability inequalities concern the same concentration functional, but the inspected primary statements do not compute its full finite-N Fourier shape Hessian, strict mode ordering, or sharp second harmonic. Gaussian Fock-space quantitative results concern a limiting different space. The explicit binomial-tail finite-degree spectrum does not follow from the qualitative bounds without new calculation.

## value

PASS

Exact local sharp stability constants and null directions for optimized spin-coherent localization are natural spectral-geometric data. The full angular mode ordering establishes the least-stable nontranslation perturbations and a controlled finite-spin/Gaussian interpolation, a motivated nontrivial invariant for all N and cap areas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
