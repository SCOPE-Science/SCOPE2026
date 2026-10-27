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

The stationary function for the intermediate variable \(y\) is \(G_r(y)=f'(y/r)+rf'(y)\), and the exact derivative is \(f'(z)=f(z)[2/z-\tanh(z/2)]\). The provided `verify_schottky.py` runs using the Python standard library and performs 42 finite checks across seven explicit gap ratios, including sign changes, stationary residuals and quantitative comparisons to the asymptotic formulas.

Run with `python3 verify_schottky.py`. Output observed: `PASS: 42 finite diagnostic checks across 7 gap ratios.`

The proof in RESULT.md establishes the unbounded-gap-ratio claim analytically by a positive monotone derivative ratio with uniform asymptotics. Finite testing is not substituted for this argument. The fixed model assumes exact noninteracting canonical equilibrium; no experiment or external independent assessment has been performed.
