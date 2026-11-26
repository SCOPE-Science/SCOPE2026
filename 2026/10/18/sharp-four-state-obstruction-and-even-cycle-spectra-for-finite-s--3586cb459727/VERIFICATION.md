---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the finite discrete definitions the diagonal is an admissible neighborhood, so forward RP is exactly the union of the map kernels. Backward RP is contained in the diagonal and contains it since the monoid contains identity. Direct composition gives a²=a, ab²=b²a, aba=a and b^(2m)=1; moving even shift powers to the left and removing successive a's gives exactly b^k and b^k a b^e (e=0,1). The rank-m forms are distinguished by their values at 0 and 1 and are distinct from the 2m shifts. Their two fiber matchings alternate around C_(2m); m≥2 makes 0 and 2 nonadjacent. The cyclic shift supplies minimality and forces any invariant probability to be uniform, which a does not preserve; ab and ba disagree at 0. In any monoid action nonmergeability is forward invariant by composition; on three points failure of transitivity would leave just one nonmergeable pair, an invariant proper set. At most two points is immediate, and a single generator of a finite minimal action must be a cyclic permutation. The frozen verify.py and VERIFICATION.md were inspected, not executed; their finite checks do not prove the unbounded or arbitrary-generator assertions. Independent exact closure and kernel checks for n=4,6,8,16 passed in section 1 of python3 -B /workspace/review-evidence/rederive.py.

## originality

PASS

The kernel-graph interpretation is established and the abstract C4 complement with two maps generating its hull is covered. The literature also already exhibits nontransitive regional proximality for noncommutative infinite actions. The supported distinct result is the complete minimal two-generator family with both relations and explicit monoid and rank counts, together with the sharp finite-state obstruction in the specified class; it is not a claim to have discovered the kernel-graph framework, the abstract four-vertex hull, or noncommutative nontransitivity generally.

## value

PASS

A sharp smallest counterexample is natural for the commutativity boundary of regional proximality. The family does more than test one small example: the two matchings give an explicit infinite class of chordless cycles with a small closed monoid, complete forward/backward relations and exact rank spectrum. These data make the obstruction readily usable without mistaking it for a counterexample in the invariant-probability class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
