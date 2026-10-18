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

# Reproducibility and boundaries

Run `python3 verify.py` using Python 3.9 or later. This standalone program uses only the standard library and constructs \(\mathbb F_{2^f}\) for \(f=1,2,3,4\) using explicit irreducible binary polynomials. It enumerates all linear maps on each test algebra, not just maps in the claimed set, and verifies the weight-one Rota–Baxter identity on each unordered basis pair. Bilinearity and commutativity make these tests equivalent to all pairs of elements for a given map.

Exhaustive cases and totals: \((q,n)=(2,2)\): \(4/16\); \((2,3)\): \(4/512\); \((2,4)\): \(4/65536\); \((4,2)\): \(4/256\); \((4,3)\): \(4/262144\); \((8,2)\): \(4/4096\); \((16,2)\): \(4/65536\). In each case the exactly four solutions agree entry-for-entry with the zero, identity, constant projection, and radical projection operators.

All runs reported `ALL_EXHAUSTIVE_CHECKS_PASSED`. The proof in `RESULT.md`, not the finite experiments, establishes the statement for all characteristic-two fields and all \(n\ge2\). Literature-search coverage is imperfect; no independent scientific audit was performed.
