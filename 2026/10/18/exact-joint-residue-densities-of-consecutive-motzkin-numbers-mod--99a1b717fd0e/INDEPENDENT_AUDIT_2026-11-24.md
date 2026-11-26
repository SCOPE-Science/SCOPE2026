# Independent mathematical audit

## correctness

PASS

The published digit predicates supply the pointwise input at positive indices; the unaddressed index n=0 is directly the allowed pair (1,1). The high-bit chain has sixteen states with two incoming labeled transitions each. From trailing bit zero, 10 and 110 add generators (1,0) and (2,1), and the zero loop gives aperiodicity. The ordinary five-bit prefixes resolve the carry and keep a common boundary bit. For low residues 13, 14, 15 the first zero at or above bit 4 and the next bit resolve both exceptional tests and the carry. Lengthening the run by four adds multiples of four to the necessary statistics and preserves the exceptional parity; for residue 15 the successor has its low run reset, and its ordinary residue-0 evaluator is independent of bit 4. The geometric sum for each exceptional representative includes the factor 1/8 for the eight uniform tail statistics. On every aligned block the fixed high suffix merely translates the uniform statistics conditional on the last free bit, so convergence for each bounded prefix is uniform over blocks. The omitted late exceptional prefixes have uniformly vanishing block proportion; binary partition of [0,N) then proves the ordinary density. Independent exact rational evaluation matched all 64 entries, both marginals, the mass 192 in scaled units, and all 44 positive entries; positive weights and exhaustive prefix types also show the zero cells are impossible rather than only sparse. An independent bounded evaluator check matched the exact recurrence for the first 512 terms with n=0 handled separately. The frozen verifier was inspected, not executed.

## originality

PASS

The distinct supported claim is the full evaluated ordinary adjacent-pair density law modulo 8, with its joint support, not the pointwise congruences or marginal parity counts. Inspected pointwise classifications and the known mod-8 automaton encode all values; neither supplies the adjacent distribution or establishes the required limiting behavior without further sequence-specific analysis. The closest indexed exact pair laws differ in modulus or sequence. The no-zero-residue fact is prior input.

## value

PASS

Adjacent terms at modulus 8 form a natural first joint statistic beyond the established pointwise and single-coordinate Motzkin laws. The complete ordinary density matrix identifies precisely how marginals fail to describe local dependence and distinguishes support restrictions from quantitative biases (e.g. marginal mass at 4 but no adjacent (4,4)). It provides a usable exact benchmark for automatic-sequence block-frequency calculations, not just sampled pairs or chosen entries of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
