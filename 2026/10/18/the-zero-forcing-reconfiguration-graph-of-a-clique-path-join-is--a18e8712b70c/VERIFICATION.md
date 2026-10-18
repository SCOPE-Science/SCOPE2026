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

# Reproducible finite checks

Compile the included C++17 source from the directory containing `check.cpp`:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic check.cpp -o check
./check
```

The expected output, recorded in `verification_output.txt`, is:

```text
VERIFICATION_OK graph_cases=54 initial_sets_checked=261879 minimum_sets_found=486 reconfiguration_edges_checked=1062
```

For all \(1\le s\le6\) and \(4\le n\le12\), the program independently constructs the graph, exhausts every initial set of cardinality at most \(s+1\), applies the ordinary zero-forcing process to closure, compares the successful sets to the explicit classification, and checks that token-jumping adjacency yields two complete blocks with exactly one cross-edge. The main theorem is for \(s\ge2\); including \(s=1\) tests the separately known boundary. The check exhausts *small parameter instances*, not all possible parameter values or larger subsets, and is not an infinite-family proof. The proof in `RESULT.md` establishes the universal result.

The mathematical research comparison was based on full-text inspection of the principal zero-forcing reconfiguration study, on the directly relevant fan-graph enumeration, on a distinction from zero forcing *on* barbell base graphs, and on literature involving cone operations. A negative search is not a priority certificate. Independent validation has not been performed.
