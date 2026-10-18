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

The standalone `verify.py` is executable with Python 3 and only its standard library: `python verify.py`. It reconstructs exact fractional binomial-mixture probabilities, checks normalization, both curvature implications and their analytic ratio factors for 1,755 rational parameter settings (12,285 interior indices), and verifies the strict fractional witness \(a_1^2/(2a_0a_2)=80/81\). The program prints `PASS` only after all assertions succeed.

The general theorem is not certified by finite enumeration. Its proof uses the exact three-term ratio identity, the global elementary maximum \(z/(1+z)^2\le1/4\), the surjectivity of the strictly interior mixing weight onto each prescribed \(z_k>0\), and exact maxima over all interior indices. The consecutive-failure assertion follows from strict second logarithmic derivatives on the real interpolated index interval.

A prior-literature comparison and scientific correctness/originality/value review were performed for this result. Independent audit and independent validation are not performed. Residual uncertainty: an equivalent earlier result using other terminology could exist.
