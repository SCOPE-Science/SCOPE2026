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

The strict Jury conditions for z^2-ap z-a(1-p) are |a|(1-p)<1, a<1, and 1+a(2p-1)>0; their convex-weight feasible union is -3<a<1, whereas p=1/2 permits -2<a<1. Yule-Walker elimination yields V/sigma^2=(1-a+ap)/[(1+a-ap)(1-a)(1-a+2ap)]. Symbolic differentiation gives d(V/sigma^2)/dp=2a^2 Q_a(p)/[(1-a)(1+a-ap)^2(1-a+2ap)^2]; Q has its unique feasible root p*=sqrt(1-a)/(1+sqrt(1-a)), is negative before, positive after, and p* passes all strict Jury conditions. At a=0 all weights tie at sigma^2. With t=sqrt(1-a), V*=sigma^2/[t^2(2-t)^2] and (a+3)^2 V*/sigma^2 ->4. Independent sympy exact derivative, exact-radical substitutions and limit passed, corroborating the algebra.

## originality

PASS

Best-of-knowledge, with material uninspected-source risk: the jointly optimized fixed-p convex AR(2) noise variance, sharp -3 stability frontier and exact critical singularity are not established by the accessible abstract of the motivating deterministic moving-average paper or by the nearby Resultary records. The entire 38-page source could not be read.

## value

PASS

Convex two-lag memory weights are a natural tuning variable with fresh stochastic iteration errors. The complete best feasible feedback range -3<a<1, uniquely noise-minimizing weight for a!=0, and variance singularity coefficient 4 form a usable stability-versus-noise design diagram; not a mere rewriting of an unconstrained AR covariance identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
