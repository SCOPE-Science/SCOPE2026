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

## Checks
The standalone `verify.py` enumerates every induced three-vertex path and all vertex subsets of triangular graphs for \(n=2,3,4,5,6\). It determines general position independently by forbidden-path avoidance, then maximality by one-vertex extension, and compares every cardinality coefficient with a separate labeled-block recurrence derived from component weights. Exact assertions include \(M_4(z)=3z^2+8z^3\), \(M_5(z)=15z^4\), and \(M_6(z)=15z^3+60z^4+6z^5+10z^6\). It additionally checks the extremal degree bounds on recurrence-generated polynomials for \(3\leq n\leq49\).

Run `python3 verify.py`. The checker is finite and supplies no exhaustive evidence for arbitrarily large \(n\); that range is covered by the combinatorial proof in RESULT.md. No independent audit has been performed.
