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
# Verification and limits

The embedded `verify_partition_births.py` runs on Python 3 with only the standard library. Execute it in the same directory as this document. It generates integer partitions, constructs transfer edges independently from partition multisets, constructs the donor-recipient upper-link graph and verifies the exact line-graph adjacency for every upper-neighbor pair. It also checks the cycle-rank formula and, separately, all clique counts and Euler characteristics on sizes 1–22. The support-based formula and its series are compared with published first 25 numerical coefficients and expanded through size 60.

The checker successfully examined 4,507 partitions with sizes 1–22 and printed PASS. Exact computations are independent finite consistency checks, not a proof of the all-integer theorem. The proof's decisive infinite steps are the transfer classification, graph-nerve equivalence, null cone-attachment maps, and integral long exact sequence with graph-cycle quotients.

The documented numerical series may follow from a previously published exact face-vector series; uniqueness or numerical novelty is not asserted. The new claim is the local height-resolved integral birth and survival theorem. No external or independent scientific audit has been performed.
