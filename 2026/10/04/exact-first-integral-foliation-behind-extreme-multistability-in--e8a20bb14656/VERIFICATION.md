---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Use exactly the 2019 five-state polynomial system x_dot=y, y_dot=z, z_dot=w, w_dot=(41/25)x²-(51/50)w+v+(7/25)xy, v_dot=(121/50)xw-(3/10)yz. Direct differentiation of I=v-(121/50)xz+(34/25)y² yields zero IDENTICALLY; ∂I/∂v=1 makes each M_C={I=C} a global smooth invariant 4-manifold and allows v=C+(121/50)xz-(34/25)y². On M_C equilibria require y=z=w=0 and C=-(41/25)x²: none for C>0, one at C=0, two x=±sqrt(-25C/41) for C<0. The reduced linearization has quartic λ⁴+(51/50)λ³-(121/50)x λ²-(7/25)x λ-(82/25)x. Routh-Hurwitz gives stable negative branch exactly x<-213282/38297 (and corresponding C<-1865057672484/36666505225), while positive branch has a positive real root. At equality there is a simple imaginary pair ±i sqrt(8364/5471); independently evaluated the nonlinear first Lyapunov coefficient at the boundary as +28979146362140275630693 sqrt(11439861)/59821451963209362724599892320 >0 under the standard normalized eigenvector convention, which confirms weak instability at equality rather than confusing marginal linear stability with asymptotic stability. For any compact invariant K lying on one M_C, a trajectory converging to K must have I=C by continuity of invariant I; its basin lies in that codimension-one leaf and has no 5D open basin. This does NOT deny attractors relative to leaves or an attracting union of many leaf levels. The published v(0)-scan changes C affinely and its no-equilibrium section is a derived, source-specific fact.

## originality

PASS

Best-of-knowledge PASS for the EXACT polynomial conserved integral and complete sharp leafwise equilibrium/stability classification on the very Ahmadi et al. 2019 five-variable model. The source primary paper and Hens et al. 2015 full OA paper were materially read. Hens and Ngonghala explicitly anticipated GENERAL conserved-quantity slicing and measure-zero full-space basins in other coupled models; hence those abstract concepts are not novel. However neither implies I=v-2.42xz+1.36y² or the exact C/x thresholds for the 2019 system. The distinction is central, not hidden under a title search.

## value

PASS

The exact I is a nontrivial missing structural invariant for the flagship extreme-multistable 2019 five-variable flow. It reduces the effective dynamics from five to four dimensions, gives an exact no-equilibrium region in the article's numerical initial-data scan, makes the otherwise approximate equilibrium stability boundary rational and sharp, and explains why individual pictured leaf-attractors have no full-dimensional open attraction basin. While generic conserved-foliation principles are known, their source-specific realization and exact quantitative consequences directly clarify the motivating model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
