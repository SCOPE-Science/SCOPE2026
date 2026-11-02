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

# Reproduction and verification

Run `python3 verify.py` from the directory containing this document; Python 3 standard-library support suffices. The checker independently represents an outward-star monoid element as either a leaf subset or a pair of disjoint leaf subsets separated by the center generator. It implements multiplication directly from these canonical words.

For \(m=1,2,3\), it checks closure and associativity of the full monoid multiplication, checks that the idempotents have exactly the two specified types, and enumerates every tuple of potential images of the \(m+1\) generators. Each tuple is accepted only after independently evaluating all idempotence, commutation, and directed Hecke–Kiselman relations using the multiplication table. The resulting endomorphism counts are \(15\), \(339\), and \(22233\), with agreement in every finer center-bit stratum. It also checks formula values \(4780047\), \(4058199945\) for \(m=4,5\) and prints numerical ratios toward the predicted limiting constant for \(m=10,20,30\).

The expected final output marker is `VERIFY_OK`. The checks provide finite counterexample screening and reproducibility. They do not certify the unbounded parameter theorem; that theorem is proved symbolically in `RESULT.md`. The normal-form uniqueness step relies on the cited 2019/2020 confluence theorem. No formal proof assistant or external mathematical validation is claimed.
