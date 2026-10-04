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
The proof is uniform. The finite checker is used only to replay the low-rank boundary and the concrete witness.

For \(n=7,8\), `artifacts/verify.py`:

- generates all partitions of \(n\);
- computes \(S_n\)-character degrees using the hook-length formula;
- applies the standard restriction rule to \(A_n\);
- confirms that exactly one irreducible character has degree \(n-1\);
- enumerates every element of \(A_n\);
- constructs the Cayley graphs from a \(3\)-cycle and from two disjoint \(3\)-cycles;
- verifies that every component in both graphs has size \(3\);
- verifies the fixed-point character sums and their difference \(6\).

For \(n\ge9\), the only non-elementary premise used is the classical uniqueness of the degree-\(n-1\) irreducible character of \(A_n\).

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the infinite-range Cayley-graph decomposition or the character-sum formulas.
