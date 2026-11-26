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

Independence of the Brownian driver gives a centered conditional Gaussian of variance 2A_t with A_t=∫₀ᵗD_s ds, hence μ²t²α(t)=Var(A_t)=2∫₀ᵗ(t−s)Cov(D_0,D_s)ds. Detailed balance diagonalizes the generator in the stationary inner product, and irreducibility removes the zero relaxation mode from the centered observable. Integrating each active covariance exponential gives exactly the stated K with K(0)=1. Conversely, for each designated mean share h_j and weight w_j, the binary probability p_j=h_j²/(h_j²+w_j) and step size a_j=(h_j²+w_j)/h_j give mean h_j and variance w_j. The two positive flip rates sum to λ_j and give a stationary reversible product chain of 2^m states. Subtracting the total mean shares from μ leaves a strictly positive baseline, with no ceiling required on state diffusivities. Independence makes all cross covariances zero, including when other product-generator eigenvalues collide with an active rate. Differentiating t²α(t) twice recovers the normalized covariance, and successive isolation of the smallest active rate proves uniqueness of the rates and normalized weights. Varying the h_j changes at least the minimum diffusivity while preserving the curve; the empty mixture is constant diffusivity and also admits different unobserved switching generators. In an independent exact replay at t=log 2, enumerate the 64 stationary state pairs for binary probabilities (1/4,1/8,1/16), steps (1/2,1,4), baseline 1/8, and rates (1,2,3), using P_j(b,c)=2^−λ_j 1_{b=c}+(1−2^−λ_j)π_j(c). This gives mean 5/8 and covariance 180355072/1073741824=43/256, as predicted by the three modes. The supplied verification/verify.py was located and inspected, not executed; it checks examples and evaluates covariance via the eigenbasis, not an independent matrix exponential or a proof of exhaustiveness.

## originality

PASS

The distinct supported claim is the converse realization for every finite positive spectrum and arbitrary fixed positive mean, with strict positive diffusivities and an explicit finite-state bound. The variance identity, forward spectral form, and uniqueness of a finite exponential sum are not originality claims in isolation. The closest inspected literature has real forward and spectral-design overlap; the two strongest inaccessible full texts leave specific priority risks, not negative evidence.

## value

PASS

The observable arises naturally when inferring switching diffusivity from displacement data; forward formulas alone leave open which spectra are physically feasible at a specified mean. The converse supplies an explicit positive realization even for arbitrarily large normalized weights, which a symmetric binary example cannot do. The simultaneous inverse classification and nonidentification distinguish which features of ideal kurtosis data can or cannot be inferred. The result does not claim minimal state counts, noisy-data identifiability, or full displacement-law realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
