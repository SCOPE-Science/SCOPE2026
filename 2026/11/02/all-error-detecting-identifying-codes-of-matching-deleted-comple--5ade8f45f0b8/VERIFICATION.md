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

Two unmatched vertices on one shore cannot be distinguished: each exclusive closed-neighborhood difference has size one. For distinct deleted-edge indices i,j, both same-shore comparisons impose the same alternative: select both a_i,b_j or both a_j,b_i. For t>=2 this allows at most one omission on either shore, and simultaneous omissions must have distinct indices; conversely each such omission pattern satisfies these comparisons. An unmatched a_* forces itself and every matched b_i by comparison with a_i, and likewise for an unmatched b_*. Across shores, an adjacent matched pair has exclusive sets B without b_i,b_j and A without a_i,a_j, respectively. At t=4 in the crown, two distinct omitted indices leave two other indices that witness failure, while a full shore suffices for the single-omission case. For t>=5 each allowed crown omission leaves at least two selected vertices in both exclusive sets. With just one unmatched vertex, all t opposite-shore vertices are forced, so for t>=4 their exclusive differences suffice; at t=3 an omission causes failure on the two other indices. With both unmatched vertices only the full set survives and adjacent matched comparisons require t>=3. For pairs involving an unmatched vertex on the opposite shore the exclusive set on that shore excludes just the compared vertex; for a missing edge the two closed neighborhoods are disjoint and two-domination suffices. The admissible candidates are two-dominating: each vertex has at least two selected vertices on the opposite shore after its possible deleted neighbor is excluded. The small excluded cases have a matched adjacent pair with both exclusive differences of size at most one, or an isolated vertex/low-degree edge (at t=1 the only remaining graph under a,b>=2 is a three-edge path). The stated labelled coefficients then count the listed omissions exactly.

## originality

PASS

The supported distinct claim is the complete labelled EDIC census for all matching-deleted bicliques, including the unmatched-shore classification and exact multiplicities. The detection criterion and a particular Q_3 witness were available before this record and are not credited as new. The closest indexed census on the same graph family counts ordinary, not error-detecting, codes.

## value

PASS

For a natural dense bipartite test family and an established false-negative model, the theorem determines feasibility, minimum detector counts, and the entire distribution of labelled feasible sets. It describes how unmatched vertices force detectors and change the number of optimal deployments from quadratic to linear to a unique full set, with sharp low-order exceptions. This is useful structural information not supplied by an ordinary-code count or by one witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
