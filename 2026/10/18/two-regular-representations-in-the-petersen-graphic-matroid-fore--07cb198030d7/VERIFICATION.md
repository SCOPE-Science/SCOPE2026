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

# Reproduction of the exact finite checks

Run `python3 verify.py` with Python 3.10 or newer; only the standard library is required. The script reports success only after checking the seven conjugacy-type orbit polynomials and a separately computed oriented-face Lefschetz trace for each of the \(120\) five-label permutations.

The graph model starts with the ten two-subsets of \(\{0,1,2,3,4\}\), listed lexicographically, and the fifteen edges joining disjoint pairs, also listed lexicographically. The test enumerates all \(32768\) subsets of those fifteen edges and verifies that exactly \(22292\) are forests. The forests contribute to the augmented simplicial chain complex; the empty forest must be included to obtain the reduced character.

The mathematical bridge from the finite trace to the actual homology representation is the standard matroid shellability/concentration theorem. The checker does not independently prove the shellability theorem. Character equality is a rational semisimple group-representation conclusion, not an integral module calculation. No independent external audit is represented by these checks.
