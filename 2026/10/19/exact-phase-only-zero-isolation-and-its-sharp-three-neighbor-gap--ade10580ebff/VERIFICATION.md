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

The Vandermonde determinant makes the frequency differences bijective with the two-dimensional root grid. Equilateral cancellation gives exactly two orientations, which cannot be interchanged by p-th roots since p is coprime to 3; each frequency thus yields two distinct projective classes, with no overlap between frequencies. To check the gap, fix r and write the first two terms as 2 cos(pi/3+pi r/p) times a unit phase. Nearest angular matching of the third term gives the stated parity-dependent nearest-integer rule, and the reverse triangle inequality gives the row lower bound h(r). Between the zeros 0, p/3 and p of the continuous lower bound, only maxima can intervene, so outside the exceptional rows the indicated adjacent integers suffice. In particular the p=5 outside row r=q+2=3 does require a check: h(3)=D_-(2 epsilon), and the strict comparison at RESULT.md lines 64–68 applies also to p=5 (u=pi/15). Row r=0 is excluded except for the known zero by the chord bound. For p=3q+1 row r=q+1 has an exactly opposing third term and value D_-(epsilon); for p=3q+2 row r=q has an exactly opposing term and value D_+(epsilon). Cyclically permuting the three terms and dividing by the new first term yields (r,s)→(s−r,−r), which takes that exact-angle pair to the other two stated pairs. The nearest-angle rule excludes other s on these rows. This certifies strictness and exactly three minimizing frequencies with the raw-sum normalization. Independent high-precision cosine-grid enumeration at p=5,7,11,13,17 agreed with the squared gap and all equality pairs; this is finite numerical corroboration, not the all-prime proof.

## originality

PASS

The supported contribution is the exact conditional nonzero amplitude, its attainment set, and the full projective census on the parabolic grid. The three-point reduction and qualitative zero rigidity are closely tied to prior results and should not be presented as new methods.

## value

PASS

For the natural three-site phase-only cancellation problem, the nearest surviving Fourier amplitude determines the exact separation available for distinguishing an actual sample zero from all other samples of that same sum. The p mod 3 dependence, raw amplitude scale, and three sharp frequency differences are information a qualitative uncertainty bound cannot supply. No uniform noise-robustness result for arbitrary phases is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
