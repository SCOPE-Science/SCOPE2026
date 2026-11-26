---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under simultaneous affine transformation the induced cotangent densities pull back, so one can work on the inner cube. Projection onto each facet yields the asymmetric axial cross-polytope P_m(z); its orthant simplices give density 2^m/[m!∏(1−z_j²)] before the Holmes–Thompson factor. The substitution z_j=tanh(u_j) cancels that weight, yielding the formula for F_d and a uniform cube average of the difference-body ratio. At finite z all 2m vertices survive, ruling out the simplex equality case. Central symmetry would pair the axial vertices with a common midpoint: a midpoint with one nonzero coordinate is incompatible with the vertices on another axis; one with two is incompatible with both signs on either of those axes, and a pair cannot supply three nonzero coordinates. Thus the center must be zero, and the axial lengths agree only at z=0. Near each corner, coordinate reflections and diagonal rescaling give a nondegenerate simplex limit. Equivalently take U=aV with V fixed uniform on [−1,1]^m; tanh(U) approaches a corner almost surely, so the bounded local ratios converge in mean to β_m. For m=2 the sum of the absolute pairwise edge determinants gives the difference-body area, since the oriented edge segments sum to a zonotope with the polygon's width as support function. Dividing by the original area gives 1+max(|y|,|w|)/2. The maximum of the two absolute logarithmic coordinates has density 2u/a²; the resulting integral has positive derivative, and expanding 1−tanh u as 2/(1+e^(2u)) gives the π²/24 coefficient. The uploaded checker was inspected, not executed; the argument checks the decisive formula analytically.

## originality

PASS

The cotangent-ball identity and the general numerical comparison are already known. The distinction supported here is strict finite-radius comparison and saturation within the restricted homothetic parallelotope family, the exact Funk area, and the dimension-three integrated ratio and gap. A sharp local bound on each cotangent section does not determine this integrated saturation, because the weighted distribution of facet positions must also be analyzed.

## value

PASS

This gives a concrete sharpness family for a surface-area comparison inside the restrictive setting of two concentric, homothetic and centrally symmetric bodies, even though local symmetry of the ambient cube does not force equality at the lower endpoint. The exact radius dependence and gap in dimension three quantify the comparison rather than merely exhibiting a limiting local simplex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
