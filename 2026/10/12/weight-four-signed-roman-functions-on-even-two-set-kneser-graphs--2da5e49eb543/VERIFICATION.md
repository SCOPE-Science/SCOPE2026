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
# Verification

The included `verify.py` has two independent checks on the explicitly specified construction. First, it forms the Kneser adjacency relation literally by disjointness and verifies both signed Roman conditions for every two-set. Second, it computes endpoint incidence sums and checks the closed-neighborhood identity \(W-s_i-s_j+2f(\{i,j\})\), the total weight, and defenders for every negative pair.

The direct adjacency checks cover every even \(n\) from \(10\) through \(30\); the incidence-sum checks cover every even \(n\) from \(10\) through \(100\). An additional finite check lists the degree-capacity cases in the proof of restricted optimality for every even \(n\) from \(10\) through \(100\).

Output from the standalone file:

```text
VERIFY_OK
literal_definition_checked_even_n=10..30: 11 cases
row_identity_checked_even_n=10..100: 46 cases
one-weight-four witness per tested order; both signed Roman conditions hold
template lower-weight integer capacity alternatives checked for 46 orders
```

These finite checks are not an exhaustive search over all signed Roman functions and do not establish the unrestricted minimum. The arbitrary-order proof rests on the explicit algebraic verification and degree-capacity argument in `RESULT.md`.
