---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For unit vectors let \(a=\|x+y\|_p\), \(b=\|x-y\|_p\). The P-angle objective is \((a^2+b^2-4)/(2ab)\). Clarkson gives \(a^m+b^m\le2^m\) with \(m=p\) for \(p\ge2\) and \(m=p'\) for \(1<p\le2\). At fixed ratio \(t=a/b\), the objective increases with common scale, so the problem reduces to the boundary scalar function \(R_m(t)=[1+t^2-(1+t^m)^{2/m}]/(2t)\). Symmetry reduces to \(t\ge1\), and the derivative sign is equivalent to \((1+v)^\alpha-(1-v)^\alpha\le2^\alpha v\) for \(\alpha=2/m\in(0,1]\); the left side is convex with the same endpoint chord, proving the bound globally. The submitted disjoint-coordinate and Hanner pairs attain the two branches, while the elementary endpoint argument gives 1/2 at p=1 and infinity. All quantifiers and the Hilbert boundary p=2 are consistent.

## originality

PASS

Yang--Li define the same invariant, prove the universal bound \(0\le S_P(X)\le1/2\), and in Example 3.4 choose the same natural \(\ell_p\) witness types. The inspected primary text then describes these as bounds/estimates and does not state a matching all-p upper bound. The audited Clarkson-to-one-variable argument supplies that missing upper bound, giving exactness for every real \(\ell_p(I)\). Resultary's exact search returned the assigned theorem as the exact P-angle hit; nearby \(\ell_p\) constants concern different invariants.

## value

PASS

Real \(\ell_p\) spaces are the canonical calibration scale for Banach-space geometric constants. The exact formula closes the gap between the defining paper's natural witnesses and its general ceiling, identifies the Hilbert phase transition at p=2, and exposes Hölder-duality symmetry. This is a natural complete benchmark of the invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
