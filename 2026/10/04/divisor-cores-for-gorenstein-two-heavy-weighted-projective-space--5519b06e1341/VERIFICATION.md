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

From \(h=r+a+b\) and Gorenstein divisibility, \(x=h/a\) and \(y=h/b\) satisfy \(1=r/h+1/x+1/y\). Writing \(x=gu\), \(y=gv\) with \(\gcd(u,v)=1\) gives \(k=guv-u-v\), \(a=rv/k\), \(b=ru/k\), and the coprimalities \(\gcd(k,u)=\gcd(k,v)=1\) force \(k\mid r\). Setting \(A=gu-1\), \(B=gv-1\) gives exactly \(AB=gk+1\), the congruence/gcd conditions, and \((g-1)^2\le gk+1\) gives \(g\le k+2\). The converse reconstructs integral weights and the required divisibility. Applying the two-heavy Reid--Tai inequalities to \(x,y\) proves automatic canonicity and terminality iff \(y>2\) and \(x>3\), equivalent to \(B>1\), \(A>2\). The nonterminal cases \(y=2\) and \(x=3\) give exactly the divisor family plus \((r,r)\). An independent exact finite reconstruction through \(r=30\) matched the core parametrization, direct divisibility, age tests, and boundary set; this finite replay only corroborates the symbolic proof.

## originality

PASS

The general literature gives the Gorenstein divisibility/unit-partition correspondence and general Reid--Tai criteria, but the inspected primary sources do not state a complete all-dimensional solution for the two-heavy subfamily. The published SCOPE triangular theorem supplies the canonical/terminal inequalities for arbitrary two-heavy weights, but not the Gorenstein divisor-core bijection or the exact \(\tau(2r)+1\) boundary count. Resultary returned the audited record as the direct exact match and no earlier dominating classification.

## value

PASS

The two-heavy family is a natural infinite slice of weighted projective spaces. The divisor-core factorization turns the general unit-partition condition into a finite enumeration in every dimension and simultaneously identifies the complete Gorenstein canonical/non-terminal boundary with an exact divisor-function count. That is a structural classification rather than a routine fixed-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
