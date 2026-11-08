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

# Reproducible mathematical checks

Run `python3 verify_sinkhorn.py` using only Python's standard library. On the supplied program, this returns `PASS: 624 rational identities, 1026 finite-iterate comparisons, 42 asymptotic spot-checks; total 1692.`

The 624 rational tests independently compute complete row-then-column sweeps and confirm the proposed fractional-linear map, its positive determinant factorization, and the off-diagonal row entries. The 1,026 finite-iterate checks examine the geometric projective cross-ratio and the bounded-time Riccati approximation. The 42 asymptotic spot-checks cover balanced, mismatched and critically mismatched marginals at multiple small kernel values. Direct execution tests can support algebraic consistency and detect mistakes, but do not prove uniformity over all positive real data or an asymptotic limit.

For analytic verification, first derive the exact map from the two componentwise balancing operations. Confirm its projective fixed points and eigenvalue ratio via its positive two-by-two representing matrix. Show the critical map expansion \(F_\delta(x)=x+\delta f(x)+O(\delta^2)\) on compact positive subsets, and show the positive fixed points remain uniformly bounded away from zero and infinity. Discrete Gronwall then yields a uniform \(O_T(\delta)\) difference from the Riccati solution. Separately expand the spectral discriminant uniformly for every \(b_\delta\to a\), dividing by the strictly positive scale \(\sqrt{(b_\delta-a)^2+4a(1-a)\delta^2}\). Finally compute the row-normalized fluxes and column residual directly from the multipliers. No external computational or independent scientific certification is claimed.
