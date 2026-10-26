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

# Verification and limits

The universal proof is the scalar annihilator polynomial identity in `RESULT.md`; it is not based on a numerical sweep. The key algebraic bounds are \(\deg(\operatorname{adj}(P)b)\le2(n-1)\), the nonsingularity of \(P(\xi)\) and \(\xi\ne0\), and the Vandermonde independence of the positive definite witness.

Run `python3 verify.py` with standard Python 3 to reproduce `verification_output.txt`. The checker uses `fractions.Fraction` and exact row elimination, tests eight dimensions, three expansion centers, and every derivative order from zero through \(2n+4\). No external mathematical package is required.

Finite tests do not establish the theorem for unbounded dimension. Nothing here verifies floating-point orthogonalization behavior, PDE discretizations, or independent evaluation.
