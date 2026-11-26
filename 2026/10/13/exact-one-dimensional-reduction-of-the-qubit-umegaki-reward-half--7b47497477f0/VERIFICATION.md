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

Faithfulness makes every singular competitor have infinite divergence; the diagonal state at reward τ is finite. For a feasible faithful competitor above τ, mixing toward ρ until reward equals τ strictly lowers D by convexity and D(ρ||σ)>0. On the boundary, spectral calculus gives log σ=(1/2)log[(1−q²)/4]·I+(artanh q/q)s·σ_Pauli. At a nonzero transverse radius, p>0 makes the azimuth aligned with the arm uniquely optimal; at radius zero the azimuth does not distinguish states. Substituting the aligned vector gives the claimed D and differentiation gives D′. Along this affine line the second derivative is 2∫Tr(ρ BHBHB)du>0, with B=(σ+uI)⁻¹ and H=σ_x/2, by the integral representation of −log and ρ>0. At zero radius D′(0)=−p·artanh(|z|)/|z|<0, continued to −p at z=0. At the positive pure-state endpoint the positive (1−q²)⁻¹ term dominates the logarithmic term, since the arm Bloch norm is strictly less than one. Hence there is exactly one interior root and global minimizer. Independent 60-digit bisection gave x*=0.2559243261276990811, D_inf=1.1173300547617507845, K_inf=0.8303656034108254540 and 1−K_inf/D_inf=0.2568305131755495459, agreeing with the published rounding in the frozen result. Ng's running parameters and converse were checked against the primary text. The bundled artifacts/verify.py was inspected, not executed; the reproduction supplements the proof. The percentage bounds a potential coefficient reduction, not an attainable operational improvement.

## originality

PASS

Pass for the faithful-qubit analytic boundary reduction, explicit scalar objective and unique minimizing-root characterization for the range of projector thresholds, not for the Umegaki converse, the example, or the already tabulated numerical divergence and approximate percentage.

## value

PASS

The infimum is an independently motivated converse constant, not an arbitrary qubit statistic. The scalar equation and uniqueness yield a reproducible analytic evaluation in the entire faithful projector-reward regime without general matrix optimization. That is useful independently of the known example and does not resolve adaptive or collective attainability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
