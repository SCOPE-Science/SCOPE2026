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

The polynomial classification is exact. Equality of the two absolute quadratic outputs for every integer implies equality of their squares as polynomials; the sum of the two quadratics has leading coefficient six, so the quadratics themselves are equal. Linear-coefficient equality gives a common \(k=2u-v\), and constant-term equality factors as \((u-u')(4k-3(u+u'))=0\). Excluding identical triples forces the second factor and then \(3\mid k\), yielding the stated one-parameter family. Exact pair-collision equations give only \(q=0,1\); central symmetry makes \(q\leftrightarrow1-q\) transparent, and the piecewise linear span has unique six-distinct minimum 12 at \(q=-1,2\). The inspected verifier checks the symbolic coefficient identity, exact rational collision set, involution, span formulas, and both literature specializations.

## originality

PASS

Hickerson--Kleber's primary article contains the span-12 translation-invariant six-term identity, and Shen--Wu's recent work uses the span-20 member, but neither inspected source states the converse classification of every identity in this architecture. The proof's coefficient-factorization converse, parameter involution, and sharp span classification are not implied by the existence of those special cases. Fresh Resultary search found no prior full parametrization. Originality therefore passes best-of-knowledge.

## value

PASS

This is a natural complete classification of the precise six-term mechanism used in a recent interval-reduction solution. It unifies two historically separated examples, identifies the parameter redundancy, and proves the sharp minimum span within the architecture; that is a motivated structural result rather than a finite search or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
