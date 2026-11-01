---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: The exact source codebooks have the claimed lengths, cardinalities, and minimum distances 9,9,11; the independent bitwise count found pair-near edges 2064/7288/1517, near triangles 20388/79312/16965, valid fourfold centers 8/96/0 with all valid quartet centers distinct. For d>=2r-1, any r-ball-common pair has distance 2r-1 or 2r and has exactly binomial(2r,r) common centers, even in the odd-distance case. Every triple common center equals its binary coordinate-majority, which is forced by error-support disjointness; thus each near triangle contributes one center. A valid quadruple has a unique common center; if a five-list existed it would force at least five four-tuples sharing one center, contradicting distinctness. Inverting moments m*Vol(n,r), E*binomial(2r,r), T, Q yields all five bins and totals 2^n. This is an exhaustive finite proof for these three explicit books, not a statement about every code of the same parameters or a general optimal-code theorem.

## originality

PASS

PASS: The newly determined invariant is the full one-error-past-unique-decoding ambiguity spectrum of three explicitly published codebooks. The underlying constructions and their minimum-distance bounds belong to Ota, Osa and Harada and are not re-claimed; their results do not state ball overlap multiplicities. A distance spectrum alone would not in general supply all triple/quadruple Hamming intersection counts.

## value

PASS

PASS: Exactly one error beyond the guaranteed unique-decoding radius is the first natural list-decoding regime where performance is not captured by minimum distance. The complete size histogram determines the probability of any ambiguity, worst list size and counts of three- and four-way collisions for genuinely new high-density codes; the majority-center structural reduction is itself motivated and reusable. This is a self-contained, nontrivial exact finite invariant, not a restatement of the original packing bounds or an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
