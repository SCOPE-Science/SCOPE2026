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

# Reproducibility and verification

The analytic proof in `RESULT.md` is the evidentiary basis for the universal theorem. `verify.py` uses exact symbolic integration (SymPy) to show \(H_3'(-1)=96\log2-66\) and \(H_3'(1)=6\); it independently constructs the integral and Fourier-series versions of the pair potential, checks the global quantitative lower bound for positive residue lists at four exponents, and confirms strict negativity for six balanced perturbations below the critical mass ratio.

Reproduction: run `python verify.py` in a standard Python environment with NumPy and SymPy. The reported scientific test result was `VERIFY_OK 381 energy and Fourier comparisons; alpha3 critical mass ratio = 11.067469746461578`. The checker uses a deterministic seeded pseudorandom generator and finite Gauss-Legendre quadrature. These approximate comparisons cannot certify all configurations or all exponents; the proof handles those quantifiers separately. The potentially relevant generalized Chui manuscript was not fully accessible, and priority is not independently established.
