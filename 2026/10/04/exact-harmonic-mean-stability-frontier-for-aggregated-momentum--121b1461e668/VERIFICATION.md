---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Diagonalizing the positive-definite Hessian reduces AggMo to independent scalar curvature modes with \(s=\gamma\lambda\). Eliminating the buffer coordinates gives the exact characteristic equation \(z-1+(sz/K)\sum_i(z-\beta_i)^{-1}=0\), with the polynomial form retaining repeated damping coefficients. For a nonreal unit-circle candidate \(z=e^{i\theta}\), the imaginary part of \((1-z)\overline{H(z)}\) equals \(-\sin\theta\sum_i(1-\beta_i)/(1-2\beta_i\cos\theta+\beta_i^2)\), so no such crossing exists for positive \(s\). The root at one moves inward for small positive \(s\); the only possible boundary is therefore \(z=-1\), which gives \(s_\star=2K/\sum_i(1+\beta_i)^{-1}\). The sign of the monic polynomial at minus one excludes Schur stability above the boundary. Independent numerical root reconstruction for representative damping vectors found all roots inside at \(0.99s_\star\), a root at minus one at the boundary, and a root outside at \(1.01s_\star\), matching the exact proof. Applying the scalar condition to every Hessian eigenvalue yields the iff condition \(0<\gamma L<s_\star\).

## originality

PASS

The defining AggMo paper was inspected at the exact update, quadratic state-space analysis, default damping vectors and its discussion of open spectral questions. It analyzes quadratic convergence numerically/structurally but does not give the all-damping-vector harmonic-mean Schur frontier. Fresh Resultary searches for AggMo, exact quadratic stability, harmonic mean, Schur boundary and damping coefficients returned no equivalent published theorem. The later QHM/AggMo comparison concerns algorithmic equivalence of extended variants rather than the original equal-weight outer Schur boundary. The audited unit-circle exclusion and minus-one crossing therefore supply a genuine closed-form piece of the spectral problem rather than substituting parameters into a known formula.

## value

PASS

The exact outer stability limit is a basic property of a published optimizer whose motivation is passive damping, and the original work itself leaves closed spectral analysis as a theoretical direction. The harmonic-mean law cleanly separates absolute stability from interior damping benefits, gives immediate bounds and a limit for the proposed geometric damping family, and is useful for safe step-size design. This is a motivated structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
