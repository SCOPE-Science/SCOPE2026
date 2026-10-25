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

Run `python verify.py` next to the other extracted files. The program exhaustively enumerates all \(5^5=3125\) positive run-length quintuplets with individual lengths from one through five, independently builds full factor sets, and checks every explicit three-run bridge and the non-bridge residual bound. It also checks the simplex mean calculation in exact rational arithmetic.

The infinite theorem is justified by direct contiguous-factor reasoning, the proved run-length decomposition and bounds in Akagi et al. (2022, Lemmas 1–5), and uniform-simplex lattice convergence. The computational exploration cannot replace these arguments. Related full-text access limits and non-exhaustive novelty risks are stated in RESULT.md.
