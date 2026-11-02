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

# Verification of the quartic entropy formula

The claim is established by four analytic steps detailed in RESULT.md: (i) Perron–Frobenius linear response gives the universal doubling-map Lyapunov Hessian in terms of Green–Kubo variance; (ii) Fourier towers give its exact degree-two trigonometric null space; (iii) conjugacy removes the first-order map term and produces the second-order forcing \(f=u v'\); (iv) Fourier coefficients of \(f'\) yield the quartic loss \((a^2+b^2)(9a^2+5b^2)/128\).

A reproducible algebraic test is included as `verify_quartic.py`. It requires SymPy, invokes exact symbolic simplification without floating point, and printed:

`PASS: exact quartic coefficient, axes, and minimal Fourier kernel`

The test checks the polynomial identity, both pure-harmonic axes, the mixed sample \((1,1)\), the zero case, and the two-harmonic kernel. It is an algebra check, not an independent verification of the transfer-operator theorem.

For additional nonrigorous comparison, a periodic-grid transfer-operator computation with 32768 grid points and 42 iterations, at \(\varepsilon=0.08\), gave approximately \(0.070806\), \(0.039551\), and \(0.224855\) for \((\log2-\lambda)/\varepsilon^4\) at \((a,b)=(-1,0),(0,1),(1,1)\), compared with the exact predicted limits \(0.0703125\), \(0.0390625\), and \(0.21875\). These finite-grid figures do not certify truncation errors and are not relied upon for the theorem.

The analytic proof is local in \(\varepsilon\), with a remainder depending on fixed \((a,b)\). General publication priority and any independent audit remain unperformed.
