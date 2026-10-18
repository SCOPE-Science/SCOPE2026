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

The map from binary operations to flip-equivariant maps X²→X² reverses composition but preserves idempotence/conjugacy/commutation. Idempotents are precisely equivariant retractions. Fixed and free flip orbits give profile constraints d+sum b_i=n, a+sum c_i+sum h_j=N, d>=1. Units form S_n×(C2 wr S_N), order n!2^N N!; matching rooted fibers prove orbit-transitivity and stabilizers with b_i!2^{c_i}c_i!, 2h_j! and identical-cluster permutation factors. Commutation with retraction e is exactly g(image e) subset image e plus g(y) in fiber over g(e(y)), yielding the stated block products using B=1+b,H=1+b+2c,L=1+h. Empty-product cases including n=1 are consistent. An independent literal equivariant-map enumeration for n=2 found all 16 maps, 7 idempotents, 4 unit orbits, and commutant counts [6,6,8,8,8,8,16]; n=3 global count 706 and 31 orbits are supporting independent/package tests, not all-n proofs.

## originality

PASS

Known magma-monoid work defines the monoid and counts/idempotents/units, but individual root-fiber unit-conjugacy orbit sizes and full-monoid commutant cardinalities are not the same as total counts. Read Baiduk–Kozerenko 2026 arXiv HTML and López-Permouth 2026 open-access article: relevant idempotent classifications/counts but no theorem stating the exact joint orbit and full-monoid commutant formulas. Ruiz-Medina 2025 counts equivariant maps and units, not equivariant retraction orbit profiles. Best-of-knowledge PASS; a different formulation in older finite equivariant-map literature remains a stated originality risk.

## value

PASS

A natural, recently studied transformation monoid has thousands of operations and hundreds of idempotents already for n=3. Complete unit-conjugacy classification and explicit orbit/centralizer sizes are intrinsic, reusable structural invariants; they distinguish many idempotents of the same image cardinality and give more than known aggregate totals. The theorem covers every finite n>=1 without a conjectural downstream result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
