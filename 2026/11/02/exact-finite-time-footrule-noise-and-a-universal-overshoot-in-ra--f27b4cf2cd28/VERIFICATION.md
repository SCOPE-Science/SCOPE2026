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

# Verification and limitations

The exact claim is derived by a four-eigenvalue decomposition of the ordered-two-position permutation representation and explicit arithmetic enumeration of the zero-, one- and two-step second moments, not by a simulation cutoff. The supplied `verify_footrule.py` requires only Python 3's standard library and reproduced all 59 checks: exact state-distribution recursion at \(n=4,5,6\) and \(0\le t\le5\), direct triple/quadruple combinatorial sums at \(4\le n\le12\), and numerical checks of the unique limiting maximum. In addition, symbolic identities were checked for the moment interpolation and stationary second-moment formula.

The all-\(n\), all-\(t\) assertion depends on the standard representation decomposition and the algebraic moment identities written in `RESULT.md`. The checker is corroborating evidence, not an exhaustive proof over all integers and not external certification. The resulting crossover holds at fixed rescaled observation time; no uniform finite-size maximizer convergence or quantum-walk counterpart is asserted. No independent audit has been performed.

Reproduce with `python3 verify_footrule.py`.
