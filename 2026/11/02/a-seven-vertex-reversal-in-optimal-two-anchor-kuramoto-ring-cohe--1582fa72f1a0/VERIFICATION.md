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

# Reproducibility and verification limits

The accompanying `verify.py` is a standalone check of the theorem's matrix and polynomial computations. Invoke `python verify.py` with Python 3.10+ and SymPy. NumPy and SciPy enable the optional independent numerical checks of local sine-coupled equilibria.

The actual extracted script was run successfully and printed `PASS: 355 deterministic algebraic, graph, and local-equilibrium tests`. It verifies the exact Dirichlet Green inverse and power-sum identities for 13 sizes, performs symbolic polynomial equivalence and concavity comparisons, enumerates all inequivalent two-pin geometries for every \(4\le N\le30\) using full inverse matrices, checks the fixed-reference contrast, and solves local nonlinear sine-coupled equilibria for representative sizes at two weak disorder levels.

The infinite-\(N\) minimizer statement is justified by the exact Green sum formula and the strictly concave polynomial proof, **not** by the finite enumeration. Local existence, stability, evenness of the expansion, and transfer of a strict coefficient gap to sufficiently small nonzero disorder follow analytically from the implicit-function theorem. There is no assertion of independently certified mathematical correctness or originality, nor of a result at arbitrary finite disorder strength.

