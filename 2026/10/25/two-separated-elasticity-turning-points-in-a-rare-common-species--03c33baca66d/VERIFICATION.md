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

For independent homogeneous Poisson intensities 1 and ε, expected richness is S=2−exp(−x)−exp(−εx) and elasticity z=xS′/S. Independently differentiated to H=S P−x(SQ+P²) and used symbolic algebra to verify exactly the three-term decomposition with p=e^(−x), q=e^(−εx), y=εx. Its denominator S² is strictly positive. The proof covers the entire x>0 domain in four complementary pieces: small x, early-to-transition x≈L+logL, long positive middle interval, and late tail x≈y*/ε to infinity. Early centered limit H/ε→1−e^(−u) and derivative→e^(−u) gives one simple minimum; late H/ε→e^(−y)[2(1−y)−e^(−y)] gives one simple maximum because the bracket strictly decreases. Uniform exponential bounds rule out other zeros between and after. Independent symbolic derivative and four progressively smaller ε tests reproduced x−, y*, z heights. The limit is explicitly only ε sufficiently small, not all ε.

## originality

PASS

Qualified PASS: earlier common-versus-rare species-area literature already demonstrates accelerating / sigmoidal shapes for two unequal-abundance species and random placement, so nonmonotonicity itself is covered. In the materially inspected full Tjørve et al. (2008) article the finite-grid occupancy model and qualitative bending do not yield this continuous-Poisson exactly-two-critical-point theorem or logarithmic-plus-logarithmic asymptotic. The Coleman 1981 and 1982 original random-placement papers remain important priority risks; complete bodies were unavailable.

## value

PASS

PASS: the familiar two-species Poisson richness law has a delicate three-scale elasticity profile, requiring global zero exclusion and two different asymptotic coordinates. The sharp location/height transition is a natural interpretable species–area invariant and not the mere observation that rare species affect larger surveyed areas. It is not extrapolated to empirical heterogeneity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
