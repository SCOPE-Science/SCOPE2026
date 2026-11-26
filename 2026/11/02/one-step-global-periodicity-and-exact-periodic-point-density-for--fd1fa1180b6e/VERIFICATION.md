---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For w=Rz and e=Uz−w in the open half-unit square S, v=Ue lies in the diamond D=US. Its fractional rounding residual r=v−N(v) remains in D: if a coordinate has magnitude above 1/2, it is the only such coordinate and subtracting its signed unit strictly decreases the Manhattan norm. Neither v=Qz−Uw nor any attainable rotation coordinate has half-integer ties. Writing q=N(v) gives Rw=Qz−q and U(Rw)=Qw+Ur with Ur in S, so R²w=Qw. The image is invariant, hence R⁴w=−w and R⁸w=w, ruling out all proper period divisors at nonzero w. Periodic points have predecessors, and (2,0) has none: its inverse-rotated center has Manhattan distance 2(√2−1)>1/√2 from the nearest lattice point. In the preimage diamond, all distinct lattice pairs are unit-coordinate neighbors, so three points would give a triangle, impossible. The four equal overlaps contribute half their summed areas to double coverage; the diamond's area is one, so the uncovered and doubly covered areas agree. Weyl averaging over a rectangular box is a product of two geometric averages, with at least one irrational coefficient per nonzero frequency. Polygonal boundaries are null. This proves the densities, with periodic density equal to image density.

## originality

PASS

The supported distinct result is the global nearest-rounding orbit identity and classification, hence the identification of periodic density with image density. The multiplicity constants are a resonant validation of a known general statistical form, and the first-image density already follows from prior frequency machinery. No separate originality is assigned to the numerical constants or generic cell-area method.

## value

PASS

For an established discretized rotation, the global identity resolves all transients and exact least periods, despite noninvertibility on the full lattice. It lets one transfer prior one-step frequency information into a dynamical density of genuinely periodic points, not merely image points. The substantive value is the classification, not evaluating a known statistical expression at a special angle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
