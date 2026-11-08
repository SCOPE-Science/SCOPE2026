---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

RESULT.md steps 1-5 parameterize x=a cosh u, y=b sinh u as z=cw+conj(c)/w, w>0. The deck involutions w->r/w and w->conj(r)/w imply invariance by rotation r^2. Infinite rotation order forces a constant rational function by finite generic fibers; finite order m=q/gcd(q,2) yields fixed field C(w^m+epsilon/w^m), equal to rational functions of a real-valued Dickson T_m(z). Degree of rational maps composes multiplicatively, giving first ambiguity at m with T_m±i. Multiplying |P(z(w))|²-|Q(z(w))|² by w^(2n) yields polynomial degree <=4n, proving any 4n+1 distinct samples suffice for n<m. The zero-polynomial case and quotient poles on the real branch are separately addressed. Independent SymPy rederived T_2=-i(z²-1) and exact identical moduli for a=b=1.

## originality

PASS

Best-knowledge PASS for the exact single-conic rational-fiber and exceptional-degree classification; general reflection methods are prior and not claimed. Two intersecting curves, two circles, and complete parallel lines do not give the identical observation set or precise one-branch degree cutoff in the inspected statements.

## value

PASS

Natural and useful full classification for polynomial phase retrieval on a single noncompact conic, with sharp arithmetic exceptional degree and constructive sufficient finite sampling. The contrast between irrational uniqueness and finite-order ambiguity is a mathematically motivated boundary, not an arbitrary parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
