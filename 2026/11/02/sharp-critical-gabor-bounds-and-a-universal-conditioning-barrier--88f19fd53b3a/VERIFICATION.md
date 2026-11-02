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

# Verification

The analytic derivation in `RESULT.md` proves the claim for every admissible positive compactly supported Borel measure. The reproducible standard-library script `checker.py` was executed successfully and reported 79024 supplementary checks: exact rational pair-kernel partial fractions and positivity, sampled monotonicity, explicit corner identities, direct complex Zak evaluations for several lattice widths, and random positive-mixture conditioning tests. The arithmetic test confirms \((3+2\sqrt2)^2=17+12\sqrt2\) up to floating-point precision; the closed-form equality is proved symbolically in the text.

The two-pole exact benchmark \(R_1=2,R_2=3\) gives \(B/A=36\), while the one-pole minimizer has \(B/A=17+12\sqrt2\). A further analytical normalization check gives
\[
\int_0^1\int_0^{2\pi}\Lambda(u,\theta)\,\frac{d\theta}{2\pi}\,du
=\|g_\nu\|_2^2=2\pi\iint\frac{d\nu(w)d\nu(v)}{w+v}.
\]

Finite assertions and sampled plots do not establish universal measure-valued inequalities, spectral extremizers, external priority, or independent certification. Those mathematical assertions rely on the explicit analytical proof.
