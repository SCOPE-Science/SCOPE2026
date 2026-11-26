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

Reconstructed RESULT.md lines 20–81. Unit-edge increments identify the anchored Lipschitz ball with the cube intersected by |Σx_i|≤t; the closing edge is essential since t<m. Duality preserves the real Hilbert distance. Averaging the two homogeneous norm-square inequalities over coordinate permutations preserves the distortion bounds, so optimizing the quadratic with eigenvalues 1 on the zero-sum subspace and r>0 on the constant direction is unrestricted. Odd m and 1<t≤2 leave exactly two feasible exterior vertex shells: cube sign vectors with sum ±1, or strip-edge vertices with fixed sign sum ±2 and free coordinate ±(t−2). This includes t=2. Evaluating q_r gives the two stated affine outer terms. The inverse quadratic gives the two exact facet-support squares (m−1+1/r)/m and m/(t²r); multiplying their maximum by the outer maximum gives the squared distortion. The exterior switch r_F exceeds r_G (the support-square switch), and r_F≥1+m/3≥√(m+1). In fact the first outer term alone times the support maximum is a global lower bound, strictly decreasing to r_G and then minimized at max(r_G,√(m+1)); at this minimizer the first outer term is still active. This proves the claimed global optimum without a symmetry restriction or any assumption about later contacts. The crossing r_G=√(m+1) occurs exactly at T_m, giving both formulas, which agree there. Differentiation shows strict decrease in the first region before T_m; the limit of the square as t↓1 is m. T_m>1 follows from √(m+1)<m+1. Since m²−4>0, squaring the T_m≤2 criterion gives the stated cubic; it is negative at each odd m=5 through 15 and positive for m≥17 (then m²(m−16)+8m+16>0). Thus equality T_m=2 does not occur in scope and every asserted plateau is nontrivial. The frozen checker was inspected, not executed here; the listed PASS lines are expected and the finite tests are not used in the proof.

## originality

PASS

The quotient and dual clipped-cube model are known, as are the unrestricted formulas for the four-cycle and for an exceptional edge no longer than one. The inspected statements do not cover the exact long-edge Hilbert optimum for odd m≥5, its two branches, or the order-sixteen plateau cutoff. This is a best-of-knowledge statement about the new parameter regime, not priority for the graph model or the general ellipsoid method.

## value

PASS

The optimum concerns unrestricted real linear maps on a natural weighted cycle space, not just a proposed ellipsoid or near-optimal bound. It gives a sharp change from strictly improving distortion to constant distortion, and pinpoints the last even cycle order where the plateau occurs. That all-dimensional cutoff distinguishes the effect from the already known four-cycle plateau and is useful for understanding which active facets govern Euclidean conditioning as the exceptional length varies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
