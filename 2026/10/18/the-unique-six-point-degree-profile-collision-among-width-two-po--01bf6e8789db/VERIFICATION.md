---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Reconstructed exhaustive finite coverage: any poset has a linear extension, so every type appears as a transitively closed upper-triangular relation on n<=6 vertices. Read source verify_uppertriangular.py and independently implemented and ACTUALLY EXECUTED a separate enumeration of all 2^{n(n-1)/2} ordered relation masks through six, checks every transitive triple and 3-antichain, and tests all degree-profile-preserving bijections. Independently observed iso types (1,2,4,10,26,75), profiles (1,2,4,10,26,74), one six-point doubleton. Checked displayed E0 plus (1,2) vs plus (1,3) are strict posets of width two with exactly six distinct profile values; unique profile-preserving bijection fails the adjacency test. First-round unique color labels force second refinement to reveal the mismatch. Exhaustion restricted to n<=6, no claim of general reconstruction.

## originality

PASS

The exact first degree-profile collision is not contained in inspected permutation-poset background or published net-degree theory. A more general 2017 assertion by Gellert–Sanyal, Theorem 3.6, appears to claim connected width-two transitive digraph uniqueness from labelled net degrees, but after aligning uniquely occurring in/out degree pairs the exhibited P/Q provide an explicit contrary connected transitive width-two witness. Accordingly do not rely on that inconsistent published assertion as proof of the negation or coverage. No prior 75/74 table found; risk of prior specialized enumeration remains.

## value

PASS

The first failing order of a natural directed local counting invariant, its unique pair, and the fact two refinement rounds suffice at that order give an exact expressivity boundary. The witness also identifies a precise issue with a stronger printed degree-reconstruction assertion; scientifically motivated finite classification rather than arbitrary small-table enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
