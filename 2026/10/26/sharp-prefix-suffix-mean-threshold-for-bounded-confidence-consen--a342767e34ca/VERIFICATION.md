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

For the strict confidence rule on the ordered path, x_k is the maximum on the left and x_{k+1} the minimum on the right. Thus d_k <= Delta_k <= D_k. The sole update changing Delta_k is across k, with decrement mu*d_k*(1/k+1/(n-k)). A blocked cut cannot unblock because internal updates only move the two boundary opinions apart, and its two conserved means differ. Above Theta all edges are active; the product for a full sweep contracts the mean-zero sphere strictly, since equality at every norm-nonincreasing pair update would require every initial adjacent difference to be zero. Independent positive-rate clocks produce such sweeps infinitely often in disjoint windows of the edge word. Below Theta, repeating the edges on both sides of an omitted maximizing cut either freezes some edge in a finite prefix or forces the cut gap to converge to Theta, which also forces finite freezing. At equality, reaching the envelope requires a maximizing cut, no prior positive exchange across it, and two homogeneous blocks. When mu<1/2 all initially positive within-block gaps survive at every finite step. For midpoint updates a last positive gap cannot disappear in a block of length at least three, because that update creates a positive neighboring gap; singleton and pair blocks can be homogenized with at most one update each. The pair updates used for the exceptions are receptive because the strict initial order makes each initial adjacent gap strictly below its own centroid separation. This proves the n=3 and central-cut n=4 exceptions and excludes all others. Arithmetic progressions have D_k=nh/2 for all k. The independent rational replay includes a noncentral maximizing n=4 case (0,1,2,9), Theta=8, and recovers both stated small-size freezing examples. Finite replay is corroboration only.

## originality

PASS

The closest indexed three-agent sharp threshold uses a directed neighbor-average confidence gate and different conclusions. Primary Deffuant and averaging sources checked do not cover the deterministic profile criterion or the strict equality classification. Credit the existing averaging argument as background, not part of the distinct claim.

## value

PASS

On a natural sparse interaction graph this gives a computable exact criterion for consensus with probability one, including a constructive positive-probability obstruction on the opposite side and a nontrivial change at equality which depends on compromise and path length. The cut centroid identifies the invariant governing the threshold rather than just bounding initial neighbor gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
