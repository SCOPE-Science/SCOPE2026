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

# Reproducible checks

The geometric identification as the regular zero scheme of \(\mathcal E=(\operatorname{Sym}^2\mathcal U^\vee)^{\oplus 2}\), its normal sequence and the 84-term torus-localization identity justify converting exact sums to intersection numbers. The accompanying self-contained `verify.py` replays all eleven characteristic integrals for two distinct integer torus actions and checks agreement with the displayed integers. It also independently extracts the coefficient giving \(\int_F H^6=3904\). An independent formal mathematical audit has not been performed. The implementation does not determine the integral Chow ring or the cohomology outside these characteristic numbers.
