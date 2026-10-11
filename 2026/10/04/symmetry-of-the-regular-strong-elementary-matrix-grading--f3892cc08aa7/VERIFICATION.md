---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Any component-permuting algebra automorphism must preserve the neutral diagonal component because it contains the identity. It therefore permutes the primitive diagonal idempotents, say by \(\sigma\), and each one-dimensional matrix corner forces \(\varphi(E_{x,y})=d_xd_y^{-1}E_{\sigma(x),\sigma(y)}\), yielding the diagonal factor \(T_G=(k^\times)^G/k^\times\). If \(\pi\) is the induced degree permutation, the degree equation \(\sigma(x)^{-1}\sigma(y)=\pi(x^{-1}y)\) implies \(\pi(e)=e\), \(\sigma(y)=\sigma(e)\pi(y)\), and then \(\pi(xg)=\pi(x)\pi(g)\). Thus \(\pi\in\operatorname{Aut}(G)\) and \(\sigma\) is left-affine. Conversely every diagonal conjugation and left-affine permutation has the required action. Hence the full component-permuting group is \(T_G\rtimes\operatorname{Hol}(G)\), the componentwise stabilizer is \(T_G\rtimes G\), and the quotient is \(\operatorname{Aut}(G)\). The finite-field orders follow immediately. The package checker independently confirms the permutation factors for \(C_2,C_3,C_4,C_2^2,S_3\).

## originality

PASS

Diniz and Bezerra already analyze the permutation subgroup for crossed-product elementary gradings and, in the crossed-product case, identify the componentwise graded permutation subgroup with the grading group. Gordienko and Schnabel provide the broader weak-equivalence framework. The recent strong-elementary classification identifies the regular action as the canonical strong extremal case. None of the inspected statements computes the complete self weak-automorphism group, the diagonal extension by \(T_G\), or the resulting quotient \(\operatorname{Aut}(G)\). Current Resultary search returned only the assigned exact theorem. The newest classification paper's full body was not accessible through the inspected public routes, so a residual same-paper overlap risk is retained.

## value

PASS

The regular strong elementary grading is the canonical extremal full-matrix case, and its complete weak symmetry group is a natural structural invariant. Identifying the Weyl-type quotient exactly with \(\operatorname{Aut}(G)\) cleanly separates diagonal and translation symmetries from genuine degree relabelings and extends the previously known componentwise permutation subgroup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
