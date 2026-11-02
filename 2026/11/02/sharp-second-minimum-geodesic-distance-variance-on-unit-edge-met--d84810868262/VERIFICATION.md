---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and scope

Run with `python3 verify_tree_variance.py`; the script needs only the Python standard library. The executed run returned:

`VERIFY_OK 19544 exact Prüfer-coded trees plus four direct shortest-route quadratures; n=4..7 exhaustive, n=8..20 seeded samples`

The code enumerates all Prüfer sequences with four through seven labeled vertices (all labeled trees of those orders), and checks 100 reproducibly sampled Prüfer sequences for each order eight through twenty. It directly constructs graph edge adjacency, computes line-graph distances, integrates conditional moments with exact rational arithmetic, and compares exact extremal and identity formulas. Four direct two-dimensional midpoint quadratures compute genuine geodesic lengths using vertex-to-vertex shortest routes independently of the line-graph moment reduction. Symbolic algebra separately checked the rational gap and star-variance simplifications.

The general mathematical proof is contained in `RESULT.md`. None of the finite enumerations is claimed to exhaust trees of arbitrary order or constitute infinite certification. The companion code checks only the new result, and no independent external audit was performed. The first-day evidence and the unresolved historical-priority risk are described in the references and review.
