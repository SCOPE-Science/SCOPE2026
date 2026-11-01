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

# Reproducibility and verification

Run `python3 verify.py` from the directory containing `certificate.json`. The code uses only the Python standard library (Python 3.9 or later). Successful execution prints `VERIFY_OK` after completing all checks; `verification_output.txt` is the recorded output.

The verifier independently constructs the face-cardinality distribution by a row-transfer recurrence, cross-checks it against explicit graph-face enumeration, and checks every matched edge, all reversed Hasse incidences for acyclicity, and every signed gradient-path calculation. It computes all integral Morse boundaries, confirms their compositions vanish, and reduces each exactly through **unimodular** integer row and column operations with only unit pivots. Every residual matrix is exactly zero. Original unreduced mod-two boundary ranks are also computed for sizes through five.

Exact scope: \(1\leq n\leq6\). The six-by-six run enumerates \(202841\) faces (including the empty face), pairs \(101331\) pairs of incident faces, and leaves \(179\) critical cells. Its nonzero Morse boundary ranks are \(8\) in degree six and \(7\) in degree seven, with unit-only integral invariant factors. The five-by-five case enumerates \(6427\) faces and has nonzero boundary ranks \(1\) and \(3\) in degrees three and four. Checks are exhaustive for these finite boards, not evidence for any unrestricted-width theorem. These checks do not amount to independent human or mathematical certification.
