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

The included `verify.py` uses exact symbolic arithmetic. It reconstructs the six-dimensional bracket and metric with symbolic parameters \(a,b,f\), assuming \(af\ne0\). It checks the generic Malcev identity, the metric eigenvalue multiplicities, the derived and lower-central spans, centrality and isotropy of \(\operatorname{span}\{e,e_1\}\), the Jacobiator \(J(d,e_4,e_2)=af\,e\), and the five nonzero Levi-Civita products obtained from the Koszul formula.

The captured run in `verify_output.txt` ends with `CHECK_OK`. The script does not substitute the classical Lie curvature formula for the Malcev-specific curvature introduced by the primary source; flatness of this family is therefore cited to arXiv:2609.13950v1. The new conclusion requiring verification is the nilpotent class, exact center, metric index, and the resulting sharpness of the Lorentzian theorem.
