---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Dual to the equilateral free space is the oscillation norm N(f)=max_i f_i-min_i f_i on centered real m-vectors. Averaging any Hilbert comparison quadratic form over the coordinate-permutation group preserves distortion inequalities and makes Q(f)=c sum f_i^2 on the centered hyperplane globally optimal. On N(f)=1, min sum f_i^2=1/2 (two opposite half entries, remaining zero), while the maximum of centered sum squares is floor(m^2/4)/m by convexity of the centered quadratic on [0,1]^m and balancing binary vertices. Hence d_BM^2=max/min=2 floor(m^2/4)/m, and finite-dimensional duality transfers it back. m=2 yields 1; exact rational finite checks m=2..16 only corroborate the all-m proof.

## originality

PASS

Prior equilateral Lipschitz-free norm and unit-ball volume-product formulas do not directly imply the globally minimized Euclidean Banach–Mazur distance in all dimensions, including the parity formula. Published related zero-sum ell4 and deformed four-point findings concern different norms/metrics, not this full equilateral result. An older oscillation norm/type-A root-polytope ellipsoid theorem remains a risk.

## value

PASS

This is the exact optimal Hilbert distortion of the natural, dimension-unbounded class of equilateral finite metric Lipschitz-free spaces. The parity-sensitive value and proof of optimality over all ellipsoids make it a mathematical benchmark, rather than a computation of a chosen embedding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
