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

The supplied \(verify.py\) recomputes the bivariate polynomial symbolically, rather than interpolating from a few numerical values. It checks both eight-vertex edge sets and their orbit quotients and exhausts all faithful \(C_2\)-actions on graphs through seven vertices using graph-atlas representatives. The exact polynomial difference is displayed in \(RESULT.md\). \(verification_output.txt\) contains the executable's actual output, including the nonzero orbital difference and the number of deduplicated lower-order cases.

The lower-order enumeration uses the published complete standard graph atlas as its finite universe and NetworkX's graph-isomorphism enumeration; this dependency is listed in \(requirements.txt\). It is not an independent third-party mathematical audit. No inference from finite experiments to an infinite statement is made.
