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
# Exact verification

The accompanying `verify.py` is a self-contained Python 3 script. Its check is exhaustive for the finite twelve-arc graph; there are \(4096\) candidate edge subsets. It verifies the arc-set definition against a separate forbidden-two/three-cycle characterization, counts all simplices, builds an explicit acyclic Morse matching, verifies that the full reversed Hasse graph has no directed cycles, and computes every signed integral degree-two Morse boundary coefficient.

Run `python3 verify.py` from the directory containing the script. Expected output:

```
VERIFY_OK faces=101 nonempty=100 matching_pairs=47 critical=(1,1,4,0) gradient_DAG=100 Morse_d2=[0, 0, 0, 0]
critical_cells= [(0, 512), (1, 272), (2, 19), (2, 168), (2, 1216), (2, 3200)]
```

No symbolic-algebra package, external dataset or network access is needed. The script proves the listed finite assertions provided the standard Python integer and collection operations behave as specified; the interpretation of its result as a homotopy equivalence uses the standard discrete-Morse theorem. An independent external mathematical audit has not been performed.
