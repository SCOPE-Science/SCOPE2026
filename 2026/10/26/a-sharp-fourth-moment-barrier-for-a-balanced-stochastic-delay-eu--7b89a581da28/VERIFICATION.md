---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Re-derived the 3×3 second-moment recurrence and stationarity equations yielding T=S/2 and S=1/(2/3−u); irreducible nonnegative moment map crosses spectral radius one at u=2/3. Independently reconstructed the 5×5 Gaussian Wick fourth-moment map K_4(u) for all degree-four mixed monomials; exact symbolic determinant equals Q(u)/19683 and solving (I−K)m=f with f=(0,0,S,3S/2,6S−3) gives m4=27R/[(2−3u)Q]. Transform u=(2/3)t/(1+t) yields −2(901t^4+10549t^3+5667t²−12929t−7004), having exactly one positive root by Descartes, with opposite rational signs at u=1/3 and 7/20. Positivity/irreducibility of K_4 and increasing Perron radius give finite fourth moments only below the crossing; for u>=u4 while u<2/3, the positive left eigenvector and finite-past conditional-Jensen construction force infinite fourth moment rather than merely a singular matrix. The positive simple Perron crossing makes Q' negative at u4 and gives simple-pole divergence. The independent symbolic check matched the exact determinant, resolvent and polynomial transform; the initial unexpanded SymPy expression equality failure was a simplification artifact and vanished after computing the zero difference.

## originality

PASS

The second-moment stability, random-coefficient autoregressive stationarity and spectral moment approach are prior theory. The candidate new result is the explicitly determined fourth-moment algebraic threshold and exact stationary fourth-moment rational function for the balanced Gaussian lag-one Euler benchmark. The highly relevant Truquet–Yao primary paper is now read in lawful full text and gives general moment existence machinery, not this special closed form.

## value

PASS

A balanced, contractive yet randomly forced stochastic-delay Euler benchmark has a substantial parameter interval with finite variance and infinite fourth moment, directly relevant to stability diagnostics, kurtosis estimates and high-moment numerical-analysis assumptions. The exact cutoff Q(u), full rational stationary moment and divergence constant go beyond known second-moment stability checks and give a reproducible sharply located stress test; this is a motivated benchmark rather than an arbitrary tiny parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
