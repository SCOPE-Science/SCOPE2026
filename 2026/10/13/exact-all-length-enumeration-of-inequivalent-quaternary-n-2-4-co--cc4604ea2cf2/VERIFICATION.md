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

The verifier `verify.py` uses only the Python standard library and reads `inequality_certificate.json` from the same directory.

It performs four exact checks:

1. It implements \(\mathbb F_4\) arithmetic and confirms the Hermitian Gram-rank trichotomy for all \(32\) parity subsets of the five points of \(\operatorname{PG}(1,4)\).
2. It reconstructs the Burnside counts from the four cycle types of the natural \(A_5\)-action on five points and reproduces the listed values of \((I_{n,0},I_{n,1},I_{n,2})\).
3. It reconstructs the three rational generating functions by exact polynomial/rational arithmetic and verifies that the reduced difference functions recorded in the certificate are algebraically identical to the differences of those generating functions.
4. It checks \((1-x^{60})^6D_{ij}=P_{ij}\) exactly and, on each of the sixty residue classes, expands the eventual degree-five coefficient polynomial after its finite shift and verifies that every ordinary coefficient is strictly positive; the finitely many preceding cases with \(n\ge4\) are checked directly.

A successful run prints `VERIFY_OK`. The computation supplements the symbolic proof; it is not used as a substitute for the all-length argument.
