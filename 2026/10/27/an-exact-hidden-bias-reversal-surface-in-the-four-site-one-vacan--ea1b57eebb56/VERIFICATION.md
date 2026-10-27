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

# Verification and scientific limits

Run `python verification.py` in an environment with SymPy. The program builds a three-particle four-site generator via allowed exclusion hops and computes stationary weights as signed principal minors. The exact rational expression, even current, quadratic coefficient, and nonreflective balanced-sums witness are checked by polynomial reduction. Two smaller-ring particle-sector identities are also checked. On execution, it reports 21 passing checks. Source is the embedded standalone `verification.py`, not a log from another package.

The factorization plus the Markov tree theorem, not finite parameter checks, establishes the universal claim. Positive escape rates and \(|\varepsilon|<1\) are required. Only the leading codimension-one all-bias parity classification is claimed as evaluated structural content; a general periodic-walk velocity law existed in the literature. Independent audit has not been performed.
