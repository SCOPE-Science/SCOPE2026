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

The accompanying `verify_dwork.py` uses \(\mathbf F_9=\mathbf F_3[i]/(i^2+1)\), lists all \(7462\) reduced-row-echelon presentations of two-dimensional vector subspaces of \(\mathbf F_9^4\), and tests each restricted quartic at five distinct projective parameter points. Its exact output is:

```
GF9_DWORK_LINES_{0: 112, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}_OK
```

The independent `verify_local.py` constructs the fourth-root sets, checks the two orbit counts and the first-order implicit-function calculation at the exotic representative. It outputs:

```
DWORK_LOCAL_TANGENT_48_REDUCED_64_LENGTH_TWO_TOTAL_176_OK
```

Both use only the Python standard library. The computations are exact in finite fields and can be replayed using `python verify_dwork.py` and `python verify_local.py` from the containing directory. The proof of completeness for algebraically closed characteristic-three fields, the full absence of lines for every nonzero geometric parameter, and the scheme-theoretic local lengths is given in `RESULT.md`; neither exhaustive \(\mathbf F_9\) enumeration nor first-order data alone would establish those assertions.

No independent external verification has been performed. The principal scientific limitations are the restriction to the specified Dwork pencil and characteristic three, and residual literature-priority uncertainty.
