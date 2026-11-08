---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: Richardson’s exact finite Chebyshev optimizer is a cited premise. Replacing x=cos(t/N) in S_n(x)=A_N T_N(a_N(x+1)-1)/(x-1), with theta=pi/(2N), gives N² A_N→pi/2, N²(x-1)→-t²/2, and Chebyshev phase→cos sqrt(t²+pi²/4). Markov derivative bound |T_N'|<=N² around removable x=1 and |T_N|<=1 away from 1 imply a uniform integrable C/(1+t²) bound on t∈[-pi N,pi N]. Dominated convergence gives L¹ convergence of rescaled symbols; Fourier inversion hence uniformly bounds all tap coefficients independent of k. Differentiating the Fourier-Bessel integral for J0 at a=1 yields a distributional identity for cos sqrt(t²+m²), including boundary delta masses; K'' gives the stated compactly supported inverse with mass F(0)=1. For m=pi/2, J1(m sqrt(1-s²))>0 from alternating series, so strict interior concavity, positivity and monotonicity follow. Independent quadrature of Khat at five frequencies and independent finite Chebyshev coefficients at n=8,16,32 give decreasing max discrepancies .002387,.000668,.000177. This corroborates but does not prove the all-n uniform limit.

## originality

PASS

PASS, qualified: Richardson 2023 supplies the EXACT finite optimizer Chebyshev formula, its norm and visual near-Epanechnikov comparison; these facts are credited and deliberately not claimed new. The inspected original arXiv paper does not give the Bessel continuum density, Fourier transform of the scaling limit or uniform all-index convergence. Kravitz–Steinerberger 2020 handles first differences and constrained positive Fourier second-difference smoothing; its triangle kernel is a different optimum. Related published exact radius-one smoothing records do not imply a continuum n→∞ profile. Residual risk of an earlier transform tabulation or unpublished analysis remains.

## value

PASS

PASS: The continuum shape of the unique wide optimal discrete averaging kernel is an intrinsic mathematical question about scaling a sharp Fourier variational problem. The exact nonparabolic Bessel density, strict concavity, and strong uniform convergence over every tap supply a reusable spatial characterization and distinguish the unconstrained optimum from familiar Epanechnikov and triangle kernels. Not just a low-radius numerical coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
