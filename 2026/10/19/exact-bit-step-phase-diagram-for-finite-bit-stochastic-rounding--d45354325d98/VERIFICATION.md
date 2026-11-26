---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The original counts and adjacent-pair formulas are correct for the specified b=2^r, exact affine proposal and single truncating rounding. For nonpositive j, the absorbing inequality is strictly T(j)<j+1/b; at equality the up move has probability 1/b. The absorbing interval is [a,0] with a=1−N when N>0. The repaired theorem checks all starts: monotonicity of T forces T(j)<T(a)<a+1/b below a, so rounding cannot overshoot a even for multigrid moves. Above 0 no move can jump below 0. Outside the interval, monotonic moves on a finite start-dependent set and positive exit probabilities give eventual absorption at the clipped initial state. For N=0 the analogous argument gives entry into the closed pair; its nonunit eigenvalue 1−u−d has modulus <1, and bounded convergence gives global uniqueness and the stationary simplex in the respective regimes. The exact-rational checker and its recorded PASS 6089 were inspected, not rerun; finite tests of ingredients do not certify the strengthened all-start result.

## originality

PASS

The frozen adjacent-pair law is expressly covered by a distinct indexed record under K=b, including the integer-resonance law as a corollary; the catalog dates do not establish priority. The repaired result credits this overlap and adds the global deterministic absorption location and complete stationary-law classification. The two-state theorem cannot classify starts below zero, and the checked primary-source kernel and error results do not provide the finite-state no-overshoot and arbitrary-start conclusion.

## value

PASS

A complete phase diagram for this elementary low-bit model distinguishes a single limiting law from an initial-state-dependent family of nonoptimal traps. The clipping calculation identifies the exact outcome of any initialization, not just the number of absorbing states, and determines the entire space of stationary measures. This is useful when comparing updates with identical adjacent-cell behavior but very different global trapping, without claiming general hardware or SGD convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
