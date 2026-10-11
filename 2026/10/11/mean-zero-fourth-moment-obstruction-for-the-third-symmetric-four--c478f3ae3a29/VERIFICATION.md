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

The included `verify_bessel.py` is a standalone Python 3 program with no external packages. The actual execution at the packaged source path produced `VERIFY_OK`. The calculation uses exact fractions and alternating-series inequalities to enclose the three Bessel values at \(t=1\), and independently checks the exact formal Taylor expansion through \(t^{10}\).

Mathematical steps independently reconstructed in the accompanying proof are the Fourier coefficients of the odd unimodular witness, the four nonzero autocorrelation coefficients of its degree-three projection, and Parseval's fourth-moment identity. The algebraic certificate proves a strict inequality; it does not establish the exact operator norm, nor any claim about all Poisson operators or all Fourier sections.

Independent audit has not been performed.
