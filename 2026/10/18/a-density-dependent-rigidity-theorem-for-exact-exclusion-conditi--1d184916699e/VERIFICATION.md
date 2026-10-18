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

# Reproducible checks and limits

The analytic proof first verifies the killed generator \(K=Q^{\mathrm{ex}}-\operatorname{diag}(c_k)\), then derives its finite-horizon path-density tilt. Positivity on the open simplex of jump times yields global constancy of \(c_k\) from one-start/one-horizon equality; the subset-sum rank argument and the one-hole complement identity complete the classification.

Run `python3 verify.py` using a Python 3 standard-library interpreter. The shipped checker uses deterministic enumeration and a fixed pseudorandom seed. It passed 22,872 finite classification assertions when executed for this package. These checks compare pair-weight subset sums across a variety of small connected support graphs and verify exact boundary examples, rather than certifying a general theorem by exhaustion. Unbounded graph size and arbitrary positive real rates are justified by the written proof alone.

Independence, external certification and a formal proof assistant are not asserted. The scientific comparison has residual uncertainty about differently named older graph-weight or killed-chain classification results.
