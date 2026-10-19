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

Run `python3 verify.py` using standard Python 3 with no external packages or input files. The program constructs the pairwise alignment automaton from explicit transitions, determinizes it and takes a triple product. It checks the following properties using exact integers: pair-state count \(27\), triple-state count \(1549\); annihilator \((E-4)^3(E-1)\) on \(27\) consecutive pair outputs; annihilator \((E-4)^4(E-1)^3\) on \(1549\) consecutive triple outputs; the complete closed forms for those transfer terms; and direct deletion-ball graph counts at lengths one through four.

The proof uses the Cayley–Hamilton theorem to extend these recurrence identities beyond the finitely checked range; it does not infer an infinite statement from sampling. Direct graph enumeration is an independent semantic check, not the infinite argument. The certificate establishes the stated four-letter radius-one triangle count only; it does not establish optimal code sizes or general-alphabet formulas. Independent assessment has not been performed.
