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

# Reproduction and limits

Execute `python3 verify.py` with a standard Python 3 interpreter. No third-party dependencies or external files are needed. The code reconstructs maximum triple packings on alphabets of sizes two through eight using direct examples; checks each proposed set of four-multisets for one-deletion shadow collisions; independently confirms the five multiplicity-profile resource counts for every four-multiset in these small alphabets; and verifies a noncanonical 24-word six-symbol optimum from an explicit six-cycle and six distinct uncovered wedge triples.

Expected final line: `VERIFY_OK`. The actual run completed with that line. In the six-symbol mixed construction the checker found 24 words and 54 distinct possible three-multiset deletion outputs, with no overlap across codewords. The canonical codes had respectively 3, 6, 11, 16, 24, 35 and 50 words for alphabet sizes two through eight.

The finite computation is not an exhaustive census of all optimal codes at these alphabet sizes, nor a proof of the unrestricted classification. The universal statement is proved using deletion-shadow resource equalities and a two-way correspondence with graph pairings. The infinite Steiner corollaries rely on Hanani's established quadruple-system existence theorem. The complete code construction and hypothesis checks, rather than a log alone, provide the reproducible finite evidence.
