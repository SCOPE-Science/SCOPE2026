---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The counterexample is exact: the coefficient energy \(|x_1|^2+|x_1+x_2|^2\) dominates \(|x_1|^2=\|K^*x\|^2\), while the resulting frame operator satisfies \(Se_1=2e_1+e_2\notin R(K)\). Thus \((S|_{R(K)})^{-1}e_1\) is undefined when the inverse is correctly viewed on \(S(R(K))\). For the repair, \((K^\dagger)^*K^*x=x\) on \(R(K)\) gives \(\langle P_RSx,x\rangle\ge A\|K^\dagger\|^{-2}\|x\|^2\); bounded self-adjoint coercivity makes the compression invertible and both reconstruction identities follow by substitution.

## originality

PASS

The published formula is genuinely ill-typed without range invariance, and the displayed three-dimensional example is an exact witness. Later literature explicitly distinguishes the invertible map \(S:R(K)\to S(R(K))\) or adds \(S(R(K))=R(K)\), but the checked sources do not give this concrete obstruction to Huang--Yang equation (2.10). The universal compression itself is close to a standard corollary of Huang--Yang Theorem 3.3(2): on \(R(K)\) the same coefficient family is an ordinary g-fusion frame, whose subspace frame operator is the compression. That prior ingredient materially narrows the novelty claim, but it does not itself expose the domain error or supply the counterexample. Best-of-knowledge originality is therefore retained for the correction/obstruction, not for the abstract existence of a positive invertible compression alone.

## value

PASS

Although the positive compression theorem is close to standard frame theory, the source-specific defect is substantive: a published reconstruction formula can be undefined under its stated hypotheses, and a minimal exact frame demonstrates the failure while the projection repair gives a usable corrected formula without adding range invariance. This is a motivated correction rather than a free-standing normalization exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
