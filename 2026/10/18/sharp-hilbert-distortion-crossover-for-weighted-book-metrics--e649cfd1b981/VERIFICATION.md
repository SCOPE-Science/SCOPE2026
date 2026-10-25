---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The actual Lipschitz dual ball of the weighted m-leaf/two-hub graph is N_H=max(|h|/H,|h|+max_i|z_i|), H=t/2. All triangle inequalities hold exactly for 0<t≤2; leaf differences are implied by spoke distances. Independently changing coordinate signs and permuting leaves preserves this norm, so averaging arbitrary positive quadratic forms at fixed sandwich constants cannot worsen their ratio and restricts the global Banach–Mazur optimization to q_r=rh²+Σz_i². Direct extremization gives outer radius max{m,rH²+m(1−H)²} and inner radius min{rH²,r/(r+1)}, with the spoke minimizer feasible exactly when it beats the hub facet. The piecewise ratio decreases up to r=max(H^−2−1,m(2−H)/H), then increases; comparison yields τ_m=2/(m+sqrt(m²−m+1)) and stated two branches, both uniquely minimized in t at τ_m. The dual-to-primal Hilbert distance identity is standard. Exact rational reconstructed minimax checked 25 dimension/parameter cases against 299 rational positive shapes each; finite sampling is not a proof of the all-real optimization, which was verified analytically. Nonmetric t=0 is correctly excluded.

## originality

PASS

Best-of-knowledge originality of the actual final claim, with explicit antecedent coverage and residual risk. None of the compared theorems implies both branches and the optimal τ_m=Θ(1/m); reducing to exact quadratic radii and optimizing is a separate nontrivial argument.

## value

PASS

Banach–Mazur distortion to Hilbert space is a natural quantitative invariant of transportation/free spaces. The complete dimension-parameter formula includes a sharp crossover between two geometrically different active constraints and a unique optimal hub length shrinking as m^-1; this is not a routine substitution into a pre-existing graph-wide theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
