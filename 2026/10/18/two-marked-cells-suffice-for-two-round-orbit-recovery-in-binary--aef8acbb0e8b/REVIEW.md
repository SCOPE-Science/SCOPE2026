# Self-review

## Correctness — PASS
The proof in `RESULT.md` derives the full stabilizer, constructs first-round singleton witnesses for every generated-subspace coordinate, and proves that second-round counts recover the exact orbit invariant. Boundary depths are treated separately. The two executable checks establish finite corroboration: 27 refinement cases and 15 independent group-enumeration cases. No finite experiment is used as an infinite proof.

## Originality — PASS (priority provisional)
The closest literature is Stones–Vojtěchovský–Wanless (2012) for Latin-square autotopisms, Pratt-Hartmann (2015) for counting with equivalences, Kiefer–Schweitzer–Selman (2015) for global counting identification, and Scheidt–Schweikardt (2025) for relational refinement. None of the inspected statements asserts or implies this exact two-round stabilizer-orbit partition for binary group-table three-nets. Targeted comparisons with related mathematical results showed no equivalent implication. A specialized coherent-configuration treatment may exist and remains a priority risk.

## Value — PASS
Two individually marked cells induce a bounded, sharp, and fully characterized counting-refinement orbit partition in an unbounded and highly symmetric family of Latin-table relational structures. The result includes explicit orbit sizes and explains the exact mechanism of counting reconstruction, not just a computational classification. It does not establish global structure identification among arbitrary finite models.

Self-review: passed. Independent audit: not yet performed.
