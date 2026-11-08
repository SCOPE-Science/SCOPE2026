---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read pinned RESULT.md and checker. Subtracting nonlinear weighted vertex equations gives edge equation with neighbors a_i=c_{i-1}/m_i, b_i=c_{i+1}/m_{i+1}, diagonal d_i=c_i(1/m_i+1/m_{i+1}). A max absolute edge has normalized value 1; cyclic closure sum e_j=0 yields four feasible neighbor regions. n=3 neighbors sum -1 (strict p>2 minimization or concave p<=2 endpoint); n=4 neighbor sum in [-2,0] (H=|a-b|); n=5 neighbor sum<=1 and monotonic optimum x+y=1 (concave p<2 power norm / max for p>=2); n>=6 neighbors can both be 1 using remaining -3/(n-3). Every scalar optimum is integrated to real cyclic vertex slopes, giving an attained instantaneous K=max(H-d), not merely an upper bound. Dini max rule + convex flow well-posedness proves L nonincrease iff K<=0. For n>=6 sum_i(a_i+b_i-d_i)=0; K<=0 forces equality of mass-weighted differences and then all c_i equal. Pentagon c=(1,1,1,1,3/2) yields unique p≈1.336485730165 transition via strictly decreasing ℓ_r norm. Independent 500 exact rational p=3 witnesses and root check corroborated finite cases; general proof is analytic and includes p=2 method as antecedent.

## originality

PASS

Best-of-knowledge PASS for the nonlinear all-positive-weights, all-cycle-length *sharp one-input* gradient coefficient and long-cycle rigidity, not the p=2 curvature-based criterion. Mugnolo's graph p-Laplace semigroup is vertex-space contractive, which does not generally imply unit-edge Lipschitz contraction. Hua–Mugnolo addresses time/long-time behavior; Münch–Wojciechowski characterizes general *linear* p=2 Lipschitz gradient decay through Ollivier curvature. Earlier homogeneous cycles and weighted trees lack arbitrary cycle conductance closure. No covering nonlinear weighted-cycle statement identified; full extended graph-gradient literature not exhausted.

## value

PASS

The sharp necessary-and-sufficient edge gradient contraction test is a natural regularity question for a nonlinear diffusion on weighted graphs. The four qualitatively different cycle-length regimes, exact p-sensitive five-cycle threshold and rigid six-edge conductor obstruction are substantive structural boundaries rather than routine parameter substitutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
