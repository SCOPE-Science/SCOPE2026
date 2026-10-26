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
# Reproduction and scope

Run `python check.py` with Python 3, NumPy, SymPy and SciPy. It checks the cubic error polynomial against symbolic formulas; computes both critical boundary cases exactly; checks a set of independent numerical minimax scans for each regime; and executes 300 seeded two-by-two stochastic Lyapunov examples, comparing three inner recurrence stages to the polynomial error operator. The mathematical proof of the global optimum is in `RESULT.md`; the finite code check is corroborating evidence only.

Scientific limits: this is a restricted symmetric two-state stochastic Lyapunov problem. The result concerns an outer-cycle Frobenius norm contraction and exact arithmetic, not positivity of intermediate approximations, performance on other spectra, or a universal floating-point guarantee. The accessible primary source provides the general recurrence; complete text of the older related Smith–inner–outer article was unavailable, so the originality conclusion retains that explicit risk. No external independent audit has been performed.
