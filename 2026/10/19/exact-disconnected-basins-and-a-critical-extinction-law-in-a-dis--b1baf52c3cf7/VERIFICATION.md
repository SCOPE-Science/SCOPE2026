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

The proof is self-contained apart from the standard interval-map convergence theorem (Coppel): absence of a primitive two-cycle for a continuous interval map ensures convergence of every orbit to a fixed point. The required absence is checked exactly by the displayed logistic second-iterate factorization and the discriminant inequality for all real parameters in the stated domain.

`checker.py` verifies the polynomial identity with SymPy, tests admissible parameter samples, and checks the lower/upper basin assignments and the critical inverse-time boundary numerically. These finite tests do not by themselves prove the infinite-time statements; the monotonic branch arguments, Coppel theorem, root inequalities, and reciprocal-difference identity provide those proofs.

The open-access publisher article's displayed mathematical text (its single-species equation, main results and Appendix A) was compared against the exact basin claim. A 2024 follow-up on related ecological dynamics was only accessible through its abstract/preview for the priority assessment. Mathematical novelty is therefore not independently certified.
