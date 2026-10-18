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

# Verification and reproducibility

Run `python3 wheel_asymmetry_verify.py` using a standard Python 3 interpreter. The program enumerates all spanning trees of \(W_n\) for \(4\le n\le8\) by union-find; for each tree it constructs the reflected point in exact integer numerators and checks all nonempty vertex-induced-subgraph inequalities. It additionally checks support extrema of the rim cycle, one hub triangle and one consecutive hub-three-rim subgraph, and exact center normalization.

Observed output:

```
W_4: spanning trees=45; exact induced inequalities=1395; verified
W_5: spanning trees=121; exact induced inequalities=7623; verified
W_6: spanning trees=320; exact induced inequalities=40640; verified
W_7: spanning trees=841; exact induced inequalities=214455; verified
W_8: spanning trees=2205; exact induced inequalities=1126755; verified
PASS: 3532 trees; 1390868 exact reflected inequalities
```

The infinite-family proof instead invokes the standard spanning-tree polytope criterion and a closed induced-run argument valid for every integer \(n\ge4\). Enumeration for finitely many \(n\) cannot establish the infinite theorem or bibliographic originality. No independent mathematical assessment has been performed.
