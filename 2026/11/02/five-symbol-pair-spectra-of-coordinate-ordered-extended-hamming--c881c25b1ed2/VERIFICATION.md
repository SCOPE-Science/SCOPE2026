---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For all eight affine points, the 16 affine Boolean maps form the [8,4,4] code; nontrivial weight-four supports are exactly 14 zero-XOR affine planes. Four-point cyclic support has pair weight 4 plus its number of runs. Four complementary windows and alternating parity planes give coefficients A5=2T and A8=2Z. Each coordinate edge belongs to three plane supports (24 incidences); the remaining A6 and A7 follow from two linear equations. AGL(3,2) has 1344 automorphisms, hence 8!/1344=30 labeled codes. The event calculation and conditional parity-direction matching yield the joint counts. Independently reconstructed every normalized affine order (5040), distinct codebooks, pair weight spectrum and T,Z table: all formulas match; the proof supplies completeness, not only finite spot checks.

## originality

PASS

Classical pair-channel definitions, Singleton bound, ten? existence of pair-MDS [8,4] and thirty labeled Fano planes are prior work. The remaining claim is all cyclic coordinate presentations classified by their five complete symbol-pair enumerators and parity/interleaving statistics. Saniga full public manuscript catalogs the thirty labeled Fano planes by defective arithmetic lines, with eight such types, not the cyclic symbol-pair enumerators or joint distribution. Nearby Resultary binary cyclic Hamming pair-generation results concern other codes/invariants. Residual risk is that Fano tables or earlier coding tables implicitly encode these five spectra.

## value

PASS

The coordinate order is inherent in symbol-pair reading but invisible to ordinary Hamming weight. The classification quantifies exactly which coordinate presentations attain the optimal pair distance, providing a natural complete invariant for a canonical eight-coordinate code; it goes beyond reproducing a known isolated optimal example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
