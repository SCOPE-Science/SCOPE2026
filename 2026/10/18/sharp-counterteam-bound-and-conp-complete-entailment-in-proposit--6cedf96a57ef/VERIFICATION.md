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

# Verification notes

The proof is mathematical and fully given in `RESULT.md`. The supplementary executable `verify_entailment.py` evaluates the syntax directly, recursively enumerating *all* lax splits on a team, including overlaps, without implementing the asserted bound as a semantic rule. Run:

`python3 verify_entailment.py`

The observed final line is `VERIFY_OK`. Direct checks covered 1605 generated formulas on one variable and 1607 on two variables, their 11 and 51 distinct truth tables, 2722 entailment pair comparisons, union closure and convexity, and explicit sharpness cases with \(m=1,2,3\). The third claim, arbitrary \(m\), is established by symbolic characteristic-valuation construction, not by an exhaustive run. The checker and this document do not constitute independent certification.

Science assumptions: finite input formulas and premises, lax splitting, Boolean valuations, inclusion of the empty team. The largest-model argument requires the finite joint variable domain; general consequence is reduced to it by locality. Complexity membership invokes the published polynomial-time model-checking algorithm for \(\mathrm{PL}(\mathrm{NE})\).
