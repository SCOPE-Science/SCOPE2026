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

# Computational checks and limits

Run \(\texttt{python VERIFY.py}\) with Python 3. The script calculates subtree counts from the displayed postorder recurrence and independently enumerates functions from sampled finite rooted-tree posets to the three-level target. Direct enumerations check every parent-edge order-preservation constraint and every vertex's complete reflexive descendant lifting requirement; they do not reuse the recurrence for those two predicates.

The recorded execution yielded \(\texttt{ALL_TESTS_PASS 1928 REGULAR_CASES_PASS 40}\). The 1,928 configurations cover rooted parent arrays through eight vertices, with a deterministic subset of larger shapes. They also test whether a surjection exists exactly when some vertex has enough nonleaf children. The 40 parameter pairs independently compare the height-two complete branching formula with a Stirling recurrence and test the existence threshold.

The checker supplies finite corroboration only. The all-size statements follow from the symbolic state decomposition, inclusion-exclusion, maximal zero-preimage argument, and monotone bounded entropy sequence written in RESULT.md. A separate independent audit has not been performed.
