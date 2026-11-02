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

The independent sampling model is \(R_1,R_2\sim2r\,dr\) and \(\Theta\sim\operatorname{Uniform}[0,\pi]\), with intrinsic developed-sector distance \(D_c^2=R_1^2+R_2^2-2R_1R_2\cos(c\Theta)\). The proof in RESULT.md supplies the required infinite-family reasoning by identifying all maximizing configurations and evaluating localized scaled integrals. This document records supplementary finite checks, not an independent certification.

The standalone, standard-library `cone_verifier.py` performs independent quadrature for \(c=0.12,0.24,1/3,0.4,0.65,0.92,1\), at three decreasing distance deficits per parameter. It also checks the exact known squared-distance moment \(\mathbb E D_c^2=1-8\sin(\pi c)/(9\pi c)\) to test sampling normalization, and compares diameter candidates on a representative numerical grid. These 67 consistency comparisons pass in the supplied program. The smallest tested deficit has less than \(0.7\%\) relative error across the four formula regimes.

Run with Python 3.9+ using `python cone_verifier.py`; no nonstandard dependencies are required. Finite numerical checks do not establish an asymptotic theorem, historical uniqueness, or independent validation. For exact assumptions, proof boundary cases, source comparisons and limitations, see RESULT.md and REVIEW.md.
