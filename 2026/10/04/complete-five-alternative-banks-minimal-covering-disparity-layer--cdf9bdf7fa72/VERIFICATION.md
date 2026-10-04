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
The embedded `verify_banks_minimal_covering_first_layer.py` performs a complete exact census of labeled tournaments of orders \(1\) through \(5\).

The Banks set is computed independently by:
1. a dynamic program for transitive subsets using repeated deletion of a maximal vertex;
2. the tournament fact that a subset is transitive exactly when it has no directed \(3\)-cycle.

The minimal covering set is computed independently by:
1. enumerating uncovered-stable subsets and taking the unique inclusion-minimal one;
2. enumerating covering sets directly from the induced covering relation.

The verifier confirms:
- \(BA(T)=MC(T)\) for every tournament through order \(4\);
- the complete order-\(5\) histogram
\[
(1,1):320,\quad
(3,3):520,\quad
(5,5):64,\quad
(4,3):120;
\]
- exactly \(120\) strict cases among \(1024\) labeled tournaments;
- exact incidence \(15/128\);
- strict containment \(MC(T)\subsetneq BA(T)\) in every strict case;
- exactly one strict isomorphism class;
- canonical encoding \(41\);
- orbit size \(120\) and automorphism-group order \(1\);
- the displayed canonical out-neighborhoods and choice sets.

Run:

`python3 verify_banks_minimal_covering_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation establishes only the complete first disparity layer through order \(5\).
