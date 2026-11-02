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

Reproduce with `python3 verify.py` (Python 3 standard library only). The script proves exact algebraic equality of the positive polynomial numerator used for the critical exponent-three far-transition case by symbolic two-variable integer polynomial arithmetic, checks 196,608 incentive comparisons by exact rational arithmetic over complete four-node weighted graphs with all six edge weights in 1 through 4 after shortest-path closure, and verifies an explicit strictly profitable exponent-four deviation. All checks passed in this package's preparation.

The universal three-agent strategyproofness proof is an analytic division into far-site, closest-pair and far-transition cases, including strict inequalities and ties. The finite metric enumeration does not cover all metric spaces, all real exponents or all possible deviation points. No independent external review or formal proof assistant validation has been performed. The most significant originality limitation is possible unindexed equivalent work on power-law randomized facility omission; the power-law welfare ratio and failure above exponent three were previously established and are not newly claimed here.
