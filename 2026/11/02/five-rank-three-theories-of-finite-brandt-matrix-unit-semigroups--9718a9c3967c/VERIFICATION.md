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

# Verification details

All scripts use only Python 3 standard-library modules. They are standalone and can be run independently in the same directory.

`python3 verify_direct.py` constructs the full \(1+n^2\)-element multiplication table for each \(1\le n\le7\), computes equality and every ternary multiplication atom involving the named zero and up to three selected elements, then recursively computes exact one-element-extension type *sets*. The output type identifiers use a common global interning dictionary across all sizes; matching identifiers therefore mean equal full recursively defined types, not coincidentally equal local ranks.

`python3 verify_orbits.py` computes an independently organized orbit-compressed recursion on canonical equality patterns of ordered row and column indices, for each \(1\le n\le14\) and ranks one through four. At rank three it finds distinct root types for \(1,2,3,4,5\) and the same root type for each \(5\le n\le14\). Type identifiers are globally interned.

`python3 verify_boundary.py` independently evaluates four explicit first-order boundary formulas on \(1\le n\le9\) and checks equality of the *complete* atomic diagrams for \((e_{12},e_{34},e_{56})\) and \((e_{12},e_{34},e_{15})\), with zero named. The Boolean formula vectors match the truth conditions \(n\le j\) for \(j=1,2,3,4\).

The included `direct_output.txt`, `orbits_output.txt`, and `boundary_output.txt` are recorded outputs of these checks. No program's finite range is used as a proof of stabilization for all sizes; the text's explicit three-round strategy proves the infinite assertion. No independent audit is claimed.
