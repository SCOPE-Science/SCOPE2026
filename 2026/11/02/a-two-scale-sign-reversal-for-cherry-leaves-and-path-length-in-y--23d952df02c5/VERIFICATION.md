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

# Reproducibility and boundaries

Run `python3 verify_yule.py` with a standard Python 3 interpreter. The script has no third-party dependencies and uses `fractions.Fraction` for exact rational arithmetic.

The checked package emitted `PASS: 60677 exact assertions; 46233 growth histories; 873 independent transition cases.` Its enumeration covers all uniformly leaf-selected Yule growth histories through nine leaves. It independently checks conditional transition identities on 873 tree histories through seven leaves, and algebraic formula substitution on integer sizes three through 1,000. The separate induction in `RESULT.md` proves the formula for all sizes and does not rely on a numerical cutoff.

The code tests the fixed-size topology law and not substitutions of branch lengths, extinction or sampling schemes. There is no independent audit or external proof certificate.
