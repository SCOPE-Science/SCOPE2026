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
# Reproduction of mathematical checks

Run `python verify_is4_profiles.py` using only the Python standard library. Its literal checker iterates all reflexive binary relations on chains of size at most four, tests the two quantified existential witness confluence requirements and transitivity, and independently tests closure of their row/column maxima. It separately enumerates all pairs of closure maps for sizes one through eight and computes the forced-edge transitive closure and maximal allowed relation, verifying they are valid frames with exactly those extrema, that the local forbidden pattern is equivalent to unique reconstruction, and that the unique count equals the theorem's formula. For sizes at most six it enumerates every intermediate relation and tests reflexive/transitive confluence literally; for sizes at most four it cross-checks this count against direct enumeration.

Expected output ends with `VERIFY_OK`. Direct whole-relation counts for sizes one through six are \(1,4,20,126,1026,11324\); ordered profile counts are \(1,4,16,64,256,1024,4096,16384\); unique-profile counts are \(1,4,12,36,108,324,972,2916\).

The general theorem is established by the mathematical proof, not by a finite census. No independent audit was performed.
