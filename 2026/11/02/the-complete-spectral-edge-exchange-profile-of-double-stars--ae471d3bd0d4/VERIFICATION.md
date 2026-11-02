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

Run `python3 verify.py` from the extracted package; NumPy is required. This is a finite reproducibility checker, not independent mathematical certification.

The program directly enumerates forest matchings from each reconstructed graph's edge set and verifies the stated characteristic-polynomial coefficients for original and central-exchange graphs for all positive leaf counts with the larger count at most seven (112 exact integer polynomial cases).

It separately constructs every labelled double star, deletes each edge, finds the two connected components, reconnects every admissible cross-component nonedge, and computes the largest eigenvalue from the actual adjacency matrix. For all 78 pairs with \(1\le m\le k\le12\), all 19,565 valid exchanges agree with the theorem's improving/neutral/decreasing classification. Equality is recognized using a tolerance of \(10^{-8}\); this is corroboration, not an exact algebraic decision procedure.

Expected terminal lines include:

```
EXACT_MATCHING_CHARACTERISTIC_POLYNOMIALS_OK 112
INDEPENDENT_ALL_EDGE_EXCHANGES_OK 78 19565
VERIFY_OK
```

The infinite proof uses exact characteristic-polynomial comparisons and diagonal resolvent inequalities in `RESULT.md`. No independent audit has yet been performed. Neutral exchanges are counted on the labelled graph, and no claim is made about multi-edge operations or other graph families.
