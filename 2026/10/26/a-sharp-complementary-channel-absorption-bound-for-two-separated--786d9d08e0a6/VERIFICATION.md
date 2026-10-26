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
# Reproduction

With Python 3, run `python3 verify_cpa.py` beside this file. It has no third-party dependencies. It reports 4,743 independent scalar/matrix test assertions, including randomly generated strengths and phases, both analytically predicted CPA branches, and the unique minimax configuration. The transfer-matrix computations and singular-value computations are independently implemented, but remain finite numerical diagnostics. The proof in `RESULT.md` supplies the analytic all-parameter quantifiers; no external certification or independent audit has been performed.

The delta sheets are modeled by derivative jumps and flux-normalized exterior amplitudes. The absorption fraction is defined for any normalized two-component complex incident vector. As a check on the modeling conventions, `verify_cpa.py` verifies reciprocity, matrix unimodularity, scattering contractivity and determinant relations across sampled parameters. No result is claimed for finite thickness, broadband excitation or zero-strength sheets.
