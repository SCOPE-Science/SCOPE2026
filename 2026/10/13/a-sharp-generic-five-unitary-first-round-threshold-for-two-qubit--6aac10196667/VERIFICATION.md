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

The analytic proof reduces the two-qubit random-unitary first-round question to exact ranks of pair-product spans and their sums with the two four-dimensional local matrix algebras.

`verify_generic_random_unitary.py` contains the explicit Hermitian Gaussian-rational Cayley witness. It reduces the witness modulo the prime \(1009\), where \(469^2\equiv-1\), and checks exact ranks. The required rank rows are
\[
(3,6,6),\quad(7,10,10),\quad(13,16,16),\quad(16,16,16),
\]
where each triple is pair-product rank, rank after adjoining Alice's local algebra, and rank after adjoining Bob's local algebra for \(m=2,3,4,5\), respectively.

The modular calculation certifies nonzero characteristic-zero minors; it is not a finite experiment standing in for the generic theorem. The all-tuples-outside-a-null-set conclusion follows from nonvanishing real-analytic minors on \(U(4)^m\).

The proof does not establish LOCC implementability for \(m\ge5\); only the first-round obstruction is shown to vanish.
