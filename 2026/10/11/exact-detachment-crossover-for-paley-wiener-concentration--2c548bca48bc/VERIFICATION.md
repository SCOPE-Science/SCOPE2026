---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

PASS for every fixed s>0 and joint epsilon->0, epsilon<=b_epsilon->0. From the exact E removal/addition identity D_0(E)=int_{r-epsilon}^r int_0^b -u_s'(x+t)dt dx and continuity of the prolate ground-state density derivative, D_0=-u_s'(r)epsilon*b[1+o(1)], with u_s'(r)<0 (Zelent (13)). The interval mass profile Phi_0(a)=int_{-r}^r u_s(x-a)dx has unique global maximum at a=0 (bathtub inequality from the strict inside/outside threshold), curvature Phi_0''(0)=2u_s'(r)<0. Uniform C^2 closeness of Phi_E to Phi_0 (symmetric-difference measure 2epsilon) forces its maximizer a_E to zero; Phi_E'(0)=int_{r-epsilon}^r[u_s'(x)-u_s'(x+b)]dx=O(epsilon*b) by bounded u_s'', so a_E=O(epsilon*b) and its gain over Phi_E(0) is O(epsilon^2*b^2). Thus D(E)=D_0+O(epsilon^2*b^2). Zelent Prop. 1 / eq (21) proves 0<=D(E)-eta(E)<=A_s D(E)^2; as D(E) asymp epsilon*b->0, eta(E)~ -u_s'(r)epsilon*b. The argument uses an analytic inequality and strict center-curvature, not experimental extrapolation.

## originality

PASS

Best-of-knowledge PASS narrowly for the explicit two-parameter leading coefficient, not the prior global concentration or stability theorems. Zelent 2026 introduces exactly this family and proves quadratic-versus-linear orders for two different regimes; its general inequality eta=D+O(D^2) is a strong pre-existing premise. The remaining new content is the asymptotic optimized discrepancy under a shrinking displacement, including quantitative recentering O(epsilon*b). A short standard Taylor argument suffices once that premise is known; therefore the priority and significance claim is intentionally limited to this exact unstated joint-limit formula. Direct searches found only the same assessed public record among exact formula hits, which is not independent evidence of priority. No inspected pre-existing statement gives the full two-scale coefficient. An unindexed corollary or routine extraction from Zelent remains a real residual risk.

## value

PASS

PASS as a motivated exact calibration of the canonical detached-piece example singled out by Zelent: the first-order deficit tracks displaced measure times distance with an intrinsic prolate boundary-slope constant, interpolating the adjacent epsilon^2 regime and genuinely mesoscopic epsilon=o(b)->0 regime. The specified infinite joint-scale asymptotic is useful for assessing whether weighted set discrepancies resolve the movement distance lost by symmetric difference. The calculation is short and heavily dependent on known general stability; it is not a broader theorem, a new stability method, a fixed-b coefficient, or proof of any numerical algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
