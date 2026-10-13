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
# Reproducibility and scope

Run `python verify.py` with any recent Python 3 interpreter; only built-in modules are imported. The script enumerates all cyclic relative-order words with \(r\in\{2,3,4,5\}\) labeled chord pairs. For the six local events, total/favourable counts are respectively \((6,2)\), \((90,12)\), \((90,6)\), \((2520,72)\), \((2520,40)\), and \((113400,720)\). These checks are exhaustive for the **specific finite supports used in the proof**. The algorithm enumerates full matchings for \(3\le n\le7\) independently of local word counting, and compares the first and second moments exactly as fractions.

The theorem for arbitrary \(n\ge3\) rests on two symbolic steps established in the proof: independence for disjoint label supports, and the exact enumeration of every shared-label overlap case. Parameter checks across further finite \(n\) serve only as arithmetic checks. No finite experiment proves asymptotic distributional convergence; none is claimed. The \(20/21\) correlation limit is an algebraic consequence of exact polynomial expressions. Historical priority and an independent scientific audit remain unverified.
