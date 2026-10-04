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

The final claim was checked symbolically from the defining operations of \(P_{3,22}(q)\).

1. **Intrinsic flags.** The associative square is \(P_q^2=Fu\), and the Lie derived algebra is \([P_q,P_q]=Fu\oplus Fv\).
2. **Adapted-basis invariance.** Writing an adapted basis as \(u_0=au\), \(v_0=bu+cv\), \(x_0=dx+ru+sv\), the equations \(x_0v_0=u_0\) and \([x_0,u_0]=u_0\) give \(dc=a\) and \(d=1\), so \(c=a\). Direct substitution then yields \([x_0,v_0]=v_0+q u_0\).
3. **Lie component for nonzero parameters.** For \(q,q'\ne0\), the linear map \(x\mapsto x'\), \(u\mapsto q'u'\), \(v\mapsto qv'\) is invertible and preserves the brackets.
4. **Zero/nonzero Lie separation.** On the characteristic ideal \(V=[P_q,P_q]\), every adjoint action from an element outside \(V\) is scalar when \(q=0\) and non-scalar when \(q\ne0\).
5. **Published premises.** The primary source proves \(P_q\cong P_{q'}\) as Poisson algebras exactly when \(q=q'\), and proves that in dimension two the associative and Lie products cannot both be nonzero.

No numerical enumeration is used to establish a universal statement. The finite-field count \(2^m-1\) is only the cardinality of the nonzero parameter set in \(\mathbb F_{2^m}\). The result does not assert completeness of the entire global fiber beyond this family.
