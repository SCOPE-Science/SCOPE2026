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

The reproducibility artifact `verify.py` uses Python 3 standard-library operations only. Run `python3 verify.py`. It enumerates all \(54{,}264\) nondecreasing six-tuples of 16 column indices, constructs disjoint recovery groups of size one or three, and independently recomputes the five-bit generator-column XOR for every selected group. The checker separately verifies the two-helper obstruction and the \(19>16\) counting bound for seven repeated requests. Its output ends in `VERIFY_OK`.

The search is exhaustive in the finite domain of six-request multisets; no finite search is extrapolated to general lengths. The distribution of support totals printed by the verifier reflects its deterministic selection of witnesses and is **not** claimed as a distribution of optimal read costs. Independent audit has not been performed.
