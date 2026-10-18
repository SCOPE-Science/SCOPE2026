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

# Reproducibility and boundaries

Execute `python checks/exact_bounds.py` with Python 3. Only standard-library exact rational arithmetic is required. It checks the ninth Taylor upper bound for \(\sin x-x\cos x\) at \(x=44935/10000\), the rational lower bound \(24/17<\sqrt2\) by squaring, and \((22/7)(44935/10000)^3/(2(24/17))<101\). It prints `OCTAHEDRAL_FOURIER_EXACT_CERTIFICATE_OK` when all assertions pass.

The **infinite-domain** part of the result does not depend on a sampled grid: the exact diamond-section derivative, the pointwise inequality \(\Phi''(r)\ge4(1-r^2)\) for \(0\le r\le1\), two integrations by parts, and a separate diagonal Fourier-zero identity are all proved in `RESULT.md`. The finite script certifies only the stated rational endpoint comparisons. No independent scientific review or external theorem-proving certification has been performed.
