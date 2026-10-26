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

The mathematical argument is a finite exact stationary-generator calculation. It does not rely on stochastic simulation or a truncated solution of an infinite system.

`verify_sixth.py` uses SymPy to build the two-parameter Fourier-moment recursion up to degree six. The tests reconstruct the known generic second/fourth moments, verify the published fourth-cumulant-zero curve, and derive on that curve the stated sixth moment, negative sixth cumulant, standardized ratio, derivative polynomial and endpoint values. Four independent choices of rational angular diffusivity are substituted into every computed generator identity, checking each residual symbolically.

Reproduction: install `sympy>=1.12` (see `requirements.txt`) and execute `python verify_sixth.py`. Its expected output is given in `verify_output.txt`. The supplied program has been run successfully from its packaged content.

The checks do not prove historical priority, identify the full stationary density, establish new results for other confining potentials, or constitute an independent audit.
