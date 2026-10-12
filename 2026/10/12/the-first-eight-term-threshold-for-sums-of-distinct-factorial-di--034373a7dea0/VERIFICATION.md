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

Run `python3 artifacts/verify.py` with the embedded artifacts in place. The standard-library-only verifier recomputes every value in the stated \(1\le n\le12\) table using exact Python integer bitsets. It independently generates divisor sets both by complementary factor pairs and by a prime-power Cartesian product. It checks exact cardinality-constrained reachability through eight terms, the 175-element maximal-length layer at \(12!\), both endpoints of that list and its content hash. A changed-order traversal verifies the decisive result a second time, while a distinct explicit-set implementation checks \(1\le n\le5\).

The run reports `VERIFY_OK first_h_eight_n=12 hard_count=175 first_hard=475785157 last_hard=479001547 permuted_order=yes independent_small_cases=yes`. The certificate is finite and gives no coverage beyond \(n=12\). The 175-line `artifacts/eight_term_layer.txt` is data, not a standalone proof without the exhaustive recurrence.
