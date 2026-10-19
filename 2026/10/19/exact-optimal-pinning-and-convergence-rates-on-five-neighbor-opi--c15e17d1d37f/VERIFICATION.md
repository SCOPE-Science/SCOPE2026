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
# Reproducibility and limits

Execute `python verification/verify.py` from the package root. The script uses only Python's standard library, explicitly constructs the graph adjacency independently of the symbolic argument, and checks 524,256 labelled pinned subsets across ring orders 5–18 for agreement of the forest, gap, minimum-cardinality, and optimal-layout formulas. It also validates constructive optimal sets for orders 19–1000, and executes 48 deterministic Runge–Kutta numerical trajectories with their observed target-error bounded by the theorem's right-hand side within the stated integration tolerance. The program reports each category of successful checks.

The theorem does not rely on floating-point checks. The all-order classification is proved by cycle/chord/gap analysis, the minimum and count by composition counting, and the global trajectory bound by the five-median three-controlled-input property and variation of constants. Exact subset enumeration is finite; numerical integration checks are not proofs for real time or arbitrary initial states.

All definitions, limiting cases, inequalities, quantifiers, and references appear in `RESULT.md`. Independent audit remains unperformed.
