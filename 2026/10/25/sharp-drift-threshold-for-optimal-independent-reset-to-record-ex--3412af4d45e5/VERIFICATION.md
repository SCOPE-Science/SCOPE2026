---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Gap G=M-X has geometric invariant distribution with λ=t(q+pλ²), t=1-r, for 0<r<1. Positive recurrence, ergodic frontier occupation, and martingale strong law give speed tp(1-λ); no-reset endpoint is max(2p-1,0), r=1 is zero. Reparameterizing by λ makes derivative sign q(1-2λ)-pλ², giving interior optimizer iff p<3/4 and critical boundary otherwise, with quadratic gain onset. Independent rational cases and 501-point reset grids checked. Uniform proof follows chain/derivative analysis, not sampled grids.

## originality

PASS

Majumdar–Sabhapandit–Schehr 2015 foundational paper explicitly uses symmetric jumps and prohibits no-op resets at the frontier; this changes its gap kernel. Other examined works preserve that conditioned reset or treat first passage, not this exact independent-clock optimized bias law. Existing generic renewal methods could yield this after specialization, acknowledged.

## value

PASS

Sharp global optimization and drift phase transition for a mathematically natural alternative resetting protocol with a continuous quadratic onset; avoids conflating different frontier rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
