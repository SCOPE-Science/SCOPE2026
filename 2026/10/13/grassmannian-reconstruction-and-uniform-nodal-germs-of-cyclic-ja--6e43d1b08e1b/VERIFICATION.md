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

The diagonal derivatives of the determinant rule out every corank-one singularity: the rank-one symmetric adjugate is czzᵀ with a nonzero diagonal entry. For every full-edge matrix the recurrence determines a solution from any adjacent pair; in corank two each adjacent evaluation is therefore an isomorphism. With q_i=(x_i,y_i) the row evaluations of a kernel basis and e_i=det(q_i,q_{i+1}), the identity e_i q_{i−1}−p_{i−1,i+1}q_i+e_{i−1}q_{i+1}=0 verifies the stated inverse. Taking two determinants of each kernel equation forces all b_i e_i equal and the specified a_i, proving projective uniqueness. The constant-rank kernel map and the homogeneous inverse obtained by clearing ∏e_i are regular. Taking q_i=(1,i) shows nonemptiness. The principal projective open D_+(∏e_i) is affine and e_1 trivializes the canonical bundle O(−n) by trivializing O(1). For the germ, split off a nondegenerate complement of the kernel for the associated symmetric form; the differential of its Schur complement is restriction to the kernel, surjective by the three variations of an adjacent 2×2 block. The radial direction restricts to zero, so surjectivity survives in any projective chart. Three formal coordinates are the Schur entries and their determinant is the local equation up to a unit. The local Jacobian ideal in the quotient is then (u,v,w), giving reducedness and multiplicity two. Exactly one missing edge leaves a single path and nullity at most one; k≥2 missing edges give k path blocks (possibly singletons), each with nullity at most one and a nonzero determinant monic in the product of its own diagonal coordinates. At least two block determinants vanish, independently on these disjoint blocks, giving ambient codimension ≥k+2. This proves the top-dimensional statement without a boundary-germ classification. Independent replay `python3 /workspace/branches/independent_examples.py 1` checks exact nodal slices at one explicit point per n=4,…,8 (SymPy); it is not evidence of exhaustiveness.

## originality

PASS

The supported distinct result is the all-n cycle-matrix kernel reconstruction and everywhere transverse-node and boundary statements. We credit the known n=4 open Grassmannian geometry, the normalized frieze identification, and the usual local model for symmetric rank strata. The strongest inspected statements do not supply the joint result; this is a bounded evidence-based decision, not a claim of priority.

## value

PASS

The all-size result turns the maximum-nullity open locus of a natural sparse symmetric determinant into an explicit smooth moduli space. The uniform local ring, reduced Jacobian scheme and actual dimension separation from all boundary singular points tell a reader substantially more than a rank bound, a generic nodal statement or the known n=4 topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
