---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For d>=2 and covariogram level fraction θ=s^d, the Euclidean unit-ball normalized overlap at translation 2r is Θ_d(r)=I_(1−r²)((d+1)/2,1/2), strictly decreasing by its exact derivative. The normalized level-body volume radius r_d(s) is unique, while the simplex has Q_d(Δ,s)=c_d(1−s), c_d=0.5*binom(2d,d)^(1/d). Brunn–Minkowski concavity makes r_d concave with r_d(1)=0, hence r_d(s)/(1−s) nondecreasing; analyticity and nonaffineness imply strict increase. Its endpoint ratios 1 and dκ_d/(2κ_(d−1)) straddle c_d (for d2 explicitly and d>=3 via gamma recurrence), yielding exactly one nonendpoint crossing and strict sides. Lens containment gives Θ_d(r)<(1−r²)^(d/2), proving s_d>(c_d²−1)/(c_d²+1). Uniform beta-integral endpoint expansion and Stirling show s_d→3/5 and s_d=3/5−[7log(πd)+18log 3−27log 2]/(50d)+O((log d)²/d²); exponentiation yields θ_d∼[2^(9/10)/(π^(7/30)3^(3/5))](3/5)^d d^(−7/30). Independently checked symbolic derivatives f_s=−25/9,f_c=8/9 at (s,c)=(3/5,2) and numerically solved for d=2,3,5,10,40,100,500 (e.g. s2≈0.41078749,s10≈0.54491306,s100≈0.59163745), all strictly above σ_d and approaching 0.6. Numerical checks corroborate analytic all-d proof, not a global minimization theorem.

## originality

PASS

PASS for the exact two-family crossing and quantitative high-dimensional correction, not the known simplex/ball formulas. Martín Goñi arXiv:2610.37066 (2026-10-27) Section 4.2 compares a spherical upper envelope with simplex, giving a sufficient exclusion threshold σ_d, but not the exact unique beta root and d^(−7/30) crossover-volume law. The more general sharp simplex interval does not determine the exact comparison below it; classical Rogers–Shephard and convex-body convolution framework supply premises, not the new phase boundary.

## value

PASS

An exact, all-dimensional two-family phase boundary converts a weaker published spherical-envelope obstruction into a sharp threshold for when ellipsoids outperform simplices. The unique crossing and d^(−7/30) correction are precise, reusable invariants in an active convolution-body extremal problem; neither establishes a global minimizer nor merely repeats a known endpoint inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
