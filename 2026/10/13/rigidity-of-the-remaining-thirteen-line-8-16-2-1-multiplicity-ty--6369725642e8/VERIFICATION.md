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

# Reproducibility and limits

Run `python verify.py` using Python 3.8 or later with no external dependencies. The checker enumerates the thirteen cyclotomic lines over finite fields of characteristics 11, 31, and 41; confirms all thirteen lines are distinct, the eight double, sixteen triple, two quadruple, and one quintuple points, the projective linewise counts and five slope multiplicities. Expected output: `THIRTEEN_LINE_INCIDENCE_OK`.

The symbolic proof in `RESULT.md` is characteristic zero and covers all complex arrangements satisfying the two additional incidence hypotheses; enumeration of finite fields cannot prove uniqueness over the complex numbers. The decisive nontrivial ingredient is the abelian-group Kneser inequality applied to a five-element quotient set. The exclusion application further invokes the necessary constraints in arXiv:2609.33584v2, Propositions 5.1 and 5.8. The argument has not been independently audited.
