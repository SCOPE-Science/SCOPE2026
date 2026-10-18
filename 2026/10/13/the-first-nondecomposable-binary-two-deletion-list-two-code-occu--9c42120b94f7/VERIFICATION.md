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

For n=2..7 and list bounds L=1,2, exact optimal cardinalities are respectively [1,2,2,2,4,5] and [2,3,4,4,7,11]. A binary incidence matrix records whether received length-(n-2) word is a distinct ordered subsequence of each candidate codeword. Explicit valid primal codebooks reach every claimed optimum. For every candidate column, nonnegative integral dual weights and slacks satisfy incidence weight plus slack >=d, yielding |C|<=floor((L sum weights+sum slacks)/d). Independent checker reconstructs deletion shadows, checks all column inequalities and each listed codebook, including n7 dual d=59 and upper bound floor(666/59)=11. At n7, 11>2*5, while no smaller n has the strict inequality. This is exhaustive finite certification for n<=7, not an asymptotic extrapolation.

## originality

PASS

The exact n6 list-two value 7 has been previously reported by published Resultary, and the unique n7 value5 is in OEIS A057591. These are properly credited and do not imply the first separation because the nontrivial new ingredient is n7 list-two optimum11. Lin, Guruswami–Håstad and Kiah–Wei–Zeng develop general bounds or asymptotic constructions rather than the 11-word exact optimum in the inspected accessible material. Full Kiah 2026 text was inaccessible and remains a genuine prior risk.

## value

PASS

Determining the earliest length where a list-two two-deletion code cannot be represented as a union of two uniquely decodable codes is a sharp structural property of synchronization-channel coding. The exact length-seven optimum with a reproducible integer dual certificate is a motivated finite cutoff, not merely a random small code enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
