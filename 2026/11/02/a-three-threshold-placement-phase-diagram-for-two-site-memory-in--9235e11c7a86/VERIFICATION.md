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

## Reproducible checks

Run `python verify.py` with Python 3 and SymPy. The source file is included alongside this note. Exact symbolic checks construct the ten-vertex Laplacian and its Green operator; verify the zero-mode projection, the five closed rational susceptibility expressions and all ten pairwise difference identities; and verify the algebraic boundaries. Twenty-five independent finite Fourier evaluations are compared at five positive rational coupling ratios. The program also tests four representative strict orderings.

The proof for every positive rate ratio uses exact polynomial signs and quadratic root positions, not finite sampling. Independent scientific assessment has not been performed. The assessment of possible overlap with inaccessible literature remains qualified.
