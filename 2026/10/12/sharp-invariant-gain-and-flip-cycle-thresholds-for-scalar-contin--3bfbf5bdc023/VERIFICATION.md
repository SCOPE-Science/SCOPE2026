---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For scalar plant x_dot=(a-k)x with u=-kx, J(k)=(1+k^2)/(2(k-a)), k>a. Differentiation yields F_t(y)=y+t(y^-2-1) after y=(k-a)/sqrt(1+a^2), t=eta/(2sqrt(1+a^2)). The global convex minimum F_t((2t)^(1/3))=(3/2)(2t)^(1/3)-t is positive iff 0<t<3sqrt(3)/2, proving strict all-gain invariance. Only positive fixed y=1 has multiplier 1-2t, stable iff 0<t<1. Distinct prime two-cycle equations imply s²=2p(p+1), t²=2p³/(p+1), p=uv>1; last expression strictly increases p>1 from 1 to infinity, giving exactly one positive cycle for t>1. Two-step multiplier M=5-8p+8/(p+1) strictly decreases from +1 and crosses -1 at 4p²+p-7=0, p=(sqrt113-1)/8, t*=1.25819035934. Independently checked symbolic t² relation, multiplier algebra, and numerical threshold. Package symbolic program also checks explicit p=9/8 witness M=-4/17. The assertions classify only hyperbolic endpoints, not global basins or t=1,t=t* nonhyperbolic behavior.

## originality

PASS

Original same scalar LQR Euclidean policy-gradient map is classical in continuous-time LQR optimization. Reviewed literature supplies small-step safety and descent, not sharp global positive-half-line invariance followed by a locally attracting nonoptimal prime two-cycle in the same strictly convex cost landscape.

## value

PASS

The theorem sharply distinguishes feedback-gain feasibility from convergence, identifies distinct invariant/fixed-point/cycle thresholds with a radical exact witness, and exhibits a structurally motivated counterexample to interpreting stability of learned controllers as optimization convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
