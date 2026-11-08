---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Disk Toeplitz eigenvalues are λ_n=1−e^(−x)Σ_{j=0}^n x^j/j! with a strict gap between the top-2 cluster and complement. Differentiating exact squared-radius monomial moments yields the V,W entries, and trace-norm smoothness follows from integrating coherent-state projectors at positive radius. The contour/resolvent isolated-cluster formula has the correct n=0,1 to m>=2 couplings, producing two positive Poisson ratios plus boundary term −x e^(−x)|hhat_k|². The k=1 cancellation matches translations, and falling-factorial denominators strictly increase in k. Independent numerical rational/symbolic evaluations at x=.2,1,3,25 confirmed H2 and monotone coefficient ordering; the submitted matrix quadrature code was inspected but not trusted as proof.

## originality

PASS

Abreu 2026 establishes global disk maximality for arbitrary measurable sets and all Ky Fan ranks, so even the sign of a second derivative is covered qualitatively. The inspected full primary proof does not supply the rank-two nonradial Fourier mode coefficients H_k, their strict order or sharp quadrupole constant. Nicola–Riccardi–Tilli radial inequality and existence papers likewise are not proven to imply these exact local coefficients. A related quantitative expansion in incompletely accessible 2026 work remains an explicit priority risk.

## value

PASS

The exact nonradial rank-two quadratic stability spectrum is the natural local refinement of global Fock isoperimetry: it identifies the only symmetry kernel, all mode-specific costs and the least stable elliptic perturbations rather than merely repeating disk optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
