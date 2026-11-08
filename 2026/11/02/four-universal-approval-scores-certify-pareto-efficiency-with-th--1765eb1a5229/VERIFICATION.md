---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For at most three unit-approval voters, classify candidate approval types as zero, full, e_i singletons and p_i=1−e_i pairs. A Pareto-optimal size-k committee cannot select any type dominated by an omitted candidate. If no singleton is selected or all pairs are selected, it consists of top-k candidates by (1,1,1) score. Otherwise select singleton e_j and omit pair p_j: no-improving-swap forces all selected singletons to be e_j and every omitted pair to be p_j; (2,1,1) with the weight 2 on coordinate j orders all remaining types and supports that committee. Each of the four universal score maxima is Pareto efficient since weights are strictly positive, and also fractionally Pareto efficient since the cardinality-k hypersimplex is the convex hull of integral committees. Conversely fractional Pareto implies integral. Boundaries k=0, k=|C| and absent voters are included. Independently enumerated all 256 subsets of the eight approval types and every feasible k, comparing integral Pareto frontiers to the four-weight union over 5,822 unique utility-profile checks, no disagreements. The original source checker also enumerates capacities 0..2 per type for 3^8 profiles; the finite test is corroboration of the infinite-candidate argument.

## originality

PASS

Best-of-knowledge original universal fixed family of only four scores supporting ALL integral Pareto-optimal committees for unrestricted at-most-three-voter approval profiles and the resulting integral=fractional frontier equality. Becker et al provide instance-dependent positive weights iff fractional PO, but not this integral-to-fractional implication on the unrestricted three-voter slice; Schünke treats restricted interval domains. Entire accessible Becker full primary text was inspected (Theorem weighted utilitarian characterization, preference domains, appendices), so source cannot be dismissed by title; unresolved possible older three-voter observations remain priority risk.

## value

PASS

A strong unbounded-candidate structural theorem reducing a difficult Pareto frontier to four election-independent weighted scores in a natural small-voter domain. The exact equality of integral and fractional Pareto frontiers improves on general fractional support characterization and yields simple O(|C|log|C|) membership checking; it is not a finite dataset recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
