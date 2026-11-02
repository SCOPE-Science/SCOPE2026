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

# Reproducibility and verification

Use Python 3.10 or later, standard library only, to run `python check_circle4.py`.

The program computes the same four-agent EPCD expected full-profile cost in two logically separate ways: enumerating each deleted report and selecting among the surviving three by the opposing-gap PCD rule, and applying the direct four-report gap probabilities. It compares both answers exactly using rational arithmetic.

- Exhaustive grid profiles with one cyclically rotated report at zero: 2,600 (denominator 24), 8,436 (denominator 36), and 19,600 (denominator 48), for 30,636 total.
- Seeded additional rational profiles: 6,500; 37,136 four-report profiles tested in total.
- Exact checks of all three polynomial regime identities at 4,851 additional rational parameter triples (regime counts 1,771; 1,540; 1,540).
- Direct exact witness calculation: \(\operatorname{OPT}=1/2\), \(C_{\mathrm{RD}}=3/4\), \(C_{\mathrm{EPCD}}=5/8\); the equal mixture ratio is \(11/8\), with multiple other sampled mixture weights checked.
- All 37,136 full profiles pass the EPCD \(5/4\), RD \(3/2\), equal-mixture \(11/8\), and sampled-weight \((5+\lambda)/4\) bounds; the final output reads `PASS exact rational checks`.

The three universal polynomial identities also follow by formal expansion of the displayed formulas; the precise nonnegative decompositions and the normal-form argument in RESULT.md constitute the mathematical proof. Finite enumeration is not an exhaustive verification of continuous profiles. No external independent audit or machine-checked infinite theorem is asserted.
