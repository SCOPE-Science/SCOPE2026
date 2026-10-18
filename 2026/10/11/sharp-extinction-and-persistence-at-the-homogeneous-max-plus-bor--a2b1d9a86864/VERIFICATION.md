---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For x>0 the first coordinates satisfy x_{n+2}=T x_{n+1}-D x_n until first nonpositive x_k; the map then gives exactly two further steps to zero (including x_k=0). In the oscillatory region the roots sqrt(D)e^{±iθ} generate a sine sequence; every positive run exits by ceil(pi/θ) and an explicit initial phase realizes the last possible exit, yielding sharp uniform nilpotency. Repeated-root and distinct-positive-root solutions have monotonic affine or exponential brackets and yield exactly the claimed persistence cone and ceiling formulas. All initial points with x<=0 are handled by the reset branch. Independently checked exact rational iteration over representative grids, critical and overdamped thresholds and sharp witnesses; this does not prove the all-real-parameter statement.

## originality

PASS

Ohmori–Yamazaki 2024 full primary treatment introduces the positive/negative branch matrices and marks B=0 as border-collision boundary, but analyzes nonzero-forcing dynamics and gives no global zero-input sharp nilpotence/persistence classification. The earlier T=0 four-step reset is known and acknowledged. Simpson 2024 studies a containing degenerate border-collision normal form but describes the forcing-zero parameter slice as outside its principal analysis; the full revised journal version was not separately compared. Published Resultary nearby fixed-initial-state reset oscillator concerns different forcing and thresholds, not an implication covering these exact all-initial extinction laws. Best-of-knowledge PASS with general border-collision alias/journal-version risk.

## value

PASS

Zero input is the natural border-collision parameter for this max-plus dynamical system. An all-states sharp finite-time nilpotency cutoff, persistent cone, and critical algebraic versus overdamped logarithmic extinction delays provide a complete dynamical phase classification, not merely elementary eigenvalue labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
