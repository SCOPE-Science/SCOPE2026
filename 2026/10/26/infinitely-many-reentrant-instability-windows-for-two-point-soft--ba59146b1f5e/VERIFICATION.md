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

# Verification and reproducibility

## Analytical checks
The form transformation \(v=(D^4+1)^{1/2}u\) reduces negative eigenvalue inertia to the two eigenvalues of the exact point-evaluation Green matrix. The Green function is checked by the constant-coefficient fourth-order equation, evenness, continuity of derivatives up to order two, and a unit third-derivative jump at zero. The strict comparison with one distinguishes unstable negative modes from threshold zero modes. The derivative \(F'(t)=-2e^{-t}\sin t\) determines all lobes without any finite cutoff; the number of lobes strictly above the threshold gives the ceiling formula for every allowed strength.

## Executable independent numerical corroboration
The standalone script `beam_instability_checker.py` (Python with NumPy and SciPy) compares the closed Green expression with direct Fourier-integral quadrature for 62 distances; verifies four exact lobe-onset values, scans 10,005 spatial points across five stiffness values, and checks eight independent large periodic finite-difference matrix spectra away from near-neutral threshold cases. Execute `python beam_instability_checker.py` from the same directory. The observed output was `PASS: 10079 quadrature/phase/threshold/finite-difference checks`.

## Scope and open verification
Finite-difference truncation is independent corroboration, not a proof of infinitely many components. Claims concern only exact linear fourth-order point-softener dynamics on \(\mathbb R\). Complete historical texts of Coman (DOI:10.1093/imamat/hxh088) and Wang (DOI:10.1061/(ASCE)EM.1943-7889.0000097) were inaccessible, so independent priority investigation remains useful. No independent audit or experimental validation has been performed.
