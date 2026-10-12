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
The proof is symbolic and does not depend on finite enumeration.

The packaged checker `artifacts/verify.py` enumerates the element orders in the odd abelian kernels
\[
C_9,\quad
C_3\times C_3,\quad
C_9\times C_5,\quad
C_3\times C_9,
\]
\[
C_5\times C_5,\quad
C_3\times C_3\times C_5,\quad
C_9\times C_{25},\quad
C_3\times C_9\times C_5.
\]

For each kernel \(A\), it builds the predicted generalized-dihedral pseudo-algebra
\[
\{(1,1),(2,1)\}
\cup
\{(d,N_A(d)/2):d>1\}.
\]
It checks integrality of every nontrivial multiplicity and verifies the degree-squared identity
\[
2+\frac{|A|-1}{2}\cdot4=2|A|.
\]

The checker then reconstructs each Sylow invariant partition solely from the pseudo-algebra values
\[
1+2\sum_{j\le k}m_G(p^j)
\]
and verifies exact agreement with the original kernel.

It also confirms that the same-order kernels
\[
C_9\times C_5
\quad\text{and}\quad
C_3\times C_3\times C_5
\]
produce different pseudo-algebras.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.
