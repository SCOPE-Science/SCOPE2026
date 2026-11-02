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

# Reproduction of the open-ladder enumerator

Use Python 3.10 or later with SymPy installed. Run `python3 verify.py` in the directory containing this document. The verifier builds the weighted transfer from the central-rung local inequalities, checks the exact formal power series rational identity by symbolic inversion and the characteristic factor by symbolic polynomial equality, and compares against an independent exhaustive graph-based test for every ladder with one through eight rungs. Each of the \(87380\) possible vertex subsets in these eight dimensions is checked directly. The observed output was `VERIFY_OK open_cases=8 examined_subsets=87380 weighted_matrix_identities=2 mu=0.514909291164 variance=0.359892854829`.

The numerical check recomputes the two limiting constants from implicit derivatives and the displayed algebraic root, but the exact formulas in `RESULT.md` are the mathematical definitions. The symbolic checks establish the infinite enumerator; the analytic central limit theorem is proved in the written proof, not by a finite computer experiment. The asymptotic estimates concern uniformly selected admissible sets and do not assert quantitative Berry–Esseen rates, local limits, or results for wider grids.
