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

# Reproducible mathematical checks

The result is a deductive theorem and requires no opaque numerical table, hidden proof package, solver or external execution. Its steps can be independently replayed from the displayed definitions and the standard completeness and finite-model properties of normal modal logic \(\mathsf K\).

1. Verify the atom/box truth clauses of Bevan (2025), §1.1. At a Kripke point, take \(\Gamma\) to be its full immediate-successor theory. Soundness for each \(\lambda\subseteq\mathsf K\) proves that \(\Gamma\vdash_\lambda\psi\) iff every successor satisfies \(\psi\).
2. For the inductive tree construction at depth \(n\), list all operands of box subformulas occurring in the finitely many target formulas. Divide them according to \(\Gamma\vdash_{L_{n-1}}\). For each negative operand \(\chi\), derive the contradiction that would follow if \(\mathsf K\vdash(\bigwedge B^+)\to\chi\). The formula has depth at most \(n-1\), so the induction premise applies exactly at the required boundary.
3. Apply ordinary Kripke completeness to the resulting \(\mathsf K\)-consistent finite conjunctions. Standard finite-model property and depth-\(n-1\) unraveling turn each witness into a finite rooted tree. Adding one root changes modal depth by exactly one and preserves every requested box truth value.
4. At the sharpness boundary, \(\Box\top\notin\mathrm{PC}\); by induction \(\Box^r\top\notin L_{r-1}\), so \((M,\varnothing,L_{r-1})\not\models\Box^{r+1}\top\), whereas theorem lifting puts \(\Box^{r+1}\top\in L_{r+1}\). This establishes strictness without finite enumeration.
5. Use the prior-work identity \(V\mathrm{INT}(\lambda)=\mathsf K_0+\Box\lambda\) to see that the increasing union contains the distribution axiom and is closed under necessitation, hence equals \(\mathsf K\). Strictness rules out any finite stabilization index.

These are proof-reconstruction instructions, not execution logs. The induction covers all natural numbers; no finite experiment is claimed to establish universal correctness. Literature priority and independent auditing remain open.
