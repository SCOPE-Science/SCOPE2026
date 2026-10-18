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
# Reproduction and limitations

Run `python3 verify_gap.py` with Python 3. The script uses only the standard library and on successful completion prints `PASS: 10064 numerical checks ...`.

The tests compare exact Fourier-pair energy differences with the claimed closed formulas on \(3\le n\le69\) at deterministic random and boundary fluxes. They check global maximality and strictness at sampled points, test the Hamiltonian matrix against independent Fourier-mode residuals, evaluate finite-time Cesàro integrals by the analytical sinc kernel on \(3\le n\le34\), verify probability normalization and the displayed universal upper bound, and compare large-size coefficients at four ring lengths.

These numerical assertions cannot exhaust all integers, all fluxes or all times and are not presented as an independent audit. The all-size proof is by sorted folded angles, cosine difference identities, one-variable monotonicity, and Fourier time averaging. A best possible spectral denominator is not equivalent to an optimal actual mixing time. External bibliographic verification of equivalent historical optimizations is incomplete.
