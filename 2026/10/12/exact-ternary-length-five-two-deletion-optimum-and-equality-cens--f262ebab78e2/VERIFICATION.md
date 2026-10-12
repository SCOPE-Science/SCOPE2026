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

`verify.py` is a complete standard-library verifier for the finite claim. It regenerates all \(243\) ternary length-five words and their two-deletion shadows. It independently computes longest common subsequences and checks all \(29403\) unordered pairs for equivalence with shadow disjointness.

The script then runs two exhaustive searches on the resulting compatibility graph. The first is a maximum-clique branch-and-bound with greedy-color upper bounds; the second is an ordered fixed-cardinality recursion that counts all cliques of prescribed size. The searches return maximum \(6\), exactly \(478\) six-cliques, and zero seven-cliques.

It next regenerates the natural order-\(12\) action of all alphabet permutations and reversal, verifies closure on the equality set, computes \(46\) orbits with sizes \(2^1,4^2,6^8,12^{35}\), performs a Burnside fixed-set check, and computes the exact received-word coverage distribution. It also reruns the same finite maximum search for lengths \(2\) through \(5\) and evaluates the cited Kulkarni–Kiyavash bound as \(14\).

Run:

`python3 verify.py`

The final line must equal the contents of `EXPECTED.txt`. The canonical list of all \(478\) maxima is serialized internally and checked through SHA-256 `7dff591068a541f40fd02801d35ef2e263638e21eadbc7c0b9d9f1a71837a99d`.

Limits: this verification proves only the stated finite parameter case and natural-group orbit data. It does not prove a general formula beyond these parameters or that the natural order-\(12\) group is the full automorphism group.
