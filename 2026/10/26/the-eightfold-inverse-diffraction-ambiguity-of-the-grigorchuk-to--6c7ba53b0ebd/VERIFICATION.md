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

The proof reduces the full diffraction and its inverse fibers to the Haar characters of the dyadic odometer. The essential analytic identity is the exact integral of a primitive character over each valuation shell; its three cases yield the coefficients \(M,V,P,Q,R\), with \(P+Q+R=0\). The linear inverse and the real zero-sum absolute-value lemma then classify every fiber, including degenerate cases.

Run `python3 verify.py` with Python 3 and its standard library. The standalone verifier reconstructs nine substitution iterates and compares the resulting word with the valuation coding, checks the rational inverse and exact diffraction Parseval identity for all 625 vectors with entries between \(-2\) and \(2\), checks the Bragg-scale period three, constructs four positive and eight real homometric weightings, verifies their first 25 exact intensities, compares eight independently summed finite Fourier modes with analytic amplitudes, and compares 33 independent finite autocorrelation lags.

Observed verifier output:

`VERIFY_OK: substitution prefixes; 625 exact four-coordinate inversions and Parseval identities; 4 distinct positive and 8 distinct real homometric weightings; 25 exact Bragg intensities per weighting; 8 independently sampled dyadic Fourier modes; 33 finite autocorrelation lags; max_error= 0.00263074`

Finite approximants omit one exceptional two-adic position at each scale. Their nonzero error is expected and does not establish the infinite formulas. The infinite conclusions rely on the valuation-shell integration, spectral completeness of dyadic characters, and exact inverse linear algebra. No external scientific audit has been performed.
