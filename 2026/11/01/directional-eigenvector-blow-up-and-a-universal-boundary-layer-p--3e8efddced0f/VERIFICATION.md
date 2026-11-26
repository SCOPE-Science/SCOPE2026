---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The recurrence fixes the eigenline. The proof writes its product only near the boundary; for existence on the whole radial path, the roots start inside at r=0 and cannot hit the unit circle there: on |u|=1, u+ρ/u parameterizes the boundary of the ellipse (an invertible real-linear image), whereas r(e^(−iθ)+ρe^(iθ)) is interior for r<1. Thus the ODE denominator is zero-free on the closed disk, including at interior repeated roots. Near r=1 the separated root gives 1−|u|∼κθ(1−r) and the singular exponent tends to γθ with an O(1−r) error. An independent normalization check: Fourier Plancherel in Y on the Laplace representation of (1+X+iY)^(−γ), followed by integration in X>0, gives integral πΓ(2s)/(2^(2s)|Γ(γ)|²) for the squared modulus. The rescaled disk exhausts the half-plane pointwise, the second factor tends to its boundary value, and the common integrable majorant in RESULT.md lines 118–134 justifies the mass limit and coefficient, uniformly in angle for the norm law. At c=0 the exact norm is (1−r²)^−1 and C=1/2, including the area normalization. Read VERIFICATION.md and check_boundary.py as evidence; did not execute the supplied script.

## originality

PASS

The affine-symbol eigenline and the ODE are known, as is the isolated singular-factor norm asymptotic. The supported distinct claim is the sharp angular law for the actual normalized eigenvectors and their complex half-plane mass profile, not the spectrum, eigenvector formula, or hypercyclicity.

## value

PASS

At a fixed natural normalization the eigenvectors approaching different points of the same spectral ellipse can diverge at genuinely different powers. The sharp range recovers the coefficient contrast, and the normalized profile describes the direction-dependent mass lost at the boundary. The result makes no claim that this implies a hypercyclicity or resolvent theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
