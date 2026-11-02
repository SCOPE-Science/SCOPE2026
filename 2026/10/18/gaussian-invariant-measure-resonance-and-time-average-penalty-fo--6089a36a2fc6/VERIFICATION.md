---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Reconstructed the displayed SRK-I and SRK-II stage equations against Ye 2026 §2.2, and independently substituted the affine gradient K(x-m). Both give exactly e_{k+1}=(I-hK+h²K²/2)e_k+sqrt(2)(Delta B_k-K J_k) pathwise for any real symmetric quadratic K and shared Brownian pairs. The Gaussian covariance of (Delta B,J) is [[h,h²/2],[h²/2,h³/3]]⊗I, giving Q=2h(I-hK+h²K²/3), strictly positive in every eigendirection. For SPD K, r(z)=1-z+z²/2∈(0,1) iff 0<z<2, so a unique invariant law exists iff 0<h lambda_max(K)<2; if an r>=1 eigenmode exists, the positive Gaussian noise yields no invariant probability by the characteristic-function iteration. Scalar Lyapunov balance gives Sigma_h=K^{-1}f(hK), f=(1-z+z²/3)/(1-z+z²/2-z³/8). Its exact defect is z²(3z-4)/(24(1-z+z²/2-z³/8)), with denominator positive on 0<z<2 and sole positive zero 4/3. For all eigenmodes to match K^{-1} requires K=lambda I, h=4/(3lambda). At this step r=5/9 and stationary covariance 1/lambda, giving lim_(N→∞)(Nh) Var(N^-1 Σ Z_k)=14/(3lambda²) versus 2/lambda² for the continuous-time OU integral, ratio 7/3. Independently constructed a separate SymPy stage/noise/variance identity script (not copied from verify.py) and checked all these polynomial identities, Brownian covariance multiplication, stability boundary and long-run ratio exactly; independently reconstructed the seven-blob Git tree SHA-1 557c09b938395d675525e9e6dab13e776d74369b. Finite stage examples are corroboration, while universal claims follow from the algebra and spectral decomposition.

## originality

PASS

Best-of-knowledge novel exact Gaussian benchmark for the specifically defined 2026 SRK-I and SRK-II maps: their pathwise coincidence for every real quadratic drift, precise 0<h*lambda_max<2 stationary-existence criterion for SPD curvature, rational spectral covariance defect with sole positive root 4/3, isotropic-only simultaneous invariant exactness, and exact physical-time asymptotic variance ratio 7/3 at resonance. Ye 2026 supplies the exact two schemes and a small-step O((Nh)^(-1)+h^4) MSE theorem; Yang–Wang 2026 supplies coefficients and general W2 bounds; Li et al 2019 uses a different three-gradient SRK-LD map. Neither the actually read main theorem/method sections nor the compared Resultary records establishes this combined fixed-h Gaussian classification. Logical deduction from prior scheme definitions plus standard Lyapunov/AR(1) formulas is acknowledged; the exact joint classification and nonzero root are not themselves among the cited prior results. Earlier unindexed special-case calculations remain a residual priority risk.

## value

PASS

The two stochastic Runge–Kutta samplers are concrete modern algorithms with distinct gradient-stage budgets. Their exact coincidence on Gaussian targets is a useful caution for benchmarking; the sharp nonzero stationarity resonance and anisotropic obstruction separate target marginal accuracy from step-size stability. At the sole isotropic exactness step the physical-time average variance is 7/3 of the continuous OU coefficient, a nontrivial quantitative demonstration that an exact invariant marginal need not make time averages efficient. Even comparing against the exact OU sampled on the same mesh gives a strictly larger penalty (numerically 4.6667 vs 2.2879 in units lambda^-2). The theorem is a motivated exact benchmark, not only a textbook AR identity or an arbitrary numerical slice; its limitation to quadratic fixed-step algorithms and unequal-work comparison is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
