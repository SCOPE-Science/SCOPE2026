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

The exact proof is contained in `RESULT.md`; no independent validation is claimed. Run `python verify.py` with `mpmath` installed and compare with `verification_output.txt`.

The program checks the known integrated-range coefficient using Gaussian-order-statistic quadrature, exhaustively enumerates the distinct ordered-pair Gram configurations in dimension five using exact rational arithmetic, and checks numerical equivalence between the elementary primitive and a separately integrated positive correction. It also evaluates the derivative identity, monotonicity at selected sample points, endpoint values, and the sharp fractional-power onset. The recorded execution passed 406 finite assertions. Neither the finite enumeration of pair types nor these numerical tests replaces the analytic proof: the continuum inequality follows from the Gram geometry, and the exact CDF follows from an explicit cross-sectional integral.

Scientific limitations: the result ends at the first overlap threshold, and priority risk remains for an unavailable historical full text. No external review or certification was performed.
