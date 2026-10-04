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
The general finding is proved analytically from the printed fitting equations and compartment definitions.

The verification script checks the published numerical values:
- the initial plotted cumulative quantity is \(20736+633=21369\);
- the fitted parameters give the increment ratio
  \[
  \frac{0.1836+0.0185}{0.1836}\approx1.1007625272;
  \]
- the corresponding relative excess is approximately \(10.0763\%\);
- holding the published trajectory fixed, \(H+R\approx68000\) corresponds to the model-consistent confirmation counter
  \[
  C\approx63731.4523.
  \]

The script does not perform parameter estimation and does not treat the converted endpoint as a new forecast. No independent audit has been performed.
