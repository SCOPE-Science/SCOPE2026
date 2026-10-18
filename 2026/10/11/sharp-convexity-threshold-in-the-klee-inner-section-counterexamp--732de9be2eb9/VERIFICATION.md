---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n>=3 and 0<=epsilon<1, the meridian radial function is positive. Direct independent symbolic differentiation proves that r^2+2(r' )^2-r r'' has the sign of F_epsilon(c)=1+epsilon(2c-c^3), c=cos(phi). The cubic has its unique global minimum -4sqrt(6)/9 at c=-sqrt(2/3); endpoints give -1 and +1. Thus 3sqrt(6)/8 is the exact convexity bound, strict positivity below it, one zero curvature latitude at it and negative curvature above. The Hausdorff limit argument correctly retains endpoint convexity. Independent SymPy simplification returned zero for the curvature factorization; finite checks were not treated as proof.

## originality

PASS

Best-of-knowledge PASS for the *exact maximal convexity parameter* of the specific radial family. Gardner–Ryabogin–Yaskin–Zvavitch Lemma 3.2 gives the same curvature expression and a sufficient numerical 0.91 but does not identify the exact global minimization. A Resultary record on a cubic support function has the same radical but different geometry and is not an implication. Any folklore exact endpoint remains a historical priority risk.

## value

PASS

PASS: the family is a geometrically canonical input to the Klee inner-section counterexample, and the full sharp geometric convexity range is a natural unknown exact invariant. The improvement beyond the published 0.91 is numerically small, but the mathematical object is an exact endpoint and first degenerating latitude; it is not presented as extending all other analytic conditions in the counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
