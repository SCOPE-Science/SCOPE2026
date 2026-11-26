---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The published equations (3.3) and (3.6) give the coefficients in the frozen statement, including right-end factor 2λ/(1+λ) under the homogeneous Neumann condition. At t_0=0 the diagonal coefficient is b_0=[1−λ+(M−m)Δt]/(1+λ), and b_n≥b_0 when the exponent is nonnegative. The left and right forward coefficients are nonnegative. If b_0,c≥0, induction through nodes and time steps preserves the closed cone, also at equality. If b_0<0, choose zero boundary and the first interior basis vector; if c<0, choose zero boundary and the second interior basis vector. The first output component isolates the respective offending coefficient, so no conclusion from a signed coefficient hidden by later sweep entries is required. Rearrangement gives exactly the two inequalities. Substituting the printed numerical values directly into the printed stencil gives λ=9, b_0=−79941/100000 and the time ceiling 100/89941. With the given nonconstant input h_1=25+exp(0.01)<27 and C_1^0=100,C_2^0=0, the upper bounds on the first interior output are −55.5735, −55.1685 and −54.7635 for the three velocities. The sign is independent of the nutrient/light exponent at t_0. Independent `python3 /workspace/checks/frozen_replay.py 5` passed exact sweeps of the cone generators on a 3×3 parameter grid that includes both equality boundaries, as well as the three exact witness bounds. The frozen claim is about the printed formula and direct numerical inputs, not the physical rescaling or what the authors' implementation and constant-25 initial condition do.

## originality

PASS

Neither entrywise positivity as a general method nor the pure diffusion Saulyev threshold is new. The supported distinct result is the sharp combined advection/reaction constraint for this printed one-way sweep with its boundary, and its explicit all-velocity negative witness on direct substitution of the article's mesh numbers. The source's discussion of stability is not an all-input cone-invariance claim. Inspected work on an alternating diffusion pair does not cover this time-dependent, advective mixed-boundary update.

## value

PASS

The general coefficient test alone is elementary. The useful result is the complete target-specific boundary with an explicit severe negative first-step value at each printed velocity under the article's own left boundary input. It separates universal numerical admissibility from stability and provides concrete guidance on when the printed update can guarantee meaningful nonnegative concentrations. The raw-numeric example exposes a reproducibility problem for any user who plugs the supplied grid numbers into the formula; it does not claim that the physically converted or plotted run is negative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
