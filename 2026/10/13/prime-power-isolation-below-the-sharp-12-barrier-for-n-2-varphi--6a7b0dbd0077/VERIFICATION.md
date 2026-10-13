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

The proof in `RESULT.md` is unrestricted.

The attached `verify.py` checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes the exact factorization, \(\sigma(n)\), \(\varphi(n)\), and
\[
F(n)=n^2-\varphi(n)\sigma(n).
\]

For every input with at least two distinct prime factors it asserts
\[
F(n)\ge12
\]
and verifies that equality occurs only at \(6\). It also verifies that every nonprime value below \(12\) is exactly one of
\[
(4,2),(8,4),(9,3),(16,8),(25,5),(27,9),(49,7),(121,11).
\]

The finite replay is corroborative only. The infinite result follows from the symbolic Euler-product proof.
