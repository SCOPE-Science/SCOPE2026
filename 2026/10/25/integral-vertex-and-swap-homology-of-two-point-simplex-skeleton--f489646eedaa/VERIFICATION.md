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
Run `python3 verify_deleted_skeleton.py` with Python 3 in a directory containing the included file. No third-party libraries or downloaded data are required.

The checker enumerates all admissible cellular products \((A,B)\) with disjoint supports. For \(n=4,5,6\) it uses independent bit-vector elimination to compute mod-two cellular homology and verifies precisely one reduced group of rank \(2n-1\) in dimension \(n-3\); for \(n=4,5,6,7\) it verifies thirty-two signed Lefschetz identities. In the full deleted product it also constructs an integral fundamental cycle from codimension-one incidence relations, checks the cycle condition and primitivity of every one of the \(2n\) relative coordinates, and verifies the action's global orientation degree for the selected permutations and swaps.

Expected completion lines include `SIGNED_CELLULAR_LEFSCHETZ_VERIFIED 32 cases for n=4..7` and four `PRIMITIVE_RELATIVE_FUNDAMENTAL_CYCLE_VERIFIED` lines (\(n=4,5,6,7\)). The all-parameter theorem is mathematical and is proved in `RESULT.md`, rather than being inferred from a finite enumeration. The testing method has not undergone external independent validation.
