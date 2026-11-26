---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The repaired finding is the exact coefficient-shape theorem. The background polynomial is correct: pairwise intersecting families lie in a star or are a triangle, and a family with a disjoint pair must remain on its four labels. The subtraction (1+2z)^3 excludes the intersecting subfamilies of the three-edge matching. Dividing by W=binom(n,4) gives a transparent coefficient table; the determinants at degrees five and four factor as W^2 H_5(n)/150 and -W^2 H_4(n)/(5(n-3)). The first is negative for the nine orders 13–21; H_4(22+s) has positive coefficients, proving the second is negative thereafter. Independent exact binomial arithmetic recovered the nine positive minima at orders 4–12, all modes through 13, and the 25025,24024,25025 dip at 14. From order 15 the low coefficients strictly increase through degree seven by the positive translated difference polynomials, and the binomial tail completes unimodality. The frozen maximal-set claims are mathematically sound (every proper candidate can be extended in its star or four-label support, and outsiders obstruct both kinds of full family) but are not part of the revised claim. The frozen scripts and output were inspected, not executed; the supplied shape checker in fact checks weak log-concavity, and the independent finite arithmetic and all-order proof address strictness directly.

## originality

PASS

For the repaired claim only. The frozen record presented the complete polynomial and maximal-set enumeration as distinct contributions as well as the shape theorem. The inspected same-family Resultary entry states both polynomials, maximal structures, purity and gaps. Its later path is not proof of relative discovery, but the two catalogue findings materially overlap on enumeration. The corrected result credits the formula as counting input, makes no priority claim for it, and removes the maximal-set theorem from the Finding. The remaining exact shape transitions are not stated or supplied by the inspected sources without the coefficient sign proof.

## value

PASS

The repaired theorem classifies two standard coefficient properties on a canonical infinite graph family, with a persistent log-concavity failure and an isolated nonunimodal order. This contrast survives independently of any priority for the counting formula; it is an all-order shape result rather than a finite table lookup or generic extremal graph bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
