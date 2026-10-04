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

The central proof is semantic.

If accessibility is defined by
\[
wRv
\quad\Longleftrightarrow\quad
\forall\varphi\,
(w\models\varphi\Rightarrow v\models\varphi),
\]
then for every \(\varphi\), failure of the reverse implication would give
\[
v\models\varphi,\qquad w\models\neg\varphi,
\]
and preservation would force
\[
v\models\neg\varphi,
\]
a contradiction. Thus \(R\) is symmetric. Reflexivity and transitivity are immediate, so \(R\) is an equivalence relation.

The bundled `verify.py` checks the finite truth-signature analogue and separately checks the explicit three-world countermodel to axiom \(4\).

The computation prints `VERIFY_OK`.

## Limits

The proof addresses the Section 5 relation exactly as printed. It does not propose a complete replacement semantics or assess the independent Section 4 Boolean-valued completeness theorem.
