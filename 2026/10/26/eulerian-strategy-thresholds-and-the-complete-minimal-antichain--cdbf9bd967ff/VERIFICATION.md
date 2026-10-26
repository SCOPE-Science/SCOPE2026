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
# Reproducibility

Run the attached self-contained `verify.py` using Python 3 and the standard library only:

```sh
python3 verify.py
```

The output is embedded as `verify_output.txt` and ends with `VERIFY_OK`. The checker does not assume the greedy parking theorem: its `park` function simulates each car's physical search in both directions; it checks equivalence to the separately computed statistic for every strategy with \(1\le n\le8\) and each \(m\in\{1,\ldots,n\}\). It checks that immediate coordinate decreases exhaust all minimal-successful elements and compares their sets to the claimed construction. It tests a separately constructed insertion map for injectivity, surjectivity and descent preservation, and compares the exact Eulerian counts. It also tests the recurrence and reflection symmetry through order 100.

These checks are exhaustive only over the finite stated domains. The logical proof in `RESULT.md` handles arbitrary orders. No independent external verification has been performed.
