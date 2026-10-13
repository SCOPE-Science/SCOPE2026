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

# Reproducible checks and limits

The accompanying `verify_exact.py` requires only Python 3 and SymPy, makes no network requests and loads no external data. From the actual source code in the same package, invoke `python verify_exact.py`.

For each tested \((a,b)\), the checker constructs the whole adjacency matrix of \(S(K_{a,b})\), computes \(H^2\), uses rational spectral interpolation to obtain all distinct squared-energy projectors, and reconstructs the continuous-time average mixing matrix as the sum of projector Schur squares. It then compares every entry with the separately programmed closed decomposition, verifies stochastic row sums and computes exact ranks for orders up to fifteen vertices. The tested pairs are \((1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4)\).

The observed successful output was:

`VERIFY_OK exact_pairs=9 exact_entries=1131 3_3_order=15 2_3_rank=7 1_3_rank=5`

The reported 1,131 matrix entries are exact equalities in rational arithmetic. Finite execution is not an exhaustive test of unbounded integer pairs and cannot prove originality; unrestricted correctness is supplied by the algebraic proof in `RESULT.md`. In particular, the checker does not test weighted, directed, or normalized-Hamiltonian variants.
