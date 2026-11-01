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

# Finite verification

The result concerns exactly two deletions from ternary source words of lengths \(4\), \(5\), and \(6\). All certificates and checks use exact integers.

Run `python3 verify_ternary_cover.py`. This checks each upper-bound codebook; proves the length-four lower bound directly; generates all \(243\) possible length-five shadows and all of their \(15141\) submasks; excludes every fourth-center completion of all \(132651\) necessary triples with three distinct majority symbols; and sums the 10-class weight table across all \(81\) length-six targets and the shadows of all \(729\) source words. It reports total target weight \(90\) and maximum source-shadow weight \(11\).

Independently compile and run `c++ -O2 -std=c++17 verify_ternary_cover.cpp -o verify_cover && ./verify_cover`. Instead of using the submask reduction, the C++ code directly checks the maximum union over all \(51^3\cdot 243=32234193\) ordered quadruples containing one source with at least three copies of each alphabet symbol. It finds maximum \(26\) distinct length-three descendants. Its independently implemented subsequence enumeration and integer weight function agree with the Python verifier.

The exact outputs from the actual runs appear in `verification_output.txt`. Exhaustive finite enumeration proves only the stated finite cases; it is not evidence for an infinite family or independent scientific audit.
