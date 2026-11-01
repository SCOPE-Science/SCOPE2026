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

# Verification of the sharp quadratic Hankel testing constant

The analytically established statement concerns every nonzero complex quadratic pair, not a sampled subset. The full \(2\times2\) Hankel matrix, normalized kernel profile, norm-one parametrization, and two-regime global lower certificate are derived in `RESULT.md`. Sharpness follows from the independent exact identity
\[
\frac{25}{27}-F(\sqrt{2/3},r)
=\frac{(\sqrt6\,r-1)^2(6r^2+4\sqrt6\,r+8)}{54}.
\]
This identity holds at all nonnegative radii and makes the equality case explicit.

The companion script `verify.py` uses only Python's standard library and can be run with `python3 verify.py`. It checks the quartic identity in exact rational coefficient arithmetic, evaluates both global lower-test profiles over a finite grid, compares numerical kernel maximization against the sharp bound, samples arbitrary complex coefficient phases, and checks phase-rotated equality cases. Its output reports the actual finite assertion count. The script is **not** used to establish the proof's universal quantifiers.

The motivating 2026 paper's quadratic example and its later qualitative equality classification are credited as prior knowledge. The claim here is specifically the globally sharp quadratic testing multiplier and its complete equality modulus ratio. No independent audit or priority certification has been performed.
