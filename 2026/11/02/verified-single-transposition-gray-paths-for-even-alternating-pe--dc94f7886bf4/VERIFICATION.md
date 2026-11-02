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
# Finite-certificate verification

The binary file contains consecutive zero-based indices into lexicographically sorted alternating permutations on zero-based symbols. It has four unsigned little-endian 16-bit blocks for even lengths \(4,6,8,10\). The exact block lengths are \(5,61,1385,50521\).

`verify_primary.py` enumerates all candidate permutations by a full permutation iterator, extracts alternating states, and checks every position of the index certificate. The independently implemented `verify_alternative.cpp` recursively generates only valid alternating prefixes and rechecks every block, transition and index uniqueness. Both are complete finite checks. Command lines:

```
python3 verify_primary.py gray_paths_u16le.bin
c++ -std=c++17 -O2 verify_alternative.cpp -o verify_alt
./verify_alt gray_paths_u16le.bin
```

Checks performed on these packaged bytes: `PRIMARY_PASS` for sizes \(4,6,8,10\), `ALL_PATHS_VERIFIED`, `ALTERNATIVE_PASS` for each size, and `ALTERNATIVE_ALL_PASS`.

The certificate is an explicit proof for only the four finite sizes. No all-even-size extension or independent external scholarly validation was performed.
