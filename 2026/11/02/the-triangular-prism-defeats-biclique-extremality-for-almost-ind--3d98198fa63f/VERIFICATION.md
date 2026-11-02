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

# Reproducibility and limits

The mathematical proof evaluates two independent finite combinatorial sums over all subsets of the two graph types. It then uses the exact classification of 2-regular complements to exhaust all simple cubic graphs on six vertices; the latter classification is analytic and not assumed from a graph database. For admissible \(d\ge2\) and \(2d\mid n\), no nonisomorphic comparison graph exists below six vertices.

Run `python3 verify.py` with a standard Python 3 interpreter, with no downloaded data and no third-party dependencies. The verifier independently enumerates each graph's \(64\) vertex subsets and also computes both polynomials by the separate layer formulas. It asserts the exact induced-edge distributions, the factorization of their difference, and the cumulative threshold values. It checks every labelled nine-edge simple graph on six fixed vertices, retaining the \(70\) cubic ones and comparing their polynomials with the two claimed types. The expected terminal string is `VERIFY_OK`.

Verification returned:

```text
CUBIC_LABELLED_GRAPHS_OK {(6,): 60, (3, 3): 10}
EDGE_COUNT_DISTRIBUTIONS_OK K33= (15, 9, 18, 6, 9, 0, 6, 0, 0, 1) PRISM= (13, 15, 12, 8, 9, 0, 6, 0, 0, 1)
PHASE_DIAGRAM_OK [-2, 4, -2, 0]
EXACT_COUNTEREXAMPLE_OK 28 > 24
VERIFY_OK
```

The computations use exact integers, not floating-point approximations. The result pertains to vertex subsets inducing at most a fixed number of edges, not independent sets alone or arbitrary larger orders. No independent scientific audit or exhaustive historical-priority certification is claimed.
