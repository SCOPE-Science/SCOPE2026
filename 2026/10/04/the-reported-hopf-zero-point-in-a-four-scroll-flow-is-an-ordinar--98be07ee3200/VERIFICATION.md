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

The bundled `verify.py` uses only the Python standard library and exact rational complex arithmetic. It checks the local bifurcation calculation for the printed four-scroll vector field at \(a=0\), \(b=27\), \(c=8\), \(d=1/10\).

The script verifies:

- the factorization \(p(\lambda,0)=(\lambda+b)(\lambda^2+1)\), so the full spectrum is \(\{-8,-27,\pm i\}\) and contains no zero eigenvalue;
- the separate zero-Hopf spectral factorization \(p(\lambda,a)=\lambda(\lambda^2+1-a^2)\) when \(a=b\), with an imaginary pair precisely for \(0<a<1\);
- the exact crossing derivative \(d\operatorname{Re}\lambda/da=729/1460\) at the source point;
- the normalized right/left eigenvector relation \(\langle p,q\rangle=1\);
- the quadratic Hopf formula via exact four-by-four Gaussian elimination for \(A^{-1}B(q,\overline q)\) and \((2iI-A)^{-1}B(q,q)\);
- the exact value \(l_1=-58491/724744000\), and its agreement with the closed family formula.

Running `python3 verify.py` produces the bundled `verification_output.txt`, whose first line is `VERIFY_OK`.

The verification proves only the local statements encoded above. It does not numerically integrate the nonlinear flow, establish global attractor structure, or independently audit the literature search.
