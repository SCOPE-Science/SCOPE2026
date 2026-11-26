---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The corotating directed circulant has real parts −Γℓ; Γℓ=Γ(N−ℓ), so the critical first mode includes its conjugate, and the zero mode is removed by the phase quotient. The continuum first-mode integral factors as sin(u)(1−cos u)(3cos²u−cos u−1)/3, with a simple interior zero on [20π/91,2π/9]. The displayed trigonometric formulas give uniformly positive integrals for modes 2–6 (in particular cos²(2π/9)>7/12 for mode 2); bounding the two sum frequencies ℓ±3 gives the positive continuum margin for ℓ≥7. For finite modes, Abel summation gives a bound N/ℓ on the weighted cosine term for ℓ≤N/2, whereas the unmodulated weight sum is >2m/5 uniformly for large m. This controls ℓ≥32, with fixed-mode uniform Riemann convergence controlling 2–31. The cos-sum identity gives the centered variable M=m+1/2 exactly; the cosecant expansion in C¹ gives G_m(n)/n=J(t)+t²E(t)/M²+O(M^−4), t=M/n, with uniform J'<0 near the limiting interval and opposite endpoint signs. Inversion gives the unique real zero κM+(E/J')/M+O(M^−3), where reduction by 3c²−c−1=0 recovers the stated negative A. Strict stability signs give nonlinear quotient attraction or instability for integer networks; nothing is inferred at equality or outside the interval. Independent geometric-sum bisection at m=100,236,536 gives M³-scaled residuals about −0.3811, −0.3811, −0.3804, with positive noncritical spectral margins at the neighboring integers. This is corroboration only. The frozen script and its recorded finite output were inspected, not executed.

## originality

PASS

The continuum threshold and finite Fourier criterion are credited to earlier coverage. The supported distinct result is the uniform all-mode finite-ring classification in the stated asymptotic window with both explicit centering and the M⁻¹ term; the closest finite and continuum sources were compared at their actual statements.

## value

PASS

Near the physical stability boundary, a half-neighbor correction is order one in the integer network size, and the inverse-centered-degree coefficient resolves the next displacement. The result turns an exact but mode-by-mode finite test and a continuum threshold into a uniform finite-network classification, including which conjugate Fourier pair is critical. This addresses a natural finite-versus-continuum discrepancy rather than assigning significance to a numerical refinement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
