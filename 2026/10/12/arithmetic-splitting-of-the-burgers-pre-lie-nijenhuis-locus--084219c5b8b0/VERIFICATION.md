---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For the two-dimensional Burgers pre-Lie product e₁e₁=2e₁,e₁e₂=e₂,e₂e₁=0,e₂e₂=e₁, independent symbolic expansion of the four ordered basis-pair Nijenhuis torsions yields C(B+C)=0, C(A−D)=0, (A−D)²+B(B+C)=0. Solving by C≠0 or C=0 gives rotation plane R and Q: C=0,(A−D)²+B²=0. Split -1 produces 3 planes sharing scalar line; nonsplit K-rational Q contributes only scalar matrices, hence R(K). For q odd split: N=3q²−2q, rank (1,6(q−1),(q−1)(3q−5)); nonsplit: N=q², ranks (1,0,q²−1). Aut two elements; Burnside with q scalar fixed points yields orbit counts q(3q−1)/2 or q(q+1)/2. Extension-field parity yields zeta (1−qT)²/(1−q²T)³ split or (1−q²T²)/((1−q²T)(1−q⁴T²)) nonsplit. Independently checked torsion exactly in SymPy; reviewed finite-field exhaustive source checker, not used for infinite proof.

## originality

PASS

Best-of-knowledge PASS only for arithmetic descent, finite-field rank/orbit and zeta package, NOT the 2D complex classification. Wang–Bai–Liu–Sheng pre-Lie paper treats Burgers under skew-adjoint assumption and scalar polynomial closure; Zou–Gao–Kang–Lü completely classify 2D complex Nijenhuis operators including the split case. These do not yield the finite-field square-class-dependent K-points/rank/zeta formulas without explicit arithmetic descent. Resultary search showed no direct equivalent in available hits.

## value

PASS

PASS: an exact arithmetic splitting phenomenon with different odd finite-field point counts, ranks, automorphism conjugacy classes, and zeta functions is a natural complete invariant package for the recognized 2D Burgers pre-Lie algebra. It is not claiming a new split complex list or an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
