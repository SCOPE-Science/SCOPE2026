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

# Reproducibility and mathematical checks

Run `python3 verify.py` in a directory containing that embedded standalone program. It uses no external packages. The expected exact-rational and exhaustive-regression output is recorded in `RESULT.md`.

The program checks all profiles meeting the support cap for the four finite shapes \((n,m)\in\{(2,3),(3,3),(4,3),(3,4)\}\), with all legal committee sizes, totaling 10,893 eligible profile-and-committee-size configurations and 37,417 committees. It checks JR/core agreement and the greedy maximal-support construction. It checks the fractional blocking assignments of the family at integer quota 1 through 50 with exact fractions, including bounds on every variable, each voter assignment constraint, and the quota inequality.

The universally quantified correctness argument instead depends on two transparent exact arguments: an incidence double count for integral blocks, and a payment/reserve certificate applying the published core+ dual criterion. These do not require enumerating elections. No generic claim about all possible above-quota elections, noise, weighted approvals, or independent validation is made.
