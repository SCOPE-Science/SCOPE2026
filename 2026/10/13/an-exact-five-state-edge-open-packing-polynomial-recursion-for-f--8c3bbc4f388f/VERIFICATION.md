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

# Verification notes

The full reproducible proof is in `RESULT.md`. The accompanying `edgeopen_forest_verify.py` reconstructs the polynomial from the five recurrences and independently tests candidate edge sets against the literal requirement that no **third distinct graph edge** joins endpoints of any two chosen edges. Thus it does not rely on the induced-star theorem when computing brute-force values.

Run with:
```
python -m pip install -r requirements.txt
python edgeopen_forest_verify.py
```

The captured file `edgeopen_forest_verify.out` records `ALL_CHECKS_PASSED` and exact case counts. Full nonisomorphic-tree census: 436 trees on 1 through 11 vertices, 310,855 candidate edge subsets. Independently, the support-induced-star equivalence was checked against the direct condition on those 310,855 candidate subsets. Random forest sample: 600 examples with 350,018 directly tested subsets. The star test verifies all binomial coefficients for 98 orders from 2 through 99. Specific paths and stars are printed. Repetitions across tests are possible; these are check counts, not a claim of mutually distinct graphs.

The random sample, finite census, and executable code do **not** prove the theorem for all orders. The inductive proof in `RESULT.md` supplies the infinite argument. The verifier requires Python and NetworkX solely to generate nonisomorphic tree representatives; the polynomial recurrence itself uses elementary exact integer lists. Arithmetic-operation complexity is not a bound on bit complexity. Self-review has been performed; independent audit has not.
