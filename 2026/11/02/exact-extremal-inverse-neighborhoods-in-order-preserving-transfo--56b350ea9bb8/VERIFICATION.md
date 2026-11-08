---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For f weakly increasing on [n], each semigroup inverse g must select one image point in each of f's r interval kernel blocks, and each cut separating g-fibers must lie between adjacent images b_i,b_(i+1) of f; conversely these independent choices satisfy both fgf=f and gfg=g. This establishes |V(f)|=product(a_i)*product(b_(i+1)-b_i). Balancing positive compositions gives the rank maximum B(n,r)B(n-1,r-1). A separate integer-break argument handles the coupled r/r-1 partition maxima and equality cases in each n mod 3, with small n separately. The two weighted generating-function coefficients give (binom(n+r-1,2r-1))^2 for ordered rank-r inverse pairs; rank one and empty products are included. Independently computed BOTH inverse equations directly on all weakly increasing transformations for n=1..6 and reproduced (M_n,E_n)=(1,1),(2,2),(4,2),(12,1),(24,2),(48,2), and ordered-pair totals 1,5,26,153,931,5794. These finite tests are only corroboration for the unrestricted n proof.

## originality

PASS

The 2026 Higgins result establishes a permutation matching of the order-preserving transformation monoid using balanced structure weights and inverse incidence; that machinery motivates, but the accessible stated result does not give the sharp max inverse-neighborhood, modulo-3 equality ranks/counts, or per-rank squared-binomial inverse-pair census. The 1993 Higgins monoid paper's accessible full text concerns other combinatorial properties (including idempotents), but a historical equivalent formula in semigroup literature cannot be ruled out. The balancing lemma is elementary prior technique, while the coupled exact extremal classification is the evaluated contribution.

## value

PASS

The inverse graph of the canonical finite isotone transformation monoid has highly nonuniform local degrees despite admitting a permutation matching. The sharp maximal congestion scale 9^(1/3), all extremizing maps and exact rankwise edge counts answer natural structural questions of this graph for every order; these are not arbitrary slices or a mere restatement of existence of a matching.

The dated certificate retains the supplied scientific assessment, sources and limitations.
