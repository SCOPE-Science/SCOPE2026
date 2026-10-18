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

The reproducible Python script `verify_logchirp.py` uses `mpmath` to cross-check independent consequences of the analytic argument.

It compares nine direct beta integrals with the exactly solvable \(\tau=1\) beta/gamma ratio (weights \(a=0.7,1,2.5\), degrees \(n=0,3,15\)); four subcritical \(\tau=0.6\) gamma-law evaluations; and four complex-contour integrations (weights \(a=1,2\), \(\tau=1.3,1.5\), logarithmic scales \(L=100,500\)) against the predicted moving gamma factor. The result was:

`VERIFY_OK 17 beta identities, subcritical phase, and complex-contour gamma ratios`

The supercritical ratios for \(a=1,\tau=1.3\) were \(1.0368885737226+0.00440039031917i\) at \(L=100\) and \(1.0160035331928+0.00574843819853i\) at \(L=500\). For \(a=2,\tau=1.5\), they were \(1.3204854579815+0.26005465937562i\) and \(1.1797366040089+0.20003925183391i\), respectively. The approach toward the asymptotic factor is visibly slower closer to \(\tau=2\), in accordance with the proof's Taylor remainder.

To reproduce, install a standard Python distribution with `mpmath` and execute `python3 verify_logchirp.py` from the folder containing that script. The proof of the infinite statements is in `RESULT.md`; no finite numerical sampling is treated as proof of an asymptotic or a universal Schatten-class assertion.
