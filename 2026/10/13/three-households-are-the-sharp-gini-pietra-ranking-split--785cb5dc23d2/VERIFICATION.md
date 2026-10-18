---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n=2 the pairwise-difference and mean-deviation formulas reduce to (b-a)/[2(a+b)]. For n=3, sum of pairwise differences is 4(x3-x1), hence G=2(ell+nu)/3. The unique above-mean or below-mean extreme sets show P=max(ell,nu). Direct rational computation gives G(A)=1/3 >7/24=G(B) and P(A)=13/48<7/24=P(B). Independently exhaustively enumerated all positive integer sorted triples sharing totals 3..16; no reversal for <16 and the only total-16 pair is (1,6,9),(3,3,10). The universal statement follows from elementary algebra, not enumeration.

## originality

PASS

Fellman (2018) already recognizes different Gini/Pietra ranking and Lorenz non-dominance; Vila–Saulo–Quintino (2026) gives a general interpolating family, not the equal-weight empirical support cutoff in inspected text. The new fact is a minimum-support boundary and exact two-endpoint classification, not the generic possibility of index disagreement.

## value

PASS

The fewest-households dimension at which two standard Lorenz-compliant inequality rankings can disagree is a natural structural question, relevant to fairness and sample-size interpretation. The exact endpoint formula isolates how aggregate spread and maximum deviation differ; supplemental first integer total shows a concrete minimal-scale example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
