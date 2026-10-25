---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

From the beta-binomial entry formula, exact gamma ratios give row squared mass S_n=C(a,b)^2[Gamma(n+1)/Gamma(n+a+b)]^2 sum_{k=0}^n [Gamma(k+a)/Gamma(k+1)]^2[Gamma(n-k+b)/Gamma(n-k+1)]^2. For m>1/2 the interior beta-integral convolution gives S_n~C^2 B(2a-1,2b-1)/n; at an endpoint m=1/2 harmonic divergence gives r C²(log n)/n; for m<1/2 endpoint dominance gives r C² U_m n^(-2m) with U_m=Gamma(m)^2 Gamma(1-2m)/Gamma(1-m)^2 via Gauss summation. Summation establishes three regimes. At a=.5+u/logN, b=.5+v/logN, uniformly bounded u,v, the proof estimates each row as C²/n[(1-n^(-delta_a))/delta_a+(1-n^(-delta_b))/delta_b]+O_R(1/n). Logarithmic harmonic integration yields (logN)^2/π²[Phi(u)+Phi(v)]+O_R(logN). The u=0 definition of Phi is continuous. Independent checks confirm exact Cesàro energy E_N(1,1)=H_N for N=100, exact gamma recurrence finite energies, and bounded crossover diagnostics; no extrapolation replaces the stated uniform estimates.

## originality

PASS

The underlying beta-binomial row law and Gauss hypergeometric summation are standard, but the fixed-shape HS-energy trichotomy and uniform jointly-moving beta-shape crossover are not implied by the cited urn approximation, Hardy operator norm, or generic Hausdorff inequalities.

## value

PASS

The Frobenius collision energy of natural finite beta-binomial/Hausdorff matrices has a sharp summability threshold and meaningful two-shape double-logarithmic crossover, beyond routine row normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
