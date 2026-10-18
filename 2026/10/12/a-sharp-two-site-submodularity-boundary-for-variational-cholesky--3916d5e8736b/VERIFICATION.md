---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The reviewed RESULT.md at Git blob 4ba21ff33d3bd749c0790f77fb663867019a7997 defines the exact noise-one Titsias VFE gain for two Nyström subsets. Rank-one determinants are 2+r² and the full determinant 4-r²; Sherman–Morrison applied to y=a(1,-1) yields D=B(r)-C(r)a², B=r²-log(2+r²)+(1/2)log(4-r²), C=3r(1-r)/((2+r²)(2-r)). For 0<r<1, B>0 by f(0)=0 and f’(t)=1-1/(2+t)-1/(2(4-t))>1/3, and C>0; the iff threshold follows. Independent symbolic substitution gives D(1/2,1)=1/36+(1/2)log(20/27)≈-0.12227451845. Taylor expansion yields -3a²r/4+O_a(r²) for any fixed a>0 as r↓0, and the ordered large-a, r↑1 weak-submodularity ratio tends to zero. Positive-semidefinite directional derivative proves monotonicity, which is not submodularity. The inspected verify.py checks 2170 rational-kernel configurations with floating logarithms; this finite check corroborates, not proves, the continuum theorem.

## originality

PASS

The precise data-amplitude dependent two-site phase boundary and vanishing uniform weak-submodularity ratio go beyond the prior VFE gain, monotonicity, and general qualitative non-submodularity already in the literature. The 2026 Jakkala–Akella article actually DOES report the SGP/SVGP bound is not generally submodular (Appendix, around Equation 28); this is acknowledged as important prior coverage, not described as new here. Its zero-label sensor-placement setup and empirical/general argument do not give this nonzero-antipodal-observation two-site if-and-only-if inequality or ordered ratio. The relevant Schaub–Zaspel full preprint establishes exact rank-one ΔVFE and monotonicity but not the subsetwise boundary. Priority is best-of-knowledge, not guaranteed.

## value

PASS

The exact phase boundary separates marginal complementarity and diminishing returns for a live data-aware kernel objective; this is a motivated sharp small-dimensional obstruction, not an arbitrary parameter sample. Its weak-correlation failure rules out intuition from almost-orthogonal kernels, and its zero uniform ratio limits use of weak-submodularity guarantees. Earlier qualitative failure is credited; the original value is the quantified complete frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
