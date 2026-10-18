# Review of the exact progression census

## Correctness

PASS. Lucas' binary digit theorem identifies the odd-binomial index support as a product of independent integer intervals at separated binary runs. The step requiring proof is the additive rigidity: each coordinate difference in a relation of two sums lies strictly between consecutive multiples of the next block's base, so no carries can cancel between blocks. This gives an exact correspondence for all consecutive three-term identities, hence for every progression length. The signed-step interval count, subtraction of constant sequences and reversal involution complete the enumeration. The maximum and Fibonacci consequences are deduced from the same formula. Independently enumerating 8192 finite instances and checking boundary identities supports but does not substitute for the proof.

## Originality

PASS on the literature comparisons performed, with residual risk. The closest exact-object source is Meštrović's 2014 Lucas-theorem survey, section 6.1, which records the count of odd entries in each Pascal row, not their arithmetic-progression counts. Rolnick (2014) proves digitwise avoidance results for ternary Stanley sequences, with different mathematical objects; his results do not imply the claimed Pascal-row census. Kuca (2018) uses Sierpinski-triangle patterns and additive homomorphisms for Ulam-type sequences but does not supply the row-by-row factorization. Targeted searches for Pascal parity support, arithmetic progressions, binary runs, maximum lengths, and equivalent formulations found no statement covering the present theorem. An equivalent unindexed result may exist.

## Value

PASS. Arithmetic progressions in the parity support of binomial rows are a natural additive statistic of the familiar Sierpinski-Pascal structure. The result replaces a general exponential enumeration with a full closed expression for all progression lengths and every row, gives an exact extremal count and a sharp combinatorial criterion, and connects the sequence of progression-free row indices to Fibonacci enumeration. Its value does not depend on an unproved downstream application; the mathematically motivated full census and additive rigidity are the contribution.

## Closest literature and limitations

Meštrović, *Lucas' theorem: its generalizations, extensions and applications*, arXiv:1409.3820v1, section 6.1; Rolnick, *On the classification of Stanley sequences*, arXiv:1408.1940v1, section 3; Kuca, *Structures in Additive Sequences*, arXiv:1804.09594v1, sections 3--5. This result is restricted to parity modulo two and does not enumerate progression counts by fixed common difference. Publication priority and universal mathematical correctness have not received independent validation.

Self-review: passed. Independent audit: not yet performed.
