---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Every nonalgebraic type is an admissible ideal/filter pair (L,U) over a finite named poset, giving t(P)=2i(P)-1+m(P). For a chosen maximal x and Q=P\{x}, its strict predecessors D form an ideal; the incomparable subposet H=Q\D yields i(P)=i(Q)+i(H) and j(P)=j(Q)+|H|. Since i(H)>=|H|+1, induction gives i(P)>=n+1+j(P). Each comparable a<b gives a distinct mixed type (downarrow a, uparrow b), so m(P)>=c(P), yielding t(P)>=binom(n+2,2)+j(P) and exact nonnegative two-term defect. Nonchain connected comparability components contain an incomparable distance-two pair sharing a neighbor; their union downset/upset gives an additional mixed type not associated with a comparable pair. For disjoint k chains, i(P)=prod(n_i+1), j=e2 and m=c, so defect=2 sum_{r>=3}e_r and equality iff k<=2 (including empty poset). A fresh independent exhaustive enumeration for all labeled posets n=0..4 matched both the inequality and exact equality classification.

## originality

PASS

Dolinka–Mašulović and a published #P-completeness finding already establish the ideal/filter parameterization. The inspected complete Resultary finite-parameter #P paper gives chain/antichain values and a top-chain complexity reduction but not the sharp incomparability-sensitive coefficient-one lower bound, exact two-slack defect or global equality iff at most two chain components. The deduction uses elementary combinatorics, so a hidden extremal poset ideal-count inequality remains a real priority risk. No stronger theorem was located that mathematically implies the full stated equality classification.

## value

PASS

This is a natural extremal counting question for the automorphism-stabilizer type profile of the universal homogeneous poset. Its coefficient-one penalty per incomparable pair and exact structural equality cases distinguish how incomparability grows beyond a chain; it is a complete all-finite-poset bound/classification, not a renamed counting-hardness result. The result is modest/elementary but mathematically useful as a sharp extremal benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
