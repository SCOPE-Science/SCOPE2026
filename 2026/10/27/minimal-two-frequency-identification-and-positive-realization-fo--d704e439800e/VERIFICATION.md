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

# Verification scope

Analytic identities in RESULT.md establish the universal claim without reliance on finite sampling. The direct rational witness is \(C=2\), \(C_D=6\), \(\lambda=1\), \(\gamma=3\), with frequencies \(1,2\), inverse phasors \((17+16i)/5\), \((65+80i)/17\), and impedance differences \(36/85,72/85\).

Run `python verify.py` with Python 3 standard library. The script independently evaluates the physical ODE transfer via elimination, reconstructs parameters and confirms 12,000 seeded positive parameter configurations whose test frequencies resolve the exchange scale. It also checks the exact rational example, replay at both frequencies, and a two-dimensional family of positive parameters giving identical single-frequency responses.

A separate exact computer algebra calculation checked that the two impedance differences have common positive denominator and ratio \(	au=C_D/\gamma\). The paper provides the same derivation directly; neither code nor finite tests certify all real parameter values. The calibration requires exact measured phase, forcing gain, and constant positive two-layer coefficients. Ill-conditioning is expected for weak coupling, nearly equal frequencies and adverse parameter scales; the randomized test purposely avoids such numerically singular regimes. Inaccessible complete historical appendices and possible general inverse rational results remain originality uncertainties. No independent assessment has been performed.
