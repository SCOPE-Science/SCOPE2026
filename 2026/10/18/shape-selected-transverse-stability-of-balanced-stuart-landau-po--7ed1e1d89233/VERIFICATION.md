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

In units of a, the Jacobian is a block diagonal operator −2P_j (P_j the radial rank-one orthogonal projector), plus common injection of K times the mean perturbation, K=[[x,−y],[y,x]]. Noncollinearity gives a rank-two phase-balance derivative and precisely M−2 tangential neutral directions. A rank-two determinant update gives characteristic polynomial [t(t+2)]^(M−2) det(t(t+2)I−[(t+1)I−S]K), where S=2 mean(P_j)−I has eigenvalues ±d. The trace in the determinant is 2x(t+1) and det([(t+1)I−S]K)=((t+1)^2−d²)(x²+y²). This reproduces all factors including exceptional t=0,−2 by polynomial identity. With the notation b_j of the proof, b_1 b_2−b_3=2(1−x)[y²+(2−x)(4−x)] and (b_1 b_2−b_3)b_3−b_1²b_4=4H. For x≥2 b_1 fails, and for 1≤x<2 the first determinant fails. For 0<x<1, b_1,b_4 and the first determinant are positive, so H>0 forces b_3>0 and then b_2>0, which completes strict Hurwitz equivalence. In u=y², H has positive leading coefficient, negative constant term and is strictly negative at u=x(2−x); its unique positive root decreases strictly with d². At equality the stated factorization gives a simple imaginary pair and a Hurwitz quadratic. At x=1/2, y=1 the exact threshold is d²=13/18, with an unstable square (H<0 and no imaginary or zero collective roots) and an attracting antipodal-pair polygon at φ=π/6 (d²=3/4), at the same coefficients. Independently replayed symbolic identities and 12 exact rational four-node Jacobian comparisons: python3 /workspace/replay/stuart_landau.py (SymPy). If Ω=0 the solution is an equilibrium, so the spectrum is interpreted as characteristic rates, not as multipliers of an orbit with an intrinsic period. For Ω≠0 the co-rotating transformation is periodic and the exponents give the claimed Floquet real parts. No nonlinear Hopf or single-orbit asymptotic-attraction claim is made.

## originality

PASS

Credit existing balanced polygons, sampled shape-dependent stability, and the second-moment collective-reduction precedent. The supported distinct result is the complete quartic and exact necessary-and-sufficient threshold for identical oscillators with positive dissipative and potentially nonzero reactive coupling, with an explicit fixed-coefficient four-agent contrast. The strongest indexed overlaps give exact pure-reactive or real-coupling results or small-positive-coupling persistence, not the full strict boundary. This is a bounded comparison, not priority certification.

## value

PASS

The scalar shape statistic converts a population-size Jacobian into an exact spectral law and explains when reactive coupling overcomes dissipative destabilization. The same-parameter attracting and unstable polygons are a concrete demonstration that shape is dynamical data, not just geometric labeling. This improves on numerical sampling without asserting anything about global basins or nonlinear dynamics at the threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
