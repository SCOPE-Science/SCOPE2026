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
# Verification

`verify.py` is standalone Python 3 code requiring `numpy` and `sympy`. Run `python verify.py` from the directory containing the script; it requires no input files or web services.

For each integer \(3\le m\le8\), it builds an exact integer transfer matrix for the lattice points of the \(m\)-dimensional wheel dual ball at dilations \(0,1,\ldots,m\). The defining graph-incidence inequalities are totally unimodular, hence the polar is an integral lattice polytope. The \(m\)-th finite difference divided by \(m!\) therefore equals its Lebesgue volume. The script compares this independent exact rational result with the coefficient of the proved arctangent generating function, then combines it with the published primal wheel-volume formula and checks the normalized product exceeds one. All six dimensions passed.

This checks six rational instances exactly; it does not verify all dimensions by enumeration, nor independently re-prove the integral-operator spectral completeness or bibliography. Those arguments are given in RESULT.md. Independent audit remains not performed.
