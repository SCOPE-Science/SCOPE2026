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

# Verification of the triangular-graph closure classification

Run `python3 verify.py`. The checker uses only Python 3 standard-library modules and computes the induced-path Horn closure from elementary disjoint-edge pairs rather than calling the proposed closed-form predictor. It enumerates all \(2^{\binom n2}\) edge subsets for \(n=4,5,6\), determines the number of simultaneous rounds, and checks the exact criterion for two rounds. It independently reconstructs all closed subsets and their ranks from longest inclusion-chain computations.

Its successful recorded output is:

```
EXHAUSTIVE 4 subsets 64 closed 28 ranks [1, 6, 12, 8, 1] time_counts {0: 28, 1: 36} PASS
EXHAUSTIVE 5 subsets 1024 closed 82 ranks [1, 10, 30, 30, 10, 1] time_counts {0: 82, 1: 822, 2: 120} PASS
EXHAUSTIVE 6 subsets 32768 closed 214 ranks [1, 15, 60, 80, 45, 12, 1] time_counts {0: 214, 1: 29854, 2: 2700} PASS
AUTOMORPHISM_T4 48 PASS
VERIFY_OK exact_closure=PASS two_round_cherry=PASS graded_rank=PASS mobius=PASS strict_logconcavity=PASS exceptional_symmetry=PASS
```

Further checks: the checker calculates Möbius values by interval recursion in dimensions four and five, verifies the strict log-concavity inequalities for dimensions four through one hundred, and directly enumerates the automorphisms of the six-vertex triangular graph \(T_4\). The computational tests do not validate every parameter; the infinite assertions rest on the written proof. Independent external review is not performed.
