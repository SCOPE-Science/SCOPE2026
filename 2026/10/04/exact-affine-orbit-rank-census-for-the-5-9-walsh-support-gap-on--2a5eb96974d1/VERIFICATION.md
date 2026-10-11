---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For fixed five-support S and seven-frequency zero set T, exact support (5,9) is feasible exactly when W[T,S] has nonzero kernel and neither a coordinate functional nor any outside Walsh row vanishes identically on that kernel; the row-space formulation is standard annihilator duality, and over C finitely many proper hyperplanes cannot cover a nonzero kernel. The bundled verifier constructs the affine group action and exhausts both five-support orbits and every seven-set T using exact rational row reduction after a sound modular full-rank filter. I independently replayed the census and reproduced orbit sizes 1680 and 2688, the 3248/160 deficient counts, the rank distributions, the 3184/64/160 obstruction split, and zero admissible cases.

## originality

PASS

The bare absence of a (5,9) support pair is not new: the Krahmer--Pfander--Rashkov primary paper presents the order-at-most-16 uncertainty diagrams as numerical evidence and includes the elementary abelian order-16 group. The surviving final claim is the exact affine-orbit/rank/obstruction census. Full primary-text inspection found the general rank criterion and the numerical diagram discussion, but not the two support orbits, exact deficient-rank counts, or the forced-coordinate versus forced-extra-zero split.

## value

PASS

This is a natural complete classification of the mechanism behind a historically numerical boundary point. It compresses a large singular-value census into two affine support types and exact row-space obstructions, providing reusable finite Walsh-matrix structure rather than a bare recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
