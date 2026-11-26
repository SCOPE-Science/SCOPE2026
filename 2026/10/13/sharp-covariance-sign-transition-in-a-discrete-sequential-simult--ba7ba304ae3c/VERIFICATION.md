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

At the first trial with either shock, the time A has the zero-based geometric law with parameter d. The type of that trial, independent of A, is common-fatal (including both streams succeeding together) with probability v/d, or sequential-only with probability rb/d. In the latter case the gap L to the next fatal event is an independent geometric wait on {1,2,…} with parameter d; otherwise L=0. Thus Var(A)=ab/d² and E L=rb/d². Since A,L and the Bernoulli orientation I are independent, the covariance of A+(1−I)L and A+IL is Var(A)−θ(1−θ)(E L)², using I(1−I)=0; conditioning on I leaves Var(A)>0. For an independent sign check, multiply by d⁴/b>0: the sign equals that of F(b)=a(1−ab)²−cr²b, which decreases strictly in b. At b=0 it is a>0 and at b=1 it is r²(a−c), proving the all-v and unique-transition cases including strict interior positivity at a=c. The substitution π=v/d is strictly increasing and yields (1−π)(1−aπ)=a/c at a zero; the smaller quadratic root is exactly the displayed π*, followed by inverse v*=rπ*/(1−aπ*). Numerical live-state propagation with trials 0–159, separately accumulating deaths and paired death products, gives covariances −0.130508276920493 at (r,v,θ)=(.9,.1,.5), +0.0112979568872811 at (.9,.7,.5), approximately zero at v=.5496502702061786, and +0.00724118921310 at the equality regime (.75,.01,.5); these checks do not replace the full-support proof. RESULT.md, VERIFICATION.md and checker.py read, frozen checker not executed. Scope is independent iid Bernoulli streams and independent orientation with parameters strictly in (0,1); no unconditional quadrant-order result follows.

## originality

PASS

The Lee–Cha experiment and its joint probabilities are prior. The supported distinct contribution is the exact unconditional covariance and necessary-and-sufficient sign diagram, in particular the transition in tie probability despite positive orientation-conditioned covariance. The closest inspected prior conditional-dependence result is not an unconditional sign result.

## value

PASS

The all-parameter sign diagram answers when a common-fatal shock overcomes the opposing effects of randomly assigning an earlier and later failure. It provides a usable diagnostic based on observable tie mass and demonstrates a reversal despite positive covariance in both strata, with an exact boundary rather than a selected instance. This is specific to the motivated reliability experiment and does not confuse covariance with quadrant dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
