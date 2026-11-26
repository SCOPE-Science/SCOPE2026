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

The derived space equals the center Z, and any automorphism inducing g on V must induce ∧²g on Z. Conversely these actions and arbitrary central shears preserve the bracket. Writing U for the projection of an ideal and W for its central intersection, the necessary and sufficient bracket condition is V∧U⊆W. For each admissible pair the ideal modulo W is a graph U→Z/W, with q^{u(3−w)} choices. A difference between two graph maps lifts and extends to a shear on V, so all the lifts of a fixed pair are conjugate. The dimensions of V∧U are 0, 2 and 3 for u=0, u=1 and u≥2, respectively. For u=0 the exterior action is the projective contragredient action on V*, transitive in each dimension; for u=1,w=2 the plane is forced by U; for w=3 only U varies. This proves transitivity and separation of all eight strata, including exactly three singleton orbits, four of size Q and one of size qQ. Sorting by u+w gives the polynomial and summing gives 3+(q+4)Q. The volume pairing is symmetric, nondegenerate and invariant (cyclically permuting the three exterior factors preserves sign), so ideal orthogonals give the claimed reciprocity also in characteristic two. A fresh exhaustive RREF and orbit calculation at q=2,3 found 2825 and 56632 subspaces, 45 and 94 ideals, and the exact eight orbits in each case; scripts and outputs are in /workspace/branches/2e4b655e-6ba3-43c6-9f6f-53577ab10954/. The frozen verifier was inspected, not run; neither prime-field test substitutes for the field-uniform proof.

## originality

PASS

Pass specifically for the full ambient automorphism-orbit classification of actual finite-field ideals, not for the aggregate count, the individual stratum counts without their orbit interpretation, or the dimension polynomial alone. A stronger indexed count gives every (u,w) stratum size and therefore all the numerical enumerators by specialization. It does not establish that each stratum is a single orbit. Nearby indexed orbit results classify different objects, and the primary zeta and abstract Lie-algebra classifications do not give the rank-three ambient action on these ideals in the inspected passages. The later displayed date of the count record does not by itself establish priority or dependence.

## value

PASS

In the first rank where the free two-step center has dimension three, the ideal dimension alone already fails to separate conjugacy: the two dimension-three types are the center and the qQ noncentral ideals forming a single other orbit. The result gives exact equivalence criteria, representatives and orbit sizes for kernels under changes of the full free algebra, including nongraded choices and characteristic two. This is useful information distinct from recomputing counts by dimension or identifying abstract algebra types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
