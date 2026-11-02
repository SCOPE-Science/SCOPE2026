---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Read entire RESULT.md and verify.py. For synchronous three-site binary majority, every zero edge x_i=x_(i+1) persists, making fixed equal adjacent boundary pairs. In each maximal intervening alternating strip of d consecutive unequal edges, the unresolved interior erodes from both ends, last change at floor(d/2); all-one edge word is possible only on an even ring and is an already-periodic 2-cycle. Hence tau_n=floor(D/2), max floor((n-1)/2), and exactly 2n maximizers by parity and cyclic position. The 2L-state directed transfer matrix (j,p), j<L=2t+2, tracks forbidden runs and total edge parity; its closed-walk trace counts 2 spin lifts per permitted even-parity edge word. Add 2 checkerboards for n even. For rare run beginnings 0 1^L, windows of length L+1 have probability 2^(-L-1) (global parity is irrelevant for strict subsets), overlapping starts are incompatible and fixed-order separated starts independent, proving Poisson factorial moments for n*2^(-2t-3)->lambda. Geometric upper/lower tails bound E tau=(log2 n)/2+O(1). Independent newly executed checker exhaustively simulated 8184 states n=3..12, 55 exact transfer traces, sharp maxima, orbit periods; all passed. No numerical sample proves limit; that follows from moments.

## originality

PASS

Qualified PASS for ring-specific exact tau formula, all-n transfer census and lattice-correct critical Poisson law. Classical Rule232 density-classification work and period-two results supply context, not this triple. Standard runs and Poisson approximation are not separately original; priority risk is earlier cyclic transient enumeration under different terms.

## value

PASS

A complete all-n time-to-attractor distribution and its logarithmic typical-vs-linear-worst-case separation answers a natural dynamics question for the classical majority Rule 232 under cyclic boundary conditions. Precise parity corrected counts and lattice-subsequence Poisson critical scale are nontrivial, not just general finite period-two folklore.

The dated certificate retains the supplied scientific assessment, sources and limitations.
