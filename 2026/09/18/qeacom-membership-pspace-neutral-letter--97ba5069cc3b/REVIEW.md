# Review status

Fresh independent mathematical audit: **PASSED**.

## Correctness — PASS

With a neutral letter, the stable syntactic semigroup is a monoid; the EACom identities specialize to aperiodicity and commutativity, and conversely. PSPACE hardness follows directly from ordinary NFA universality by accepting everything except marked rejected prefixes and then adding a neutral-loop symbol; a missing word makes \(wcd\) rejected and \(wdc\) accepted. The upper-bound search over Boolean transition relations and syntactic equality uses polynomial space.

## Originality — PASS

The primary 2026 paper introduces QEACom, characterizes it and proves a PSPACE result for the distinct constant-circuit problem, but the inspected material does not state QEACom-membership complexity. Resultary and repository searches found no earlier equivalent theorem.

## Scientific value — PASS

This settles the natural NFA decision problem for a newly introduced pseudovariety, including a neutral-letter promise, and yields a useful representation-sensitive complexity boundary.

Detailed originality comparisons, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

Historical same-model evidence remains identified separately in `AUDIT.json`.
