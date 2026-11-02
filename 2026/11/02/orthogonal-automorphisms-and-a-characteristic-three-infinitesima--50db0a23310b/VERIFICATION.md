---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the algebraic classification

The exact proof is in `RESULT.md`. The reproducibility check is the ordinary Python standard-library script `verify.py`: run `python3 verify.py` from this directory. It enumerates all invertible side blocks for complete-bipartite graph evolution algebras over the three prime fields \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), filters the bilinear product equations, and obtains \(8,8,24\) automorphisms of \(K_{2,2}\). It independently constructs the complete linear system of derivation conditions and calculates their modular ranks for the seven reported parameter cases. On its current execution the script returned `VERIFY_OK`.

The finite checks do not prove the infinite-field or scheme claims; the proof identifies the entire left-multiplication rank-one locus, solves the exact block equations, calculates the identity neighbourhood of the affine group scheme, and derives the tangent-space equations. No outside expert or independent audit was performed. The exclusions for characteristic two and noninvertible part sizes remain in force.
