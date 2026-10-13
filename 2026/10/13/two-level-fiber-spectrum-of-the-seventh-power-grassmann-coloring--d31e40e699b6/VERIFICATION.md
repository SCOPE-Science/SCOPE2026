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

Run `python3 artifacts/verify.py` using the Python standard library. It reconstructs the binary extension field, enumerates all binary three-spaces independently by RREF and by independent triples, verifies the seventh-power/Moore-determinant identity for all \(1395\) spaces, computes all \(63\) nonzero fiber cardinalities, identifies the nine norm-one heavier fibers, partitions the spaces into the unique size-\(9\) subfield orbit and \(22\) size-\(63\) free orbits, verifies all seven coset counts, and checks distinct colors through all \(651\) binary two-spaces. Success prints `VERIFY_OK`. No probabilistic claims or large-parameter extrapolations are certified; independent audit is not performed.
