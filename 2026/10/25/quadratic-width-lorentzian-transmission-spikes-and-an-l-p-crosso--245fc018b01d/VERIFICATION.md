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

# Reproducibility and mathematical verification

Run `python verify.py` in a Python environment containing NumPy and SciPy. A completed local replay reported `PASS: 39 derivative, resonance, Lorentzian, threshold and norm checks`, and evaluated the regular and resonant squared-norm constants as approximately \(2.175694782703539\) and \(0.11635528346628861\), respectively. The latter equals \(\pi/27\).

The script checks six symmetric finite-difference evaluations of the regular perturbation derivative. At three distinct high-energy cells it checks the exact resonance equation, five samples of the rescaled Lorentzian, three superlevel-set widths, and the \(p=1,2,4\) norm formula via adaptive quadrature. It uses the normalization \(\ell=a=1\), with all other positive fixed values handled by the symbolic scaling of \(x\) and \(\delta_n\).

The key exact identities are the two-resonator rational transmission formula, its phase-coordinate reduction, and the derivative \(g\). The analytic proof also requires monotonicity of the local resonance equation, the uniform envelope on the inner strip, bounded second derivatives outside it, and dominated convergence after Lorentzian rescaling. The finite script does not establish those uniform or infinite-parameter facts, and does not independently certify priority or publication status.
