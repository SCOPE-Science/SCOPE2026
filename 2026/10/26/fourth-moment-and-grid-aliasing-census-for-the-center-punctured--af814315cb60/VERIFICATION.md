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

With probability-normalized Haar or grid measure, expanding |P|^4 retains exactly ordered quadruples a,b,c,d whose vector a+b−c−d is zero, or zero modulo the grid order, with weight ε_a ε_b ε_c ε_d. This also gives the two contraction formulas by first grouping sums or differences. Independently enumerated all 8^4 quadruples, compressed their weights by the parity mask of the four indices, and evaluated the resulting integer sums on all 256 sign assignments for moduli 3,4,5 and on the integer lattice. All three histogram rows agree entry by entry (hence the minima, maxima and their counts). Values modulo 5 and on the integer lattice agree mask by mask. Analytically, two pair sums in [−2,2]^2 cannot collide modulo any n≥5 unless equal, proving all-orders stabilization for every mask. For the continuous moment I independently enumerated the entire group as the eight signed coordinate permutations, each combined with the eight sign/checkerboard modulations. Both types preserve |P|^4 averages (or permute the convolutions up to signs). The enumeration found 13 orbits, with exactly two minimum-88 orbits represented by `----+-+-` (8) and `----++-+` (16) in the frozen order. For n≥3 the eight characters are distinct, so the zero-displacement autocorrelation is 8 and the two quoted merit factors follow from 64/(M−64). The independent replay is `python3 /workspace/branches/review_replay.py 2`; the frozen checker was inspected, not executed.

## originality

PASS

The supported distinct objective is the complete binary moment distribution through the order-three/order-four aliasing transition, including all ordered multiplicities and the stabilized histogram. There is real same-support coverage of the aperiodic extrema, minimizing masks (hence their coarser square orbits), and no-aliasing for orders at least five in Resultary 225492f9c9fb; those facts are not independent contributions here. Its date label is later, but the coverage assessment does not depend on priority. The exact near-grid distributions and full moment census are not supplied by the inspected prior statements.

## value

PASS

The centrally deleted square is the symmetric one-erasure case of the natural 3×3 Fourier array. The invariant quantifies precisely how sampling changes the entire binary energy spectrum: order three lowers the attainable minimum, while order four has the same minimum as the stabilized problem but different optimizer multiplicities and intermediate energies. Hence the aliased census shows effects invisible from the known aperiodic extrema and serves as an exact benchmark for finite-grid versus continuous aperture calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
