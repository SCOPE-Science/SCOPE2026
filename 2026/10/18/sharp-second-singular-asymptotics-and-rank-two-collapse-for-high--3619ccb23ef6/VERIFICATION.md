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

# Verification evidence

The proof is analytic. Direct algebra checks the kernel expansion \(e^{-(u+v)}[(u+v)-(u+v)^2/2]=a(u)g(v)+g(u)a(v)-h(u)h(v)\), and exponential moments yield \(\langle g,h\rangle=0\), \(\|g\|_2^2=1/2\), \(\|h\|_2^2=1/8\). The high-order remainder is bounded in Hilbert–Schmidt norm using a weighted integral over \(u+v\). The spectral conclusions follow by self-adjoint min–max and Eckart–Young, and the norm coefficient by the exact Hilbert–Schmidt mass.

For reproducible finite checks, execute `python check_volterra.py` with NumPy >=1.24 and SciPy >=1.10. The script uses 70-point Gauss–Laguerre Nyström discretization at five specified real orders and prints `FINITE_NUMERICAL_CHECKS_OK`. It compares \(\alpha s_2\), a second-order scaled norm residual, and finite quadrature against \(1/(4-2/\alpha)\). These calculations cannot establish the infinite-order limits; they only check representative finite cases. No formal proof assistant or external auditor is involved.

Known limits: no exact third-or-later singular coefficients; no sharp trace-norm correction; incomplete full-text access to specific early papers. Independent external audit was not performed.
