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

The proof is analytic. On the full real six-coefficient jerk family with \(b_4\ne0\), differentiation of the displayed polynomial \(P\) gives \(\dot P=b_4x^2+(b_5-b_8)y^2\). SymPy exact assertions in `CHECK.py` check this identity, the explicit harmonic witnesses for \(b_4(b_5-b_8)<0\), the stationary harmonic moments, and the published table's nine signs.

The global conclusions use the invariance of omega-limit sets of bounded forward trajectories, the restriction of the zero-derivative locus to the origin, and flow invariance of compactly supported measures. Neither a finite symbolic check nor numerical simulation establishes these infinite-time dynamical steps; their complete arguments are given in `RESULT.md`.

The closed-sign theorem assumes boundedness only for the forward convergence assertion; it does not establish universal boundedness. Its compact invariant set assertion is two-sided. The opposite-sign construction establishes existence for suitably chosen remaining coefficients, not for every individual equation. The bibliographic overlap comparison has a residual risk from inaccessible full text of a 2015 zero-Hopf study and unindexed literature.
