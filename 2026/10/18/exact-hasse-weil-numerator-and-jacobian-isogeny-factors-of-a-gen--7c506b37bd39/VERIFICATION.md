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

The executable `verify_zeta.py` supplies two separate exact algorithms. One counts on the smooth affine plane model and adds the geometric ramification points. The other counts rational elliptic points and applies the absolute-trace criterion for the Artin–Schreier equation, treating each simple pole as one geometric point. The two sequences agree in every field of cardinality from \(2\) through \(512\).

The program verifies binary irreducibility of each field modulus by polynomial gcd/Frobenius tests; its exact Newton recursion yields the first nine coefficients, and the genus-nine functional equation supplies the rest. Plain integer multiplication verifies all four factors (with one factor squared), and evaluation at \(T=1\) yields \(1024\).

The curve's geometric genus, smooth normalization and branch divisor are cited from Tafazolian, Proposition 7.2. The verification does not prove a theorem for any other member of the family, nor a polarization-preserving Jacobian splitting. No independent external audit has been performed.
