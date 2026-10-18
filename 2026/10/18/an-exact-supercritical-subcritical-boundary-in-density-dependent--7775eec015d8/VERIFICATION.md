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
# Exact symbolic verification and limits

Run `python verify.py` using Python 3 and the declared SymPy dependency in `requirements.txt`. The executable takes no input files and performs symbolic differentiation with exact arithmetic. It checks the Cartesian Poincaré–Lyapunov formula after the rotation-normalizing change of variables, independently computes the multilinear complex-eigenvector coefficient, verifies the conversion of the two coefficient conventions, and checks two exact opposite-criticality examples with matching imaginary-axis spectra.

Executed result: `Exact Cartesian and complex Hopf coefficients agree. Both opposite-criticality examples share the spectrum +/-i. All exact symbolic checks passed.`

The analytic Hopf theorem is needed for existence, uniqueness in a neighborhood, and orbital stability of the bifurcating periodic orbit. Algebraic tests do not establish global uniqueness, larger-amplitude structure, or fifth-order criticality at the coefficient-zero boundary. Independent audit and experimental validation have not been performed.
