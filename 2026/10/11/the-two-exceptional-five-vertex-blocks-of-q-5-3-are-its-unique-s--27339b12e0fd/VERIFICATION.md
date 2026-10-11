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
Run `python3 verify.py` from this package. The checker uses only the Python standard library and reconstructs \(Q_{5,3}\) from the published Example 7 formula.

It verifies the face vector \((15,45,30)\), that every edge is in exactly two triangles, the exact mod-two ranks, exhaustive enumeration of all \(65{,}536\) one-cocycles, the four cohomology classes, the three nonzero minimum-support profiles, the cup squares, the Wu characterization of \(w_1\), and the explicit five-edge supports and carrier sets.

The computation is finite and exhaustive. It does not certify that no unindexed publication contains the same result, and it does not extend the result to other parameters of the Datta--Upadhyay family.
