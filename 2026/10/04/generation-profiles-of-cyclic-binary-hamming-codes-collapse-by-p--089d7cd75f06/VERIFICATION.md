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
The theorem is algebraic. The executable `verify.py` supplies finite consistency checks for the polynomial identities and small instances.

It performs the following exact checks:

1. It implements arithmetic in \(\mathbb F_2[x]\), irreducibility testing, and the multiplicative-order test needed for primitiveness.
2. For \(g=x^6+x+1\), it verifies primitiveness, finds \(\ell=6\), and checks \(\gcd(1+x+x^6,x^{63}-1)=g\).
3. For \(g=x^6+x^4+x^3+x+1\), it verifies primitiveness, finds \(\ell=56\), and checks \(\gcd(1+x+x^{56},x^{63}-1)=x^8+x^7+1\). Hence the radius-five span has dimension \(55\) inside a dimension-\(57\) code, giving four components.
4. It exhaustively enumerates the degree-three and degree-four cyclic Hamming codes, computes cyclic pair weights, and verifies that the generation profile agrees with the polynomial-gcd formula through radius six.

The finite checks do not certify the theorem for arbitrary \(m\); that scope is supplied by the proof in `RESULT.md`. No claim of independent validation is made.
