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
# Verification record
The included `verify.py` was run with Python 3. It printed one `OK` line for each of the three forms over each of five prime fields and ended in `VERIFY_OK`. Actual group actions, not merely expected numerical values, were enumerated and checked. Every example is nondegenerate and has a one-dimensional square, and multiplication is represented by its exact bilinear form and derived generator.

Over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), and \(\mathbb F_{13}\), the script checked: \(B=\operatorname{diag}(1,1),u=(1,0)\); \(B=\operatorname{diag}(1,a),u=(1,0)\) with \(a\) a nonsquare; and \(B=\operatorname{diag}(1,-1),u=(1,1)\). The latter has isotropic derived line and a transitive multiplicative automorphism group. The former two have exactly two automorphisms. The script checks each candidate matrix's multiplication action exactly modulo the prime, counts all projective orthogonal pairs, and partitions them by the automorphism group.

Limitations: These are finite tests over five prime fields, whereas the proof covers every odd prime power and an arbitrary infinite field of odd characteristic. The checker is a reproducibility artifact, not an independent or exhaustive verification of the general theorem. Independent mathematical audit has not been performed.
