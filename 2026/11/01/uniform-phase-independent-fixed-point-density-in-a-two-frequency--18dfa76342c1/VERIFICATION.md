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
# Reproducibility and verification

Run `python3 check.py` from this directory, with no third-party dependencies. The script evaluates the exact coefficient's torus integral by two quadratures of resolutions 256 and 512 per axis, checks the strict coefficient inequalities, and counts sign changes of the scalar fixed-point residual for amplitudes 160, 320, 640, 1280 and phases 0, 0.37, 2 at frequencies \((1,\sqrt2)\).

The reported 512-grid coefficient is approximately \(1.016927688461\). Twelve finite sign-change samples have normalized counts within 0.085 of this value, and two independent quadrature resolutions agree to better than 0.0002. The sign-change discretization can miss closely spaced or tangential roots, so these computations are not a certificate for a complete finite census. The theorem itself is proved in `RESULT.md` by a uniform local root-multiplicity lemma, torus equidistribution, and an explicit bound for exceptional cells. No independent external proof audit was performed.
