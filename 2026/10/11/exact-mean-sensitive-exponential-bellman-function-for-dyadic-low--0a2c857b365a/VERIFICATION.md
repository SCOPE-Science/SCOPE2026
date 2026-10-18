---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

Normalize ess inf on the root interval to zero and BLO seminorm <=1. In the dyadic child split write a=(a0+a1+d)/2 and d between child minima. The affine Bellman candidate B_lambda(a)=1+Ca with C=(e^lambda−1)/(2−e^lambda) is a supermartingale: for d≤1 use convexity e^{lambda d}−1≤(e^lambda−1)d; for 1≤d≤2 use a1≤2−d and e^{lambda(d−1)}(1−(e^lambda−1)(d−1))≤1. Martingale approximations and Fatou transfer the bound to arbitrary integrable BLO functions. Geometric dyadic staircases have BLO=1 and root excess a, achieving the envelope for each a and diverging at lambda≥log 2. Independently checked all child-inequality boundary regimes numerically as diagnostics only; analytic inequalities supply proof.

## originality

PASS

PASS for the exact fixed-mean a-dependent binary-dyadic lower-centered exponential Bellman envelope and matching extremizers. Osękowski 2014 proves a sharp threshold/denominator for a different maximal-function observable centered at f_Q, not this full affine conditional local-mean envelope; Zhang 2026 studies standard non-dyadic interval tail bounds, not the target statement in inspected material. Passarelli 1996 full text unavailable, retained as unresolved priority risk without using lack of access as automatic failure.

## value

PASS

The envelope solves a natural complete extremal Bellman problem: it determines every local mean a in [0,1], the sharp λ phase transition at log2, and exact extremizers. This adds nontrivial mean sensitivity beyond known global maximal-BLO bounds, with explicit dyadic construction rather than routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
