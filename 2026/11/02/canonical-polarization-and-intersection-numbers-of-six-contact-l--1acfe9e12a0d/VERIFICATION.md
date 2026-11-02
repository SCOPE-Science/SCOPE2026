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

# Reproducibility

Run `python3 verify.py`. This standalone exact-arithmetic script requires only Python 3's standard library. It implements two independent evaluations of the top intersections: (i) Segre-class pushforward on the projectivized tangent bundle and (ii) Atiyah--Bott localization using pairwise distinct integer torus weights for all thirty fixed flags. It checks every integer degree from 6 through 27 for both polynomial formulas, and every degree from 6 through 14 via localization (two invariants in each degree). The output observed from the packaged file is `VERIFY_OK; 44 Segre + 18 localization checks; examples d=6,7 checked`.

The symbolic formulas and universal Gorenstein/positivity statement rely on the explicit theoretical proof in `RESULT.md`. The finite checks are consistency tests only, not independent certification. The lci assertion uses Theorem 1.2 of arXiv:2610.28558 as an external proved hypothesis. The known point-flex-locus degree from arXiv:2502.02075 agrees with the separate intersection \(\int H^3c_6(E_d)=274d^2-720d\). Independent audit has not been performed.
