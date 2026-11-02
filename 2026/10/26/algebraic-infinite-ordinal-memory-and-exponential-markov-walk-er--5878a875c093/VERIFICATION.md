---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The four Markov partition cells have lengths 1/3,1/6,1/6,1/3, and restricted rise-state transition Q=[[1/3,1/6],[0,1/3]], whose nontrivial Jordan block gives R_n=(n+2)/(2*3^n). The next-rise conditional ratio (n+3)/(3(n+2)) strictly changes with n, impossible for any finite Markov order. The calibrated binary surrogate has plus-stay 4/9, stationary plus probability 1/2, so its run likelihood (1/2)(4/9)^(n-1) divided by actual R_n tends exponentially to infinity. This is only a statement about the observable binary factor, not the four-state hidden chain.

## originality

PASS

The explicit Jordan-block algebraic run law and resulting infinite binary memory quantitatively distinguish the deterministic observation from the finite constructed transition-network Markov walk studied in source literature; no matching earlier run formula was located in the inspected texts.

## value

PASS

A canonical expanding map provides exact infinite-length run laws, rigorous infinite memory of a binary observable, and exponential failure of a widely motivated one-step Markov approximation despite a positive spectral gap. This is a mathematically sharp information-loss example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
