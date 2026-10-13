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

The verifier starts from the ternary prefix \(\mathtt{0121012}\) and exhaustively appends each of \(0,1,2\). For every candidate it forms the binary morphic image and checks richness and \(\frac{14}{5}\)-power avoidance exactly.

Richness is reconstructed in two ways. The first enumerates all distinct nonempty palindromic factors and requires their number to equal the binary length. The second applies the equivalent condition that every nonempty prefix has a unioccurrent longest palindromic suffix. The two complete searches must agree at every ternary length through \(50\).

Power avoidance is checked by computing the least period of every nonempty factor and rejecting precisely when \(5|x|\ge14p\). The three length-\(49\) images are then rescanned independently for their exact critical exponents and palindrome counts.

The verification proves only the stated finite equality classification. Independent audit has not been performed.
