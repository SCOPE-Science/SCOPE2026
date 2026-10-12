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

The included `verify.py` uses only the Python standard library. It performs the following exact finite checks:

1. Constructs all \(81\) ternary length-four columns and the defining three-column separation predicate.
2. Uses independent symbol relabeling to normalize a selected codeword to \(0000\), then proves by branch-and-bound that no normalized family has ten columns.
3. Enumerates all normalized size-nine families; there are exactly eight.
4. Directly checks every enumerated family for the perfect-hash condition and for the \(\operatorname{OA}(9,4,3,2)\) pair-projection condition.
5. Exhausts all \(6^4\cdot24=31{,}104\) coordinate/symbol symmetries. One representative has an orbit of \(72\) labeled unordered families, exactly eight of which contain \(0000\). Thus the orbit exhausts the normalized census and therefore all maxima; its stabilizer has order \(432\).
6. Canonically serializes the normalized census and checks SHA-256 `6ae9b8858ab49282946cb1b34c64525624a51904f01fe99130fc913df5cffa59`.

A successful run ends with:

`VERIFY_OK maximum=9 normalized_maxima=8 labeled_maxima=72 natural_group=31104 orbits=1 orbit_size=72 stabilizer=432 all_maxima_OA=True bound_nodes=18705 enum_nodes=21771 census_sha256=6ae9b8858ab49282946cb1b34c64525624a51904f01fe99130fc913df5cffa59`

The computation proves only this finite parameter. It does not certify analogous statements for other alphabet sizes, row counts, or strengths.
