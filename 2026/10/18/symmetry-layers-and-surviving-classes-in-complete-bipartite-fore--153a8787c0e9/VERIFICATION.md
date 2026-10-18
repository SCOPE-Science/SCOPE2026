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

# Verification and reproducibility

The proof in `RESULT.md` is all-parameter and integral. It uses an explicit natural cover, its graph intersection, relative homology of simplex skeletons, and Mayer–Vietoris. The only rational step is decomposing the stage-two character of an extension; the integer extension itself is retained as a short exact sequence.

Run `python3 check_forest_filtration.py` using Python 3.8 or later and compare to `checks.txt`. The script independently enumerates vertex-subset faces of the filtration, forms exact signed simplicial boundaries, computes ranks over primes 2, 3 and 5, verifies standard rectangle two-cycles survive to stage three, and sums signed permutation actions on every fixed face. The tested sizes are (2,2), (2,3), (3,3), (3,4), and (4,4), with all filtration stages through one beyond stabilization and every side-preserving permutation.

Checks are finite cross-checks only. They do not establish the theorem for arbitrary part sizes and do not determine the integral equivariant extension class at stage two. An independent mathematical audit has not been performed.
