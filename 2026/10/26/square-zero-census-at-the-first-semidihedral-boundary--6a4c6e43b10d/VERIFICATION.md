---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

The complete binary finite enumeration is in `verify_binary.c`. Its construction of the group table follows the presentation, its square test uses every ordered pair of basis elements, and its rank computation uses standard pivot elimination over \(\mathbb F_2\). Three independent \(65,536\)-element sweeps are made, one per group, and the program exits unsuccessfully if any coefficient differs from the stated spectra.

The additional `verify_ring_lift.c` uses the different \(R\oplus Rb\) equations, with \(R=\mathbb F_q[a]/(a^8-1)\), to enumerate square-zero elements. It checks the binary distribution and the total numbers at \(q=4\). The generic all-\(q\) count is proved by valuation and coefficient equations, not by interpolation. Neither program classifies conjugacy orbits or higher-order nilpotents, and neither is an independent mathematical audit.

Commands: `cc -std=c99 -O2 verify_binary.c -o verify_binary && ./verify_binary`; `cc -std=c99 -O2 verify_ring_lift.c -o verify_ring_lift && ./verify_ring_lift 2 1 && ./verify_ring_lift 4 1`.
