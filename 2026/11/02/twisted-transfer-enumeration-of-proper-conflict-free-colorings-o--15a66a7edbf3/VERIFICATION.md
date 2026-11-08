---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For 3 colors each column is a pair of distinct names. Properness and one uniquely occurring neighbor color force non-swapping transitions of one of two orientations, and a direction switch forces three equal neighbor colors; the surviving 3-cycle orbit cannot satisfy the Möbius row-swap closure, proving at least four colors. Explicit ABC-block 4-color words with three residue-class endings supply a witness for all m≥3. The 84 legal adjacent-column states and row-swap involution J give a_m=tr(JT^m), b_m=tr(T^m) and 42-dimensional even/odd blocks. Independently rebuilt the full exact integer characteristic polynomials of both 42×42 blocks and verified tr(JT^m) for m=3,…,8 gives 216,336,3600,17280,75600,426816; this is an exact finite matrix certificate combined with a transfer identity valid for all m, not an extrapolation. The anti-invariant spectrum {2,1×3,−1×2, roots of x²+x+2 each ×3} yields b−a=2^(m+1)+6+4(−1)^m+6L_m, positive m≥6 by root modulus √2 and checked m3,4,5 exceptions.

## originality

PASS

Published subcubic four-choosability yields a broad upper bound only. Caro et al prior general results and the related crown-graph proper-conflict-free record do not enumerate the row-swapped ladder family. The finite transfer and its exact spectral decomposition provide a specific new closed count subject to standard historical risks. The 2026 broad paper full text was not independently accessible, retained explicitly.

## value

PASS

A sharp natural family classification beyond the subcubic upper bound, with a complete rational enumerator of all named optimal colorings and a precise twist penalty. Transfer symmetry reveals an enumerative mechanism that does not follow from existence/list-coloring bounds; this is not an arbitrary small-slice computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
