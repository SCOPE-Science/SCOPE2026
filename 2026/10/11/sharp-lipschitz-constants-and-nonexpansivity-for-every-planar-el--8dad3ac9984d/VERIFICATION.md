---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Every nonzero line direction w in real ell_p^2 has linear nearest-line projection Π_w(x)=w[J_q(w)·x]/(|w1|^q+|w2|^q), because the minimizing residual must be proportional to the duality map of a perpendicular functional. Its rank-one operator norm is R_p(w) and is >=1 by Π_w w=w. Unique nearest-point projection onto any pointed solid cone with independent rays u,v selects from four linear maps I,0,Π_u,Π_v depending on feasible face. Continuity of strict convex metric projections and subdivision of arbitrary line segments where two candidate linear maps agree yield global Lip<=max(1,R_p(u),R_p(v)). For each boundary ray there exists an input with strict KKT inequality on the other ray and positive active-ray coefficient, so a full neighborhood uses Π_u or Π_v; its rank-one norm gives matching lower bound, while the cone interior gives 1. Equality in Hölder for R_p(w)=1 requires p=2, or w with one coordinate zero or equal coordinate magnitudes. Check both independent rays for exact nonexpansivity classification. Independent deterministic candidate-map numerical experiments for p=1.7 and p=3.4 corroborate the sharp constant; optimization solver inaccuracies were resolved by direct candidate verification, not misreported as counterexamples.

## originality

PASS

PASS with bounded risk: the published scaled Lorentz cone theorem computes R_p for the two symmetric rays only, not arbitrary skew wedges, and its n>=3 obstruction is irrelevant. Domokos–Marsh supply metric projection and duality-map machinery without an exact all-wedge Lipschitz constant. Real ell_p has few linear isometries for p!=2, so the symmetric wedge result does not imply all asymmetrical cones via rotation. Other projection studies involve weighted ℓ1 balls or Euclidean metric. Possible unindexed classical planar formula remains.

## value

PASS

The sharp global stability of nonlinear cone metric projection is a natural normed-geometry invariant; the two-boundary-ray max formula and complete geometric nonexpansivity classification for *every* pointed solid planar cone extend the known symmetric one-parameter cone into a genuinely general two-generator structural theorem with explicit attainable local norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
