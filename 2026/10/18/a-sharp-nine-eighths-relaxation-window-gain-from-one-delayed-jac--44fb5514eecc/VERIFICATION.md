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

`verify.py` was run from the completed local source directory using Python 3, NumPy and SymPy, producing: `PASS: 104 symbolic and numerical comparisons`.

The program constructs the three exact companion matrices and checks their factored characteristic polynomials by symbolic simplification. It checks the exact polynomial square establishing the \(9/8\) ratio bound, the coupling \(r=2/7\) endpoint identities, and the factorization at \(\beta=7/4\). It then checks directly computed eigenvalue moduli at couplings \(1/13\), \(1/4\), \(2/7\), \(2/5\), \(3/4\), and \(99/100\) on either side of each stability boundary. Delayed-update formulas are compared with companion matrices for specified real histories, and the three \(\beta=1\) spectral factors are checked separately.

Finite comparison grids and floating-point eigenvalues cannot establish an if-and-only-if result over all real parameters. That conclusion is supplied analytically by the root-location arguments and the exact maximization identity in `RESULT.md`. No external certificate or independent validation is claimed.
