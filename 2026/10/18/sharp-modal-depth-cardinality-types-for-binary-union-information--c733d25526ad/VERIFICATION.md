---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

At depth 0, fixed marker valuations Z(X)=[|X|=0], A(X)=[|X|=1] yield exactly sizes 0,1,>1. For a depth-d child size cutoff t=2^d, exact finite child cardinalities i,j<=t can cover X iff max(i,j)<=|X|<=i+j. If |X|>2t, including infinite cardinality, attainable child-type pairs are uniformly those with >=1 tail child (choose that component X) and impossible for two exact children. Thus formula truth depends solely on sizes 0..2t or >2t at depth d+1. Conversely the join of exact t and k-t cardinality formulas defines [t,k], and subtracting exact lower sizes inductively defines each size k=t+1,...,2t at depth d+1. Hence all 2^d+2 types and arbitrary Boolean unions are realized, yielding 2^(2^d+2) classes, including arbitrary infinite ambient sets. Direct independent cardinality signature refinement for sizes 0..69 at d=0..5 gave 3,4,6,10,18,34 as predicted. The least depth separating 1<=n<m is ceil(log2 n).

## originality

PASS

Sharp logical cardinality visibility profile for one fixed-marked lax binary-join modal language, with all finite/infinite pointed types and formula-class numbers.

## value

PASS

The binary-only fragment of a recently defined information logic has a concrete sharp expressive resource hierarchy: exact cardinality visibility as a function of modal nesting depth, all pointed theories including infinite states, and a closed formula-algebra size. These are natural logic invariants that inform expressivity and model comparison, independent of claims about the full richer language.

The dated certificate retains the supplied scientific assessment, sources and limitations.
