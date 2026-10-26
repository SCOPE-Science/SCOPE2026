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

# Reproduction and limits

With Python 3 and SymPy, execute `python verify.py` from this directory. The script uses exact symbolic algebra and rational comparisons, with no external services or numeric root solver.

The script verifies the exact predator-nullcline and quartic identities, degree/sign pattern, the four rational root-isolation values, the upper-branch trace formula and positivity bound, and the two predator-free eigenvalues. The determinant sign follows by differentiating the positive-equilibrium nullcline and is stated explicitly in `RESULT.md`. These are corroborating symbolic certificates, not an independent scientific audit.

The variational critical threshold and exhaustive count over all parameter values are established by the analytical proof in `RESULT.md`; they are not inferred from finite checks. The double root is algebraic and no unconditional nonzero transverse eigenvalue or global basin classification is asserted.
