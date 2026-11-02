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

For two fixed distinct singleton indicators in n independent uniform allocations to m boxes, the exact probabilities are P1=(n/m)(1-1/m)^(n-1) and P11=n(n-1)/m^2(1-2/m)^(n-2). For m>=3 the covariance sign equals F_m(n), where F_m(x)=log(1-1/x)-2log(1-1/m)+(x-2)log(1-1/(m-1)^2). The exact derivative F_m'' = -(2x-1)/[x^2(x-1)^2]<0, with F_m(2)<0 for m>=4, F_m(m)>0 by Bernoulli bound 1+1/(m-1)^3, and F_m(∞)=-∞, yields precisely two real positive-interval roots alpha_m<m<beta_m. Cases m=2 and m=3 follow from exact formulas. Independently expanded F_m(m+s sqrt(m)) symbolically as m^-2(1/2-s²)+m^-5/2(s³-s)+O(m^-3), giving roots m±sqrt(m/2)-1/4+O(m^-1/2) and m² covariance ->e^-2(1/2-s²). Source verifier is finite corroboration only; all-m/n signs are analytic.

## originality

PASS

The pair probabilities and their binomial/multinomial covariance are standard. Penrose’s isolated-ball urn analysis studies singleton-count normal approximation, while Barbour–Gnedin examine infinite frequency-count covariance limits; neither inspected primary result gives the fixed pair’s exact two-switch sign window and its sqrt(m) location/shift. Resultary surfaced related theorems about occupied boxes (nonempty, different indicators) and richness-frequency covariance (aggregate counts, different pairs), but not the fixed-singleton-pair theorem. Best-of-knowledge original refinement with possible classical implicit covariance formula qualification.

## value

PASS

The strict transition from negative pairwise singleton dependence to a positive window near n=m and back to negative is a natural nonmonotone correlation phenomenon in finite occupancy, quantified by a sharp sqrt(m)-scale window and finite constant shift. An exact sign classification of a natural statistic can be useful without a new CLT; it is more than a routine restatement of the pair probability formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
