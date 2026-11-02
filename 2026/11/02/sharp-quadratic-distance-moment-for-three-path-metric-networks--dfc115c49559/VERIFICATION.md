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

Run `python3 verify_second.py` with Python 3 and its standard library. The program checks the quartic against independent midpoint-quadrature integration of the original four-branch path-distance formula on 22 configurations, including arms violating the triangle inequality. It checks exact rational nonnegative-coefficient certificates and equality cases across hundreds of length triples and confirms the two exactly derived CDF expressions at the common short-distance threshold. Execution observed:

```text
VERIFY_OK 1064 exact rational identities, independent double quadratures, and CDF-limit comparison
```

The analytical proof is in `RESULT.md`: the computation does not exhaust the infinite parameter family. All formulas and certificates can be independently reconstructed by integrating six regions; no external verification service, proof assistant, or independent mathematical audit is claimed. An earlier full-text article remains a historical-priority uncertainty, not a failure of these checks.
