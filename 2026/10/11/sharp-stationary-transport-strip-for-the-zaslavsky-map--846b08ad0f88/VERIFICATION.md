---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For q=e^(-r) in (0,1), η=(1-q)/r and κ=νη/q, direct substitution y_{n+1}=q(y_n+εcos 2πx_n) into the canonical lifted x increment gives Δ_n=ν+κ y_{n+1}. Telescoping yields X_N-X_0-Nν=κΣ_{j=1}^N y_j. For any compact invariant support K, max_K |y|≤q(max_K |y|+ε), hence |y|≤qε/(1-q); invariance gives E y=qε E cos/(1-q) and drift ρ=ν+(νε/r)E cos, |ρ-ν|≤νε/r. Endpoint means E cos=±1, forcing x=0 or 1/2 a.e.; the strictly contracting affine fiber has only stationary y=±qε/(1-q). Rotation of those fibers is invariant iff ν±νε/r is integer, proving necessity, sufficiency, uniqueness of endpoint measure and strictness for all other invariant probabilities. Equality in distribution follows from pushforward invariance of y; finite-N variance identity is an algebraic consequence, not a CLT. No claim of realized interior drifts or finite diffusion coefficient. Independent algebra substitutions were checked without relying on VERIFY_OK.

## originality

PASS

Compared the exact final theorem and quantifiers against all materially relevant inspected same-object and related published statements. Actual source readings and residual priority risks below; no negative search is treated as novelty proof.

## value

PASS

The drift of unfolded phases in the classical dissipative kicked-rotor map is a natural transport observable. Exact stationary transport-law calibration, a parameter-uniform sharp drift interval, and arithmetic rigidity of BOTH extremal drift measures give an independently usable boundary classification beyond merely renaming variables; the result is modest and does not solve anomalous diffusion or interior rotation sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
