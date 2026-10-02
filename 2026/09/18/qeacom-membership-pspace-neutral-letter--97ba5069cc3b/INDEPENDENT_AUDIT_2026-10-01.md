# Independent audit — QEACom membership is PSPACE-complete even for neutral-letter NFAs

Audit date: 2026-10-01 (UTC) UTC

Final disposition: **PASSED**

## Correctness — PASS

With a neutral letter, the stable syntactic semigroup is a monoid; the EACom identities specialize to aperiodicity and commutativity, and conversely. PSPACE hardness follows directly from ordinary NFA universality by accepting everything except marked rejected prefixes and then adding a neutral-loop symbol; a missing word makes \(wcd\) rejected and \(wdc\) accepted. The upper-bound search over Boolean transition relations and syntactic equality uses polynomial space.

## Originality — PASS

The primary 2026 paper introduces QEACom, characterizes it and proves a PSPACE result for the distinct constant-circuit problem, but the inspected material does not state QEACom-membership complexity. Resultary and repository searches found no earlier equivalent theorem.

### equivalent_formulations

The neutral-letter collapse was compared directly with the defining identities.

Evidence: No exact membership theorem found.

### broader_coverage

Generic aperiodicity complexity does not directly give the exact combined stable-semigroup test.

Evidence: The source's PSPACE result concerns constant circuit complexity, not QEACom membership.

### exact_database_or_table

No exact prior row found.

Evidence: Only the audited record matched the exact NFA membership theorem.

### claim_vs_prior_implication

The inspected prior statements do not imply the exact final claim.

Evidence: The final theorem needs an additional identity test and neutral-letter hardness construction.

## Source inspections


- **Rational Reductions and Regular Languages of Constant Circuit Complexity** (arXiv:2609.18484): PRIMARY_PARTIAL. Material read: arXiv abstract; direct full-text and institutional fallback attempts failed. Evidence: Abstract states QEACom introduction/characterization, logarithmic upper bounds and PSPACE-completeness of the distinct constant-circuit problem.


## Scientific value — PASS

This settles the natural NFA decision problem for a newly introduced pseudovariety, including a neutral-letter promise, and yields a useful representation-sensitive complexity boundary.

## Residual risks and limitations


- The primary QEACom preprint full text could not be retrieved through the available full-text routes; the abstract was inspected and the main reduction was reconstructed independently.
