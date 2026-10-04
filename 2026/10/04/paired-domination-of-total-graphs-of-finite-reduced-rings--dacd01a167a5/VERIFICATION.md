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

The verification separates the symbolic proof from finite corroboration.

1. **Lower bound.** If no coordinate projection of a total dominating set equals its field, choose one coordinate value outside the negative selected projection in every factor. The resulting tuple has unit sum with every selected vertex and is therefore undominated. Hence every total dominating set has size at least the smallest field order \(q\). A paired dominating set is total dominating and has even cardinality, giving the least-even-at-least-\(q\) lower bound.

2. **Even witness.** The \(q\) vertices with arbitrary first coordinate and all remaining coordinates zero induce \(K_q\) and totally dominate. For even \(q\), this clique has a perfect matching.

3. **Odd witness.** For odd \(q\), one vertex with zero first coordinate and a fixed nonzero second coordinate is added. It matches the zero vector, and the remaining \(q-1\) clique vertices match in pairs.

4. **Finite replay.** `verify.py` constructs the actual total graph using additive models of finite fields, exhaustively computes ordinary, total, and paired minima for nine profiles, and checks the explicit witnesses for seven additional profiles containing field orders \(4\), \(8\), and \(9\).

Exact output:

```text
profile=(2, 2) vertices=4 gamma=2 gamma_t=2 gamma_pr=2
profile=(2, 3) vertices=6 gamma=2 gamma_t=2 gamma_pr=2
profile=(2, 4) vertices=8 gamma=2 gamma_t=2 gamma_pr=2
profile=(3, 3) vertices=9 gamma=2 gamma_t=3 gamma_pr=4
profile=(3, 4) vertices=12 gamma=3 gamma_t=3 gamma_pr=4
profile=(3, 5) vertices=15 gamma=3 gamma_t=3 gamma_pr=4
profile=(4, 4) vertices=16 gamma=4 gamma_t=4 gamma_pr=4
profile=(3, 3, 3) vertices=27 gamma=2 gamma_t=3 gamma_pr=4
profile=(5, 5) vertices=25 gamma=4 gamma_t=5 gamma_pr=6
VERIFY_OK
exhaustive_profiles=9
witness_only_profiles=7
projection_lower_bound=proved_symbolically_in_RESULT
```

The finite search is not an infinite certificate; the arbitrary-product result is established by the three symbolic steps above.
