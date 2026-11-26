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

The order is bottom<a<e<b. The product is associative: bottom absorbs, otherwise b wins over a, and a wins over e; e is the unit. The rows are monotone and start at bottom, so each translation has the residual obtained by taking the largest eligible argument. Under the designated-atomic homomorphism convention, P changes from b to e without losing designatedness and R stays at the undesignated a. The source fusion is b and the target fusion is a. For a source below size four, the unit is either top or, in the only nontrivial nonintegral case, the middle element of a three-element chain. In the integral case x⊗y≤x∧y, so a designated product forces both inputs to be designated; in the three-element nonintegral case the only undesignated value is the absorbing bottom and the same conclusion holds. The trivial source has every atom designated. Induction on the fragment then propagates truth: a true source join on a chain has a true disjunct, a true existential over the finite chain has a witnessing assignment, and source meet and fusion both require true inputs. In a target with a unit-generated filter, meet, join and fusion propagate designatedness as needed, even for a different target algebra. The result does not assert failure for homomorphisms required to preserve atomic grades or value-order inequalities.

## originality

PASS

Carr anticipates the formula and nonintegral obstruction, and its standard UL product restricts to the submitted four-element multiplication on {0,1/3,1/2,1}. Thus neither the qualitative failure nor the product rule is the distinct contribution. The supported contribution is the exact minimum source carrier size in the stated finite unit-generated-filter setting; the inspected prior integral lemma and infinite example do not give that sharp threshold. The printed example's listed atomic assignments also do not witness its stated homomorphism; the qualitative construction can be fixed without changing the infinite algebra.

## value

PASS

The exact threshold answers how small a truth algebra can separate lattice-positive from fusion-positive preservation under designated-atomic maps. It identifies the needed order configuration (an undesignated nonbottom value and a designated value strictly above the unit), and supplies a chain attaining it. This is a meaningful finite boundary for an existing preservation problem, not a claim to have discovered the qualitative phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
