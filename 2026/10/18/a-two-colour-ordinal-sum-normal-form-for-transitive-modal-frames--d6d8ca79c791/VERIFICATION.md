---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For root o and k>=1 labelled maximal leaves, literal upward-confluence applied to oRs forces every leaf to point to s, while back-up applied to bRo forces b to point to all leaves. Define U and V as universal leaf-target/source sets. If S nonempty, transitivity of o->s->u for u in U gives S=U; dually if B nonempty, V=B. A common element in U and V makes the leaf relation complete; intersecting S,B then forces every root edge and oRo, yielding exactly the complete exceptional relation. For disjoint S,B, transitivity excludes reverse block edges and leaves arbitrary transitive T on M, proving the exact B⊕T⊕S normal form. If c=1, confluence at oRo requires nonempty leaf rows and columns, respectively reducing to row/column fullness of T depending on absent B or S; if c=0 there is no extra condition. Counting partitions with |M|=j gives the two asserted binomial sums and the e.g.f. e^(2z)T(z). Independently implemented original quantified confluences and transitivity, and independently constructed all normal forms. Exact exhaustive comparison across all 16, 512 and 65536 binary relations for k=1,2,3 gave zero misses/extras; constructed k=4 gave 7182 valid frames split (5754,1428). Therefore all-k claim rests on algebraic necessity/sufficiency, not on k<=4 computation.

## originality

PASS

Best-of-knowledge original infinite labelled-fork structural classification and root-loop census. Full 2024 primary text gives the two confluence axioms and bi-preorder decidability/finite-model problems; it does not derive a rooted-fork ordinal-sum classification or exact counts. Published finite-chain normal forms use a different underlying total order, sometimes distinct confluence laws, and do not imply the branching star theorem. The 2026 IK4 decision-procedure paper could be checked only through bibliographic abstract, because arXiv/OA full-text attempts failed and authorized institutional access was disconnected; its unread body remains an explicit historical-overlap risk. The classic unrestricted transitive-relation counts t_j are properly credited as inputs, not new outputs.

## value

PASS

The rooted fork is the first natural branching departure from linear intuitionistic Kripke orders. Understanding all transitive accessibility relations satisfying both Fischer–Servi confluences is a motivating finite-frame structural question. The B⊕T⊕S decomposition classifies every k-fork for arbitrary k rather than tabulating tiny examples, and the distinct loop/no-loop formulas show precisely how root reflexivity changes the search space. These are directly reusable exact semantic model enumerators, not merely an arbitrary low-parameter slice or a routine substitution from the known unrestricted transitive-relation sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
