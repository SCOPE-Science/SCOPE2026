# Review of the period-doubling Lie-complexity classification

## Correctness

PASS. The defining recurrence forces every one to an odd global position and excludes `11` and `0000`. These facts eliminate all odd lengths at least five. At even lengths, every eligible cyclic class has ones on just one parity, giving a unique desubstitution, and the inverse rotation argument proves a genuine bijection of classes. The initial length-one, length-two and length-three factor sets are explicitly checked. These steps prove the formula for all positive lengths without extrapolating finite enumeration. The standalone checker agrees at every length through 192 using a proved finite prefix-coverage bound.

## Originality

PASS, with residual priority risk. Bell–Shallit (arXiv:2102.03821v1, especially the statement of Theorem 1.4 and Section 7) give automaticity and several explicit examples, but not this fixed-point formula. Cassaigne–Fici–Sciortino–Zamboni (arXiv:1402.5843, Proposition 17 and Example 1) give ordinary cyclic complexity at powers of two, not all-rotations Lie complexity at all lengths. De Luca–Fici (arXiv:2206.00995) treat Sturmian words; Li (arXiv:2207.05859) treats general variants. Direct searches for an explicit period-doubling Lie function and actual relevant research-record comparisons did not reveal an equivalent. An unindexed earlier treatment remains possible; absence of a search hit is not proof of priority.

## Mathematical value

PASS. Lie complexity is a well-motivated invariant of cyclic completeness in factor languages. The exact support and constant multiplicity for this canonical non-Sturmian automatic word complement the earlier explicit Thue–Morse and Sturmian computations, and the proof reveals a strong desubstitution mechanism that identifies every qualifying necklace rather than merely bounding the number. The result treats all lengths and is not a known-table recomputation or a finite cutoff.

## Scope and sources

The claim concerns the morphism \(0\mapsto01\), \(1\mapsto00\) and all positive lengths. Four primary papers and relevant statements were compared; finite checks cover lengths 1–192, and the infinite proof is self-contained. The earlier cyclic-complexity theorem has only partial, different-direction coverage. No priority claim beyond the available evidence is made.

Self-review: passed. Independent audit: not yet performed.
