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
The proof applies to the three-dimensional unit-population simplex for the printed \(n=2\) model with \(\beta_s=\beta_1=1\), \(\beta_2=0\), and \(\mu_1=\mu_2=1/100\). The new calculation is an exact local spectral classification, not a simulation-only inference.

Run `python verify.py` using Python with SymPy and NumPy. The program reconstructs the equilibrium polynomial, the characteristic cubic, the exact quartic Routh identity, the strict monotonicity of the equilibrium parametrization, the two positive-root intervals, and representative eigenvalue signs at \(\gamma=0.5,0.7,0.9,0.99\). It prints `VERIFY_OK` and the two spectral thresholds when all assertions pass.

The exact completeness proof uses Descartes' two-positive-roots bound together with rational isolating intervals \((1/5000,1/4000)\) and \((1/100,1/50)\). For every \(0<\gamma<1\), it then uses the cubic Routh-Hurwitz criterion. The numerical root approximations are reproducibility checks rather than substitutes for this proof.

The four-dimensional unconstrained equations have a conservation-induced zero eigenvalue; all stated stable, unstable, and nonhyperbolic conclusions are relative to the fixed-total population simplex. The work does not establish nonlinear periodic branches.
