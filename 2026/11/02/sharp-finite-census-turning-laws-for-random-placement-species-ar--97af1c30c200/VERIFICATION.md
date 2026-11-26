---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the revised claim, the iid individual-absence probabilities give S(a)=(1-q)(1+G_n(q)) for (1,n), with q=1-a. The quotient derivative numerator is n(n-1)q^(n-2)(1+G_n)-(1+nq^(n-1))G_n'. For n>=3 its possible term of degree 2n-3 cancels; at lower degrees the printed coefficients are strictly negative through n-3 then strictly positive through 2n-4. At q=0 it is -1, and at q=1 the numerator is n(n-1)(n+1)/2 because G_n'(1)=n(n-1)/2. Descartes plus the endpoint signs gives one simple positive root in (0,1), and dq/da=-1 gives the strict global minimum in area. The n=1 and n=2 cases are constant and strictly decreasing, respectively. For n=3, solving 3q²+10q-1=0 gives the stated exact area. The census <=3 partitions are exhausted by all singletons, a single species, and (1,2). A single species with n>=2 has positive derivative in q since (n-1)G_n-qG_n' is positive, and all singleton cases are constant. Thus no smaller census can turn, whereas (1,3) does. The retained endpoint corollary is also correct: differentiating aS'/S at a=1 uses S=s, S'=r1, S''=-2r2, and a sign persists by continuity. The supplied script was read, not run; its radical comparison uses floating point, while the exact value follows from the quadratic. The proof independently establishes the universal claims.

## originality

PASS

For the frozen original's novelty scope, FAIL: the named terminal singleton/doubleton law is a mechanical derivative of He–Legendre's existing general equation and is not a separate originality contribution. The delivered repair keeps it explicitly as background, not in the Finding or slogan, and claims only the all-n singleton/common global turning classification and the sharp census-four onset across all abundance partitions. No inspected equivalent theorem or stronger result was found for this surviving scope; this judgment does not establish historical priority.

## value

PASS

The revised finding classifies scale-dependent elasticity for a natural extreme abundance pattern and shows exactly when a reversal is possible at the smallest total population. Even in a model with no spatial interaction, the local exponent can reverse; separating that effect from an assumed fixed log–log slope is useful. The all-n uniqueness and global census boundary, not the routine terminal derivative in isolation, support the value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
