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
# Reproduction and limits

The analytic derivation starts with the exact monomial norm \(\|z^n\|^2=\alpha^{-2n/m}\Gamma((2n+2)/m)/\Gamma(2/m)\); it then computes the backward-shift weight sequence, its gamma-ratio limit, and a second-order Schatten-small remainder for \(e^{bD}-I\). Ky Fan singular-value inequalities recover the sharp leading coefficient. At the critical exponent, compare the derivative with the unilateral backward shift modulo compacts, factor \(e^{bD}-\mu I\) holomorphically, and evaluate the Calkin matrix norm using the unitary shift symbol.

The packaged standalone `check_translation.py` ran successfully and reported 75 finite checks. Run with Python 3, NumPy and SciPy: `python check_translation.py`. The code verifies finite gamma asymptotics, shift and exponential identities, and resonance counts. It does not prove the spectral or asymptotic conclusions beyond finite size. No external or independent audit was undertaken.
