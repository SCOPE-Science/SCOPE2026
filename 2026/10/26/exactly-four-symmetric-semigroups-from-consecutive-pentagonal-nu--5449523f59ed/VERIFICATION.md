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
# Reproduction and limits

Run `python3 verify_pentagonal.py` with the Python standard library. Its Dijkstra algorithm finds the least semigroup element in every residue class modulo \(P(n)\). The exact Apéry formula computes genus and Frobenius number without relying on the gluing classification. It then compares symmetry with a separately coded gcd-and-membership test for every \(2\le n\le99\), and independently checks all \(100\le n\le3000\) against the explicit inequalities and criterion.

Observed result: `VERIFY_OK: n=2..99 independently Apéry/genus and gluing; exceptions: [(2, 22, 43), (3, 67, 133), (5, 850, 1699), (40, 129265, 258529)]; n=100..3000 no gluing, exact inequalities`.

No finite range certifies the infinite statement. The proof in `RESULT.md` supplies the global gcd restrictions, all integer-threshold inequalities, and checks every remaining finite case. This is a self-review, not an independent audit.
