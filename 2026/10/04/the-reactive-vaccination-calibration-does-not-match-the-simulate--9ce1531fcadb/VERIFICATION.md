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

The standalone checker `verify.py` reconstructs the vaccination-only calibration in both equations using high-precision decimal arithmetic.

It verifies that the supplement's affine target-relaxation law maps \(0.33\) to \(0.165\) and \(0.22\) to \(0.11\) over 150 days at rates \(0.006581243690\ldots\) and \(0.008461585371\ldots\), respectively. It separately verifies that the counterfactual equation printed in the main article and implemented in the public notebook requires
\[
\nu_{1/2}=\frac{\log 2}{150\cdot0.93}=0.004968796993\ldots
\]
per day to halve either susceptible fraction.

Finally, it inserts the supplement's two rates into the multiplicative counterfactual law and checks the resulting endpoints \(0.1317635673\ldots\) and \(0.0675748848\ldots\), which are distinct from the stated half-targets.

The checker addresses only the isolated vaccination calibration. It does not simulate epidemic transmission, reproduce posterior inference, or assess total intervention effectiveness in the full model.
