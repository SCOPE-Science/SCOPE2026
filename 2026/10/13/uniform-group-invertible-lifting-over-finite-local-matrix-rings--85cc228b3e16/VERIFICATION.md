---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a group inverse B=A#, the common idempotent AB=BA yields R^n=im A⊕ker A and an automorphism A|im A. Conversely every free ordered decomposition with invertible restriction gives A#; orbit-stabilizer gives |GL_n(R)|/|GL_{n-r}(R)|. Reduction GL_s(R)→GL_s(F_q) has kernel size j^{s²}. A fixed rank-r residue group-invertible matrix has j^{2r(n-r)} lifted ordered decompositions and j^{r²} invertible restrictions, hence j^{n²-(n-r)²} lifts, probability j^{-(n-r)²}. Independently enumerated all 16 F2 2×2 matrices and checked group inverses directly: ranks (1,6,6). The package verifier for Z4 and F2[ε] was read, not blindly treated as a proof.

## originality

PASS

Best-of-knowledge: exact prescribed-residue-fiber survival law is not stated in the inspected most relevant primary count of idempotents or block group inverses, despite a strong near-implication of the rank formula by standard orbit weighting. This is a qualified narrowly original exact invariant, not a new foundational structural theorem.

## value

PASS

The exact survival rate j^{-k²} for a prescribed group-invertible residue matrix is a uniform, distribution-sensitive lifting theorem over all finite commutative local rings; it has a natural rank/nullity parameter and potential use in random lifting and index-one matrix calculations. Value is modest because the group-invertible count is close to classical idempotent orbit counting, but the new conditional fiber statement is exact and not merely recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
