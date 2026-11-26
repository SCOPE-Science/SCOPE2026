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

The change u=de x, θ=dy mod 2π preserves the angular increment. A quotient fixed point has u=2πj=A/(1−k cos θ)>0, so j is positive and cos θ=(1−r_j)/k completely gives existence and multiplicity. The trace is 2−r_j, and the two determinants are 1−r_j±S_j; on the positive-sine branch the Schur quantities are S_j, 4−2r_j+S_j, and r_j−S_j. The middle one is positive since r_j<2. The negative-sine characteristic polynomial is negative at 1, proving a real multiplier >1. The phase-merger endpoints have eigenvalue 1, and S_j=r_j in the interior gives a unit complex pair; no nonlinear classification at those boundaries is needed. In the explicit family r_m=1+t and r_{m+1}=1−t. The larger of the ratios S_j/r_j has square π²/m² times (1/50+1/[10000(m+1)²]), strictly below one. The integer band A/[2π(1+k)]≤j≤A/[2π(1−k)] lies strictly between m−1 and m+2 and contains m and m+1 in its interior; the strict margins persist locally. A hyperbolic sink gives summable increments u_n−2πj after the orbit reaches its local neighborhood, hence the stated lift with an orbit-dependent constant and open disjoint basins. The bound |u_{n+1}|≤A+k|u_n| gives liminf u_n≥A(1−2k)/(1−k)>0 at the explicit k_m, proving global eventual upward drift without claiming a global limiting speed. Independent exact band and Schur-margin tests at seven indices, with supplementary direct eigenvalue checks, agree. Replay: python /workspace/branches/independent_replay.py 3.

## originality

PASS

On the available statement-level evidence, the supported contribution is the explicit coexistence of adjacent attracting windings in this specific cosine map, with an exact one-step census and coexistence points as k tends to zero. A staircase in the dissipative standard map, plane drift without a compact invariant measure, and translational replicas of a bounded attractor are not equivalent to that statement. The two relevant 2022 primary texts have unresolved access limitations, so this is not priority clearance against their full mathematical content.

## value

PASS

The exact construction turns qualitatively similar planar escape into two robust and strictly different selectable velocities, with a complete count of the one-step candidates at those parameters. The weak-feedback sequence shows this is not just a large fixed-feedback numerical coincidence. The proof of basin-dependent winding speeds is stronger than the separate coordinate drift bound and is the substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
