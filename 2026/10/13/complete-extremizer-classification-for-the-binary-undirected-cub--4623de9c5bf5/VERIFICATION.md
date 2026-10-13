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

Run `python3 verify.py` beside `certificate.json`.

The verifier starts from the empty word and extends every surviving binary prefix by both letters. Since avoidance of \(\mathtt{xxx}\) up to reversal is inherited by factors, every admissible word is reached.

For each appended bit, it checks every suffix of length \(3m\), splits it into \(A,B,C\), and rejects exactly when both \(B\) and \(C\) belong to \(\{A,A^{R}\}\). It regenerates the complete survivor-count vector
\[
1,2,4,6,10,16,18,12,10,6,0
\]
for lengths \(0\) through \(10\), verifies the exact six words at length \(9\), and verifies that length \(10\) is empty.

A separate whole-word procedure scans every factor of each of the six extremizers for every possible block length, avoiding reliance on the incremental-search invariant. The verifier also recomputes the reversal/complement orbits and checks that their sizes are \(2\) and \(4\).

The verification establishes only the finite equality classification stated here. Independent audit has not been performed.
