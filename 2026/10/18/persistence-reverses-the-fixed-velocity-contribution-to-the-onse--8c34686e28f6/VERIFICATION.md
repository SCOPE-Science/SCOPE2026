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
# Verification record

The standalone `verify.py` requires NumPy, SciPy and SymPy and runs without downloading papers, datasets, or executables. It verifies symbolically the passive criterion root and derivative and the exact slow-relaxation value \(\chi(0+)=4/125\). It computes \(\chi(\eta)\) in two independently implemented ways: elementary hyperbolic formulas (using a complex-step derivative) and nested quadratures of the Dirichlet–Neumann Green kernel. At six tested rates, their absolute discrepancy is below \(2\times10^{-10}\). Independently, it assembles a finite-difference/Hermite representation of the full nonzero-amplitude joint backward generator, solves first and second hitting-time equations, and uses centered amplitude differences to recover the critical-point derivative. At relaxation rates \(0.05,1,10\), discrepancies are below \(4\times10^{-6}\).

The exact continuum proof does not rely on the finite-difference or Hermite truncations. The numerical crossing near \(0.2112213694\) is not accompanied by an exhaustive root-isolation certificate and no uniqueness statement is made. The outcome of any future independent audit is not represented here.
