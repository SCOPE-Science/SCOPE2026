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

The attached standalone `verify.py` uses only the Python standard library. Execute it with `python verify.py`; its direct reference routine computes the utility of every selected agent using exact rational arithmetic and examines every nonempty subset, independently of the threshold-counting formula.

Successful execution compared the full polynomial coefficient sequence on 2,628 complete labeled partitions for \(1\leq a,b\leq4\), \(a+b\leq7\), including 19,814 coefficient comparisons. It also compared 450 reproducibly seeded partitions with \(1\leq a,b\leq6\) and 90 matched-pair configurations with \(1\leq a\leq9\), \(0\leq m\leq9\). The checker tests that the matched-pair partition is core-stable exactly for \(m\leq1\), that \(M(a,2)=a\), and that \(M(3,5)=132\).

Proof boundaries: exhaustive finite verification does not establish the general theorem; that follows from the eligibility inequalities, bijection to selected eligible subsets, and the central limit theorem. No independent external audit has been performed. Integer-arithmetic operation counts ignore input/output bit costs.
