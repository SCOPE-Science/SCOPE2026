---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

In R=Z[a]/(a^2+a+2), the 21 explicit coefficient rows in the assigned verify_klein_reduction.py give 49 projective cross-product classes (21 fourfold, 28 triple) by exact arithmetic. The 1330 triple determinants have norm histogram {0:112,1:169,2:228,4:271,8:320,16:156,32:70,64:4}, so nonzero determinants are units at all odd residue primes. At a mod 2=0: line multiplicities 1^3 6^3; at a mod2=1: 1^3 2^3 12^1. Independent uniformizer-normalized cross-products give point-section profiles at p0: axes (1,4), pair points (2,0), diagonal (12,16); at p1: axes (1,0), pair points (6,8), diagonal (0,4). Char2 reduced supports have respectively 4 triple+3 node, or 7 triple, with Tjurina 19 vs28 and arithmetic genera 10 vs15. Exact independent enumeration and the norm-unit argument cover every claimed residue characteristic, not just sampled primes. No claim is made about the Hilbert-scheme limit of union of 49 sections or nonreduced-fibre singular schemes.

## originality

PASS

Best-of-knowledge PASS for the specified marked Klein integral model's two distinct characteristic-two Cartier residual fibers plus the complete 49-section collision classification and odd-prime incidence persistence. All 21 lines, 49 generic points and their complex incidence are antecedents. Historical arithmetic-degeneration calculations, possibly unpublished, remain a material priority risk.

## value

PASS

The Klein 21-line/49-point configuration is a canonical highly symmetric geometric arrangement. Arithmetic degeneration at the two conjugate primes over two is natural because its coefficients live in Q(sqrt(-7)), and the full 49-section collision profile distinguishes two ostensibly similar F2 reductions. The determinant-norm proof closes all other residue characteristics for the incidence lattice, making this a self-contained substantial exact classification; the specific integral model is explicit and motivated, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
