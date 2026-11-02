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
# Reproducibility and analytical verification

The program `verify.py` uses only the Python standard library. Run `python3 verify.py` from the directory containing this file. It performs 60 tracked exact rational cases (40 reduced-generator mixed-tilt identities, eight zero-coupling identities, nine independently built full two-lane position-generator mixed-tilt identities, and three large-ring rational estimates).

For the physical \(N^2\)-state generator, independent entry and exit rates are constructed directly from the occupation-based jump rule. The mixed derivative of the leading eigenvalue of the two-field tilted generator is evaluated using finite linear Poisson equations with exact fractions; the same algorithm is independently applied on the reduced relative chain. Stationarity is checked by exact row and column balances. The numerical evidence agrees with the closed formula for the tested systems and rational rates.

The general proof is analytical: reversibility of the relative displacement, the explicit discrete Poisson solution for total-count intensity, effective conductance for signed count, an arithmetic–harmonic mean inequality, and a fixed-time coupling with independent Poisson walkers. The finite-state checks are not a proof of all ring sizes or continuous parameters. No proof assistant or external independent certification was used. Independent audit status remains not performed.
