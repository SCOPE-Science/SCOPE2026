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

For \(u>0\), the equilibrium equations imply \((a+mu-u^2)v=1=(b+cu+du^2)v\). Eliminating \(v\) gives \(F(u)=(1+d)u^2+(c-m)u+b-a=0\), but reconstructing \(v\) also requires \(a+mu-u^2>0\). Since \(a>0\), this concave quadratic is positive for positive \(u\) exactly when \(0<u<	au=(m+\sqrt{m^2+4a})/2\). On the source branch \(b=a\), \(m>c\), substituting \(u=(m-c)/(1+d)\) gives the exact numerator \(a(1+d)^2+(m-c)(md+c)\). At \(a=b=d=m=1\), \(c=-3\), the only positive quadratic root is \(u=2\), for which \(v=-1\); thus the source's listed case can contain no positive equilibrium. The universal criterion is symbolic and does not depend on finite enumeration.

## originality

PASS

The primary preprint version states \(a,b,d>0\) with \(m,c\in\mathbb R\), derives the two equilibrium equations, and then classifies positive equilibria from the reduced quadratic without separately enforcing positivity of the denominator defining \(v\). Fresh Resultary and exact formula/source searches found no prior source-specific correction. Public/OA retrieval of the exact preprint was incomplete and the authorized fallback did not return a verified PDF, so the audit records that access limitation explicitly; the theorem statement and equations needed for this comparison were nevertheless available from lawful full-text excerpts. Best-of-knowledge originality passes with a residual risk of a later revision or erratum.

## value

PASS

A positive equilibrium is the base object for the source's subsequent stability and pattern analysis. The filter is necessary and sufficient for every quadratic candidate, and the exact witness changes the equilibrium count within a stated theorem case by exposing a negative water coordinate. That is a substantive feasibility correction rather than a cosmetic sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
