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

# Reproduction and limits

The supplied `checker.py` uses Python 3 standard-library modules only. Run `python3 checker.py` from the directory containing this file; no network, platform account, external datasets, or external packages are required. Its expected output is:

```text
ALL_CHECKS_OK canonical_cases=108 arbitrary_cases=12 rigidity_cases=13 witness_cells=2600
```

It checks the canonical cut-cover minimum in \(108\) cases, independently compares arbitrary rectangles in \(12\) cases, enumerates optimal cut rigidity in \(13\) cases, and checks \(2600\) explicit witness entries. The arguments for all \(r,s,t\) are proved in `RESULT.md` using maximal/minimal rectangle indices and a cut-free-gap count. Computation is not an exhaustive test of arbitrary infinite relations and is not treated as such. The proof does not depend on probabilistic experiments.

This package has undergone self-review only. Independent audit and external certification have not been performed.
