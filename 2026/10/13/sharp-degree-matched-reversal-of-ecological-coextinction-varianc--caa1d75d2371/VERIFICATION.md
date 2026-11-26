---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independence gives E[X_i]=q^|N_i| and E[X_i X_j]=q^|N_i∪N_j|. Same plant margins cancel the mean terms; same pollinator margins fix the total pair-intersection size by summing binom(deg(j),2). Thus the difference of pair-union polynomials has zero constant term, value and derivative zero at q=1, and degree ≤r. For r≤3 it is a constant times q(1−q)^2, ruling out an interior strict sign reversal without a plant-count bound. For r=4 one residual factor is linear, a+bq, with a switch exactly when a(a+b)<0. Independently enumerated ordered positive-margin incidence matrices and expanded their exact E[X²] polynomials from the 16 loss outcomes rather than forming pair unions. The admissible counts for m=1–4 were 1,79,2161,41503, with 1,8,33,103 margin classes and 0,0,5,48 distinct polynomial comparisons. There were no switches. The displayed witness has the claimed matching labeled margins, equal mean 2q+3q² and the variance difference with coefficients (0,2,−8,10,−4), giving the strict switch at q=1/2 and ties at the stated three points. This proves the nested minimum: four pollinators, then five plants at exactly four pollinators.

## originality

PASS

The supported distinct claim is the sharp pollinator-first minimum (four regardless of plant count, five plants at that pollinator minimum). A separate indexed nine-total-species theorem in the same iid model subsumes the finite non-reversal statement at four pollinators and at most four plants, and contains the same covariance identity. It does not bound three pollinators at unrestricted plant count or exhibit reversal with four pollinators. Its displayed five-pollinator witness does not become the frozen witness by transposition: the two degree-multiset pairs differ, and swapping the guilds changes the loss variable. No inspected source supplies the full nested minimum. This is not a determination of historical priority.

## value

PASS

Equal degree margins fix the expectation and constrain pair intersections, yet can leave even the direction of the variance comparison sensitive to the risk parameter. The sharp number of independently lost primary species needed for this phenomenon isolates a model-specific boundary, and the unconditional three-pollinator obstruction explains why no larger plant guild can lower it. This is more informative than another nine-total-species example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
