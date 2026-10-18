---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The 3D family A_n=diag(1,R(2π/n)) has finite cyclic order n for n>=3 and A_n→I3. The planar 2D real rotation is irreducible for n>=3, inequivalent to fixed 1D coordinate, yielding block sizes (1,2); I3 yields trivial real isotypic block (3). The discrete block-count output jumps 2→1 in the promised finite-order subspace. Type-2 computability of discrete codes would imply continuity, contradiction. Scope explicitly requires the isotypic code, not merely an orthogonal matrix with arbitrary one-block output. No numeric experiment can substitute for this topological argument.

## originality

PASS

The explicit Type-2 discontinuity at the identity addresses a stated open input-removal branch of Burnik Question 8.3. Burnik already proves computability with a Cayley table and cites a different general symmetric-matrix noncomputability theorem; neither implies the promised finite-order generator-only cyclic counterfamily. A prior Weihrauch/representation-theoretic equivalence may exist, so priority is best-of-knowledge, not absolute.

## value

PASS

Computability of full real isotypic block diagonalization is naturally an algorithmic representation-theory problem and Burnik explicitly poses group-information removal as a question. A fixed dimension-three, one-generator counterfamily isolates a discrete-input-information obstruction that is mathematically useful for delineating computability and potential Weihrauch complexity; this is more than a routine numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
