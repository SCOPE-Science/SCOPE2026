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

Run:
```text
python3 artifacts/verify.py
```

Expected first line:
```text
VERIFY_OK q=3 n=4 optimum=11 words=81 witness_size=11 equality_triples=8 feasible_c42_triples=0 search_nodes=271
```

The program uses only the Python standard library. It reconstructs all 81 ternary length-four words, computes distinct one-deletion shadows, verifies the displayed 11-word code, and solves the complete compatibility graph exactly by branch-and-bound with a greedy coloring upper bound. It separately enumerates all eight equality-case triples of type \((a,b,c,a)\) and confirms that none has pairwise disjoint deletion shadows.

The exhaustive search is finite and complete for \(q=3,n=4\). It is not used to infer any statement for larger alphabet sizes. The symbolic proof in `RESULT.md` supplies the mathematical upper-bound mechanism; the exhaustive search is an independent finite replay.
