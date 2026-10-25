---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For fixed finite-dimensional symmetric positive semidefinite H1,H2, T>0, h=T/(2N), M=(R2R1+R1R2)/2 and D=(R1R2−R2R1)/2, the exact expansion is M−exp(−2hA)=h²Q/2+O(h³), D=h²[H1,H2]/2+O(h³). Telescoping the mean gives (EX_N−u(T))/h→(1/4)∫exp(−(T−s)A)Q u(s)ds. The centered recursion is an orthogonal martingale array whose replacement error has L² order h^(5/2); its scaled covariance is a 2h-mesh Riemann sum converging to K=(1/8)∫exp(−(T−s)A)J u(s)u(s)^T J^T exp(−(T−s)A)ds. The bounded normalized summands establish multivariate Lindeberg; the independent-with-replacement control uses h-sized half-difference and yields h^(−1/2) with coefficient 1/4. A nonzero 2×2 skew J is invertible, ensuring positive trace K for u0≠0; commuting H1,H2 give exactly identical block products. The total uncentered error remains O(h), not O(h^(3/2)). Independent NumPy/SciPy recreation for source positive-definite H1,H2 gave trace K=0.023058504869619058, trace Kiid=0.06185138964147487, mean-bias vector [0.31950664,0.58462062]; paired covariance trace ratios at N=10,80,400 were 0.82465,0.97552,0.99506. These finite values corroborate, not prove, the CLT.

## originality

PASS

The explicit centered commutator Gaussian law for randomized *order* of a two-resolvent balanced macrostep and its same-cost covariance comparison are more specific than known randomized splitting convergence bounds or random unitary product concentration; no directly implying theorem was found in the materially read sources. This is a best-of-knowledge assessment.

## value

PASS

Pairwise without-replacement balancing is a natural variance-reduction mechanism in numerical operator splitting. The exact h^(3/2) commutator noise, sharp 2D criterion, and contrasting iid h^(1/2) noise provide a quantitative diagnostic and clean benchmark beyond an arbitrary small-dimensional calculation; deterministic bias is carefully separated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
