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

Run `python3 verify_transmission_windmill.py` in a standard Python installation. No nonstandard dependencies, downloaded content, random seeds or internet access are required. The verifier constructs \(K_1\vee(kK_m)\), simulates every initially filled labelled vertex subset using exact rational arithmetic under simultaneous rounds, and counts all successful sets by size. It separately computes the coefficient sequence predicted by the closed formula and checks equality at every tested parameter.

Verified graph sizes: \((2,2),(3,2),(4,2),(2,3),(3,3),(2,4),(3,4)\), expressed as \((k,m)\). The test used \(337\) parameter/graph combinations, including exact threshold values and rational perturbations around all four critical levels. All comparisons passed. An additional constructive example verifies that a successful set can have an unsuccessful strict superset.

For \(k=4,m=2,\alpha=1/20\), the tested \(\beta\) values \(1/25,3/50,2/25,1/5,7/10\) have minimum seed-set sizes \(5,7,8,8,9\) and minimum-set multiplicities \(48,8,9,1,1\), respectively.

# Scope and limits

The program checks finite instances and exact rational parameters. It does not mechanically prove an infinite all-real theorem or exhaust all parameters; the general proof is supplied in `RESULT.md`. Scientific priority is assessed against accessible published records and does not amount to independent external audit or a guarantee that no equivalent unpublished result exists.
