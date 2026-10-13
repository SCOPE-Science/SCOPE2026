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

The standalone file `verify_laplacian_join.py` recomputes every ordinary graph Laplacian and its real spectral projectors directly from the displayed graph edges. It checks completeness and idempotency, constructs the left side as the sum of projector Schur squares, and separately constructs the proposed reduced-factor formula and predicted ranks. Run with `python3 verify_laplacian_join.py` with SymPy installed.

Replayed result: `VERIFY_OK exact_pairs=100 exact_entries=3800 singular_cases=52 K4_rank=4 C4_join_O3_rank=5`.

The sample list includes a singleton, empty graphs, paths, stars, cycles and complete graphs. All matrix identities are checked in exact rational arithmetic, without finite-precision eigenvalue grouping. The 100 pairs are tests, not exhaustive over all graph orders. The proof of the unrestricted claim is the complement-component argument and exact spectral decomposition in `RESULT.md`.
