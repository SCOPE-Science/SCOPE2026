---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The source identifies KRR Φtilde_y:R^(dx+dy)→R^dy at equation (3), so equation (8) powers of Φtilde_y(z0) are undefined for dx>0; equation (7) and Appendix B equation (29) in fact use coupled predicted inputs. Under the explicitly stated natural teacher-forced interpretation, let h=1/m, true z_j=(jh,1) for x'=y,y'=0, target y≡1, Gaussian kernel k_h(z,z_j)=exp(-||z-z_j||²/h^10), ridge λ=h^5. True centers have distinct distance≥h and off-diagonal Gram bound O(m exp(-h^-8)), so K=I+o(h^r) for each r and α=(K+h^5 I)^-1 1=1+O(h^5)+o(h^r). Exactly Kα=1-h^5α yields uniform teacher-forced error O(h^5). On coupled rollout the first yhat1=1-h^5(1+o(1)) and first trapezoid xhat1=h-(h^6/2)(1+o(1)), so distance squared from true z1 equals h^10(1+o(1)) and its Gaussian self-kernel tends to e^-1. All other training kernels vanish super-polynomially, hence yhat2→e^-1. With stable degree-one interpolation and globally second-order Heun/trapezoidal resolved solver, 2h-xhat2=(h/2)(3-2yhat1-yhat2)∼(1-e^-1)h/2, not O(h²) as a naive teacher-forced theorem would give. This is a rigorous small-h family, not numerical extrapolation, and carefully excludes a stronger theorem assuming the actual coupled yhat error directly.

## originality

PASS

The elementary rollout-instability principle was known, but this explicit source-specific type defect and standard Gaussian-KRR counterexample to a natural repair of Theorem 2.1 were not covered by the inspected focal manuscript or earlier general work.

## value

PASS

PASS. It pinpoints the missing stability interface in a claimed convergence theorem for learned dynamical closures. A fully explicit Gaussian-KRR witness with a sharp rate gap is mathematically substantive because it separates true-orbit approximation from on-policy coupled dynamics, and it points to the exact additional hypothesis rather than merely issuing a qualitative warning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
