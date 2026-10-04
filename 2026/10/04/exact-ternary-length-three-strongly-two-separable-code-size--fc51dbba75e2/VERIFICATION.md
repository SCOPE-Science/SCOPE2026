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

Run `python3 verify.py` in this package.

The program independently rebuilds all \(27\) ternary words, tests the strongly \(\overline{2}\)-separable failure condition directly, enumerates every subset through size five, derives the \(891\) forbidden four-subsets, verifies that every bad five-subset contains one of them, checks the explicit ten-word code, and exhausts a symmetry-normalized branch-and-bound search for an eleven-word code.

The normalization is exact: choose any codeword and independently relabel the three coordinate alphabets so that it becomes \(000\). Descendant equality and strong separability are invariant under these relabelings.

The computation is finite and exhaustive. No solver, random seed, timeout conclusion or partial enumeration is used. The verification establishes only the ternary length-three coalition-two claim and does not classify all optimum codes up to equivalence.
