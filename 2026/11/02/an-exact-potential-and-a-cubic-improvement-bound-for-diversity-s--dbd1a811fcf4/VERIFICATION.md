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

# Verification instructions and limits

From a directory containing `verify.py`, run `python3 verify.py`. The verifier requires only Python 3 standard-library modules (`fractions`, `collections`, `itertools`, and `math`). It enumerates assignments with one vacant vertex and labels from two or three types for the specified six complete bipartite graphs. It checks, for **every** unilateral move, exact equality of the moving agent's rational payoff difference and the rational potential difference. It also checks the potential interval and the lower bound on a positive increment.

The execution output obtained when preparing this result was:

```
K_{2,3}, 2 types: 320 exact transitions; 72 improvements; 70 states using every type
K_{2,3}, 3 types: 1620 exact transitions; 324 improvements; 180 states using every type
K_{2,5}, 3 types: 30618 exact transitions; 6300 improvements; 3780 states using every type
K_{3,4}, 3 types: 30618 exact transitions; 7560 improvements; 3780 states using every type
K_{4,4}, 3 types: 122472 exact transitions; 23232 improvements; 14448 states using every type
K_{4,5}, 3 types: 472392 exact transitions; 123480 improvements; 52164 states using every type
PASS: 658040 exact transition identities, 160968 positive transitions
```

The tests deliberately include assignments that omit some available type labels, although the theorem concerns partitions into nonempty types; this broadens computational edge cases without changing the proof. These are finite exhaustive tests only for the displayed parameter triples. The all-parameter identity and the step bound are proved symbolically in RESULT.md. The tests do not cover arbitrary immobile-agent subsets individually; those restrictions only delete feasible moves and the proof still applies. No independent audit or validation has been performed.
