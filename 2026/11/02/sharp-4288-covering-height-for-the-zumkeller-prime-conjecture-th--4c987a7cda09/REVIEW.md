# Scientific review

## Correctness: PASS
The stated finite theorem is reduced to exhaustive, exact integer algorithms, not experiments. Proper-divisor subset sums are characterized by a descending Boolean recurrence, full odd primality by an Eratosthenes sieve, and the entire \(55,555,554\)-element residue-class range is traversed. At the unique extremum no smaller even Zumkeller summand works, and an odd summand would require prime \(2\), forcing a larger summand. The embedded program has been compiled and executed, returning the asserted statistics; separate small-window and extremal primality checks agree. Infinite coverage is not inferred.

## Originality: PASS within inspected evidence
The 2023 Somu--Kukla--Tran primary text explicitly leaves this residue class as Conjecture 4.20, reporting only \(k\le1000\) checked. OEIS A368082 lists small examples; Li's 2026 result gives asymptotic density zero and neither this exact range nor extremal value. Related public mathematical-result searches revealed no implication giving the bound \(4288\) and unique maximizing argument. An unindexed prior finite verification remains possible.

## Value: PASS
The first omitted residue class is the only finite obstacle to a full up-to-\(X\) statement of the published conjecture. Verifying it through the natural one-billion milestone covers over fifty-five million instances, more than fifty-five thousand times the reported \(1000\)-index check. The sharp covering height is a natural extremal invariant: finite fixed families of admissible offsets cannot cover all larger integers because of CRT obstructions. Determining its exact one-billion value and unique extremizer supplies quantitative information useful for subsequent searches, beyond a routine list of examples.

## Closest literature and remaining limits
Somu--Kukla--Tran, *Some Results on Zumkeller Numbers* (arXiv:2310.14149, Sections 4--5); OEIS A368082; Li, *The Density and Quantitative Upper Bound of Integers Not Expressible as the Sum of a Prime and a Zumkeller Number* (arXiv:2610.19574, main theorem). The result is only finite and no priority or completeness of unindexed literature is asserted.

Self-review: passed. Independent audit: not yet performed.
