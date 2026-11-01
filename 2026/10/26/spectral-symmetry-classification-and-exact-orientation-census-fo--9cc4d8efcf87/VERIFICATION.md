---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The proof fixes the hub and invokes a Schur complement with path polynomials P_m, giving det(xI-H)=(prod P_{ell-1})[x-sum (2P_{ell-2}+w)/P_{ell-1}]. Path parity makes the only non-odd rational terms sum_{odd s} W_s/P_{s-1}. These fractions have distinct leading powers x^{-(s-1)} at infinity; their constant-coefficient linear independence forces every W_s=0 separately. An odd-length cycle has gain weight w=1 or -2; hence W_s=k_s-3a_s. For each odd s the edgewise phase sum equals 2, yielding a=(2^s-2)/3, b=(2^{s+1}+2)/3 and the closed orientation product. Covers k>=1, repeated odd lengths, mixed lengths, and arbitrary even petals. Independent numerical direct Hermitian eigenspectrum enumeration of all 512 orientations of three triangles reproduced exactly 216 symmetric cases with spectral mirror error <=1.6e-15. Independent exact phase enumeration for lengths 3,5,7,9 and the three-pentagon formula 14520 agree. Finite checks corroborate; arbitrary-length sufficiency/necessity follows from the Schur complement and Laurent-order argument.

## originality

PASS

On examined primary results, general Hermitian gain-graph characteristic-polynomial coefficients and one-sum closure are established background, but neither states nor immediately gives the new necessary/sufficient odd-length-multiplicity split and complete labeled count. A specialized deduction of general recurrences is still possible; priority remains qualified. No earlier exact match was located in targeted corpus and web queries, but failed searching is not novelty proof.

## value

PASS

A one-vertex cactus bouquet is a natural first non-bipartite assembly family for sixth-root Hermitian spectral symmetry. The length-by-length cancellation theorem sharply characterizes existence, shows different odd lengths cannot compensate one another, and counts every labeled orientation. This is more than a routine single-triangle identity or a small enumeration: arbitrary cycle multiplicities and lengths are handled, with a natural graph-spectral reason to need the exact balance and counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
