---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Analytical and computational verification

The statement is proved analytically in `RESULT.md`: the minimum feasible adjacent-side chord, reflection symmetry, exact quadrature and edge expansion are all derived there. The numerical checks below are not part of the proof and do not establish an external audit.

Run `python rectangle_chord_profile_check.py` with NumPy and SciPy. This checks 10 aspect ratios by two independent calculations of the exact area, compares the formula with 120,000 uniform random points for each aspect ratio, and compares the four-corner inclusion inequalities against numerical shortest full chords in 87 noncritical random configurations sampled at 16,384 angular directions. All checks passed. The computed square fraction is approximately \(0.164357556864\), and the offset constant is approximately \(1.006869844116\). The sampled transition ratios approach the analytically proved coefficient \(4/(15\sqrt3)\).

Limits: finite angular grids only approximate pointwise minimizers, random sampling estimates only sampled probabilities, and numerical checks cannot prove the infinite-domain theorem or its originality. The independent audit has not been performed.
