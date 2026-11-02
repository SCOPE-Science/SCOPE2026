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

# Reproducibility and scientific limits

Run `python3 verify_symbolic.py` with Python 3 and its standard library. The complete finite-factor computation classifies 529 capped tagged profiles, checks the only periods and sharp entrance times, and verifies the exact coefficient matrix. It also independently checks all weighted profile formulas for 81 ordered sizes between two and ten.

Run `c++ -std=c++17 -O2 verify_microscopic.cpp -o verify_microscopic && ./verify_microscopic` with a standard C++17 compiler. This separate implementation iterates all labelled vertex states on eight complete bipartite graphs, totaling 1,327,590 initial configurations, and directly compares first-entry times and eventual periods with the theorem. Outputs are in `verify_symbolic.out` and `verify_microscopic.out`.

The algebraic finite quotient and exact inclusion–exclusion arguments are necessary to infer a theorem for unbounded graph sizes. The small-graph exhaustive program does not make that inference alone. No formal proof assistant, outside human referee, or independent external audit is claimed. Historical novelty is qualified by material not examined in full.
