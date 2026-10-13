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
# Verification

The exact domain is \(\operatorname{Cr}_n=K_{n,n}-M_n\) for every integer \(n\ge6\). The proof has four critical steps: every used color meets each shore in at least \(\lfloor n/2\rfloor\) vertices; this forces at most two colors; explicit parity-dependent constructions attain two; and equality/complement arguments classify all optimal two-colorings and yield their counts.

The packaged `verify.py` independently constructs the graph and evaluates the original local majority condition. It exhaustively enumerates all labeled two-color assignments through \(n=9\), verifies the asserted structural type and count for every feasible assignment, exhaustively enumerates three-color assignments for \(2\le n\le5\), and checks the explicit constructions for \(2\le n\le200\).

Expected replay output:

`ALL CHECKS PASSED; two_color_assignment_checks=349520; two_color_counts=[(2, 2), (3, 18), (4, 6), (5, 80), (6, 20), (7, 350), (8, 70), (9, 1512)]; three_color_small_counts={2: 0, 3: 12, 4: 0, 5: 0}; construction_range=2..200; exact_claim_range=n>=6`

The exhaustive range is finite and is not an infinite proof. No computation is used to justify novelty. No independent audit or independent validation has been performed.
