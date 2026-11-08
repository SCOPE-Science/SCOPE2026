---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The neutral expectation update for each active star is the written row-stochastic 3x3 matrix with eigenvalues 1, lambda=1-1/[n(n-1)], mu=(n-2)/[n(n-1)]; tau-th powers are exact spectral-projector combinations. The stationary row of T=M_B^tau M_A^tau is (U,V,(n-2)W)/Z by substitution/tree formula, and coalescence ensures fixation equals limiting expectation. Explicit subtraction yields V-U=(n-1)(n-2)(1-x)(1-y)>0 and W-V=(n-1)(n-2)x(1-y)>0. For tau/n^2->theta, x->exp(-theta), y<=n^(-tau), U~n,W~n^2,Z~n^3 uniformly. Independently built full 2^n state absorbing chain n=3,4,5, tau=1,2 reproduces all three probabilities. No nonneutral or shifted-phase claim.

## originality

PASS

Bhaumik and Masuda already formulate the periodic switching neutral birth-death problem and its 1/n mean under uniformly random initial sites, and dynamic reproductive values are known. The present claim resolves two different alternating stars, site-resolved phase-specific probabilities, strict A<B<leaf and the n^2 transition; neither general recurrence alone nor a different death-birth model supplies the explicit result. Best-of-knowledge PASS subject to equivalent earlier specializations.

## value

PASS

Neutral fixation on temporally varying graphs depends on initial phase and vertex, unlike a simple average. The exact strict hub asymmetry and n^2 switching-duration crossover explain a natural difference between temporal ordering and a static aggregate, with direct use in dynamic evolutionary graph theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
