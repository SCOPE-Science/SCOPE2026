---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Piecewise-affine right branch satisfies F_R²(z)−E=−d(z−E); left branch maps all hits to y=0 section. For d>1, the only endless right orbit is E; the section return is R(u)=1−d+d²u on I=((d−1)/d²,1/d), fixed u*=1/(1+d), slope d²>1. Every other u exits after finitely many returns to attracting C; only saddle P and its countably many affine preimages avoid capture, a null set. For d<1 rectangle entry plus right-branch contraction proves unique attracting fixed E; at d=1 Q is finite-time absorbing, and F1² is central reflection. The nested return intervals of length d^(−2n−2) imply geometric law and mean d²/(d²−1). Examined verify.py exact rational boundary checks, independently checked affine algebra; global proof analytical.

## originality

PASS

No earlier mathematically implying result found in inspected material; search is not universal novelty proof. The prior frameworks motivate and partially subsume return algebra, but do not by themselves assert the single complete trace-free three-regime global classification or exact uniform-section geometric law. This is best-of-knowledge with residual overlap.

## value

PASS

A sharp complete global classification at an explicitly defined border-collision slice, including continuum of neutral periodic points, exact exceptional basin structure and nontrivial residence distribution, is mathematically motivated as an exact model of border-collision regime transition. It is more than a local normal-form restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
