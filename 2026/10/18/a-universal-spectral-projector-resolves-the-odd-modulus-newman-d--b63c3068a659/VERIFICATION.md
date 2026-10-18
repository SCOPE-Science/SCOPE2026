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

# Reproducible mathematical verification

Execute `python3 verify_newman_projector.py` from the folder containing the standalone checker. No third-party modules are needed. Expected terminal status: `VERIFY_OK`.

The code computes the exact digit-transfer matrix for each odd \(n\in\{3,5,\ldots,25\}\), uses integer matrix products to verify \(P_n(B^2)=J_n\) entry by entry, and tests the digit transition plus all residue-coordinate identities for 144 different integer cutoff/modulus pairs. It also independently counts signed digit sums over several small complete blocks for moduli \(3,5,7\) and compares the original binomial sum without relying on matrix iteration.

The infinite mathematical justification is the self-contained root-of-unity proof in RESULT.md; the finite executable checks are corroborative only. No external mathematical reviewer or independent certification is claimed. The theorem does not cover even moduli, other bases, or noninteger cutoffs. Literature novelty remains contingent on independent review.
