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

If a relation on the same worlds and valuation preserves all truth, its successor set at w is contained in E_w and satisfies exactly the formulas in H_w; hence KRep is necessary. Conversely taking E_w as successor sets proves agreement by induction. Only the direction from truth on E_w to membership can fail. Given a missing formula, one H_w-formula falsified at each of its finitely many counterworlds is a complete certificate of failure, including the empty tuple when there are no counterworlds. Membership and truth tests are effective on the total-input promise; dovetail the certificate tests if treating all codes as potential inputs. For hardness one can tabulate all subformulas on the all-false assignment and the singleton-true assignments at the input formula's finitely many atomic indices that qualify by bounded simulation. All other singleton-true assignments agree with the all-false one on its support, so the tabulation is exact, and primitive recursive. With H the intersection of the resulting theories, the concrete one-world frame under each valuation evaluates by the same recursion. Thus E and G hold under their all-valuations quantifiers, while M, C, N, K follow from classical truth at every simulated assignment. The absent contradiction excludes the dead-end relation; after halting a missing negated atom, true at the actual world, excludes the reflexive relation. Before halting the reflexive relation agrees on all formulas. This verifies both directions and preserves the promise.

## originality

PASS

The strongest inspected work provides the underlying same-carrier semantic criterion or studies recognition on materially different inputs. Neither supplies the finite-effective co-c.e. classification with a primitive-recursive normal one-world hard family. No prior coverage was established in the bounded comparison.

## value

PASS

The result identifies precisely when finite-carrier recognition differs from a finite-table test. The reduction shows that the obstruction survives even primitive-recursive membership, one world, and all the stated normality principles, so neither stronger frame assumptions of this kind nor finite branching alone repairs the algorithmic problem. This is more informative than an arbitrary undecidable encoding or a nonrepresentable example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
