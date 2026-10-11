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

# Verification of the edge-weighted correspondence theorem

The analytical argument is self-contained in RESULT.md. Its nonstandard global steps are the exact sign classification for the response-ratio derivative and the unique coexistence root; neither follows from finite sampling. Differentiating the exhibited expression proves the ratio-shape lemma globally for all \(k>1\) and \(y>0\). The Legendre reduction uses the strictly increasing Perron response and the divergence of its inverse at both endpoints. The sixth-order expansion and stationary free-energy condition give the explicit tricritical constants.

`verify.py` was executed from its actual package path, with requirements in `requirements.txt`. It passed 89 finite symbolic and numerical assertions, including an exact eigenvector identity, an exact pressure derivative, the general response expansion, the sixth-order matched free-energy polynomial, multiple numerical coexistence roots, the two predicted limiting regimes, and stationarity of explicit transition kernels. All required high-precision root tests passed at 55 decimal digits. These checks do not establish global uniqueness for continuum parameter ranges, asymptotic uniformity, or literature priority.

To reproduce, install `requirements.txt` and run `python verify.py` beside this document. No datasets or external service connections are needed. There has been no independent audit or independent certification.
