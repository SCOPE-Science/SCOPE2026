# Scientific assessment: even-length cubic Fibonacci and Lucas window GCDs

## Correctness — PASS

The claim quantifies over every integer half-window length \(m\ge1\). The algebraic proof uses explicit Binet cubic identities and integer-index extension, a telescoping expression for sliding sums, endpoint pairing, and two normalized fourth-order recurrences with unit leading and constant coefficients. Four exact initial values reduce both normalized infinite gcds to a gcd of two integer affine forms; in one case a Bezout combination is exactly \(30\). The remaining prime factors \(2,3,5\) are classified using the exact Lucas norm identity and elementary periods modulo \(2\) and \(3\). The resulting formulas are integer-valued, including for half-lengths divisible by three. Independent finite integer checks cover 320 pairs of lengths/sequence types and 1600 window-sum identities, together with symbolic-parameter tests; the argument does not rely on finite extrapolation. No lemma is unproved or external to the supplied proof.

## Originality — PASS within inspected evidence

The most relevant primary source is Mbirika--Spilker (arXiv:2204.12626, §6.1). It proves first- and second-power results and explicitly proposes an even-length third-power formula. Its printed Fibonacci conjecture gives \(4\) at length six, whereas the exact sum windows give gcd \(2\), and the new theorem proves the correct value uniformly for every even length. Guyer--Mbirika (arXiv:2104.12262) treats first powers; the Mbirika--Schrader--Spilker follow-up (arXiv:2301.05758) treats Pell-type first powers and square sums. Published-record searches found no dominating theorem about both Fibonacci and Lucas cubic windows. The accessible prior-claim comparison found only a generalized Fibonacci **odd-window first/square-power** periodicity result and a Pell/balancing **square-window** theorem, neither implying any of the present cubic formulas.

The cited 2022 paper's Lucas conjectural display contains a \(9\) subtraction where the natural cubic Lucas difference would use \(27\); its displayed expression is not taken as the definition of the Lucas cubic-window GCD. The new proof works directly from the actual definition. Main originality risks: an unindexed independent resolution, a changed later version or erratum of the preprint, and incomplete coverage of non-indexed specialist literature. These risks do not amount to identified covering prior art.

## Mathematical value — PASS

The GCD of all shifts of a fixed power-sum window is the central natural invariant in the motivating literature. The theorem determines this invariant exactly for two canonical recurrences across an infinite two-parameter family (sequence choice and arbitrary even window length). It resolves the explicitly posed cubic extension, identifies an unexpected factor \(3\) precisely at half-lengths divisible by four, separates a Lucas factor \(5\), and corrects the attempted cubic formula with a concrete boundary counterexample. This is a complete natural classification rather than a small isolated arithmetic check.

## Limitations

The proven range is every even positive window length and exactly the standard Fibonacci and Lucas sequences with third powers. Odd lengths, arbitrary generalized Fibonacci initial data, and fourth or higher powers remain unproved. Publication priority is supported by inspected papers and actual record searches but is not guaranteed against unindexed sources. Executable checks do not replace the infinite proof.

Self-review: passed. Independent audit: not yet performed.

## References

- Mbirika and Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626, first public 2022-04-26, §6.1.
- Guyer and Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262, first public 2021-04-25.
- Mbirika, Schrader and Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, arXiv:2301.05758, first public 2023-01-13.
