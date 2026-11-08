---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Use planar convex Cheeger-radius theorem: reciprocal h is unique r solving |(K+tB)⊖rB|=πr². Support halfspaces show outer offset erosion equals K+(t-r)B for r<=t, or K⊖(r-t)B for r>=t. Comparing at r=t gives exact cutoff A=πt². For t>=t* the Steiner formula A+P(t-r)+π(t-r)²=πr² yields h=(P+2πt)/(A+Pt+πt²), with K+tB self-Cheeger. For t<t* near the cutoff, small polygon insets retain each side and |K⊖sB|=A-Ps+Cs², C=Σcot(alpha_i/2); the small root of A−πt²−(P+2πt)s+(C−π)s²=0 determines r=t+s. Implicit differentiation at t* gives s'=-2πt*/B*, different second coefficient by (C−π)(s')²/B*, hence jump h''(t*+)-h''(t*-) =8π²(C−π)/B*³. The independent symbolic series check reproduced the coefficient. Jensen on exterior half turns β_i with Σβ_i=π yields C>=n tan(π/n)>π, equality iff equiangular; regular n-gons attain. The lower branch is explicitly only a germ, not a global formula for arbitrary insets.

## originality

PASS

Best-of-knowledge originality PASS after searches and real statement-level primary comparisons; no source found to imply the exact final claim. Explicit historical/inaccessible-source risks remain: The signature follows from elementary differentiation of classical parallel-body and Cheeger formulas, so another unindexed source could have calculated it already.; At offsets far below t*, the inner inset can lose sides and the quadratic branch may fail; full polygon recovery is not claimed.

## value

PASS

The scalar geometric response to disk rounding has a universal loss of twice differentiability that recovers a genuine polygonal corner-angle invariant even when original Cheeger sets are irregular. The sharp angular inequality identifies equiangular extremizers at every side count; this provides exact inverse-geometric information beyond known differentiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
