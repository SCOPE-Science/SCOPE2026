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

The proof is symbolic for all integers \(n\ge3\): its key assertions are the two complete relation lattices, the sign-conformal nonnegative decomposition of every length-nondecreasing displacement, and the primitive two-point equal-length fiber. The finite checker `verify.py` independently constructs the generators and relations, enumerates short complete fibers, and exercises the constructive monotone chain on every tested pair. An execution of `python3 verify.py` passed for parameters \(3\le n\le15\), comprising 185 nontrivial fibers and 2,923 pairs. These bounded tests do not establish the all-parameter statement without the supplied proof. No external mathematical audit or certification was performed.
