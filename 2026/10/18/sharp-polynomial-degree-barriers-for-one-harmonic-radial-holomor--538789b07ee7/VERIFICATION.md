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
# Reproducibility and limits

The file `check_radial_inverse.py` requires Python 3 and SymPy and is run with `python3 check_radial_inverse.py` in the package directory. `check_output.txt` records the reference run. The exact suite checks the highest-harmonic support identity and amplitude bound across 6,558 nonzero integer-coefficient polynomial samples, 112 exact one-harmonic instances, 110 rational-power-weight extremizer identities, and 336 one-harmonic tests using four rational power weights. A separate numerical suite constructs 42 cases with a prescribed complex phase and an amplitude close to the sharp threshold.

The analytic argument, not enumeration, establishes every real exponent \(\beta>-1\), every integer harmonic \(k\ge1\), and every degree \(d\ge k\). The finite tests do not exhaust all polynomials, and no higher-precision test or timeout is presented as a proof. Source comparisons and their residual bibliographic risks are in `AUDIT.json` and `REVIEW.md`.
