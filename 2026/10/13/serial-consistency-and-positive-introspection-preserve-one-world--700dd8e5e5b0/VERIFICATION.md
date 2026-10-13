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

The proof was checked against the broad closure definition in arXiv:2610.01433v1: the closure map is an arbitrary map on sets of formulas, so the proof-consequence construction is admissible without proving extensivity, monotonicity, or idempotence.

For a maximal consistent set \(\Delta\), define \(G=\{\chi:\Box\chi\in\Delta\}\) and put \(\chi\in\operatorname{cl}(X)\) exactly when some finite \(X_0\subseteq X\) satisfies
\[
L_\Lambda\vdash
\left(\bigwedge_{\xi\in X_0}\Box\xi\right)\to\Box\chi.
\]
At the actual generator \(G\), closure membership is equivalent to boxed membership in \(\Delta\). The forward implication uses the finite support and Modus Ponens; the reverse implication uses the singleton support. This yields the modal step of the truth lemma.

For \(\mathsf M\), \(\mathsf C\), \(\mathsf K\), and \(\mathsf4\), union the finite supports and compose with the selected axiom. For \(\mathsf N\), the theorem \(\Box\top\) gives the empty-support witness. For \(\mathsf D\), opposite closure members would give finite supports deriving both \(\Box\chi\) and \(\Box\neg\chi\), contradicting \(\neg(\Box\chi\wedge\Box\neg\chi)\) and consistency.

For a single non-theorem, use a maximally consistent set over the finite augmented subformula set used by Nishimura. Its generator is finite. The same closure and frame-condition arguments remain valid; the truth bridge is required only for boxed formulas in that finite set. Hence the countermodel has one world and a finite generator.

No experiment or finite enumeration is used as proof. No effective decidability or complexity bound is asserted.
