---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For any prime power q>=2, the normalization t->(1:t+t^q:t^{q+1}) identifies exactly non-Fq conjugate pairs in P1(Fq²), producing δ=q(q-1)/2 ordinary Fq-rational nodes with Frobenius-conjugate branches. Gluing trivial line bundles along the normalization gives geometric Pic^0=(G_m)^δ; descent exchanges gluing ratios and each factor is a nonsplit norm-one torus, with Frobenius -1. PGL2(Fq) is transitive on unordered pairs and its stabilizer is the normalizer of the nonsplit torus, dihedral of order 2(q+1); branch swapping gives signed induced integral character lattice Ind_H^G Z_ε. Exact integral coinvariants are Z/2, not a rational invariant calculation, so group-scheme fixed points are μ_2, including nonreduced μ_2 in char2. For q=5 the subgroup under S5 corresponds to S3×S2 with sign on S3; Pieri multiplication s_111*s_2=s_311+s_2111 gives rank6+rank4. Independently programmed PGL2 signed actions for q=2,3,5 verified pair transitivity, index, stabilizer sign counts and character norm squared 2 at q5. This finite evidence is not the all-q proof.

## originality

PASS

PASS best-of-knowledge for full equivariant integral torus character lattice, uniform scheme-theoretic G-fixed group μ_2 and S5 rational decomposition. Prior full-text geometry determines nodal pairs and automorphism group, and ordinary generalized-Jacobian gluing determines nonsplit torus factors: these components are prior-implied, not newly discovered. Specific equivariant lattice and characteristic-two fixed scheme were not found in inspected sources; specialist equivariant generalized Jacobian literature might still imply them.

## value

PASS

The integral action and infinitesimal fixed subgroup are complete structural symmetry invariants of a natural family of nodal rational curves, not recoverable from point counts or rational character decomposition alone. The ten-node sextic decomposes the symmetry module into two distinct irreducible pieces. This sharp group-scheme classification is independently useful in related arithmetic and curve automorphism studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
