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

The analytic argument proves three independent steps: (1) the exact BLD rank-one choice from Sherman–Morrison and Rayleigh extreme eigenvectors; (2) a lower bound for every positive or negative signed Hermitian rank-one update through two-dimensional orthogonality subspaces; and (3) the unique discrepancy-crossing root and the sharp regret interval. No matrix-commutativity assumption is made in step (2).

To reproduce the standalone checks, run `python verify.py` with Python, SymPy, and NumPy installed. The script verifies symbolic determinant/trace/derivative identities; the rational example \(M=6\), \(\varepsilon=1/20\); four unbounded-regret subfamily points; score-root consistency; and 1,200 randomly drawn signed rank-one preconditioners. Expected output begins with `VERIFY_OK`. These computations support, but cannot replace, the universal proof or a bibliographic originality determination.

The preprint is dated from its first public version, 11 December 2023. The exact statement is limited to the condition number, not CG iteration counts. Independent audit has not been performed.
