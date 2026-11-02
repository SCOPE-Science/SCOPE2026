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

# Reproducibility and limits

Run `python VERIFY.py` from the extracted directory with Python 3, SymPy, NumPy, and SciPy. The script directly builds full weighted graph Laplacians and exact-rational grounded matrix inverses, then compares the hub–periphery performance difference with the separate spectral formula for cliques, cycles, cubes and a triangular prism. It also checks orbit symmetry, the complete-graph transition, numeric cycle threshold equations and predicted two-term finite-size differences. `VERIFY_OUTPUT.txt` records the actual local run.

The experiment comprises 126 exact comparison identities, 210 symmetry comparisons, 16 cycle threshold/bound checks and 16 quadratic-plus-linear comparisons; all passed. Those are finite checks and do not establish the all-size conclusion by themselves. The proof's essential nonstandard ingredients are the joint eigenmode decomposition, vertex-transitive spectral projector diagonals, strict monotonicity, exact cycle resolvent identity, and the nonzero derivative needed for the asymptotic remainder. Originality is assessed from inspected literature with residual historical risk. No independent scientific audit has been performed.
