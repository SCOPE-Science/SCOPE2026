---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Q sigma=-alpha sigma, Q sigma²=beta-(alpha+beta)sigma² yield two- and ordered four-point correlations. Subtracting pair products gives connected velocity cumulant beta/(alpha+beta)² exp(-alpha(x+z))[alpha exp(-(alpha+beta)y)-2beta exp(-2alpha y)]. Integration over ordered gaps gives rational Laplace transform with H=t*(t exp(-alpha t))*exp(-(alpha+beta)t)*exp(-2alpha t). This strictly positive increasing kernel is log-concave by Prekopa; its analytic logarithmic derivative decreases strictly from infinity to zero (small-time t^5/120, large-time linear), proving all strict sign cases and unique crossing, not only limits. Independent 15x15 Feynman-Kac lift vs 6x6 convolution cascade tested 54 alpha/beta,v,t cases, including phi and 2 boundaries.

## originality

PASS

Best-of-knowledge comparison of exact mathematical implications, including stronger prior results and aliases. The reviewed additional conclusion is not established by the primary/public mathematical results actually inspected; stated access and historical risks are retained.

## value

PASS

A complete non-asymptotic kurtosis sign and one-crossing phase diagram for a natural three-state intermittent velocity model goes beyond diffusion and mean-square-displacement formulas, with a sharp golden-ratio boundary and a second threshold 2. The positive-kernel proof gives an interpretable analytic mechanism and a calculable crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
