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

At stationarity the age is Exp(r); conditional on it the coordinates are IID normal with variance (D/μ)(1−e^{−2μT}). Thus Y=e^{−2μT} has CDF y^θ, and the exact count is the binomial mixture with q(y)=erf(A/√(1−y)). The conditional strong law gives H=q(Y); inversion and q(y)=p*+By+O(y²) give the stated CDF and lower density. For the rounded count set y=z/(B√N). The triangular binomial CLT gives Φ((x−z)/s*); flooring changes the CLT scale by O(N^{-1/2}). For small y, q(y)−p*≥By/2 gives an integrable Hoeffding bound exp(−2(z/2−x)²) for z>max(2x,0); for y bounded away from zero the contribution is exponentially small even after multiplication by N^{θ/2}. The limiting integral at x=0 equals (s*/B)^θ times the θ moment of the positive part of a standard normal, giving the stated gamma factor. At the other endpoint erfc(w)~e^{−w²}/(√πw) gives P(1−H≤u)~θA²/log(1/u). Bounding E[H^N] at 1−H=N^{−1±ε} and then letting ε→0 establishes θA²/log N, with θA²=ra²/(4D). All constants are for fixed positive parameters: p* is a floor only for the limiting fraction, not for the finite count. The frozen verification materials were read only; no numerical evidence is needed for these limits.

## originality

PASS

Pass attaches to the central-window counting result with its resolved lower-edge finite-population profile and comparison of the two count edges, not to the established conditional mixture or a standalone claim of priority for the upper logarithmic coefficient. The latter is closely covered by same-model maximum asymptotics; the inspected sources do not resolve the lower counting crossover at a positive occupation floor.

## value

PASS

Central-window counting probes an occupation fraction rather than the largest coordinate. The full Gaussian rounding profile at its equilibrium floor quantifies a natural sharp phenomenon unreported in the checked counting and maximum sources: order-√N downward fluctuations of the count are weighted by a power of size governed by the ratio of resetting and relaxation rates. Contrasting this with the logarithmic all-inside law clarifies two different mechanisms without depending on standalone novelty of the upper law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
