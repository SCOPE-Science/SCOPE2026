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

# Verification of exact conditional triangle-area moments

`verify_center_triangles.py` is standalone Python 3 code requiring only its standard library. Run:

```sh
python3 verify_center_triangles.py
```

The locally executed test returned `VERIFY_OK`, with \(595665\) total distinct-vertex triangles and \(148800\) strictly center-containing triangles across the complete range \(3\le n\le62\). Membership is computed by three Cartesian oriented-edge inequalities, independently of the cyclic-gap criterion; areas are computed from determinants. The tests compare probabilities, normalized first moments, second moments, and independently evaluated gap formulas against the closed forms. Further numerical spot checks concern the asymptotic expansions.

The mathematical proof is the finite geometric-series evaluation and cyclic-composition argument in `RESULT.md`. The finite computations cannot certify any statements for arbitrarily large orders. Conditional values are intentionally absent for \(n=4\), because the strict containment event is empty. Mathematical priority and completeness of the historical search have not been independently certified.
