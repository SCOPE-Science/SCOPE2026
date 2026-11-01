---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The Gaussian first-column ratio T=c/a is standard Cauchy. Partial row pivoting maps it to R=T if |T|≤1, otherwise 1/T, giving density 2/(π(1+r²)) on (-1,1). The independent second-column Gaussians produce Z|R=r~N(0,1+r²); direct integration yields CF, all integer moments, variance and fourth moment; a Cauchy-square ratio makes unpivoted variance infinite. Numerical independent check sampled 200,000 matrices and separately computed exact second/fourth normalizers, agreeing within Monte Carlo variation.

## originality

PASS

Trefethen–Schreiber (1990) is the strongest historical comparison: its author-hosted complete primary PDF was read in the sections on pivot magnitudes, multiplier distribution and growth, and gives approximations for general n but does not establish the exact random last-pivot distribution or all even moments at n=2. Spielman–Yu (2026) and Gunawan–Peca-Medlin–Zhong (2026) address different random GEPP observables. The exact formula follows from standard Cauchy and Gaussian conditioning, which are prior tools, not novel. Possible earlier elementary n=2 distribution is residual risk.

## value

PASS

Finite-dimensional GEPP has a canonical final-pivot observable. Its complete exact moment sequence and the sharp finite-versus-infinite variance comparison quantify what row pivoting actually regularizes, a motivated benchmark not merely a renaming of standard normal/Cauchy facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
