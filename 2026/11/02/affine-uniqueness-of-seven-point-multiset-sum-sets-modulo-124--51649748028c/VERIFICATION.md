---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Any collision among 64 subset sums of the six translated nonzero residues produces a forbidden seven-term multiset by exchanging disjoint supports and padding zeros. Without unit differences, parity compression gives <=62 subset sums or mixed parity forces all points congruent mod31 and cardinality<=4; hence a unit pair normalizes A to contain 0 and1. The direct source C++ loops cover all C(122,5)=207288004 normalized candidates, and check all C(13,6)=1716 multiplicity vectors after necessary subset-sum injectivity. Its separate bitset-pruned C++ generator checks each possible prefix, and an independent fresh C++ implementation reproduced 5,192,384 injection survivors and exactly ten valid normalized sets. Checked its ten lines byte-for-byte against the frozen normalized_valid.txt. Independent Python computed all 7440 affine images of canonical C, trivial stabilizer, and exactly the normalized ten; checked the sum-multiset condition for each. Thus exhaustiveness is finite and actually established at modulus124, with no claim for other moduli or general n.

## originality

PASS

Fonollosa's 2026 minimum-modulus result supplies the natural modulus124 for seven points and conjectural/computational optimizer equivalence, not a proof of exhaustive uniqueness. The frozen record supplies a complete finite C++ census and affine-orbit exhaustion of this specific group; I inspected proof and two complete enumeration algorithms. Inal's unrestricted finite-abelian-group minimum-order theorem concerns a different ambient optimization, and Bedert's two-term unique-sum invariant differs. Historical priority risk remains for Fonollosa's companion Fourier/permanent article (body not accessible) or an unindexed equivalent optimizer classification.

## value

PASS

A fixed modulus124 is not arbitrary: it is the natural minimal modulus for the canonical seven-element construction. Proving the complete affine-optimizer classification and exact orbit size is a substantive finite rigidity question identified in predecessor work; the complete census establishes the exact fact for a natural bounded case, without claiming a general n classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
