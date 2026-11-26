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

The Lindblad equations give z_i(q)=-eta+q(z_i+eta) and b_i(q)=qb_i. In units of h, e_i(q) is the nonnegative upper root of F_i(u)=u^2-2z_i(q)u-qb_i; the other root is nonpositive. For e_1(q)>0, the sign of e_1-e_2 is therefore the sign of F_2(e_1)=q[2(z_1-z_2)e_1+b_1-b_2]. Implicit differentiation gives e_i'=e_i(e_i+2eta)/(2q sqrt(z_i(q)^2+qb_i))>0 on the positive locus. If b_1<b_2, initial ordering forces z_1>z_2 and e_1(1)>e_*>0; as q runs down from 1 to 0 the affine sign changes exactly once, and e_2>0 even if e_1 later vanishes. If b_1>b_2, e_1>0 and the affine sign is positive at both ends of the level range [0,e_1(1)]. For equal b, initial ordering forces z_1>z_2 and monotonicity in z excludes inversion; zero plateaux are not reversals. Substituting the unique level in the quadratic gives the quoted q_* and t_*. With A=2e_*z_1+b_1, q_*(0)=e_*^2/A<1, so dq_*/deta=2e_*(A-e_*^2)/(A+2eta e_*)^2>0, giving the fixed-rate time claim including the bath endpoints. Direct rational substitution for the frozen example gives e_*=7/40, q_*(0)=49/400 and q_*(1)=203/320.

## originality

PASS

The frozen record credits the already-known mixed-qubit coherence-ordering criterion and pure-input exact-time formula. The distinct portion is the analytic arbitrary-mixed-input positive crossing level and time, with uniqueness and comparison of temperatures at fixed total rate. The strongest prior treatment uses purity in its exact inversion and does not state the mixed-pair bath-independent work invariant.

## value

PASS

Knowing that the order reverses does not give the extractable work at reversal. The common work is an exact experimentally interpretable invariant of a natural shared thermal channel, separating two effects (unchanged work level, changed elapsed time). The formula answers a mixed-input question left open by the qualitative criterion and the pure formula and applies through diagonal and endpoint baths without a dynamical approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
