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

# Exact arithmetic checks and scope

The exact standalone verification program `verification/check_arithmetic_rank.py` expands all twelve published algebraic point identities, computes the height pairing \(H\), reconstructs the new cross-conjugate pairing \(G\) from the source's type-IV intersection rules, verifies both specialized fibre calculations \(v=5\) and \(v=7\), and checks the two stated nonzero principal determinants.

The machine-readable input `verification/cross_pairing.json` records the complete integer matrix \(3G\), the source point order, and both determinant index sets. `verification/check_output.txt` records a successful invocation with exact rational computation; the checker recomputes the entries instead of trusting those results. Further group-law tests at three rational specializations corroborate the conjugation map; they are not offered as a proof from finite samples.

The mathematical argument uses exact specialized height determinants to prove generic independence, then the geometric rank bound previously established for the source curve. The checks do not establish an integral basis, torsion over unrelated extensions, or any geometric claim not stated in the theorem. No external independent audit has been performed.
