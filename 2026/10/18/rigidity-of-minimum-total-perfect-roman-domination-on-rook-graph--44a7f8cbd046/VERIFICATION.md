---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Definition verified: every zero has exactly one neighbor with label 2; induced positive-labeled subgraph has no isolated vertex. A full column of 2s weighs 2m for K_m □ K_n, 2<=m<=n. For k<m twos meeting r rows and c columns, cells outside both sets and unchosen cells in their r×c crossing are compelled to be ones; w>=k+(m-r)(n-c)+rc. The published case split m>=4 and m=3 and m=2 rules out equality 2m (for 3×3 equality candidates violate positive support or need extra ones). For k>=m equality forces exactly m twos and no ones. The exact-one defender condition then forces a full column, or a row if square; otherwise unselected cross corners see two defenders. The k=0 all-one function weighs mn and is minimal only at 2×2. On the four-cycle there are eight additional labelings with one 2 and two 1s and the all-one, alongside four full row/column functions, total thirteen. Independent exhaustive labelled enumeration confirms (m,n,weight,count)=(2,2,4,13),(2,3,4,3),(2,4,4,4),(3,3,6,6),(3,4,6,4). Bounded tests do not replace all-parameter proof.

## originality

PASS

Compared mathematical implications against primary literature, Resultary semantic findings, aliases and broader formulations. Best-of-knowledge priority only. The exact minimizer normal form and count require extra arguments, including 3×3 and 2×2 exceptional cases, not logical specializations of found prior statements.

## value

PASS

This completely classifies all minimum configurations, not merely their weight, on a natural Cartesian-product graph family. Exact rigidity and exceptional four-cycle multiplicity can support extremal graph domination and labeling census calculations. Neither the positivity restriction nor exact-one Roman defense is interchangeable with perfect Roman, total Roman or ordinary Roman variants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
