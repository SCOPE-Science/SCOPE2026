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
Run `python3 verify.py` from the directory containing the files; only Python 3 standard-library components are used. The checker constructs every distinct cut of each complete graph on \(4\), \(5\), and \(6\) vertices and determines the Galois closure of every subset of the edge attributes. It independently computes bipartite-component closures and ternary-rule saturation, comparing exact edge bitmasks in each case.

For the direct basis, it checks all subsets through six vertices and verifies for every newly implied edge that some subpremise of size at most the asserted bound entails that edge. It tests the required odd-cycle lower-bound witnesses on four through nine vertices, including every proper subset obtained by deleting a cycle edge. It checks the weighted-partition concept count, which is known in OEIS A307389.

Observed successful run:
```
EXHAUSTIVE n=4 subsets=64 closed=30 triple_rules=16 PASS
DIRECT_BOUND n=4 width=3 exhaustive=PASS lower_witness=PASS
EXHAUSTIVE n=5 subsets=1024 closed=137 triple_rules=70 PASS
DIRECT_BOUND n=5 width=3 exhaustive=PASS lower_witness=PASS
EXHAUSTIVE n=6 subsets=32768 closed=738 triple_rules=200 PASS
DIRECT_BOUND n=6 width=5 exhaustive=PASS lower_witness=PASS
DIRECT_BOUND n=7 width=5 lower_witness=PASS
DIRECT_BOUND n=8 width=7 lower_witness=PASS
DIRECT_BOUND n=9 width=7 lower_witness=PASS
VERIFY_OK exact_cut_closure=PASS iterative_width_three=PASS direct_arity_bound=PASS concept_number=PASS
```
The checker does not test every larger graph and does not prove the infinite statement; that conclusion follows from the structural argument in RESULT.md. No independent external review or certification is claimed.
