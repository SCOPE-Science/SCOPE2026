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

# Reproducible checks

Run `python3 verify_star.py` (Python 3.8+ with integer bit_count support, practically Python 3.10+). The verifier enumerates every subset of the non-reflexive, non-mandatory leaf-origin arrows for star sizes 1–4, closes reachability, computes exact minimal extra-arrow counts without using the theorem's formula, compares the computed minima with the formula, and verifies that the displayed single-box/one-atom truth signatures distinguish all distinct stage preorders. It independently counts labelled partial orders through size four and checks agreement with the classical count, then checks the maximization expression for sizes 5–39.

Observed output:

```text
k=1 relations=2 maximum_minimal_extra_edges=1 all_minima_and_semantics_ok
k=2 relations=7 maximum_minimal_extra_edges=2 all_minima_and_semantics_ok
k=3 relations=45 maximum_minimal_extra_edges=3 all_minima_and_semantics_ok
k=4 relations=500 maximum_minimal_extra_edges=5 all_minima_and_semantics_ok
EXTREMAL_FORMULA_OK k=1..39
ALL_CHECKS_OK
```

The verifier does not establish the all-sizes extremal bound or prove novelty. These rely on the written proof and on the literature comparisons respectively. The finite checks are exhaustive only within their explicitly reported limits.
