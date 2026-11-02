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

# Verification

The full proof appears in `RESULT.md`. The independent arithmetic check in `verify_star_ideals.py` enumerates all reduced-row-echelon bases for subspaces of \(\mathbb F_q^{2n+1}\) in six small prime-field cases. For each candidate subspace it directly tests whether the brackets of all spanning rows with each standard Lie-algebra basis element remain in that candidate subspace. The resulting ideal-dimension counts agree exactly with the formula in the theorem.

Command: `python3 verify_star_ideals.py`.

Expected final output: `VERIFY_OK`. Exact exhaustive cases: \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\). Additional high-field polynomial evaluations: \(q=257\) and \(n=4,5,6,7\), with the stated dimension sets carrying more than \(95\%\) of the mass. These diagnostics verify implemented arithmetic and finite cases but do not by themselves establish an all-parameter identity or the limit. The unrestricted mathematical justification is a subspace-graph counting proof followed by a degree comparison. Only prime fields are exhaustively enumerated; finite extensions are covered by the proof, not by direct enumeration.

Self-review: passed. Independent audit: not yet performed.
