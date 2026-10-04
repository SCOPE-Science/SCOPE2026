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
The general theorem was checked by reconstructing every radius regime in the proof.

For \(0\le x\le\delta\), the critical radii are \(\delta+x\), \(1+\delta-x\), and \(1+\delta+x\). The cap \(\rho_c=1-2\delta+m\) is exactly the value that makes the small-radius bound \((1+\rho_c)/2\) equal to the smallest candidate maximum \(1-\delta+m/2\).

For \(x\ge1+\delta\), the endpoint interpolation slope is
\[
k=\frac{1+m}{1+2\delta}.
\]
The identity
\[
k-\rho_c=\frac{2\delta(2\delta-m)}{1+2\delta}>0
\]
controls partial perturbation mass, while \(k<1\) controls the interval after the whole perturbation has entered. The endpoint crossover occurs at
\[
x_{\delta,m}=\frac{1+3\delta+m\delta}{1+m},
\]
and
\[
x_{\delta,m}-(1+\delta)=\frac{2\delta-m}{1+m}>0.
\]

The sharpness construction was checked directly at \(x=\delta\): a perturbation equal to \(\rho\) immediately to the left of the tower boundary forces small-radius averages to equal \((1+\rho)/2\), which exceeds the below-threshold value when \(\rho>\rho_c\).

`verify_shape_threshold.py` additionally performs exact finite checks for several rational step perturbations and for one above-threshold witness. Its output is stored in `verification_output.txt`.

Same-model review status: passed. Independent audit: not yet performed.
