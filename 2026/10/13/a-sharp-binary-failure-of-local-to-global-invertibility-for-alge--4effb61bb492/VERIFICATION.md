---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For F_2^3, E={[[b,0,0],[a,b+c,b],[0,0,c]]:a,b,c in F_2} has determinant bc(b+c)=0 for all eight members. The pointwise hull condition T(v) in E(v) for all eight v is exactly T=[[p,0,0],[q,r,s],[0,0,t]] with r+s=t, hence Ref_a(E)=E+F_2 I and has 16 members. Its only invertibles have p=r=t=1,s=0 and q free, namely I and I+E21. An independently written exhaustive 512-operator-by-eight-vector check confirmed the hull and its two invertibles. Enumerating all 2 subspaces of End(F_2) and all 67 of End(F_2^2) shows that no smaller ambient dimension has identity in the hull of an all-singular linear space; for any invertible hull element its inverse can be used to normalize the identity, so the search proves minimality. For all n>=3 append an arbitrary scalar I on the extra block, preserving singularity and admitting I_n locally by choosing the three-block witness pointwise.

## originality

PASS

The motivating Hao–Chen algebraic-reflexive invertibility-transfer theorem explicitly assumes an infinite field; the finite F_2 example refutes the removed hypothesis, not its theorem. A relevant characteristic-two published finding concerns Lie closure instead of transfer of invertibility. No stronger finite-field linear-space theorem covering this example was identified from actual searches; risk of differently phrased identity-in-reflexive-cover counterexamples remains.

## value

PASS

An explicit smallest-dimension binary obstruction isolates why the infinite-field determinant-polynomial argument cannot be carried to finite fields. Exact hull and invertible-element counts plus minimality make the example a substantive boundary to a natural theorem, rather than an arbitrary matrix curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
