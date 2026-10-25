---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Full six-state half-filled Ising generator at per-edge attempt rate one has three global-reversal pairs with exact stationary probabilities for each microstate a=(p+q)/(2D), b=q(p+q)/(2D), c=q/D, D=p(1+q)+3q+q². Independent symbolic construction of all original six microscopic transition rates verified each master equation and both hot/cold correlation formulas (not only aggregated chain). Hot/opposite correlation is 4a−1, other cold 4c−1, yielding exact strict sign boundary and feasibility q<sqrt2−1. Hot uphill net flux 2cp−2b=q(p−q)/D gives heat 4J times this and entropy rate q(p−q)log(p/q)/D. For p=1, derivative A'=(1−2q−5q²)/(1+4q+q²)^2, and strictly increasing right side of the stationary equation establishes unique maximum q≈0.13001877. All q>0 and T_h finite/infinite boundaries covered; no cold zero-temperature claim.

## originality

PASS

The bounded search found previous simulation and small-system work on two-temperature Kawasaki rings but did not locate the exact four-site one-hot-bond formulas, sign boundary, and current/entropy optimum. Full 2014 article was unavailable, so coverage risk is acknowledged.

## value

PASS

The smallest energy-sensitive conserved-spin cycle yields an exact finite-size local-order threshold distinct from positive entropy production; a useful model-motivated boundary rather than an arbitrary numerical special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
