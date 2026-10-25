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

# Verification and reproduction

The analytic proof in `RESULT.md` establishes the theorem for all integers \(k\ge3\) and \(r\ge1\). Computational checks are finite corroboration only. Execute `python verify_guardian_core_gap.py` with Python 3, NumPy and SciPy. The independent script enumerates complete \(k\)-member committees and every alternative proposal up to \(k\) candidates, checks the exact Hare affordability inequality by integer multiplication, and compares each committee against all other committees for Pareto dominance. It independently solves a linear program for the fractional payment certificate with a common strict reserve slack.

Reproduced output: \(296\) committees total. The six exhaustive cases yield \((k,r;\mathrm{core},\mathrm{core+})=(3,1;4,3),(3,2;35,15),(3,3;117,36),(4,1;5,4),(4,2;120,56),(5,1;6,5)\). Every committee is independently checked Pareto efficient. An LP tolerance of \(10^{-8}\) is used; the exact analytic payment and obstruction arguments remove dependence on numerical tolerances for the general theorem.

Limit: these finite runs do not certify the infinite parameter statement or publication priority. The separate scientific proof and literature analysis address those questions to the stated scope, with independent audit not performed.
