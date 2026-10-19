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

# Verification scope

The finite claims are checkable with the two standalone sources in `verification/`. The Python program reads every line in `certificates/witnesses.tsv`, constructs all distinct descendants by choosing retained positions (not deletion positions), confirms disjoint two-deletion balls and cardinality of their three-deletion intersection, and matches the explicit 18-element common-descendant set for the ternary example. Each source word has length at most 11, so every check is a finite combinatorial enumeration.

Compile the C++ program with `g++ -O3 -std=c++17 verification/verify_binary_census.cpp -o verify_binary_census` and execute `./verify_binary_census`. It constructs independent bitset representations from deleted-index combinations. It checks all distinct unordered pairs of binary words at lengths 3 through 13, with no symmetry pruning, and verifies that size 18 never occurs under two-deletion separation. At length 13 it also checks that each of 0–20 except 18 does occur. The set of lengths after 13 has not been enumerated or excluded.

The global upper bound comes from Sun and Ge (arXiv:2606.25822, Theorem 1.1) and is not proved by the finite checker. The finite tables plus the published universal bound together establish the all-alphabet claim for alphabets of cardinality at least three. These checks do not provide external auditing or independently certified verification.
