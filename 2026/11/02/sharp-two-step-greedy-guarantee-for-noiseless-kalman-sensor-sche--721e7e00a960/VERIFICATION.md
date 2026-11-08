---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Direct posterior covariance propagation gives J11=(1+a2^2)p2+q2, J12=p2+q1, J21=p1+q2, J22=(1+a1^2)p1+q1. For p1>=p2, greedy G=min(J11,J12) and O=min(G,J21) because J22>=J12. Comparing them gives strict regret iff p1-p2<min(q1-q2,a2^2 p2). If greedy is suboptimal, G/O<=(1+a2^2)p2+q2 over p1+q2 <=1+a2^2, with analogous relabeling. p1=1+delta,p2=1,q1=R+2,q2=delta attains limit 1+R as delta down to zero, R=max a_i^2>0. Independently regenerated 2500 rational schedule tables and exact greedy/optimum expressions, including 360 strict-regret samples. The boundary R=0 gives ratio one; positive process noise means supremum may not be attained.

## originality

PASS

General finite-horizon Kalman scheduling and greedy nonoptimality are established. The precise four-schedule and sharp two-time boundary is narrower than published general mixed-integer scheduling or longer-horizon hardness. Primary Dutta et al. has positive measurement-noise formulation and does not state the exact noiseless sharp ratio in the inspected methods/results. A special-case corollary of generic greedy results elsewhere is possible.

## value

PASS

This is the minimal two-state, two-time instance permitting greedy regret, and supplies an exact, stability-dependent approximation ratio and tight witness rather than an arbitrary small simulation. It separates stable factor <=2 from dynamics-uniform unboundedness and explains why positive-noise counterexamples persist by continuity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
