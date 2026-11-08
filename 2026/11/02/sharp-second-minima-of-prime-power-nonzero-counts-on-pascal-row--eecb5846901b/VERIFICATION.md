---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Kummer borrow counts permit a digit-by-digit T_d(z) transition for the valuation distribution of binomial coefficients. Strict digitwise monotonicity of A_{p,alpha}(n) reduces a second minimum on [N,pN) to elementary rows N+p^j or 2N (for p>=3). The displayed transition product yields closed borrow polynomials for N, N+1, 2N and N+p^j. Exact truncation to valuations below alpha and exhaustive comparisons across h<alpha, h=alpha and h>alpha prove the nine-row table including all binary exceptions and odd-prime ties. Independent direct integer-binomial checks were run for small p,alpha,h and reproduced all minimum positions; this does not replace symbolic all-parameter comparisons.

## originality

PASS

Best-of-knowledge: critical exact claim compared by mathematical implication with prior work, with recognized prior components and explicit access/unlocated-priority risks; no novelty is inferred solely from failed search.

## value

PASS

After classical per-row binomial valuation formulas, identifying the uniformly second-smallest nonzero count and full equality set across all primes, all alpha>=2 and all digit heights is a new natural extremal classification rather than an arbitrary row calculation. The h=alpha transition and exact exceptional ties are mathematically interpretable and reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
