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

From v2=(A^−1−mI)v1/nu, exactly Av2=(v1−m Av1)/nu. Orthogonal projection residuals onto span{v1,v2} are proportional, so squared local mixed/split indicator ratio =m² s/(1−2mt+m²s), where m=E λ^−1, t=E λ, s=E λ² of the unit spectral measure. Define T=(2mt−1)/(m²s). Variation under a point mass uses φ(λ)=T_m/λ+T_t λ+T_s λ²; T_m≤0,T_s<0 make φ strictly concave, forcing a global minimizing measure for T to the spectral endpoints of [1,κ]. For endpoint weight p, γ^−2=Qκ(p), with unique maximum at positive cubic root by Descartes. Two-point maximizer breaks the third step; three-active-eigenvalue measures approach the infimum strictly. Checked exact symbolic derivative ∂p Q=Pκ(p)*κ(κ−1)²/[(1+(κ−1)p)^3(κ²−(κ²−1)p)^2], transformed positive cubic, and numerical Γ2=2.8835477563561254, Γ10=1.1597773406453498; all agree. Domain n≥3 SPD with at least three active distinct eigenvalues, cond≤κ and k=3 only. Neither actual floating point error nor later steps are bounded.

## originality

PASS

Qualified PASS for the sharp best-possible condition-dependent infimum on the local third-step mixed/split indicator and its endpoint/cubic extremizer, distinguishing it from Lund–Schweitzer 2026 qualitative positive-definite strict inequality. Spectral endpoint moment techniques are classical and credited.

## value

PASS

PASS: sharp condition-dependent separation improves an existing qualitative stability indicator for two practically studied extended-Krylov bases, identifies the limiting worst spectral geometry and reveals diverging ratio as the matrix approaches a scalar. This structural exact bound is motivated by real algorithm choice and does not overclaim floating point accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
