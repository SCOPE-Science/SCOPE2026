---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two simplex normal directions are excluded, and the surviving Fourier modes give conjugate blocks with characteristic polynomial λ²+(a+1−i)λ−i. The larger-real-part root is continued from i. Its imaginary part v starts decreasing, cannot hit 0 (which would require d=1=a+1 at positive a) or 1 (which would require d=0 and a=0), and cannot change the smaller d-root of (1−v)(d²+v²)=d because the discriminant is bounded below by 3/4 on [0,1]. The resulting d<1/2 means the companion root is strictly faster. Implicit differentiation gives dv/da<0 and the slow root tends to 0 at infinity. The damping d vanishes at both endpoints (d~a/2 and d~1/a²); its interior stationarity reduces to the strictly increasing quintic in the finding. At the maximum, F_d<0 and F_vv=2−6v<0 for F=(1−v)(d²+v²)−d, giving nondegeneracy. Independently optimized the original block eigenvalue and checked the quintic bracket exactly: v=0.654193472255910175741, a=0.60235493398134220867, d=0.156459729915040441875. Replay: python /workspace/calculations/reproduce_frozen.py (check dormancy). Global uniqueness is analytic, not inferred from the numerical optimization.

## originality

PASS

Best of current knowledge: the model and deterministic stabilization are antecedents. The supported distinction is the sharp exchange-rate optimum on the matched-frequency slice and its two endpoint slowdowns, not the existence of damping or stochastic coexistence.

## value

PASS

Comparative recovery speed is scientifically distinct from stability at every positive rate. Matching reactivation to the active oscillation timescale removes an independent physical ratio rather than inserting an arbitrary numeric parameter; the exact unique rate and two slow-decay limits quantify when stronger exchange is counterproductive. The result is useful on this slice without asserting nonlinear global recovery or stochastic persistence optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
