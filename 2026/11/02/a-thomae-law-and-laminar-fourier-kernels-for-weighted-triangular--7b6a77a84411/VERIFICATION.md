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

The main result is proved analytically in `RESULT.md` for all odd prime scales and all symmetric positive digit weights. The proof uses normal convergence of the Fourier-mask product, an exact cyclotomic cosine criterion, a p-adic valuation separation, and a uniform density-tail estimate. The count of two residue classes at each cancellation level produces the stated natural density; it does not rely on finite numerical extrapolation.

Run `python3 weighted_triangular_checker.py` to reproduce finite all-residue tests for \((p,k,a)=(3,1,1),(5,1,2),(5,2,7),(5,2,8),(7,1,2)\). The script checks several prime-power levels, first-hit counts, and the equal-conductor disjoint / mixed-conductor containment alternatives; if SymPy is installed, it also verifies the golden-ratio mask identity by exact symbolic simplification. Complex-mask comparisons otherwise use numerical tolerance only; they are not exact exhaustive infinite certificates. For full mathematical verification, independently check each step of the written argument.

No independent review or certification has been performed. The full text of the historically relevant Strichartz (1993) Fourier-transform paper was not accessible; originality cannot be guaranteed against that or all unindexed literature. Only the stated odd-prime symmetric-weight and integer-frequency setting is covered.
