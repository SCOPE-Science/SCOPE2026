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

# Verification of the mathematical finding

The exact mathematical objects are the full order-preserving contractions \(\mathcal C_n\) on \(\{1,\dots,n\}\). The proved result is the stabilization index's unique worst-case extremizers, conditional prefix-count representation, relative concentration, and convergence of every positive normalized moment. The proof is in `RESULT.md`.

Run `python3 check_stabilization.py` with Python 3 and no extra packages. The script enumerates all admissible maps for every \(2\le n\le11\), verifies the precise stabilization-time histogram and the count \((n+1)2^{n-2}\), checks the published fixed-point distribution, and compares explicit composition with an independently reconstructed side-distance prefix iteration. At \(n=11\), it exhaustively checks \(6144\) maps; it reports all assertions passed.

The finite enumeration does not certify the asymptotic theorem. The latter follows analytically from the union-of-Hoeffding-events bound, the uniform geometric tail for the fixed interval length, and exponential-tail control of the Bernoulli-prefix comparison cutoff. The result does not claim a second-order centered limiting law, applicability to other transformation distributions, or independent external validation.
