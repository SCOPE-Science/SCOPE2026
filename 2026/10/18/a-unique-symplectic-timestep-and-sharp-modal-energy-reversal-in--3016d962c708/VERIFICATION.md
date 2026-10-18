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

# Reproduction

Execute `python verify.py` using Python, SymPy, and NumPy. The program symbolically verifies the fourth-order Runge–Kutta stability-power polynomial, saturation determinant of all four stage directions for distinct positive frequencies and nonzero modal energies, exact crossover factorization, and two-mode action Jacobian. It establishes the rational frequency-pair benchmark and runs 150 deterministic direct-stage energy and ratio checks. The captured reference result is `verify_output.txt`. Analytic proof in `RESULT.md` supplies infinite-time assertions, symplecticity necessity, and uniqueness; finite comparisons do not replace those arguments. No formal proof assistant, human certification, or independent audit is claimed.
