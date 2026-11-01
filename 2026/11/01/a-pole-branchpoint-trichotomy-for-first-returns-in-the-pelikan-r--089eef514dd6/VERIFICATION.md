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

Run `python verify.py` in the directory containing the standalone file. The program requires only the Python standard library. It reconstructs two different recurrences for the same return coefficients: an algebraic power series and a truncated, exact-fraction state evolution. The truncation is exact for the coefficients compared because a walk beginning beyond the time horizon cannot hit zero before that horizon.

Actual execution checked all first 26 coefficients for each of the rational switching parameters \(1/2\), \(3/5\), \(4/5\), \(9/10\), and \(1\). It checked the exact doubling-endpoint geometric law and the pole residue \(45/169\) with exponential factor \(13/20\) for \(p=9/10\). Representative coefficient-to-asymptotic ratios at indices 300 or 200 were checked separately at \(p=3/5,4/5,9/10,99/100\), with reported relative errors below \(0.019\), \(0.010\), \(10^{-8}\), and \(10^{-8}\), respectively.

The singularity analysis in the proof, not the finite program, establishes the assertions for all admissible parameters and all sufficiently large times. No computer check supplies an exhaustive literature search or independent mathematical audit.
