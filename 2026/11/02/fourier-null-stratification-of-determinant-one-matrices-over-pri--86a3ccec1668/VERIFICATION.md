---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Each SL2(Fp) residue A has p³ determinant-one lifts forming the affine hyperplane with normal (adj A)^T. Character orthogonality kills the entire fiber unless barM is proportional to this normal. Primitive rank-one barM and nonsquare det barM thus vanish; primitive invertible square determinant gives two lifts of A indexed t=±sqrt(det barM), contributing two p²-th roots which cannot cancel for odd p. Imprimitive M=pN reduces to finite-field SL2 character sums: rank0 nonzero, rank1 -p, rank2 p times a Kloosterman sum of p-1 pth roots. The latter cannot vanish because zero integer-coefficient sum of primitive pth roots requires total coefficient count divisible by p. Half of invertible reductions have square determinant; p⁴ lifts per reduction yield rank. Independently counted all 648 determinant-one matrices at p3 and all 6561 frequencies with exact cyclotomic coefficient divisibility: rank 2025, nullity 4536.

## originality

PASS

General finite-field and scalar-trace prime-power Gauss-sum formulas are acknowledged and their precise scope compared; the arbitrary matrix frequency support and additive convolution rank over p² are not directly given. Qualified best-of-knowledge original, with possible implicit Kloosterman reduction.

## value

PASS

An exact spectral/kernel classification for convolution on a canonical finite additive matrix ring. The square-class phase transition, explicit dimension and limiting rank fraction 1/2 are natural invariants not reducible to simply counting SL2 elements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
