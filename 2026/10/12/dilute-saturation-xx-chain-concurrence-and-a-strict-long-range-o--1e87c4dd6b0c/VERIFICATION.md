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

# Reproduction and limits

Run `python verify.py` (Python 3 and NumPy). The script reconstructs exact Jordan–Wigner string expansions for fifteen finite combinations of density and separation; checks the corresponding independent block determinants; verifies elementary numerical convergence; and, crucially, certifies the strict sign inequality with **rational arithmetic**. The finite checks establish consistency of the proof's identities, not the infinite-limit theorem.

The analytic proof handles all positive \(s\) by termwise convergence dominated with \((2s)^m/m!\). The only numerical output used as a quantitative illustration is the Nyström value \(F(\sqrt2/\pi)\approx0.78468\); it is **not** part of the strict proof, which uses the weaker, rigorously certified inequality \(F(\sqrt2/\pi)>0.716\). The positive concurrence asymptotic follows from this inequality and \(\sqrt{1-\sin^2(\sqrt2)/2}<0.716\).

The calculation has not been independently audited. No claim is made about all finite-distance onset points or full novelty certification.
