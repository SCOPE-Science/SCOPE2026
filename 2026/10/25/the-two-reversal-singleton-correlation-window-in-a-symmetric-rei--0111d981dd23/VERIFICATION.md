---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The unit-reinforced q-color urn with one initial ball per color induces the uniform distribution on q-part weak compositions of n. Fixing N_1=1 and N_1=N_2=1 gives exact rational stars-bars moments p_1=(q−1)n/((n+q−1)(n+q−2)) and p_11=(q−1)(q−2)n(n−1)/∏_{j=1}^{4}(n+q−j). Exact symbolic common denominators give covariance =−n(q−1)F_q(n)/((n+q−4)(n+q−3)(n+q−2)^2(n+q−1)^2). Cubic F_q has signs F(-∞)<0,F(0)>0,F(q)<0,F(+∞)>0, hence precisely one negative and two simple positive roots. F_q(2) classifies initial q=3,4 vs q≥5 sign. Expansion at n=q+δ proves roots q±√q−3/4+O(q⁻¹ᐟ²); denominator asymptotics prove q² C→(1−s²)/32 in n=q+floor(s√q) and negative fixed-density qC limit. Independently compared exact weak-composition probabilities in multiple finite (q,n) and symbolic polynomial identity.

## originality

PASS

Qualified PASS: uniform Dirichlet–multinomial composition law, occupancy moments, CLTs and finite-coordinate approximations are classical. Keener–Wu 2006 work on aggregate occupancy and order-q⁻² approximation does not determine the sign of the critical order-q⁻² singleton pair covariance. The exact three-root phase diagram and root-center shift −3/4 were not located as prior theorem. Relevant 1981 Chen source full article inaccessible; substantive historical priority risk retained.

## value

PASS

PASS: the model is canonical and the exact two-sign-reversal phenomenon is a substantive finite-size dependence effect with a sharp √q critical window, resolving precisely when pairwise dependence changes sign. This is a structural occupancy statement rather than a routine sign check on a random example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
