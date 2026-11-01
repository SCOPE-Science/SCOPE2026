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

# Reproducible mathematical checks

Run `python3 verify_two_cluster_variance.py`. The script uses Python standard-library exact rational fractions for the finite four-level and threshold checks. For independent full-polytope vertex enumeration, install `numpy` and `scipy` as specified in `requirements.txt`; otherwise the optional full-vertex test is explicitly skipped. Replaying with both installed must end in `ALL_TWO_CLUSTER_LIPSCHITZ_VARIANCE_TESTS_OK`.

Recorded run from the delivered checker source:

```
EXACT_FOUR_LEVEL_VARIANCE_AND_ROUNDING_OK 600
EXACT_KINK_AND_DERIVATIVE_JUMP_OK 122
SHARP_IMBALANCE_TRANSITION_OK 600
INDEPENDENT_ALL_LIPSCHITZ_POLYTOPE_VERTICES_OK 27
ALL_TWO_CLUSTER_LIPSCHITZ_VARIANCE_TESTS_OK
```

The 600 exact cases iterate cluster sizes from one to ten and rational distances. The 122 cases verify exact crossing and derivative identities. The 27 independent tests enumerate the full Lipschitz-polytope vertex set by halfspace intersection, for selected parameter sizes; their floating comparison uses tolerance `2e-8` and is not a symbolic proof. The main theorem assumes cluster sizes at least two; tests with size one deliberately exercise boundary consistency. The universal proof uses the connected-tight-pair vertex argument and algebraic maximization, not any finite enumeration. No independent scientific audit has been performed.
