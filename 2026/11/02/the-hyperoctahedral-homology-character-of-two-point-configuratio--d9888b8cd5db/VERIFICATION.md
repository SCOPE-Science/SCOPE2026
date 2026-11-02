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

The attached standard-library Python program constructs the exact 28-by-144 and 144-by-156 signed cubical boundary matrices and verifies their composition. Sparse elimination modulo the prime 1000003 gives ranks 27 and 100. The proof supplies a separate rational rank upper bound from a topological map onto graph first homology, so the finite-field rank is not misused as an unconditional rational rank equality.

It evaluates all 384 signed permutations and their signed action on all cubical cells; both cellular boundary operators commute with those actions. Exactly twenty signed cycle classes are found. The numerical character table is reproduced in `character_table.txt` and the program's exact terminal output in `checker_output.txt`. Subgroup averages independently yield the three claimed quotient rational Betti vectors. Run `python3 crosspolytope4_check.py` from a directory containing the standalone code; no network access or external packages are necessary.

The calculations do not test integral homology torsion or other cross-polytope dimensions. External independent audit has not been performed.
