---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Translate line-graph domination to at most one uncovered K_n label. Each matched pair of selected incident edges covers three original labels, forcing 2k chosen edges at n=3k+1; equality forces k disjoint P3 stars with one hole. Count =n!/(2^k k!), and remove/insert classification gives exactly four moves per star. The bouquet-square token-swap quotient is connected via edge transpositions, and symmetric labeling yields transitivity, degree 4k, edges 2kN and triangles 2kN/3. Independently constructed canonical star forests and BFS all 12, 630, 75600 states: distance histograms exactly match claimed diameters 3,6,10, but only for k<=3; no larger diameter claimed.

## originality

PASS

Qualified PASS: Haynes–Slater introduces paired domination and general inequalities, but the accessible abstract has no exact saturated triangular-graph optimal solution reconfiguration; relevant triangulation paper concerns planar graphs, whereas T_n is the Johnson graph J(n,2). Exact bouquet quotient and finite diameters were not identified as prior classifications. Foundational original full text unavailable, recorded as a risk.

## value

PASS

The natural saturated family n=3k+1 has a complete optimal paired-dominating-set classification and a structured token-swap reconfiguration graph; connectedness, counts and small exact diameter cutoffs are mathematically meaningful even without a general diameter formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
