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
The proof is analytic and has two independent structural components.

First, every nonzero-shift Pauli expectation reduces to a quadratic exponential sum on the two-dimensional \(\mathbf F_d\)-space \(\mathbf F_{d^2}\). Its polar form is \(B_u(z,w)=\operatorname{Tr}(6uzw)\), which is nondegenerate because the trace pairing is nondegenerate and \(6u\ne0\). Squaring the sum and changing variables proves its magnitude is exactly \(d\); this establishes the universal Pauli-magnitude pattern and the purity formula.

Second, after a row-phase removal the bipartite coefficient matrix is \(B_{x,y}=d^{-1}\omega^{6\nu xy^2}\). The reduced matrix is circulant, and its Fourier eigenvalues are exactly
\[
\lambda_k=\frac1d\#\{y:6\nu y^2=k\}.
\]
The elementary square-root count over \(\mathbf F_d\) gives one eigenvalue \(1/d\), \((d-1)/2\) eigenvalues \(2/d\), and \((d-1)/2\) zeros.

The file `artifacts/verify.py` is a corroborative finite replay. It uses only the Python standard library, exhausts every generalized Pauli expectation for \(d=5\) and \(d=7\), and independently evaluates the Fourier root-count spectrum. A successful replay ends with `VERIFY_OK`.

The computation does not certify the universal theorem by enumeration, and no upper bound on arbitrary-state magic is claimed.
