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

The attached `verify.py` performs the complete finite proof with exact integer arithmetic.

It represents \(\mathbb F_{25}\) as \(\mathbb F_5[\alpha]/(\alpha^2-2)\), checks that \(g=1+2\alpha\) has multiplicative order \(24\), and constructs \(H=\langle g^4\rangle\). It then realizes all matrix entries in
\[
\mathbb Z[\zeta_{30}]
\cong
\mathbb Z[X]/\left(X^8+X^7-X^5-X^4-X^3+X+1\right).
\]

For the trivial character, the script checks all \(251\) nonempty square minors of the \(5\times5\) compressed matrix. For each of the five nontrivial characters it checks all \(69\) nonempty square minors of the \(4\times4\) compressed matrix. The zero-minor counts for character indices \(j=0,1,2,3,4,5\) are exactly
\[
0,\ 0,\ 10,\ 34,\ 10,\ 0.
\]
The corresponding character orders are
\[
1,\ 6,\ 3,\ 2,\ 3,\ 6.
\]

The verifier also checks explicit failure witnesses: a \(2\times2\) zero minor for each order-\(3\) character and a zero entry for the order-\(2\) character. It exits with `VERIFY_OK`.

Because the classification is finite and every determinant is reduced exactly in the cyclotomic quotient ring, this is exhaustive verification rather than numerical sampling. No statement about other finite fields is inferred from the census.
