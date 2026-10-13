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

Use Python 3.9 or later, with only the standard library:

```
python3 verify.py
```

The script generates every labeled tree of orders 5, 6, and 7 from all Prüfer words; for each, it tests all initial white subsets with zero through four vertices. It also tests 140 seeded trees of each order 8 through 18, 40 seeded trees of each order 19 through 26, and a star of each order 5 through 26. The direct forcing checker applies the ordinary rule to the exact complement adjacency; the formula checker independently computes the specified degree, leaf-pair and length-four-path sums. The captured output `verify_output.txt` ends in:

```
VERIFY_OK trees= 20110 white-subsets= 3134704
```

The included captured output is not a substitute for executing the included program. The finite cases validate implementation consistency, not all-tree completeness. The infinite statement rests on the proof in `RESULT.md`. All scientific limits stated there apply here. No independent audit has been performed.
