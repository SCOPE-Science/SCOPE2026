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

# Reproducibility and boundaries

The standalone `verify.py` requires Python 3, SymPy and mpmath. Run `python verify.py` in the directory holding the file. It calculates the exact Erlang-2 stationary renewal reward, characteristic polynomial, fixed-budget susceptibility factors and fairness Hessian; validates the exact inequality for the nonlocal counterexample; compares the Perron values at 60-digit precision; and checks booster budget conservation and group exchange symmetry on a finite sample grid.

The recorded run passed 228 distinct assertions. Its fair and concentrated spectral factors were approximately 0.64950401001889522231481400754699338 and 0.6486241176140524257242911631594934, respectively. The strictly positive gap was approximately 0.0008798924048427965905228443875.

The continuum assertions do not rest on the finite grid or floating-point comparisons: the accompanying mathematical proof establishes them analytically. The code does not prove originality, cover all broader vaccine models, inspect stochastic epidemic outcomes or perform an independent audit.
