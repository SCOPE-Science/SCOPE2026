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

# Verification and evidence boundaries

The analytical proof in `RESULT.md` establishes the global optimization over all real relaxation values and nonzero real preconditioner parameters for a generalized spectral pair \(u\pm iv\), \(v>0\), excluding the singular system. A modal determinant formula, Cayley-metric invariance, an imaginary-coordinate bound from two quadratic roots, and equality reconstruction provide independent, checkable critical steps.

Run `python reproduce.py` with NumPy available. The deterministic checks exercised 200 distinct real parameter pairs, their direct real block matrices and nonorthogonal similarities, 8,000 alternative parameter combinations, and the exact \(u=1\), \(v=2\) benchmark, totaling 9,209 assertions. Each code path was run against the bundled source. Numerical checks do not prove that a continuous global optimum is attained or unique; that is proved analytically.

The spectral radius need not equal the norm of one error update, and defective Jordan blocks can cause transient behavior. The parameter sequence approaching the infimum when \(u=0\) is not a finite optimizer within the prescribed nonzero-\(\theta\) family. All substantive overlap judgments require scientific reading of the cited original sources; bibliographic coverage is not claimed exhaustive.
