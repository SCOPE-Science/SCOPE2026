---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Read RESULT.md, proof and full tree_cut_verify.py. The clique complex of K_m □ T consists of t contractible column simplices plus m parallel edges over each tree edge; tree incidence has an integral right inverse, yielding H^1= (Z^m/Zdiag)⊗Z[E(T)]. A tree automorphism changes all bipartition-oriented edges by the common sign χ_T; ambient Alexander duality contributes ε=sign(σ)^t sign(a)^m. This proves integral H_{mt-4}=εχ_T⊗U_m⊗P_T with all other reduced groups zero, including mt=4 degree zero. The non-split exact sequence has order m: invariant Hom restriction Z→Z multiplies by m, the explicit equivariant lift s([z])=mz−sum(z)diag proves the upper bound, and restriction to S_m and projection to one tree edge proves lower bound. Independent small-face Euler enumerations matched three boundary cases; source verifies 192 signed traces on 10 trees.

## originality

PASS

Chauhan–Shukla–Vinayak prove the path-factor nonequivariant wedge of (m−1)(t−1) spheres, not arbitrary branching trees or integer actions. Carnero Bravo v3 §5.4 treats Cartesian products of paths and products of complete graphs, not products of one complete graph and arbitrary tree or the precise order-m integral extension. Total-cut symmetry papers examine different complexes or graph families.

## value

PASS

A complete infinite-family integral homology Γ-module for arbitrary branching trees substantially refines path-only wedge ranks. The canonical weight-lattice extension has exact unbounded order m but no torsion in ordinary homology, a sharp symmetry obstruction that disappears rationally and distinguishes natural group lattices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
