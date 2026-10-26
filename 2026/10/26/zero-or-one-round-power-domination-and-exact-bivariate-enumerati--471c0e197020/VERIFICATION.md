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

Run `python verify.py` under Python 3; no packages or external files are required. The independent simulator tests every nonempty selected-edge subset in 57 ordered positive multipartite part-size tuples with total vertex count at most six (203,826 subsets including 57 empty selections, all rejected). It compares direct power domination propagation on the line graph with the proposed residual-star criterion. Of these, 168,672 selections come from 38 part-size tuples in the stated new domain. A separate inclusion-exclusion implementation compares polynomial coefficients against exhaustive subset enumeration on eight tuples. A third enumeration independently checks the known all-singleton triangular-graph boundary cases for orders three through six; those results are not claimed as new.

All checks completed successfully. The all-parameter theorem is supported by its separate elementary proof; none of the enumerated finite tests is an exhaustive proof over arbitrarily many vertices. The publication-priority search has an explicitly documented incomplete-source risk, and no independent audit is asserted.
