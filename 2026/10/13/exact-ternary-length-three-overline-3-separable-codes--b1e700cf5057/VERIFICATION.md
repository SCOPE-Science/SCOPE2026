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

Run `python3 artifacts/verify.py` with a standard Python 3 interpreter.

The program constructs all \(27\) ternary words of length three, encodes descendant coordinate sets exactly as bit masks, and performs an exhaustive lexicographic search. Its incremental collision invariant is complete because adding one word creates exactly the singleton, pair, and triple subsets containing that word. It then directly validates all reported maxima from scratch and tests every one-word extension of every maximum, so the upper bound does not depend only on a search log.

The verifier also constructs all \(1296\) transformations in \((S_3)^3\rtimes S_3\), confirms that each maps the complete maximum census to itself, obtains the two orbits, and checks their coordinate and pair-projection profiles.

Expected terminal output:

`VERIFY_OK maximum=6 labeled_maxima=135 size7_extensions=0 natural_group=1296 orbits=2 orbit_sizes=27,108 stabilizers=48,12 nodes=6652 rejections=23387 census_sha256=5eb96554a975da8d94e0dbcd1ccd0453a081bcee2257efcab8a6128bc8f5666c`

The proof is finite and exhaustive only for \(Q=\{0,1,2\}\), length three, and coalition size at most three. No inference about larger alphabets or lengths is made.
