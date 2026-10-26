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

Run `python3 verify.py certificate.tsv` in a directory containing the two files. The code uses only Python 3's standard library, regenerates all 2048 cycles twice, verifies their de Bruijn property, checks both LZ78 dictionary implementations on all 65536 rotations, and byte-compares the supplied 2048-row certificate with its regenerated values.

Expected outputs include `VERIFY_OK cycles=2048 cases=65536 rotations=65536`, joint bins `(11,13):6, (11,14):44, (12,13):746, (12,14):1172, (13,13):30, (13,14):50`, and anchored bins `11:18, 12:480, 13:1508, 14:42`.

The enumeration is exhaustive because every length-five edge traversal must specify one of two bijections between incoming and outgoing edges at each of sixteen four-bit vertices; exactly one map is recovered from each cycle, and a single-orbit permutation is both necessary and sufficient. DFS Euler enumeration supplies a structurally independent cross-check. These finite results imply nothing automatically for order six or above. Public literature priority and compressed-bit sizes are not computationally verified by these scripts.
