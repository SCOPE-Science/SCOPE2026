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

The supplied `verify.cpp` is a complete finite checker for the claim. It reconstructs all 81 ternary words and every forbidden triple from the descendant definition. It then performs four exact branch-and-bound searches covering all Hamming-distance normal forms of a hypothetical 13-word code, enumerates every 12-word maximum containing 0000, and traverses all 31,104 coordinate/symbol equivalences.

A successful replay prints the exact `VERIFY_OK` line stored in `verification_output.txt`, followed by the two representative codes. The crucial consistency checks are also recomputed: the 832 normalized maxima imply 5,616 labeled maxima by incidence double counting; orbit sizes 5,184 and 432 sum to 5,616; stabilizers 6 and 72 satisfy orbit-stabilizer; and the orbit incidences through 0000 are 768 and 64.

The checker proves only the stated finite ternary length-four result. It does not certify any claim for other alphabets, lengths, or coalition sizes.
