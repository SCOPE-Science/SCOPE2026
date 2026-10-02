# Independent audit — A 9-by-9 elementary grading with no finite regrading

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The grading construction and finite-quotient obstruction were reconstructed from the definitions. The displayed 9-tuple gives the stated cyclic chain of matrix-unit degrees; using \(c=a^b\) and the Baumslag relation \(a=[a,c]\), the cycle product is the defining relator. Any finite regrading induces a finite quotient of the universal relations, so the images \(\alpha,\beta\) satisfy the Baumslag relator. Baumslag's theorem makes every finite quotient cyclic, hence the commutator relation forces \(\alpha=1\), contradicting the separation of the nonidentity \(a\)-component from the identity component. Appending repeated tuple entries embeds the same obstruction for all larger matrix sizes.

## Originality

**PASS.** The explicit dimension-nine obstruction improves the inspected published bound and was not found in earlier grading literature or the semantic archive.

### Equivalent formulations

The natural equivalent formulation is weak equivalence to a finite-group grading; this was explicitly compared.

Evidence: The 2018 framework characterizes finite regradings through finite factor groups that do not identify support elements. The audited tuple uses the same universal-group mechanism but with a distinct nine-coordinate realization.

### Broader coverage

No inspected earlier theorem dominates the dimension-nine result.

Evidence: The earlier construction guarantees counterexamples only in substantially larger dimensions. The newer inspected source gives an explicit all-\(n\ge14\) construction, not \(n=9\).

### Exact database or table

The problem is a dimension-threshold classification; exact bound searches are directly relevant.

Evidence: No earlier exact nine-dimensional construction or threshold entry was located.

### Claim versus prior implication

The claim genuinely combines the old group with a new small support realization rather than merely restating a prior theorem.

Evidence: Baumslag proves the group-theoretic finite-quotient property but supplies no matrix grading. The grading papers supply the regrading framework and larger constructions, but do not mechanically provide this specific 9-tuple.

### Source inspections

- **A non-cyclic one-relator group all of whose finite quotients are cyclic** — SUPPORTING_LEMMA.
  Identifier: DOI 10.1017/S1446788700007783
  Material read: Complete two-page article.
  Evidence: The paper proves that every finite quotient of \(\langle a,b\mid a=[a,a^b]\rangle\) is cyclic and that the group is noncyclic.
- **On weak equivalences of gradings** — EARLIER_WEAKER_BOUND.
  Identifier: arXiv:1704.07170
  Material read: Full 17-page preprint, including Problem 1.7, Theorem 1.8, support/factor-group criterion, and dimension-three theorem.
  Evidence: It formulates the threshold problem and proves only a much larger explicit upper bound while showing all elementary gradings for \(n\le3\) regrade finitely.
- **Finite regrading of elementary matrix gradings** — EARLIER_WEAKER_BOUND.
  Identifier: arXiv:2511.11923
  Material read: Full 21-page preprint, especially the theorem giving the explicit \(n\ge14\) construction.
  Evidence: The inspected theorem gives counterexamples from dimension 14 upward, so it does not cover the audited \(n=9\) construction.

### Residual risks

- An unindexed small-dimensional construction could exist; no such source was located.

## Scientific value

**PASS.** The result materially narrows an explicitly studied finite-regrading threshold, improving the best inspected explicit counterexample dimension from 14 to 9 and leaving only \(4\le n\le8\). The construction is structural and reusable, not a numerical census.

## Final assessment

The final claim survives unchanged on all three scientific axes. No claim text or slogan change is proposed.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
