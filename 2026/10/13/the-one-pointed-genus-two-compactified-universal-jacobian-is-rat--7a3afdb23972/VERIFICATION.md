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

The exact source Betti vector used is \((1,5,15,20,15,5,1)\), corresponding to
\[
B(t)=1+5t+15t^2+20t^3+15t^4+5t^5+t^6.
\]
Modulo \(3\), the checker reconstructs
\[
\overline B(t)=t^6+2t^5+2t^3+2t+1.
\]

For a monic degree-66 polynomial over \(\mathbf F_3\), the Rabin irreducibility criterion requires the degree-six Frobenius congruence and gcd tests for the prime divisors \(2\) and \(3\) of \(6\). `verify.py` performs polynomial modular exponentiation and Euclidean gcd arithmetic over \(\mathbf F_3\) and checks exactly:

- \(t^{3^6}-t\equiv0\pmod{\overline B}\);
- \(\gcd(\overline B,t^{3^3}-t)=1\);
- \(\gcd(\overline B,t^{3^2}-t)=1\).

These checks prove \(\overline B\) irreducible over \(\mathbf F_3\), hence \(B\) irreducible over \(\mathbf Z\) by Gauss's lemma.

The Künneth consequence is mathematical rather than experimental: for connected factors, \(b_0=1\); because all Betti numbers are nonnegative, any odd cohomology in either factor would force odd cohomology in the product. Smooth proper positive-dimensional factors also have nonzero top cohomology, so their even Poincaré polynomials are nonconstant. Thus a nontrivial product would factor \(B(t)\), impossible.

Limits: the checker verifies the finite-field algebra, not the source's cohomology computation. The result is a rational-cohomological obstruction and does not address birational, fibrational, derived, or motivic decompositions.
