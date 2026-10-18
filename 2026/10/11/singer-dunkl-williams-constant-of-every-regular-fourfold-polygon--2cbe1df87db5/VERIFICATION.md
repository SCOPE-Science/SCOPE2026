---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For all n≥1, the inradius-one regular 4n-gon has R(θ)=sec d(θ) with normals at multiples of 2α (α=π/(4n)). Its quarter-turn symmetry and Fu–Xie–Li Lemma 2.9 characterize every unit isosceles partner as ±90° rotation. Consequently the full minimization D(X)=inf||x+λy|| equals inf cos d(θ+δ)/[cos d(θ)cos δ], δ=arctan λ. The RESULT.md trigonometric case split m=0, ±1, |m|≥2 supplies lower bound 2cosα/(1+cosα), attained at θ=δ=α/2. Fu–Xie–Li Proposition 2.1 establishes D·DW_S=2, giving DW_S=1+secα. I independently tested all angular regions for N=4,8,12,16,20,28,40,64 and their sharp equality witness; the analytic proof controls all n and continuum of θ,δ.

## originality

PASS

Fu–Xie–Li 2023 introduces the invariant and proves the conversion identity and general upper bound, and already explicitly notes that l∞² (a square) attains 1+√2. Therefore the n=1 endpoint is PRIOR COVERED, not separately original. The all-n 4n-gon exact secant interpolation (particularly n≥2) survives; the primary full text examines l_p and affine-hexagon examples but does not supply the regular 4n-gon sequence. Related polygonal James/von-Neumann–Jordan constants are different invariants.

## value

PASS

This computes a natural metric geometry invariant for an entire classical family of regular symmetric Minkowski planes, interpolating from the known square endpoint to Hilbert-plane limit with an explicit strict rate. The mathematical content is the full angular optimization, not the already known n=1 special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
