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
z(n)=\sigma(n)+\varphi(n)-2n.
\]

It verifies the complete fibers
\[
z^{-1}(3)=\{8\},
\quad
z^{-1}(4)=\{27\},
\quad
z^{-1}(5)=\varnothing,
\quad
z^{-1}(6)=\{125\},
\]
\[
z^{-1}(7)=\{16\},
\quad
z^{-1}(8)=\{12,343\}.
\]

It also checks that every nonsquarefree integer with exactly two distinct prime factors has value at least \(8\), with equality only at \(12\), and that every integer with at least three distinct prime factors has value at least \(20\).

The finite replay is corroborative only. Exhaustiveness beyond the cutoff follows from the symbolic factorization-shape proof.
