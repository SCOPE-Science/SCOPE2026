---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical and numerical verification

The exact pre-aeration solution is \(g(t)=aL_0(e^{-at}-e^{-bt})/(b-a)\). Across a reset at \(s\), the downstream solution is \(g(t)-(1-q)g(s)e^{-b(t-s)}\). A strictly increasing upstream maximum and a strictly decreasing downstream maximum determine the unique optimum; hence finite computational grids are not used to claim global optimality. Differentiation gives the post-reset critical point \(h(s)\) and its curvature \(-abm(s)\); expansion of the balancing equation at \((s_\infty,T_c)\) verifies the second-order saturation coefficient.

Run `python3 CHECK.py` with a standard Python 3 installation. Expected output: `PASS: 200 randomized 101-point placement scans, exact example, endpoint checks`. The script verifies the exact parameter example \(a=1\), \(b=2\), \(q=1/2\), \(L_0=1\), computes critical threshold and limiting coefficient, checks short-length limits, and compares the analytic optimum with 101 grid placements for each of 200 reproducibly seeded random parameter draws. This is finite cross-checking and not an exhaustive proof of the theorem. No full-text validation of the inaccessible Koivo–Phillips (1975) source or independent scientific audit has been performed.
