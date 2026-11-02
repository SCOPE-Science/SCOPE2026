---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed exact geometric proof for every real SPD matrix κ≥1, every nonzero residual and 0≤epsilon<1 with a squared-norm sketch embedding on span{r,Ar}. In orthonormal basis u=Ar/||Ar||,v residual-perpendicular, the true ratio is d sqrt(1+(B21/B11)^2). The embedding eigenvalue constraint bounds the off-diagonal ratio by epsilon/sqrt(1-epsilon²), and the Gram with B11=1-epsilon² attains this. The SPD endpoint moment inequality bounds d by (κ-1)/(κ+1), and A=diag(1,κ), r=(sqrt(κ),1) attains it simultaneously. At κ=1 the residual vanishes. The iff epsilon≤2 sqrt(κ)/(κ+1) and strict-growth witness follow. Independently checked both κ=9 rational Gram witnesses and alpha values exactly, including threshold epsilon=3/5 ratio 1 and epsilon=4/5 ratio 4/3. Any stochastic samples are corroboration only, not proof of the universal quantifier.

## originality

PASS

Qualified best-of-knowledge originality: closest fully inspected primary sketched-GMRES result gives general angle/quasioptimal bounds but not the precise deterministic worst-case SPD first-step residual factor, simultaneous two-mode equality, or necessary-and-sufficient embedding-safety frontier. Classical Kantorovich angle and oblique-projection geometry are acknowledged ingredients. The inspected published Resultary findings concern different error metrics or algorithms. Inaccessible full text of the closest 2026 same-method article and possible older projector-angle reformulations remain genuine priority risks, not grounds by themselves for scientific rejection.

## value

PASS

For sketched GMRES, the sketched objective may decrease while the true Euclidean residual grows; the sharp admissible embedding distortion for guaranteed SPD first-step descent is a natural, operationally relevant unanswered mathematical boundary. This result gives an exact κ-dependent if-and-only-if certificate, distinguishes it from a weaker general quasioptimality estimate, and constructs exact simultaneous sharp two-dimensional equality/strict-growth witnesses. The calculation is not a standalone new geometric lemma—classical Kantorovich and perturbed-projection ingredients are credited—but their interaction yields a nontrivial complete safety frontier for a specific canonical algorithm. No claims about later iterations, finite precision, typical random sketches, nonsymmetric matrices, or solution error are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
