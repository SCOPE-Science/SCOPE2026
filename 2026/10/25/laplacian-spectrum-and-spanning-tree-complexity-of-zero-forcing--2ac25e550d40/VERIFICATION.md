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

# Reproduction and boundaries

Run `python3 verify.py` and `python3 verify_laplacian.py` from this package directory using Python 3.8 or newer. No third-party modules are required. The first checker exhaustively enumerates blue vertex sets and runs the ordinary forcing process in explicitly built bouquets of unequal and equal clique sizes, comparing their feasible white complements, polynomial counts, exchange degrees and all-pairs graph distances. The second independently builds the full minimum-set exchange graph and checks the exact determinant of its integer Laplacian shifted by three different scalars, as well as a principal cofactor, against the claimed spectral factorization and tree formula for five parameter pairs. `verification_output.txt` gives outputs from actual runs.

The standalone computations check only finite listed instances; the complete factorization for all \(r\ge3,m\ge2\) rests on the tensor-sector proof in `RESULT.md`. The related class of arbitrary unequal cliques is not covered by the spectral theorem. Independent audit status is not performed.
