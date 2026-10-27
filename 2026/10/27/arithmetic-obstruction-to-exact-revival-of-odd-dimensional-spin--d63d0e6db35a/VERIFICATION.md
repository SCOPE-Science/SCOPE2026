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

# Reproducible finite checks and proof boundary

Run `python3 verify.py` with Python 3 and NumPy installed. The program implements the eight-coordinate reduced map from Wang [1, equation (4.20)] and, independently for dimensions \(3,5,7\), the full spin-coupled hypercube shift/Grover operator and QBN harmonic lifts. A successful run prints `PASS 131 matrix identities and full-walk intertwinement checks`.

The tests compare both signs of the spin phase in eleven dimensions \(3,5,7,9,11,13,15,21,33,55,101\). They verify characteristic coefficient formulas, the vanishing trace-square identity, unit determinant, and spectral moduli; in the first three dimensions they check exact harmonicity and the full-matrix intertwining relation numerically to stated tolerances. They are independent floating-point diagnostics of the displayed algebra, not an exhaustive proof for all odd dimensions.

The global argument instead uses an exact algebraic-integer obstruction: every conjugate of the nonzero coefficient \(A_d\) has modulus less than one, contrary to the nonzero integral norm that would be required if all eigenvalues were roots of unity. The determinant-one identity similarly forbids finite projective order. No external independent audit has been performed.
