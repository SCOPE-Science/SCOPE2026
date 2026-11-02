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

# Reproduction and proof boundary
Run `python3 verify.py` using Python 3's standard library. The program constructs actual labelled windmill graphs and enumerates every initial partial colour assignment for \((q,n)\) equal to \((3,2)\), \((3,3)\), \((3,4)\), and \((4,2)\), including incompatible assignments, simulates forced colour propagation, tests proper completion, and separately evaluates the structural characterization and the polynomial. It also performs exact coefficient comparisons over 224 parameter pairs with \(3\le q\le16\) and \(2\le n\le17\).

Successful local execution produced:

`VERIFY_OK complete_cases=4 initial_assignments=357677 forcing_assignments=13296 symbolic_profiles=224`

These checks are independent finite corroboration; they cannot prove statements quantified over all \(q,n\). The general proof is the structural count in `RESULT.md`. No external independent audit was performed; the structured front matter records that fact.
