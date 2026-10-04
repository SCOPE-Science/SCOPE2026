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

The universal proof is in `RESULT.md`. The bundled `artifacts/verify.py` is a finite exact-arithmetic regression check, not an infinite proof.

It performs the following checks for every integer \(n\) from \(2\) through \(10\):

1. reconstructs \(g_n=x^{n+1}+x^ny+y^nz+z^n\) and its three partial derivatives as sparse exact polynomials;
2. verifies \((n+1)g_n-xg_x-yg_y-zg_z=z^n\);
3. constructs the six proposed generators of the Tjurina Gröbner basis and checks exact Buchberger reduction of every S-polynomial to zero in lexicographic order \(x>y>z\);
4. verifies that the original Tjurina generators reduce to zero by that basis;
5. counts standard monomials of its initial ideal and obtains \((n-1)(n^2-n+3)\);
6. checks the displayed closed formulas for \(\mu\), \(\tau\), and \(\mu-\tau\).

The checker does not establish the all-\(n\) Milnor intersection formula; that formula is proved symbolically in `RESULT.md`. It also does not perform an independent literature audit.
