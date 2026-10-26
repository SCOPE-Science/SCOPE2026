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

# Reproducibility and limits

The proof of the classification is contained in `RESULT.md`. The program `verify.py` enumerates additive subspaces and the ideals they form in six short \(\mathbb F_2\)-algebras and two direct products. It computes annihilators and the coprime condition for every nonzero ideal by checking all pairs of ideals, rather than using the proposed socle classification to select candidates.

A second routine tests all ideals of the integer quotient rings \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), \(\mathbb Z/12\mathbb Z\), and \(\mathbb Z/30\mathbb Z\) using integer multiplication, thereby checking mixed characteristic examples separately from the vector-space implementation.

Run `python3 verify.py` with Python 3 and no external packages. The observed terminal line is `VERIFY_OK exhaustive_coproduct_checks=12`. The checks cover explicitly named finite examples, not all Artinian rings; the uniform classification depends on the essential-socle, Nakayama and direct-product arguments in `RESULT.md`. No external mathematical certification or independent assessment is asserted.
